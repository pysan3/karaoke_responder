import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from db_setting import Base
from db_setting import ENGINE

class EventLog(Base):
    """ event logs """
    __tablename__ = 'eventlog'

    log_id = Column('log_id', Integer)
    user_id = Column('user_id', Integer)
    event_id = Column('event_id', Integer)
    start_time = Column('start_time', String(32))
    end_time = Column('end_time', String(32))

class Users(Base):
    """ users model """
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    user_name = Column('user_name', String(225))
    user_password = Column('user_password', String(225))
    created_at = Column('created_at', String(32))

def main(args):
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    print('do you really want to reload database?')
    print('hit enter to reload')
    input()
    main(sys.argv)