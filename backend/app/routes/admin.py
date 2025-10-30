# from flask import Blueprint, jsonify
# from app.utils.security import auth_required, role_required

# bp = Blueprint('admin', __name__, url_prefix='/admin')

# @bp.route('/dashboard', methods=['GET'])
# @auth_required
# @role_required(['admin'])
# def dashboard():
#     return jsonify({'message': 'Panel de administración', 'ok': True}), 200

from flask import Blueprint, jsonify
from app.utils.security import auth_required, role_required

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/dashboard', methods=['GET'])
@auth_required
@role_required(['admin'])
def admin_dashboard():
    return jsonify({"message": "Bienvenido al dashboard de administrador"})