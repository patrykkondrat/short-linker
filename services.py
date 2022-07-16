from datetime import datetime
from typing import Iterator

from sqlalchemy.orm import sessionmaker

import model, db, short_link

Session = sessionmaker(db.engine)
session = Session()

class Tasks:
    def get_all(self) -> Iterator[model.Links]:
        with session:
            return session.query(model.Links).all()
    
    def get_by_id(self, id: int):
        with session:
            linker = session.query(model.Links).filter(model.Links.id == id).first()
            if not linker:
                raise IdNotFoundInDatabase
            return linker

    def add(self, id: int, short: str, long: str, date = datetime.now(), views=1):
        with session:
            link = model.Links(id=id, long_link=long, short_link=short, date=date, views=views)
            if not link:
                raise IdNotFoundInDatabase
            session.add(link)
            session.commit()
            session.refresh(link)
            
            return link
    
    def del_by_id(self, id: int):
        with session:
            links = session.query(model.Links).filter(model.Links.id == id).first()
            session.delete(links)
            session.commit()
            session.refresh(links)

#to revision
class Service(Tasks):
    def get_links(self):
        return self.get_all()

    def get_link_by_id(self, _id: int):
        return self.get_by_id(_id)

    def create_link(self, id: int, long_link: str) -> model.Links:
        short_links = short_link.short_link()
        return self.add(id, long_link, short_links, date = datetime.now(), views=1)

    def delete_link_by_id(self, link_id: int) -> None:
        return self.del_by_id(link_id)

class IdNotFoundInDatabase(Exception):

    def __init__(self):
        super().__init__(f"Id is not in database.")

if __name__ == '__main__':
    # Task interview
    # a = Tasks()
    # a.add(11, 'sdasda', 'fsafasfasfsfaf')
    # a.del_by_id(2)
    # print(a.get_all())

    #Service interview
    b = Service()
    print(b.create_link(3, 'costam.com/sdsafaf/sfassfa/dsafaf'))