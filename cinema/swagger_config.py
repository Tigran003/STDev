from .serializers import RoomSerializer, MovieSerializer, ScheduleSerializer, SeatSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample, OpenApiTypes

def get_room_list_view_schema():
    return extend_schema(
        summary="List all rooms",
        description="Retrieve a list of all rooms.",
        tags=["Rooms"],
        responses={
            200: OpenApiResponse(
                response=RoomSerializer(many=True),
                description="A list of rooms"
            ),
            400: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Bad request. Check your input data.",
                examples=[
                    OpenApiExample(
                        name="Bad Request Example",
                        summary="Example of a bad request",
                        description="This example shows how a bad request might look.",
                        value={"detail": "Invalid input data"}
                    )
                ]
            ),
            500: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Server error. Please try again later.",
                examples=[
                    OpenApiExample(
                        name="Server Error Example",
                        summary="Example of a server error",
                        description="This example shows how a server error might look.",
                        value={"detail": "Internal server error"}
                    )
                ]
            )
        },
        examples=[
            OpenApiExample(
                name="Example of retrieving all rooms",
                summary="Example of retrieving all rooms",
                description="List of all rooms with their details.",
                value=[
                    {
                        "name": "Room 1",
                        "rows": 10,
                        "seats_per_row": 8
                    },
                    {
                        "name": "Room 2",
                        "rows": 12,
                        "seats_per_row": 10
                    }
                ]
            )
        ]
    )

def get_room_create_view_schema():
    return extend_schema(
        summary="Create a new room",
        description="Create a new room with the specified details.",
        tags=["Rooms"],
        request=RoomSerializer,
        responses={
            201: OpenApiResponse(
                response=RoomSerializer,
                description="Room created successfully"
            ),
            400: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Bad request. Check your input data.",
                examples=[
                    OpenApiExample(
                        name="Bad Request Example",
                        summary="Example of a bad request",
                        description="This example shows how a bad request might look.",
                        value={"detail": "Invalid input data"}
                    )
                ]
            ),
        }
    )

def get_room_retrieve_view_schema():
    return extend_schema(
        summary="Retrieve a room by ID",
        description="Retrieve the details of a specific room by its ID.",
        tags=["Rooms"],
        responses={
            200: OpenApiResponse(
                response=RoomSerializer,
                description="Details of the room"
            ),
            404: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Room not found. Check the ID.",
                examples=[
                    OpenApiExample(
                        name="Not Found Example",
                        summary="Example of a not found response",
                        description="This example shows how a not found response might look.",
                        value={"detail": "Not found."}
                    )
                ]
            ),
        }
    )

def get_room_update_view_schema():
    return extend_schema(
        summary="Update a room by ID",
        description="Update the details of a specific room by its ID.",
        tags=["Rooms"],
        request=RoomSerializer,
        responses={
            200: OpenApiResponse(
                response=RoomSerializer,
                description="Room updated successfully"
            ),
            400: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Bad request. Check your input data.",
                examples=[
                    OpenApiExample(
                        name="Bad Request Example",
                        summary="Example of a bad request",
                        description="This example shows how a bad request might look.",
                        value={"detail": "Invalid input data"}
                    )
                ]
            ),
            404: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Room not found. Check the ID.",
                examples=[
                    OpenApiExample(
                        name="Not Found Example",
                        summary="Example of a not found response",
                        description="This example shows how a not found response might look.",
                        value={"detail": "Not found."}
                    )
                ]
            ),
        }
    )

def get_room_delete_view_schema():
    return extend_schema(
        summary="Delete a room by ID",
        description="Delete a specific room by its ID.",
        tags=["Rooms"],
        responses={
            204: OpenApiResponse(
                description="Room deleted successfully"
            ),
            404: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Room not found. Check the ID.",
                examples=[
                    OpenApiExample(
                        name="Not Found Example",
                        summary="Example of a not found response",
                        description="This example shows how a not found response might look.",
                        value={"detail": "Not found."}
                    )
                ]
            ),
        }
    )

