class Base_services:
    def __init__(self, repository):
        self.repository = repository  # ya contiene el modelo y la sesión

    def create(self, usuario, contrasena):
        # Verificar si existe el usuario por nombre

        if self.repository.exists_by_field("nombre", usuario):
            raise ValueError("El usuario ya existe")

        # Crear usuario
        return self.repository.create(nombre=usuario, contraseña=contrasena)
    def get_all(self):
        return self.repository.get_all()
    
    def delete(self, id):
        user = self.repository.get_by_id(id)
        if not user:
            raise ValueError("Usuario no encontrado")
        self.repository.delete(user)
        return {"success": True, "message": "Usuario eliminado exitosamente"}