# pylint: skip-file
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base

# mysqlのDBの設定
DATABASE = 'sqlite:///database.sqlite3'
ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=True
)

# Sessionの作成
Session = sessionmaker(bind=ENGINE)
session = Session()

Base = declarative_base()