from db.tabla_base import TableBase
from sqlmodel import Field
from datetime import datetime

class Usuario(TableBase, table=True):
    nombre: str = Field(index=True, nullable=False,unique=True)
    contraseña: str = Field(nullable=False)
    fecha_creacion: datetime = Field(default_factory=datetime.now, nullable=False)
    fecha_modificacion: datetime = Field(default_factory=datetime.now, nullable=False)