# Django Cinema Booking System

This is a Django-based cinema booking system that allows users to manage rooms, movies, schedules, and occupied seats. The system also includes JWT authentication for secure access.

## Features

- Manage Rooms: Create, update, and delete rooms.
- Manage Movies: Create, update, and delete movies.
- Manage Schedules: Create, update, and delete schedules for movies in specific rooms.
- Manage Occupied Seats: Track occupied seats for each schedule.
- JWT Authentication: Secure access with JSON Web Tokens.
- API Documentation: Swagger and Redoc UI for API schema documentation.


## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Tigran003/STDev.git
    cd STDev
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the server:**
    ```bash
    python manage.py runserver
    ```

## Usage

### API Endpoints

- **Authentication:**
  - Obtain Token: `POST /api/token/`
  - Refresh Token: `POST /api/token/refresh/`
  - Verify Token: `POST /api/token/verify/`

- **Room Management:**
  - List Rooms: `GET /rooms/`
  - Create Room: `POST /rooms/`
  - Retrieve Room: `GET /rooms/{id}/`
  - Update Room: `PUT /rooms/{id}/`
  - Delete Room: `DELETE /rooms/{id}/`

- **Movie Management:**
  - List Movies: `GET /movie/`
  - Create Movie: `POST /movie/`
  - Retrieve Movie: `GET /movie/{id}/`
  - Update Movie: `PUT /movie/{id}/`
  - Delete Movie: `DELETE /movie/{id}/`

- **Schedule Management:**
  - List Schedules: `GET /schedule/`
  - Create Schedule: `POST /schedule/`
  - Retrieve Schedule: `GET /schedule/{id}/`
  - Update Schedule: `PUT /schedule/{id}/`
  - Delete Schedule: `DELETE /schedule/{id}/`

- **Occupied Seat Management:**
  - List Occupied Seats: `GET /seat/`
  - Create Occupied Seat: `POST /seat/`
  - Retrieve Occupied Seat: `GET /seat/{id}/`
  - Update Occupied Seat: `PUT /seat/{id}/`
  - Delete Occupied Seat: `DELETE /seat/{id}/`

## Running Tests

To run the tests, use the following command:
```bash
    python manage.py test
 ```
## Models
- **Room**
  - `name`: Name of the room.
  - `rows`: Number of rows in the room.
  - `seats_per_row`: Number of seats per row.
- **Movie**
  - `title`: Title of the movie.
  - `poster`: Poster image of the movie.
  - `price`: Price of the movie ticket.
  - `background_image`: Background image for the movie.
  - `duration`: Duration of the movie in minutes.
- **Schedule**
  - `room`: Foreign key to the Room model.
  - `movie`: Foreign key to the Movie model.
  - `start_time`: Start time of the movie.
  - `end_time`: End time of the movie, calculated based on the duration if not provided.
- **OccupiedSeat**
  - `schedule`: Foreign key to the Schedule model.
  - `position`: Array field to store the seat position as `[row, column]`.

## Views
- **RoomViewSet**
  - Handles CRUD operations for the Room model.
- **MovieViewSet**
  - Handles CRUD operations for the Movie model.
- **ScheduleViewSet**
  - Handles CRUD operations for the Schedule model. Includes validation for schedule conflicts.
- **OccupiedSeatViewSet**
  - Handles CRUD operations for the OccupiedSeat model. Includes validation for seat position and conflicts.

## Serializers
- **CustomTokenObtainPairSerializer**
  - Handles user authentication and JWT token generation.
- **RoomSerializer**
  - Serializer for the Room model.
- **MovieSerializer**
  - Serializer for the Movie model.
- **ScheduleSerializer**
  - Serializer for the Schedule model.
- **SeatSerializer**
  - Serializer for the OccupiedSeat model.
