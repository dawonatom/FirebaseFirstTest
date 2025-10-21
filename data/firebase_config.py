import firebase_admin
from firebase_admin import credentials
import os

def initialize_firebase():
    """
    Inicializa la app de Firebase Admin SDK usando variables de entorno.
    """
    # Evita reinicializar la app si ya existe
    if not firebase_admin._apps:
        cred_path = os.getenv('FIREBASE_CREDENTIALS_PATH')
        db_url = os.getenv('DATABASE_URL')

        if not cred_path or not db_url:
            raise ValueError("Las variables FIREBASE_CREDENTIALS_PATH y DATABASE_URL deben estar en .env")

        try:
            # Carga las credenciales [cite: 51]
            cred = credentials.Certificate(cred_path)
            
            # Inicializa la app [cite: 52]
            firebase_admin.initialize_app(cred, {
                'databaseURL': db_url
            })
            print("✅ Conexión a Firebase exitosa.")
        except Exception as e:
            print(f"❌ Error conectando a Firebase: {e}")
            raise