# Flask Hospital Management App

A Flask web application for basic hospital management, featuring admin and patient blueprints, SQLAlchemy models, and a SQLite database.

## Setup

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Initialize the database tables:
   ```
   python create_db.py
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your browser and go to `http://localhost:5000`

## Available Endpoints

- `/` - Homepage (returns "Hello, World!")
- `/admin/dashboard` - Admin dashboard (returns JSON with admin info)
- `/patient/dashboard` - Patient dashboard (returns JSON)
- `/patient/api/register` - Register a new patient (POST, JSON: `{ "name": "vatsal" }`)
- `/patient/<int:patient_id>` - Get patient details (GET)

## Database Structure

- Uses SQLAlchemy ORM with a SQLite database (`hospital.db`).
- Models: Facility, Doctor, Session, Patient, Appointment
- Models are defined in the `models/` directory and use a shared `db` object from `models/__init__.py`.
- Database tables are created by running `create_db.py`.

## Project Structure

- `app.py` - Main Flask application, blueprint registration, and app config
- `admin/` - Admin blueprint
- `patient/` - Patient blueprint and registration endpoint
- `models/` - SQLAlchemy models and db initialization
- `create_db.py` - Script to create all database tables
- `instance/hospital.db` - SQLite database file
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation
- `docs/day_wise_learning.md` - Day-wise learning notes

## Current Situation

- Circular import issues resolved by moving db initialization to `models/__init__.py` and importing db from there in all models and app.py.
- Patient registration endpoint (`/patient/api/register`) accepts JSON and adds a new patient to the database.
- Endpoints for admin and patient dashboards are available.
- Database models for Facility, Doctor, Session, Patient, and Appointment are defined and ready for use.

## Future Work

- Implement authentication and authorization for admin and patient endpoints.
- Add endpoints for doctor and session management.
- Implement appointment booking and token management.
- Add input validation and error handling for all endpoints.
- Create frontend pages for patient and admin interactions.
- Add unit and integration tests for API endpoints.
- Improve API documentation and add OpenAPI/Swagger support. 