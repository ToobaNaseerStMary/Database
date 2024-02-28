from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()
class Module(Base):
    __tablename__ = "Module"
    ModuleID = Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String, nullable=False)
    Code = Column(String, unique=True, nullable=False)
    Level = Column(Integer)
    ModuleLeader = Column(Integer, ForeignKey("User.UserID"), nullable=False)
    CourseID = Column(Integer, ForeignKey("Course.CourseID"), nullable=False)
