from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import os

path_to_db  = f"{os.path.dirname(os.path.realpath(__file__))}/sport/"
engine = create_engine(f"sqlite:////{path_to_db}")

base = declarative_base(bind=engine)




