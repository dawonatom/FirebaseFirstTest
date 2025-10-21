from firebase_admin import db
from domain.estudiante import Estudiante

class FirebaseRepository:
    """
    Gestiona todas las operaciones CRUD con Firebase Realtime Database.
    """
    def __init__(self):
        # Referencia principal al nodo 'estudiantes' [cite: 59]
        self.ref = db.reference('/estudiantes')

    def create_student(self, estudiante: Estudiante):
        """
        Crea un nuevo estudiante en la DB. (Create) [cite: 55]
        Usa push() para generar un ID automático. [cite: 56]
        """
        try:
            # Envía el diccionario del estudiante [cite: 57, 62]
            new_student_ref = self.ref.push(estudiante.to_dict())
            print(f"Repositorio: Estudiante '{estudiante.nombre}' creado con ID: {new_student_ref.key}")
            return new_student_ref.key
        except Exception as e:
            print(f"Repositorio Error (Create): {e}")
            return None

    def read_students(self):
        """
        Lee todos los estudiantes de la DB. (Read) [cite: 68]
        """
        try:
            data = self.ref.get() # [cite: 68]
            if not data:
                return []
            
            # Convierte el diccionario de Firebase a una lista de objetos Estudiante
            lista_estudiantes = []
            for key, val in data.items(): # [cite: 68]
                estudiante = Estudiante.from_dict(val, id=key)
                lista_estudiantes.append(estudiante)
            
            print(f"Repositorio: {len(lista_estudiantes)} estudiantes leídos.")
            return lista_estudiantes
        except Exception as e:
            print(f"Repositorio Error (Read): {e}")
            return []

    def update_student_course(self, student_id: str, new_course: str):
        """
        Actualiza el curso de un estudiante específico. (Update) [cite: 70]
        """
        try:
            # Referencia directa al estudiante por su ID [cite: 71]
            student_ref = self.ref.child(student_id)
            
            # .update() solo modifica los campos especificados [cite: 70, 71]
            student_ref.update({
                'curso': new_course
            })
            print(f"Repositorio: Curso del estudiante {student_id} actualizado.")
            return True
        except Exception as e:
            print(f"Repositorio Error (Update): {e}")
            return False

    def delete_student(self, student_id: str):
        """
        Elimina un estudiante de la DB. (Delete) [cite: 72]
        """
        try:
            # Referencia directa al estudiante por su ID [cite: 72]
            student_ref = self.ref.child(student_id)
            student_ref.delete() # [cite: 72]
            print(f"Repositorio: Estudiante {student_id} eliminado.")
            return True
        except Exception as e:
            print(f"Repositorio Error (Delete): {e}")
            return False