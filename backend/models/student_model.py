from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


from database import Base


class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100))

    age = Column(Integer)

    department = Column(String(100))

    email = Column(String(100), unique=True, nullable=False)