def get_movie_list_view_schema():
    return extend_schema(
        summary="List all movies",
        description="Retrieve a list of all movies.",
        tags=["Movies"],
        responses={
            200: OpenApiResponse(
                response=MovieSerializer(many=True),
                description="A list of movies"
            ),
            400: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Bad request. Check your input data.",
                examples=[
                    OpenApiExample(
                        name="Bad Request Example",
                        summary="Example of a bad request",
                        description="This example shows how a bad request might look.",
                        value={"detail": "Invalid input data"}
                    )
                ]
            ),
            500: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Server error. Please try again later.",
                examples=[
                    OpenApiExample(
                        name="Server Error Example",
                        summary="Example of a server error",
                        description="This example shows how a server error might look.",
                        value={"detail": "Internal server error"}
                    )
                ]
            )
        },
        examples=[
            OpenApiExample(
                name="Example of retrieving all movies",
                summary="Example of retrieving all movies",
                description="List of all movies with their details.",
                value=[
                    {
                        "title": "Movie 1",
                        "poster": "path/to/poster.jpg",
                        "price": 3000,
                        "background_image": "path/to/background.jpg",
                        "duration": 120
                    },
                    {
                        "title": "Movie 2",
                        "poster": "path/to/poster2.jpg",
                        "price": 2500,
                        "background_image": "path/to/background2.jpg",
                        "duration": 90
                    }
                ]
            )
        ]
    )

def get_movie_create_view_schema():
    return extend_schema(
        summary="Create a new movie",
        description="Create a new movie with the specified details.",
        tags=["Movies"],
        request=MovieSerializer,
        responses={
            201: OpenApiResponse(
                response=MovieSerializer,
                description="Movie created successfully"
            ),
            400: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Bad request. Check your input data.",
                examples=[
                    OpenApiExample(
                        name="Bad Request Example",
                        summary="Example of a bad request",
                        description="This example shows how a bad request might look.",
                        value={"detail": "Invalid input data"}
                    )
                ]
            ),
        }
    )

def get_movie_retrieve_view_schema():
    return extend_schema(
        summary="Retrieve a movie by ID",
        description="Retrieve the details of a specific movie by its ID.",
        tags=["Movies"],
        responses={
            200: OpenApiResponse(
                response=MovieSerializer,
                description="Details of the movie"
            ),
            404: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Movie not found. Check the ID.",
                examples=[
                    OpenApiExample(
                        name="Not Found Example",
                        summary="Example of a not found response",
                        description="This example shows how a not found response might look.",
                        value={"detail": "Not found."}
                    )
                ]
            ),
        }
    )

def get_movie_update_view_schema():
    return extend_schema(
        summary="Update a movie by ID",
        description="Update the details of a specific movie by its ID.",
        tags=["Movies"],
        request=MovieSerializer,
        responses={
            200: OpenApiResponse(
                response=MovieSerializer,
                description="Movie updated successfully"
            ),
            400: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Bad request. Check your input data.",
                examples=[
                    OpenApiExample(
                        name="Bad Request Example",
                        summary="Example of a bad request",
                        description="This example shows how a bad request might look.",
                        value={"detail": "Invalid input data"}
                    )
                ]
            ),
            404: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Movie not found. Check the ID.",
                examples=[
                    OpenApiExample(
                        name="Not Found Example",
                        summary="Example of a not found response",
                        description="This example shows how a not found response might look.",
                        value={"detail": "Not found."}
                    )
                ]
            ),
        }
    )

def get_movie_delete_view_schema():
    return extend_schema(
        summary="Delete a movie by ID",
        description="Delete a specific movie by its ID.",
        tags=["Movies"],
        responses={
            204: OpenApiResponse(
                description="Movie deleted successfully"
            ),
            404: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Movie not found. Check the ID.",
                examples=[
                    OpenApiExample(
                        name="Not Found Example",
                        summary="Example of a not found response",
                        description="This example shows how a not found response might look.",
                        value={"detail": "Not found."}
                    )
                ]
            ),
        }
    )

