from .models import Room, Movie, Schedule, OccupiedSeat
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from rest_framework import serializers



class CustomTokenObtainPairSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        User = get_user_model()
        try:
            user = User.objects.get(username=attrs['username'])
        except User.DoesNotExist:
            raise serializers.ValidationError('User does not exist')

        if not user.check_password(attrs['password']):
            raise serializers.ValidationError('Invalid password')

        refresh = RefreshToken.for_user(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return data


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = OccupiedSeat
        fields = '__all__'



