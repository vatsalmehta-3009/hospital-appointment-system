## [DATE: 2024-06-09] Flask & SQLAlchemy Learnings

- Understood and resolved Flask circular import issues by moving SQLAlchemy db initialization to models/__init__.py and importing db from there in all models and app.py.
- Learned that models/__init__.py should NOT import any model files to avoid circular dependencies.
- Updated all models to import db from models, not from app.
- Confirmed that blueprints and routes can safely import models after this change.
- Practiced safe unpacking of JSON data into SQLAlchemy models using **request.get_json() and Patient(**data)**, with a note to ensure JSON keys match model fields.
- Clarified how Flask route URLs are constructed with blueprint prefixes and route decorators.