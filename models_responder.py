import mysql.connector
from sqlalchemy import create_engine, Column, Integer, String, pool
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

def returnDBname(name, database, user=None, password=None, host_ip=None):
    if database.lower() == 'mysql':
        return f'database://{user}:{password}@{host_ip}/{name}?charset=utf8'
    elif database.lower() == 'sqlite':
        return f'sqlite:///{name}.sqlite3'

def connect_MySQL(name, user=None, password=None, host_ip=None):
    engine = create_engine(returnDBname(name, 'MySQL', user=user, password=password, host_ip=host_ip))
    return engine

def connect_SQLite(name):
    engine = create_engine(returnDBname(name, 'SQLite'))
    return engine

engine = connect_SQLite('sample_db')

Base = declarative_base()
Base.metadata.create_all(engine)

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(225))
    user_password = Column(String(225))
    created_at = Column(Integer,)

def get_db():
    return 1

def isAccount(datas):
    conn = get_db()
    conn = conn