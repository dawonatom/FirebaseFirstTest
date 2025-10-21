class Estudiante:
    """Define el modelo de datos para un estudiante."""
    def __init__(self, nombre: str, edad: int, curso: str, id: str = None):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

    def to_dict(self):
        """Convierte el objeto a un diccionario para Firebase."""
        return {
            'nombre': self.nombre,
            'edad': self.edad,
            'curso': self.curso
        }

    @classmethod
    def from_dict(cls, source_dict: dict, id: str = None):
        """Crea un objeto Estudiante desde un diccionario."""
        return cls(
            nombre=source_dict.get('nombre'),
            edad=source_dict.get('edad'),
            curso=source_dict.get('curso'),
            id=id
        )

    def __repr__(self):
        """Representación en string del objeto."""
        return f"Estudiante(id={self.id}, nombre={self.nombre}, curso={self.curso})"