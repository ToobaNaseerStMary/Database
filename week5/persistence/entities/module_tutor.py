from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()
class ModuleTutor(Base):
    __tablename__ = "ModuleTutor"
    TutorID = Column(Integer, primary_key=True, autoincrement=True)
    UserID = Column(Integer, ForeignKey("User.UserID"), nullable=False)
    ModuleID = Column(Integer, ForeignKey("Module.ModuleID"), nullable=False)
