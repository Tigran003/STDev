from datetime import timedelta
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)
    rows = models.IntegerField(default=10)
    seats_per_row = models.IntegerField(default=8)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters/',blank=True)
    price = models.IntegerField(default=0)
    background_image = models.ImageField(upload_to='background/', blank=True, null=True)
    duration = models.IntegerField(help_text="Duration in minutes")

    def __str__(self):
        return self.title

class Schedule(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='schedules')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='schedules')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        if not self.end_time:
            self.end_time = self.start_time + timedelta(minutes=self.movie.duration)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.movie.title} at {self.start_time} in {self.room.name}"



class OccupiedSeat(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='seats')
    position = ArrayField(
        models.IntegerField(),
        size=2,  # it contains exactly two elements: [row, column]
        help_text="Stores the seat position as [row, column]"
    )



