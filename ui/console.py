from presentation.viewmodel import EstudianteViewModel

class AppUI:
    """
    La Interfaz de Usuario (Vista). 
    Solo muestra información y captura entradas.
    """
    def __init__(self, viewmodel: EstudianteViewModel):
        self._vm = viewmodel

    def run(self):
        """Inicia el bucle principal de la aplicación de consola."""
        print("--- 📚 GESTOR DE ESTUDIANTES CON FIREBASE ---")
        while True:
            self._print_menu()
            choice = input("Seleccione una opción: ")

            if choice == '1':
                self._add_student()
            elif choice == '2':
                self._view_students()
            elif choice == '3':
                self._update_student()
            elif choice == '4':
                self._delete_student()
            elif choice == '5':
                print("👋 ¡Adiós!")
                break
            else:
                print("❌ Opción no válida. Intente de nuevo.")

    def _print_menu(self):
        print("\n-- Menú Principal --")
        print("1. Agregar estudiante (Create)")
        print("2. Ver todos los estudiantes (Read)")
        print("3. Actualizar curso de estudiante (Update)")
        print("4. Eliminar estudiante (Delete)")
        print("5. Salir")

    def _add_student(self):
        print("\n-- 1. Agregar Nuevo Estudiante --")
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        curso = input("Curso: ")
        self._vm.add_student(nombre, edad, curso)
        print("¡Estudiante agregado!")

    def _view_students(self):
        print("\n-- 2. Lista de Estudiantes --")
        students = self._vm.get_all_students()
        if not students:
            print("No hay estudiantes registrados.")
        else:
            # Imprime los datos como en la presentación [cite: 68]
            for s in students:
                print(f"  [ID: {s.id}]")
                print(f"  Nombre: {s.nombre}, Edad: {s.edad}, Curso: {s.curso}\n")

    def _update_student(self):
        print("\n-- 3. Actualizar Curso --")
        self._view_students() # Muestra la lista para facilitar
        student_id = input("Ingrese el ID del estudiante a actualizar: ")
        new_course = input(f"Ingrese el nuevo curso para {student_id}: ")
        self._vm.update_student_course(student_id, new_course)
        print("¡Curso actualizado!")

    def _delete_student(self):
        print("\n-- 4. Eliminar Estudiante --")
        self._view_students() # Muestra la lista para facilitar
        student_id = input("Ingrese el ID del estudiante a eliminar: ")
        self._vm.remove_student(student_id)
        print("¡Estudiante eliminado!")