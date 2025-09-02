from flet import  Column,  TextField,ElevatedButton,MainAxisAlignment, CrossAxisAlignment,Image,ImageFit,Page,Container
from utils.recursos import get_resource_path
from utils.dialogo import dlg_callback
from utils.overlay import overlay_progress
from config.botones_app import boton
img_path = get_resource_path("img/remove_paper.png")


class UI_iniciar_sesion:
    def __init__(self,page:Page,dlg,**kwargs):
        super().__init__(**kwargs)
        self.page = page
        self.show_dlg = dlg
        self.func_dlg = dlg_callback
        self.nombre = TextField(label="nombre", hint_text="Introduzca el nombre")
        self.contraseña = TextField(label="contraseña", hint_text="Introduzca la contraseña",password=True,can_reveal_password=True)
        self.logo = Image(src=img_path,width=200,height=200,fit=ImageFit.CONTAIN,)
        self.submit = ElevatedButton(text="Iniciar sesion",on_click=self.iniciar_sesion)

    def build(self):
        """Builds the UI for the login screen."""
        
        return Column(
            controls=[
                self.logo,
                self.nombre,
                self.contraseña,
                Container(width=20,height=30),
                boton(" Iniciar Sesion ",icon="login",onclick=self.iniciar_sesion,w=350)
            ],
            scroll="always",
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )

    async def iniciar_sesion(self,e):

        # import bcrypt
        e.control.disabled = True
        overlay_progress(self,"Iniciando sesion")
        try:
            print("Iniciando sesion...")
            
            self.page.views.clear()
            self.page.go("/Inicio")
            
        except Exception as e:
            return {"error":str(e)}
        
        finally:
            self.page.overlay.remove(self.loading_overlay)
            e.control.disabled = False
            self.page.update()