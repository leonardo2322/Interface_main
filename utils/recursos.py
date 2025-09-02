import sys
import os

def get_resource_path(relative_path):
    """Obtiene la ruta absoluta al recurso, funciona dentro y fuera del .exe"""
    
    if hasattr(sys, '_MEIPASS'):
        # Ejecutando desde el ejecutable creado por PyInstaller
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(relative_path)