from flask import Blueprint, jsonify

# Create the admin blueprint
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
def dashboard():
    """Basic admin dashboard endpoint"""
    return jsonify({
        'message': 'Welcome to Admin Dashboard',
        'status': 'active',
        'endpoints': ['/admin/dashboard']
    }) 