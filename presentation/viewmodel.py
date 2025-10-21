from data.repository import FirebaseRepository
from domain.estudiante import Estudiante

class EstudianteViewModel:
    """
    Actúa como puente. La UI habla con él, y él habla con el Repositorio.
    """
    def __init__(self, repository: FirebaseRepository):
        self._repository = repository

    def add_student(self, nombre: str, edad_str: str, curso: str):
        """Valida la entrada y pide al repositorio que cree un estudiante."""
        try:
            edad = int(edad_str) # Validación simple
            # Datos de ejemplo de la presentación [cite: 63, 64, 65]
            nuevo_estudiante = Estudiante(nombre=nombre, edad=edad, curso=curso)
            self._repository.create_student(nuevo_estudiante)
            print("ViewModel: Estudiante agregado.")
        except ValueError:
            print("ViewModel Error: La edad debe ser un número.")
        except Exception as e:
            print(f"ViewModel Error: {e}")

    def get_all_students(self):
        """Pide al repositorio la lista de estudiantes."""
        return self._repository.read_students()

    def update_student_course(self, student_id: str, new_course: str):
        """Valida y pide al repositorio que actualice un curso."""
        if not student_id or not new_course:
            print("ViewModel Error: Se necesita ID y nuevo curso.")
            return
        # Lógica de actualización [cite: 71]
        self._repository.update_student_course(student_id, new_course)
        print("ViewModel: Actualización solicitada.")

    def remove_student(self, student_id: str):
        """Valida y pide al repositorio que elimine un estudiante."""
        if not student_id:
            print("ViewModel Error: Se necesita ID.")
            return
        # Lógica de eliminación [cite: 72]
        self._repository.delete_student(student_id)
        print("ViewModel: Eliminación solicitada.")