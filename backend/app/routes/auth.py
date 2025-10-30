from flask import Blueprint, request, jsonify
from app.app import get_db_connection
from app.utils.security import verify_password, create_token, auth_required

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Faltan datos de usuario o contraseña'}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Error interno del servidor (DB)'}), 500

    cur = conn.cursor(dictionary=True)
    try:
        cur.execute("""
            SELECT u.usuarioID, u.nombreUsuario, u.contraseña, r.nombre AS rolNombre
            FROM Usuario u
            JOIN Rol r ON u.rolID = r.rolID
            WHERE u.nombreUsuario = %s
        """, (username,))
        user = cur.fetchone()
    finally:
        cur.close()
        conn.close()

    if not user:
        return jsonify({'error': 'Usuario o contraseña incorrectos'}), 401

    if not verify_password(password, user['contraseña']):
        return jsonify({'error': 'Usuario o contraseña incorrectos'}), 401

    role_map = {'Administrador': 'admin', 'Estudiante': 'student', 'Profesor': 'teacher'}
    role_to_send = role_map.get(user['rolNombre'], 'unknown')

    token = create_token(sub=user['usuarioID'], role=role_to_send)

    return jsonify({
        'message': 'Login exitoso',
        'token': token,
        'role': role_to_send
    }), 200

@bp.route('/me', methods=['GET'])
@auth_required
def me():
    # request.user está seteado por auth_required
    user_payload = getattr(request, 'user', {})
    user_id = user_payload.get('sub')

    conn = get_db_connection()
    if conn is None:
        return jsonify({'error': 'Error interno del servidor (DB)'}), 500

    cur = conn.cursor(dictionary=True)
    try:
        cur.execute("""
            SELECT u.usuarioID, u.nombreUsuario, r.nombre AS rolNombre
            FROM Usuario u
            JOIN Rol r ON u.rolID = r.rolID
            WHERE u.usuarioID = %s
        """, (user_id,))
        profile = cur.fetchone()
    finally:
        cur.close()
        conn.close()

    if not profile:
        return jsonify({'error': 'Usuario no encontrado'}), 404

    role_map = {'Administrador': 'admin', 'Estudiante': 'student', 'Profesor': 'teacher'}
    role = role_map.get(profile['rolNombre'], 'unknown')

    return jsonify({
        'id': profile['usuarioID'],
        'username': profile['nombreUsuario'],
        'role': role
    }), 200