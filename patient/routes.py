from flask import Blueprint, jsonify, request
from models.patient import Patient
from models import db
# Create the admin blueprint
patient_bp = Blueprint('patient', __name__, url_prefix='/patient')


@patient_bp.route('/dashboard')
def dashboard():
    """Basic admin dashboard endpoint"""
    return jsonify({
        'message': 'Welcome to Patient Dashboard',
        'status': 'active',
        'endpoints': ['/patient/dashboard']
    }) 


@patient_bp.route('/api/register', methods=['POST'])
def register_patient():
    data = request.get_json()
    new_patient = Patient(**data)
    db.session.add(new_patient)
    db.session.commit()
    return jsonify({
        'status': 'success',
        'patient_id': new_patient.id,
        'name': new_patient.name
    }), 201


@patient_bp.route('/<int:patient_id>')
def patient_details(patient_id):
    data = request.args.get('abc')
    print(request.args)
    """Basic admin dashboard endpoint"""
    return jsonify({
        'message': f'Welcome to Patient Dashboard {patient_id}',
        'status': 'active',
        'data': data,
        'endpoints': [f'/patient/{patient_id}']
    })