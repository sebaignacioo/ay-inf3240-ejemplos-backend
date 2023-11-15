from sqlalchemy.orm import Mapped, mapped_column
from app import db


class Usuario(db.Model):
    username: Mapped[str] = mapped_column(db.String(80), primary_key=True)
    password: Mapped[str] = mapped_column(db.String(80), nullable=False)
    email: Mapped[str] = mapped_column(db.String(120), nullable=False)
    rol: Mapped[str] = mapped_column(db.String(120), nullable=False)