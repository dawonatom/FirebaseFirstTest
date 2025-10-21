import sys
import os
from dotenv import load_dotenv

# --- Configuración de Paths ---
# Agrega la carpeta raíz al path de Python para
# permitir importaciones como 'from domain.estudiante import Estudiante'
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
# ------------------------------

# Importa las clases de las diferentes capas
from data.firebase_config import initialize_firebase
from data.repository import FirebaseRepository
from presentation.viewmodel import EstudianteViewModel
from ui.console import AppUI

def main():
    """Punto de entrada principal de la aplicación."""
    
    # Carga las variables del archivo .env 
    load_dotenv()
    
    try:
        # 1. Conectar a Firebase
        initialize_firebase()
        
        # 2. "Inyección de Dependencias" (Conectar las capas MVVM)
        # La Vista depende del ViewModel, que depende del Repositorio.
        repository = FirebaseRepository()       # Capa de Datos (Modelo) 
        viewmodel = EstudianteViewModel(repository) # Capa ViewModel 
        ui = AppUI(viewmodel)                   # Capa de Vista 
        
        # 3. Iniciar la aplicación
        ui.run()
        
    except Exception as e:
        print(f"❌ Error fatal al iniciar la aplicación: {e}")
        print("Verifica tu archivo .env y que el archivo .json de credenciales exista.")

if __name__ == "__main__":
    main()