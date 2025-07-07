from flask import Flask
from admin.routes import admin_bp
from patient.routes import patient_bp
from models import db
app = Flask(__name__)

# Register the admin blueprint
app.register_blueprint(admin_bp)
app.register_blueprint(patient_bp)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
db.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True) 