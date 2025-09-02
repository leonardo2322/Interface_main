from flet import ProgressRing, Text, Container, Column, alignment

def overlay_progress(self,message):
    self.loading_overlay = Container(
                    content=Column(
                        controls=[
                            ProgressRing(),
                            Text(f"{message}... Por favor espera", size=14)
                        ],
                        alignment="center",
                        horizontal_alignment="center"
                    ),
                    alignment=alignment.center,
                    expand=True,
                    bgcolor="#00000030"  # fondo semitransparente opcional
                )
    self.page.overlay.append(self.loading_overlay)
    self.page.update()