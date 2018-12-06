-- drop table if exists results;
-- create table results(
--     Id INTEGER primary key autoincrement,
--     title char(50) not null,
--     `data` text not null,
--     `img` text not null,
--     `created` datetime default CURRENT_TIMESTAMP
-- );

drop TABLE if EXISTS eventlogs;
CREATE TABLE eventlogs(
    log_id INTEGER primary key autoincrement,
    user_id integer,
    event_id integer,
    start_time datetime,
    end_time datetime
);
-- class EventLog(Base):
--     """ event logs """
--     __tablename__ = 'eventlog'

--     log_id = Column('log_id', Integer)
--     user_id = Column('user_id', Integer)
--     event_id = Column('event_id', Integer)
--     start_time = Column('start_time', String(32))
--     end_time = Column('end_time', String(32))

drop table if exists users;
create table users(
    id integer primary key autoincrement,
    user_name text,
    user_password text,
    created_at datetime DEFAULT CURRENT_TIMESTAMP
);
-- class User(Base):
--     """ user model """
--     __tablename__ = 'users'

--     id = Column('id', Integer, primary_key=True)
--     user_name = Column('user_name', String(225))
--     user_password = Column('user_password', String(225))
--     created_at = Column('created_at', String(225))