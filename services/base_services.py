class Base_services:
    def __init__(self, repository):
        self.repository = repository  # ya contiene el modelo y la sesión

    def create_user(self, usuario, contrasena):
        # Verificar si existe el usuario por nombre
        if self.repository.exists_by_field("nombre", usuario):
            raise ValueError("El usuario ya existe")

        # Crear usuario
        return self.repository.create(nombre=usuario, contraseña=contrasena)
    def get_all_users(self):
        return self.repository.get_all()