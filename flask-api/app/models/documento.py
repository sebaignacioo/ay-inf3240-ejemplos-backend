from sqlalchemy.orm import Mapped, mapped_column
from app import db


class Documento(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, autoincrement=True,
                                    primary_key=True)
    username: Mapped[str] = mapped_column(db.String(80),
                                          db.ForeignKey('usuario.username'))
    titulo: Mapped[str] = mapped_column(db.String(80), nullable=False)
    contenido: Mapped[str] = mapped_column(db.String(120), nullable=False)
