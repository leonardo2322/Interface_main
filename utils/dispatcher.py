# mediador.py
import flet as ft
from config.barra_acciones import container_accion
from config.botones_app import boton
from config.form_data import usuario
from UI.base_forms import FormularioBase
from utils.dialogo import dlg_callback
from services.base_services import Base_services
from models.model import Usuario
from db.Base_model import Base_Model
from utils.tablas import DataTableManager

class MediadorPrincipal:
    def __init__(self, main, page, event_bus, dlg = None):
        self.main = main
        self.page = page
        self.show_dlg = dlg
        self._repo_usuario = Base_Model(Usuario)
        self._services_usuario = Base_services(self._repo_usuario)
        self.event_bus = event_bus
        self.event_bus.suscribir("navegacion", self.manejar_accion)
        self.form_usuario = FormularioBase(page, campos_config=usuario)
        self._datatables = DataTableManager(main=self.main, dlg=self.show_dlg, page=self.page)


    def manejar_accion(self, accion):
        self.main.controls.clear()

        if accion == "inicio":
            self.mostrar_inicio()
        elif accion == "estadisticas":
            self.mostrar_estadisticas()
        elif accion == "registros":
            self.mostrar_registros()
        elif accion == "salir":
            self.cerrar_sesion()

    def on_save(self,e,options=None):
            # Guardar en BD
        if options == "usuario":
            try:
                self._services_usuario.create_user(**self.form_usuario.obtener_datos())
                dlg_callback(
                    self,
                    e,
                    self.page,
                    "La operación fue exitosa",
                    ft.Text(f"Ha sido agregado satisfactoriamente"),
                    win_height=150,
                    icon=ft.Icons.CHECK_CIRCLE,
                    type_func=True
                    )
            except Exception as ex:
                dlg_callback(
                    self,
                    e,
                    self.page,
                    "Ha ocurrido un error ",
                    ft.Text(f"El Error es: {ex}"),
                    win_height=150,
                    icon=ft.Icons.ERROR,
                    )
            finally:
                self._services_usuario.repository.close()
                self.form_usuario.clean()

        self.page.update()

    def listar_usuarios(self):
        return [(u.id, u.nombre, u.contraseña, u.fecha_creacion, u.fecha_modificacion) for u in self._services_usuario.get_all_users()]

    def mostrar_registros(self):
        self.main.controls.extend([
            
        container_accion(botones=[ 
                boton(
                    "agg usuario",
                    icon = ft.Icons.SUPERVISED_USER_CIRCLE,
                    onclick=lambda e:dlg_callback(
                        self,e,self.page,
                        "Agregar Usuario",
                        self.form_usuario.build(),
                        win_height=250,
                        icon=ft.Icons.SUPERVISED_USER_CIRCLE,
                        action_def=lambda e: self.on_save(e,options="usuario")
                        ),
                
        )]),
            ft.Container(width=20, height=30),
            self._datatables.create_data_table(
                head_table="usuario",
                table_items=["id","nombre","contraseña","fecha_creacion","fecha_modificacion"],
                data=self.listar_usuarios()
                
                ),
            ft.Container(width=20, height=30),

                ])
        self._services_usuario.repository.close()
        self.page.update()
    def mostrar_inicio(self):
        self.main.controls.append(ft.Text("🏠 Pantalla de inicio"))
        self.page.update()

    def mostrar_estadisticas(self):
        self.main.controls.append(ft.Text("📊 Estadísticas"))
        self.page.update()

    def cerrar_sesion(self):
        self.page.views.pop()
        self.page.go("/")
