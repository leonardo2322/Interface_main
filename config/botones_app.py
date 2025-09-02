from flet import ElevatedButton,  ButtonStyle, RoundedRectangleBorder, padding, Icons

def boton(texto,w=150,h=40,onclick=None, icon=None):
    return ElevatedButton(
        texto,
        bgcolor="#2563EB",
        color="white",
        width=w,
        height=h,
        style=ButtonStyle(
        shape=RoundedRectangleBorder(radius=8),
        padding=padding.symmetric(horizontal=16, vertical=10),
    ),
        icon = Icons(value=icon),
        icon_color="white",
        on_click=onclick
    )