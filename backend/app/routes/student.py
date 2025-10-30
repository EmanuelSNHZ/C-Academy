# from flask import Blueprint, jsonify
# from app.utils.security import auth_required, role_required

# bp = Blueprint('student', __name__, url_prefix='/student')

# @bp.route('/dashboard', methods=['GET'])
# @auth_required
# @role_required(['student'])
# def dashboard():
#     return jsonify({'message': 'Panel de estudiante', 'ok': True}), 200

from flask import Blueprint, jsonify
from app.utils.security import auth_required, role_required

bp = Blueprint('student', __name__, url_prefix='/student')

@bp.route('/dashboard', methods=['GET'])
@auth_required
@role_required(['student'])
def student_dashboard():
    return jsonify({"message": "Bienvenido al dashboard de estudiante"})