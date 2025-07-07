# Basic Flask App with Admin Blueprint

A simple Flask web application that displays "Hello, World!" on the homepage and includes a basic admin blueprint.

## Setup

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the application:
   ```
   python app.py
   ```

3. Open your browser and go to `http://localhost:5000`

## Available Endpoints

- `/` - Homepage (returns "Hello, World!")
- `/admin/dashboard` - Admin dashboard (returns JSON with admin info)

## What this app does

- Creates a Flask application instance
- Defines a route for the homepage (`/`)
- Includes an admin blueprint with a dashboard endpoint
- Returns "Hello, World!" when you visit the homepage
- Runs in debug mode for development

## Blueprint Structure

The admin blueprint demonstrates:
- Blueprint creation with `url_prefix='/admin'`
- Route definition within the blueprint
- Blueprint registration in the main app

## Files

- `app.py` - Main Flask application
- `admin/__init__.py` - Makes admin directory a Python package
- `admin/routes.py` - Admin blueprint with routes
- `requirements.txt` - Python dependencies
- `README.md` - This file 