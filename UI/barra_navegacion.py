from flet import Column, Container, IconButton, Row, Text, NavigationRail, NavigationRailDestination, NavigationRailLabelType, Colors, Icons

class Barra_Navegacion:
    def __init__(self,page, destinations,main,dlg,event_bus, *args, **kwargs):
        super().__init__()
        self.bg = "#1E1E1E"
        self.page = page
        self.destinations = destinations if destinations else []
        self.main = main  
        self.show_dlg = dlg
        self.event_bus = event_bus
    def build(self):
        return NavigationRail(
            selected_index=0,
            label_type = NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            group_alignment=0.0,
            bgcolor=self.bg,
            destinations=[
                NavigationRailDestination(
                    icon=item.get("icon",Icons.HELP_OUTLINE),
                    selected_icon= item.get("selected_icon",Icons.HELP),
                    label=item.get("label","--").center(10),
                ) for item in self.destinations
            ],
            height=780,  # Ajusta la altura según tus necesidades
            width=100,   # Ajusta el ancho según tus necesidades
            on_change=lambda e: self._emitir_evento(e.control.selected_index),
        )
    
    def _emitir_evento(self, index):
        accion = self.destinations[index].get("accion")
        if accion:
            self.event_bus.emitir("navegacion", accion)