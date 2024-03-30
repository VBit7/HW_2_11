import sqlalchemy.orm as orm
import sqlalchemy as sqa

from datetime import date


class Base(orm.DeclarativeBase):
    pass


class ContactModel(Base):
    __tablename__ = 'contacts'

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    first_name: orm.Mapped[str] = orm.mapped_column(sqa.String(50), index=True)
    last_name: orm.Mapped[str] = orm.mapped_column(sqa.String(50), index=True)
    email: orm.Mapped[str] = orm.mapped_column(sqa.String(50), index=True)
    phone_number: orm.Mapped[str] = orm.mapped_column(sqa.String(50))
    date_of_birth: orm.Mapped[date] = orm.mapped_column(sqa.Date)
    additional_data: orm.Mapped[str] = orm.mapped_column(sqa.String(250))


# class Todo(Base):
#     __tablename__ = 'todos'
#     # id: Mapped[int] = mapped_column(primary_key=True)
#     title: Mapped[str] = mapped_column(String(50), index=True)
#     description: Mapped[str] = mapped_column(String(250))
#     completed: Mapped[bool] = mapped_column(default=False)