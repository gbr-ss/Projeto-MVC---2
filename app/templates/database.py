from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, Declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} #Coisa so para o Sqlite carregar outros negocios 👍
)

Session = sessionmaker(autocomit=False, autoflush=False, bind=engine)

class Base(Declarative_base):
    pass

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()