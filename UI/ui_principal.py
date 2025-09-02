from flet import Column, Row, MainAxisAlignment, CrossAxisAlignment, Page,ScrollMode
from utils.dialogo import dlg_callback
from config.botones_nav import botones_navegacion
from config.variables import background_app
from UI.barra_navegacion import Barra_Navegacion as Nav_Bar
from utils.Event_bus import EventBus
from utils.dispatcher import MediadorPrincipal
from UI.card_structura import Cards_Estructura

class UI_Principal(Column):
    def __init__(self,page,dlg,**kwargs):
        super().__init__(**kwargs)
        self.page = page
        self.show_dlg = dlg
        self.func_dlg = dlg_callback
        self.event_bus = EventBus()
        self.scroll = ScrollMode.ALWAYS
        self.main = Column(
            scroll=ScrollMode.ALWAYS,
            width=1400,
            height=800,
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
            ,
        )
        self.mediador = MediadorPrincipal(self.main, self.page, self.event_bus, dlg=self.show_dlg)


        self.nav = Nav_Bar(destinations=botones_navegacion, bg=background_app,page=self.page,main=self.main,dlg=self.show_dlg, event_bus=self.event_bus)
        
        
        self.controls.append(
            Row(
                controls=[
                    Cards_Estructura(self.nav.build())._build_ui(),
                    self.main
                ],
                scroll=ScrollMode.ALWAYS,
            )
        )

