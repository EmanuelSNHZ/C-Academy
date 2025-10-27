import os
import mysql.connector
import jwt
import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import bcrypt # Para hashear y verificar contraseñas

# Cargar variables de entorno desde .env
load_dotenv()

app = Flask(__name__)

CORS(app)


db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}


SECRET_KEY = os.getenv('SECRET_KEY')

def get_db_connection():
    
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error al conectar a la DB: {err}")
        return None

@app.route('/login', methods=['POST'])
def login():
    """Maneja el endpoint de inicio de sesión."""
    
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Faltan datos de usuario o contraseña"}), 400

    username = data.get('username')
    password_from_user = data.get('password') # Contraseña en texto plano

    conn = None
    cursor = None

    try:
        conn = get_db_connection()
        if conn is None:
            return jsonify({"error": "Error interno del servidor (DB)"}), 500
        
        # dictionary=True devuelve resultados como diccionarios (ej: user['nombreUsuario'])
        cursor = conn.cursor(dictionary=True) 

        # Consultar la DB por el usuario y su ROL
        query = """
        SELECT u.usuarioID, u.nombreUsuario, u.contraseña, r.nombre AS rolNombre
        FROM Usuario u
        JOIN Rol r ON u.rolID = r.rolID
        WHERE u.nombreUsuario = %s
        """
        cursor.execute(query, (username,))
        user = cursor.fetchone() # Obtener el primer resultado

        # Validar usuario
        if not user:
            # mensaje genérico por seguridad
            return jsonify({"error": "Usuario o contraseña incorrectos"}), 401 

        # validar contraseña
        password_from_db = user['contraseña'].encode('utf-8')
        password_from_user_encoded = password_from_user.encode('utf-8')

        # bcrypt para comparar la clave de la DB con la enviada
        if not bcrypt.checkpw(password_from_user_encoded, password_from_db):
            return jsonify({"error": "Usuario o contraseña incorrectos"}), 401

        # Traducir el rol de la bd a algo que espere el front
        role_name_from_db = user['rolNombre']
        
        role_to_send = 'unknown'
        if role_name_from_db == 'Administrador':
            role_to_send = 'admin'
        elif role_name_from_db == 'Estudiante':
            role_to_send = 'student'
        elif role_name_from_db == 'Profesor':
            role_to_send = 'teacher' # JS no maneja 'teacher', a futuro

        # Token (JWT)
        token_payload = {
            'sub': user['usuarioID'], # ID del usuario
            'role': role_to_send,
            'iat': datetime.datetime.utcnow(), # Hora de creación
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24) # expira en 24 horas
        }
        token = jwt.encode(token_payload, SECRET_KEY, algorithm='HS256')

        # Envia respuesta al frontend
        return jsonify({
            "message": "Login exitoso",
            "token": token,
            "role": role_to_send
        }), 200

    except mysql.connector.Error as err:
        print(f"Error de base de datos: {err}")
        return jsonify({"error": "Error interno del servidor"}), 500
    except Exception as e:
        print(f"Error inesperado: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500
    finally:
        # Siempre cerrar la conexión
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    
    app.run(debug=True, port=5000)