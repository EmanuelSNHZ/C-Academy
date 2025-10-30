import bcrypt
from app.app import get_db_connection  # reutilizamos tu función de conexión

def hash_passwords():
    """Recorre todos los usuarios y hashea contraseñas en texto plano."""
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        if conn is None:
            print("❌ No se pudo conectar a la base de datos")
            return

        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT usuarioID, contraseña FROM Usuario")
        users = cursor.fetchall()

        print(f"Encontrados {len(users)} usuarios para procesar...")

        for user in users:
            user_id = user['usuarioID']
            plaintext_password = user['contraseña']

            # Si ya está hasheada (bcrypt empieza con $2)
            if plaintext_password.startswith('$2'):
                print(f"Usuario {user_id} ya parece estar hasheado. Omitiendo.")
                continue

            print(f"Hasheando contraseña para usuario {user_id} ({plaintext_password})...")
            hashed_password = bcrypt.hashpw(
                plaintext_password.encode('utf-8'),
                bcrypt.gensalt()
            ).decode('utf-8')

            update_query = "UPDATE Usuario SET contraseña = %s WHERE usuarioID = %s"
            cursor.execute(update_query, (hashed_password, user_id))
        
        conn.commit()
        print("\n✅ ¡Contraseñas actualizadas exitosamente!")

    except Exception as err:
        print(f"Error: {err}")
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    hash_passwords()