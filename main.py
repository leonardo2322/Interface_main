import flet as ft
from utils.recursos import get_resource_path
from UI.ui_sesion import UI_iniciar_sesion
from db.init_db import create_db_and_tables, get_session
from UI.ui_principal import UI_Principal

def main(page:ft.Page):
    create_db_and_tables()
    page.title = "Paper-Systems.. Sistema Estadistico"
    page.window.width = 1470
    page.icon = get_resource_path("statics/img/paper.ico")
    print("Iniciando la aplicacion...")
    def show_dlg(e,data,instancia):
        if data:
            dlg = instancia.from_data(data)
            page.dlg = dlg
            page.open(dlg.build())
            page.update()
        else:
            page.open(instancia.build())
            page.update()

    def route_change(route):
        print(f"📌 Cambiando a la ruta: {page.route}")
        page.views.clear()
        if page.route == "/":
            iniciar_sesion = UI_iniciar_sesion(page, show_dlg)
            page.views.append(ft.View("/", [iniciar_sesion.build()]))
        elif page.route == "/Inicio":
            page.views.append(ft.View("/Inicio", [UI_Principal(page, show_dlg)]))


        page.update()
    page.on_route_change = route_change
    page.go(page.route)


if __name__ == "__main__":
    ft.app(target=main)