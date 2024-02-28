from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()
class Course(Base):
    __tablename__ = "Course"
    CourseID = Column(Integer, primary_key=True, autoincrement=True)
    Title = Column(String, unique=True, nullable=False)
    Award = Column(String, nullable=True)
    CourseLeader = Column(Integer, ForeignKey("User.UserID"), nullable=False)
    SubjectID = Column(Integer, ForeignKey("Subject.SubjectID"), nullable=False)
