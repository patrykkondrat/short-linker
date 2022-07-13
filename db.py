from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

path_to_db  = f"{os.path.dirname(os.path.realpath(__file__))}/sport/"
engine = create_engine(f"sqlite:////{path_to_db}")

Base = declarative_base()

class Links(Base):
    __tablename__ = "links"

    uuid = Column(Integer)
    date = Column(String)
    long_link = Column(String)
    short_link = Column(String)
    views = Column(Integer)
    
Base.metadata.create_all()


