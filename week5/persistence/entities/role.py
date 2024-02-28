from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()
class Role(Base):
    __tablename__ = "Role"
    RoleID = Column(Integer, primary_key=True, autoincement=True)
    RoleName = Column(String, unique=True, nullable=False)
