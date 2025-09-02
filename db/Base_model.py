from sqlmodel import  select
from db.init_db import get_session

class Base_Model:
    def __init__(self, model_class):
        self.model = model_class
        self.session = get_session()  # cada repositorio tiene su propia sesión
    def close(self):
        self.session.close()
    def get_by_id(self, id: int):
        statement = select(self.model).where(self.model.id == id)
        return self.session.exec(statement).first()

    def exists_by_field(self, field_name: str, value) -> bool:
        field = getattr(self.model, field_name)
        statement = select(self.model).where(field == value)
        return self.session.exec(statement).first() is not None

    def create(self, **kwargs):
        instance = self.model(**kwargs)
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def get_all(self):
        statement = select(self.model)
        return self.session.exec(statement).all()
    
    def update(self, instance, **kwargs):
        for key, value in kwargs.items():
            setattr(instance, key, value)
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance
    
    def delete(self, instance):
        self.session.delete(instance)
        self.session.commit()