from .models import Room, Movie, Schedule, OccupiedSeat
from .serializers import RoomSerializer, MovieSerializer, ScheduleSerializer, SeatSerializer
from rest_framework.viewsets import  ModelViewSet
from rest_framework.permissions import IsAdminUser
from django.http import JsonResponse
from rest_framework import status



class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # permission_classes = (IsAdminUser, )


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # permission_classes = (IsAdminUser, )


class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def create(self,request, *args, **kwargs):
        room = request.data.get('room')
        start_time = request.data.get('start_time')

        if Schedule.objects.filter(start_time=start_time,room=room).exists():
            return JsonResponse({'Error': "--------------------"},
                                status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)




class OccupiedSeatViewSet(ModelViewSet):
    queryset = OccupiedSeat.objects.all()
    serializer_class = SeatSerializer

    def create(self, request, *args, **kwargs):
        schedule_id = request.data.get('schedule')
        position = request.data.get('position')
        schedule = Schedule.objects.get(id=schedule_id)

        if OccupiedSeat.objects.filter(schedule=schedule_id, position=position).exists():
            return JsonResponse({'Error': "The seat at this position is already occupied for this schedule"},
                                status=status.HTTP_400_BAD_REQUEST)

        if not position or len(position) != 2:
            return JsonResponse({'Error': "Position must contain exactly two elements: [row, column]"},
                                status=status.HTTP_400_BAD_REQUEST)

        row, column = position
        if row <= 0 or column <= 0:
            return JsonResponse({'Error': "Row and column values must be greater than zero"},
                                status=status.HTTP_400_BAD_REQUEST)

        room = schedule.room
        if  row > room.rows or column > room.seats_per_row:
            return JsonResponse({'Error': "Invalid seat position"},
                                status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
