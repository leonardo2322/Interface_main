from sqlmodel import SQLModel, Field

class TableBase(SQLModel):
    id: int = Field(default=None, primary_key=True)

