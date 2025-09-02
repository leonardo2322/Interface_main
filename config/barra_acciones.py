from flet import Container, Row, Text, MainAxisAlignment
from config.variables import background_app
from config.tipografia import texto
from UI.card_structura import Cards_Estructura


def container_accion(h=100,botones=[]):
        container_acciones = Container(
            bgcolor=background_app,
            height=h,
            border_radius=10,
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                
                controls=[texto("Acciones","titulo")]+[
                        boton for boton in botones
                ]
            ))
        card_acciones = Cards_Estructura(container_acciones)._build_ui()

        return card_acciones