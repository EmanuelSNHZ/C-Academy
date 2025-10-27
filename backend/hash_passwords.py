import mysql.connector
import bcrypt
from dotenv import load_dotenv
import os

load_dotenv()

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

def hash_passwords():
    
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT usuarioID, contraseña FROM Usuario")
        users = cursor.fetchall()

        print(f"Encontrados {len(users)} usuarios para procesar...")

        for user in users:
            user_id = user['usuarioID']
            plaintext_password = user['contraseña']

            if plaintext_password.startswith('$2'):
                print(f"Usuario {user_id} ya parece estar hasheado. Omitiendo.")
                continue

            print(f"Hasheando contraseña para usuario {user_id} ({plaintext_password})...")
            hashed_password = bcrypt.hashpw(plaintext_password.encode('utf-8'), bcrypt.gensalt())

            update_query = "UPDATE Usuario SET contraseña = %s WHERE usuarioID = %s"
            cursor.execute(update_query, (hashed_password.decode('utf-8'), user_id))
        
        conn.commit()
        print("\n¡Contraseñas actualizadas exitosamente!")
        print("Ahora la contraseña 'admin123' se ve como: ", hashed_password.decode('utf-8'))

    except mysql.connector.Error as err:
        print(f"Error de base de datos: {err}")
        if conn:
            conn.rollback() 
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    hash_passwords()