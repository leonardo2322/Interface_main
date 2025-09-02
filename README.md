# 📌 Aplicación en Flet

Este proyecto está desarrollado en **Python** utilizando el framework [Flet](https://flet.dev), que permite construir aplicaciones modernas con interfaz gráfica (UI) de manera sencilla y rápida.

## 🚀 Características principales

- Interfaz gráfica basada en **Flet**.
- Sistema modular para organizar la aplicación.
- Uso de **Nav_Bar** para navegación entre secciones.
- Componentes reutilizables como `Cards_Estructura`.
- Integración con base de datos (ejemplo: `SQLModel` o cualquier servicio que se desee conectar).
- Manejo de diálogos (`dlg_callback`) para mostrar mensajes de confirmación o error.

## 📂 Estructura del proyecto

📦 mi_aplicacion
┣ 📂 src
┃ ┣ 📜 main.py # Punto de entrada de la app
┃ ┣ 📜 ui_principal.py # Vista principal con Nav_Bar y contenedores
┃ ┣ 📜 cards_estructura.py # Clase para renderizar tarjetas
┃ ┣ 📜 nav_bar.py # Barra de navegación personalizada
┃ ┣ 📜 services.py # Servicios (ej. CRUD con SQLModel)
┃ ┣ 📜 dialogs.py # Manejo de diálogos y callbacks
┃ ┗ 📜 utils.py # Utilidades varias
┣ 📜 requirements.txt # Dependencias del proyecto
┗ 📜 README.md # Documentación

bash
Copiar
Editar

## 🛠️ Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/mi_aplicacion.git
   cd mi_aplicacion
   Crear un entorno virtual (opcional pero recomendado):
   ```

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate # En Linux / Mac
venv\Scripts\activate # En Windows
Instalar dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
▶️ Ejecución
Para ejecutar la aplicación:

bash
Copiar
Editar
python src/main.py
La aplicación se abrirá en una ventana de escritorio o en tu navegador (según la configuración de Flet).

📦 Dependencias principales
Flet

SQLModel (si usas base de datos)

Otras que tengas en requirements.txt

📖 Uso
La aplicación muestra una vista principal (UI_Principal) que contiene:

Una barra de navegación personalizada.

Contenido central (main) con scroll.

Tarjetas (Cards_Estructura) para mostrar secciones dinámicas.

🤝 Contribución
Haz un fork del proyecto.

Crea una rama (git checkout -b feature-nueva).

Realiza tus cambios y haz commit (git commit -m "Agregada nueva funcionalidad").

Haz push a la rama (git push origin feature-nueva).

Crea un Pull Request.

📄 Licencia
Este proyecto se distribuye bajo la licencia MIT.
