# pylint: skip-file
import datetime

from db_setting import session
from db_tables import *

def isAccount(datas):
    try:
        result = session.query(Users).filter_by(user_name=datas['user_name']).one()
        if result.user_password == datas['user_password']:
            return 1
        else:
            return 0
    except:
        return 0

def signin(datas):
    try:
        session.query(Users).filter_by(user_name=datas['user_name']).one()
    except:
        session.add(Users(user_name=datas['user_name'], user_password=datas['user_password'], created_at=datetime.datetime.now()))
        session.commit()
        return 1
    return 0