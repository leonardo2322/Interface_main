from flet import Text, TextAlign, FontWeight

def texto(text,tipo = "cuerpo"):
    if tipo == "cuerpo":
        return Text(
            value=str(text),
            size=14,
            color="white",
            font_family="Roboto",
            text_align=TextAlign.CENTER,
            weight=FontWeight.W_400

        )
    elif tipo == "titulo":
        return Text(
            value=str(text),
            size=18,
            color="white",
            font_family="Inter",
            text_align=TextAlign.CENTER,
            weight=FontWeight.W_700
        )
    else:
        return Text(
                    value=str(text),
                    size=14,
                    color="white",
                    font_family="JetBrains Mono",
                    text_align=TextAlign.CENTER,
                    weight=FontWeight.W_400
                )

      