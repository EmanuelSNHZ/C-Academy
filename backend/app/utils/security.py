import datetime
import jwt
import bcrypt
from functools import wraps
from flask import request, jsonify
# from app.app import SECRET_KEY
from flask import current_app

# --- Contraseñas ---
def hash_password(plaintext: str) -> str:
    """Hashea una contraseña en texto plano."""
    return bcrypt.hashpw(plaintext.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plaintext: str, hashed: str) -> bool:
    """Verifica que la contraseña ingresada coincida con el hash almacenado."""
    return bcrypt.checkpw(plaintext.encode('utf-8'), hashed.encode('utf-8'))

# --- JWT ---
def create_token(sub: int, role: str) -> str:
    """Crea un JWT con ID de usuario y rol."""
    payload = {
        'sub': str(sub),
        'role': role,
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }
    secret = current_app.config['JWT_SECRET_KEY']
    return jwt.encode(payload, secret, algorithm="HS256")

def decode_token(token: str):
    """Decodifica un JWT y devuelve el payload o None si es inválido/expirado."""
    try:
        secret = current_app.config['JWT_SECRET_KEY']
        return jwt.decode(token, secret, algorithms=["HS256"])
    except jwt.ExpiredSignatureError as e:
        print(f"DEBUG (Token Expirado): {e}")  # <--- LÍNEA NUEVA
        return None
    except jwt.InvalidTokenError as e:
        print(f"DEBUG (Token Inválido): {e}") # <--- LÍNEA NUEVA
        return None
    except Exception as e:
        print(f"DEBUG (Error Inesperado): {e}") # <--- LÍNEA NUEVA
        return None

# --- Decoradores ---
def auth_required(f):
    """Protege una ruta, requiere un token válido en Authorization: Bearer <token>"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            return jsonify({'error': 'Token faltante'}), 401
        token = auth_header.replace('Bearer ', '')
        payload = decode_token(token)
        if not payload:
            return jsonify({'error': 'Token inválido o expirado'}), 401
        request.user = payload
        return f(*args, **kwargs)
    return wrapper

def role_required(allowed_roles):
    """Protege una ruta, requiere que el usuario tenga uno de los roles permitidos."""
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user = getattr(request, 'user', None)
            if not user:
                return jsonify({'error': 'No autenticado'}), 401
            if user.get('role') not in allowed_roles:
                return jsonify({'error': 'No autorizado'}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator