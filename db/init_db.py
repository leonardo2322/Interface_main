from sqlmodel import SQLModel, create_engine, Session
# from models.camisa import Camisa creacion de las tablas
# from models.pantalon import Pantalon
from models.model import Usuario
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    print("Creating database and tables...")
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)