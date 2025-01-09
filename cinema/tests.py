from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.utils import timezone
from datetime import timedelta
from .models import Room, Movie, Schedule, OccupiedSeat

class CinemaAPITests(APITestCase):

    def setUp(self):
        self.room = Room.objects.create(name="Room 1", rows=10, seats_per_row=8)
        self.movie = Movie.objects.create(title="Movie 1", duration=120,price=3000)
        self.start_time = timezone.now()
        self.schedule = Schedule.objects.create(room=self.room, movie=self.movie, start_time=self.start_time)
        self.occupied_seat = OccupiedSeat.objects.create(schedule=self.schedule, position=[1, 1])

    def test_create_room(self):
        url = reverse('room-list')
        data = {'name': 'Room 2', 'rows': 12, 'seats_per_row': 10}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_movie(self):
        url = reverse('movie-list')
        data = {'title': 'Movie 2', 'duration': 90,'price':2000}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_schedule(self):
        url = reverse('schedule-list')
        data = {
            'room': self.room.id,
            'movie': self.movie.id,
            'start_time': (timezone.now() + timedelta(days=1)).isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_occupied_seat(self):
        url = reverse('occupiedseat-list')
        data = {
            'schedule': self.schedule.id,
            'position': [1, 2]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_schedule_conflict(self):
        url = reverse('schedule-list')
        data = {
            'room': self.room.id,
            'movie': self.movie.id,
            'start_time': self.schedule.start_time.isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Error', response.json())  # Use response.json() to get the JSON content

    def test_occupied_seat_conflict(self):
        url = reverse('occupiedseat-list')
        data = {
            'schedule': self.schedule.id,
            'position': [1, 1]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Error', response.json())  # Use response.json() to get the JSON content