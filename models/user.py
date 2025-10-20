from models import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from dataclasses import dataclass

@dataclass
class User(db.Model):
    __tablename__ = 'user_table'
    id:Mapped[int]=mapped_column(primary_key=True)
    name:Mapped[str]=mapped_column(String(100), nullable=False)
    lastname:Mapped[str]=mapped_column(String(100), nullable=False)
    email:Mapped[str]=mapped_column(String(100),unique=True, nullable=False)
    telephone:Mapped[str]=mapped_column(String(20), unique=True)
    password:Mapped[str]=mapped_column(String(150), nullable=False)