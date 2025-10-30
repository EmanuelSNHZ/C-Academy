import os
import mysql.connector
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de la DB
db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

# Clave secreta para JWT
SECRET_KEY = os.getenv('SECRET_KEY')


def get_db_connection():
    """Devuelve una conexión a la base de datos o None si falla."""
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error al conectar a la DB: {err}")
        return None


def create_app():
    """Factory para crear y configurar la aplicación Flask."""
    app = Flask(__name__)
    CORS(app)

    # Importar y registrar blueprints
    from app.routes.auth import bp as auth_bp
    from app.routes.admin import bp as admin_bp
    from app.routes.student import bp as student_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(student_bp)

    # Ruta de prueba de conexión a la DB
    @app.route('/ping-db')
    def ping_db():
        conn = get_db_connection()
        if conn is None:
            return {"status": "❌ No hay conexión con la DB"}, 500
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()
            return {"status": "✅ Conexión exitosa", "database": db_name[0]}
        finally:
            cursor.close()
            conn.close()

    return app
