from flet import Column, TextField, MainAxisAlignment, Dropdown, dropdown
import bcrypt
class FormularioBase:
    def __init__(self, page, campos_config):
        self.page = page
        self.campos = {}
        self.campos_config = campos_config

        # Construir campos según configuración
        for nombre, cfg in campos_config.items():
            if cfg["tipo"] == "text":
                self.campos[nombre] = TextField(
                    label=cfg.get("label", nombre.capitalize()),
                    hint_text=cfg.get("hint", ""),
                )
            elif cfg["tipo"] == "dropdown":
                self.campos[nombre] = Dropdown(
                    label=cfg.get("label", nombre.capitalize()),
                    options=[dropdown.Option(o) for o in cfg.get("options", [])]
                )
            elif cfg["tipo"] == "password":
                self.campos[nombre] = TextField(
                    label=cfg.get("label", nombre.capitalize()),
                    hint_text=cfg.get("hint", ""),
                    password=True,
                )
        # Contenido principal del formulario
        self.content = Column(
            controls=list(self.campos.values()),
            alignment=MainAxisAlignment.CENTER
        )

    def build(self):
        print(self.campos)
        return self.content

    def obtener_datos(self):
        """Devuelve los datos limpios de los campos."""
        datos = {}
        for nombre, campo in self.campos.items():
            if nombre == "contraseña":
                valor = bcrypt.hashpw(campo.value.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

                datos['contrasena'] = valor  # Guardar como string
            else:
                if nombre == "nombre":
                    valor = campo.value.strip() if campo.value else ""
                    datos['usuario'] = valor
                else:
                    valor = campo.value.strip() if campo.value else ""
                    datos[nombre] = valor

        return datos

    

    def clean(self):
        for campo in self.campos.values():
            campo.value = ""