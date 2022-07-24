from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
import db

class Links(db.base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True)
    long_link = Column(String)
    short_link = Column(String)
    date = Column(String)
    views = Column(Integer)

    def __repr__(self) -> str:
        return f"\n id: {self.id} ; \n \
        long link: {self.long_link} ; \n \
        short link: {self.short_link} ; \n \
        date: {self.date} ; \n \
        views: {self.views}" 

db.base.metadata.create_all()