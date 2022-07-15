from datetime import datetime
from uuid import uuid4

from sqlalchemy.orm import sessionmaker

import model, db, short_link

Session = sessionmaker(db.engine)
session = Session()

id : str = 'jazda'
print(id)

class Tasks:
    def get_all(self):
        with session:
            return session.query(model.Links).all()
    
    def get_by_id(self, id):
        with session:
            try:
                return session.query(model.Links).filter(model.Links.id == id).first()
            except:
                return {"dupa": "nie pykło"}

    def add(self, id: int, short: str, long: str, date = datetime.now()):
        with session:
            link = model.Links(id=id, short_link=short, long_link=long, date=date)
            session.add(link)
            session.commit()
            session.refresh(link)
            return link
    
    def del_by_id(self, id: int):
        with session:
            links = session.query(model.Links).filter(model.Links.id == id).first()
            session.delete(links)
            session.commit()

#to revision
class Service(Tasks):
    def get_links(self):
        return self.get_all()

    def get_link_by_id(self, _id):
        return self.get_by_id(_id)

    def create_link(self, long_link):
        uuid = uuid4()
        short_link = short_link.short_link()
        return self.add(uuid, long_link, short_link, date = datetime.now())

    def delete_link_by_id(self, link_id) -> None:
        return self.del_by_id(link_id)


if __name__ == '__main__':
    a = Tasks()
    a.add(1, '111111','sdasdasd')
    a.add(2, 'dsafasfasf','sdassfdsagffs')
    print(a.get_all())