def get_schedule_list_view_schema():
    return extend_schema(
        summary="List all schedules",
        description="Retrieve a list of all schedules.",
        tags=["Schedules"],
        responses={
            200: OpenApiResponse(
                response=ScheduleSerializer(many=True),
                description="A list of schedules"
            ),
            400: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Bad request. Check your input data.",
                examples=[
                    OpenApiExample(
                        name="Bad Request Example",
                        summary="Example of a bad request",
                        description="This example shows how a bad request might look.",
                        value={"detail": "Invalid input data"}
                    )
                ]
            ),
            500: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Server error. Please try again later.",
                examples=[
                    OpenApiExample(
                        name="Server Error Example",
                        summary="Example of a server error",
                        description="This example shows how a server error might look.",
                        value={"detail": "Internal server error"}
                    )
                ]
            )
        },
        examples=[
            OpenApiExample(
                name="Example of retrieving all schedules",
                summary="Example of retrieving all schedules",
                description="List of all schedules with their details.",
                value=[
                    {
                        "room": {
                            "name": "Room 1",
                            "rows": 10,
                            "seats_per_row": 8
                        },
                        "movie": {
                            "title": "Movie 1",
                            "poster": "path/to/poster.jpg",
                            "price": 3000,
                            "background_image": "path/to/background.jpg",
                            "duration": 120
                        },
                        "start_time": "2025-01-10T14:00:00Z",
                        "end_time": "2025-01-10T16:00:00Z"
                    },
                    {
                        "room": {
                            "name": "Room 2",
                            "rows": 12,
                            "seats_per_row": 10
                        },
                        "movie": {
                            "title": "Movie 2",
                            "poster": "path/to/poster2.jpg",
                            "price": 2500,
                            "background_image": "path/to/background2.jpg",
                            "duration": 90
                        },
                        "start_time": "2025-01-10T17:00:00Z",
                        "end_time": "2025-01-10T18:30:00Z"
                    }
                ]
            )
        ]
    )

def get_schedule_create_view_schema():
    return extend_schema(
        summary="Create a new schedule",
        description="Create a new schedule with the specified details.",
        tags=["Schedules"],
        request=ScheduleSerializer,
        responses={
            201: OpenApiResponse(
                response=ScheduleSerializer,
                description="Schedule created successfully"
            ),
            400: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Bad request. Check your input data.",
                examples=[
                    OpenApiExample(
                        name="Bad Request Example",
                        summary="Example of a bad request",
                        description="This example shows how a bad request might look.",
                        value={"detail": "Invalid input data"}
                    )
                ]
            ),
        }
    )

def get_schedule_retrieve_view_schema():
    return extend_schema(
        summary="Retrieve a schedule by ID",
        description="Retrieve the details of a specific schedule by its ID.",
        tags=["Schedules"],
        responses={
            200: OpenApiResponse(
                response=ScheduleSerializer,
                description="Details of the schedule"
            ),
            404: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Schedule not found. Check the ID.",
                examples=[
                    OpenApiExample(
                        name="Not Found Example",
                        summary="Example of a not found response",
                        description="This example shows how a not found response might look.",
                        value={"detail": "Not found."}
                    )
                ]
            ),
        }
    )

def get_schedule_update_view_schema():
    return extend_schema(
        summary="Update a schedule by ID",
        description="Update the details of a specific schedule by its ID.",
        tags=["Schedules"],
        request=ScheduleSerializer,
        responses={
            200: OpenApiResponse(
                response=ScheduleSerializer,
                description="Schedule updated successfully"
            ),
            400: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Bad request. Check your input data.",
                examples=[
                    OpenApiExample(
                        name="Bad Request Example",
                        summary="Example of a bad request",
                        description="This example shows how a bad request might look.",
                        value={"detail": "Invalid input data"}
                    )
                ]
            ),
            404: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Schedule not found. Check the ID.",
                examples=[
                    OpenApiExample(
                        name="Not Found Example",
                        summary="Example of a not found response",
                        description="This example shows how a not found response might look.",
                        value={"detail": "Not found."}
                    )
                ]
            ),
        }
    )

def get_schedule_delete_view_schema():
    return extend_schema(
        summary="Delete a schedule by ID",
        description="Delete a specific schedule by its ID.",
        tags=["Schedules"],
        responses={
            204: OpenApiResponse(
                description="Schedule deleted successfully"
            ),
            404: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Schedule not found. Check the ID.",
                examples=[
                    OpenApiExample(
                        name="Not Found Example",
                        summary="Example of a not found response",
                        description="This example shows how a not found response might look.",
                        value={"detail": "Not found."}
                    )
                ]
            ),
        }
    )


