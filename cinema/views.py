from .models import Room, Movie, Schedule, OccupiedSeat
from .serializers import RoomSerializer, MovieSerializer, ScheduleSerializer, SeatSerializer
from rest_framework.viewsets import  ModelViewSet
from rest_framework.permissions import IsAdminUser
from django.http import JsonResponse
from rest_framework import status
from django.db.models import Q
from .swagger_config import *



class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # permission_classes = (IsAdminUser, )

    @get_room_list_view_schema()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @get_room_create_view_schema()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @get_room_retrieve_view_schema()
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @get_room_update_view_schema()
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @get_room_delete_view_schema()
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)





class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # permission_classes = (IsAdminUser, )

    def get_queryset(self):
        query = self.request.query_params.get('id')
        queryset = super().get_queryset()
        if query:
            args = map(int, query.split(','))
            queryset = queryset.filter(id__in=args)

        return queryset

    @get_movie_list_view_schema()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @get_movie_create_view_schema()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @get_movie_retrieve_view_schema()
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @get_movie_update_view_schema()
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @get_movie_delete_view_schema()
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    @get_schedule_list_view_schema()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        room_id = self.request.query_params.get('room', None)

        if room_id is not None:
            queryset = queryset.filter(Q(room__id=room_id))

        return queryset

    @get_schedule_create_view_schema()
    def create(self,request, *args, **kwargs):
        room = request.data.get('room')
        start_time = request.data.get('start_time')

        if Schedule.objects.filter(start_time=start_time,room=room).exists():
            return JsonResponse({'Error': "--------------------"},
                                status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    @get_schedule_retrieve_view_schema()
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @get_schedule_update_view_schema()
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @get_schedule_delete_view_schema()
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class OccupiedSeatViewSet(ModelViewSet):
    queryset = OccupiedSeat.objects.all()
    serializer_class = SeatSerializer

    @get_occupied_seat_list_view_schema()
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @get_occupied_seat_create_view_schema()
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

    @get_occupied_seat_retrieve_view_schema()
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @get_occupied_seat_update_view_schema()
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @get_occupied_seat_destroy_view_schema()
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
