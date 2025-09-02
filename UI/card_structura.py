from flet import Container, alignment, Colors, padding, Card, Margin, CardVariant


class Cards_Estructura:
    def __init__(self,contenido):
        self.contenido = contenido

    def _card_estructura(self, contenido):
        card = Card(
            content=Container(
                content=contenido,
                padding=padding.all(5),
                alignment=alignment.center,
                margin=Margin(left=0,top=0, right=0, bottom=0),
            ),
            elevation=5,
            shadow_color=Colors.GREY_500,
            color=Colors.BLACK26,
            margin=Margin(left=0,top=0, right=0, bottom=0),
            variant=CardVariant.ELEVATED,
            surface_tint_color=Colors.WHITE
        )
        return card
    

    def _build_ui(self):
        return self._card_estructura(self.contenido)