from sqlalchemy import Column, Integer, String

from database import Base, BaseDAO


class EmployersDB(Base):
    __tablename__ = "employers"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False)
    username = Column(String, nullable=False)
    phone = Column(String, nullable=False)


class EmployersDAO(BaseDAO):
    model = EmployersDB
