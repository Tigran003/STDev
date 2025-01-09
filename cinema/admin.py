from django.contrib import admin
from .models import Room, Movie, Schedule, OccupiedSeat

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'rows', 'seats_per_row')

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('movie', 'room', 'start_time', 'end_time')

@admin.register(OccupiedSeat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ('schedule','position')
