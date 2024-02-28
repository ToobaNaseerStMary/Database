from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()
class Subject(Base):
    __tablename__ = "Subject"
    SubjectID = Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String, unique=True, nullable=False)
    SubjectLeader = Column(Integer, ForeignKey("User.UserID"), nullable=False)