def get_occupied_seat_list_view_schema():
    return extend_schema(
        summary="List all occupied seats",
        description="Retrieve a list of all occupied seats.",
        tags=["Occupied Seats"],
        responses={
            200: OpenApiResponse(
                response=SeatSerializer(many=True),
                description="A list of occupied seats"
            ),
            400: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Bad request. Check your input data.",
                examples=[
                    OpenApiExample(
                        name="Bad Request Example",
                        summary="Example of a bad request",
                        description="This example shows how a bad request might look.",
                        value={"detail": "Invalid input data"}
                    )
                ]
            ),
            500: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Server error. Please try again later.",
                examples=[
                    OpenApiExample(
                        name="Server Error Example",
                        summary="Example of a server error",
                        description="This example shows how a server error might look.",
                        value={"detail": "Internal server error"}
                    )
                ]
            )
        },
        examples=[
            OpenApiExample(
                name="Example of retrieving all occupied seats",
                summary="Example of retrieving all occupied seats",
                description="List of all occupied seats with their details.",
                value=[
                    {
                        "schedule": 1,
                        "position": [1, 1]
                    },
                    {
                        "schedule": 2,
                        "position": [2, 3]
                    }
                ]
            )
        ]
    )

def get_occupied_seat_create_view_schema():
    return extend_schema(
        summary="Create a new occupied seat",
        description="Add a new occupied seat to the system.",
        tags=["Occupied Seats"],
        request=SeatSerializer,
        responses={
            201: OpenApiResponse(
                response=SeatSerializer,
                description="Occupied seat created successfully"
            ),
            400: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Bad request. Check your input data.",
                examples=[
                    OpenApiExample(
                        name="Bad Request Example",
                        summary="Example of a bad request",
                        description="This example shows how a bad request might look.",
                        value={"detail": "Invalid input data"}
                    )
                ]
            ),
            500: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Server error. Please try again later.",
                examples=[
                    OpenApiExample(
                        name="Server Error Example",
                        summary="Example of a server error",
                        description="This example shows how a server error might look.",
                        value={"detail": "Internal server error"}
                    )
                ]
            )
        }
    )

def get_occupied_seat_retrieve_view_schema():
    return extend_schema(
        summary="Retrieve an occupied seat",
        description="Retrieve details of an occupied seat by its ID.",
        tags=["Occupied Seats"],
        responses={
            200: OpenApiResponse(
                response=SeatSerializer,
                description="Details of the occupied seat"
            ),
            404: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Not found. The occupied seat does not exist.",
                examples=[
                    OpenApiExample(
                        name="Not Found Example",
                        summary="Example of a not found response",
                        description="This example shows how a not found response might look.",
                        value={"detail": "Not found"}
                    )
                ]
            ),
            500: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Server error. Please try again later.",
                examples=[
                    OpenApiExample(
                        name="Server Error Example",
                        summary="Example of a server error",
                        description="This example shows how a server error might look.",
                        value={"detail": "Internal server error"}
                    )
                ]
            )
        }
    )

def get_occupied_seat_update_view_schema():
    return extend_schema(
        summary="Update an occupied seat",
        description="Update details of an occupied seat by its ID.",
        tags=["Occupied Seats"],
        request=SeatSerializer,
        responses={
            200: OpenApiResponse(
                response=SeatSerializer,
                description="Occupied seat updated successfully"
            ),
            400: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Bad request. Check your input data.",
                examples=[
                    OpenApiExample(
                        name="Bad Request Example",
                        summary="Example of a bad request",
                        description="This example shows how a bad request might look.",
                        value={"detail": "Invalid input data"}
                    )
                ]
            ),
            404: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Not found. The occupied seat does not exist.",
                examples=[
                    OpenApiExample(
                        name="Not Found Example",
                        summary="Example of a not found response",
                        description="This example shows how a not found response might look.",
                        value={"detail": "Not found"}
                    )
                ]
            ),
            500: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Server error. Please try again later.",
                examples=[
                    OpenApiExample(
                        name="Server Error Example",
                        summary="Example of a server error",
                        description="This example shows how a server error might look.",
                        value={"detail": "Internal server error"}
                    )
                ]
            )
        }
    )


def get_occupied_seat_destroy_view_schema():
    return extend_schema(
        summary="Delete an occupied seat",
        description="Delete an occupied seat by its ID.",
        tags=["Occupied Seats"],
        responses={
            204: OpenApiResponse(
                description="Occupied seat deleted successfully"
            ),
            404: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Not found. The occupied seat does not exist.",
                examples=[
                    OpenApiExample(
                        name="Not Found Example",
                        summary="Example of a not found response",
                        description="This example shows how a not found response might look.",
                        value={"detail": "Not found"}
                    )
                ]
            ),
            500: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description="Server error. Please try again later.",
                examples=[
                    OpenApiExample(
                        name="Server Error Example",
                        summary="Example of a server error",
                        description="This example shows how a server error might look.",
                        value={"detail": "Internal server error"}
                    )
                ]
            )
        }
    )