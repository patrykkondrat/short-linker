from datetime import datetime
from uuid import uuid4

from sqlalchemy.orm import sessionmaker

import model, db
from .short_link import short_link

Session = sessionmaker(db.engine)
session = Session()

class Tasks:
    # def __init__():
    #     pass

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
    
    def del_by_id(self, id):
        with session:
            links = session.query(model.Links).filter(model.Links.id == id).first()
            session.delete(links)
            session.commit()

#to revision
class Service(Tasks):
    def get_users(self) -> Iterator[User]:
        return self.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        return self.get_by_id(user_id)

    def create_link(self, short_link) -> User:
        uuid = uuid4()

        return self.add(uuid, long_link, short_link, date = datetime.now())

    def delete_user_by_id(self, user_id: int) -> None:
        return self.del_by_id(user_id)


if __name__ == '__main__'
    a = Tasks()
    a.add(1, 'sdadsada','sdasdasd')
    print(a.get_all())