from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
import db

class Links(db.base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True)
    long_link = Column(String)
    short_link = Column(String)
    date = Column(DateTime)
    views = Column(Integer)
    
db.base.metadata.create_all()