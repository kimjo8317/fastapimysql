from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

app = {
    'name': 'mysql+pymysql',
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'dbconn': 'fookpro',
    'port': '3305'
}

conn_string=f'{app["name"]}://{app["user"]}:{app["password"]}@{app["host"]}:{app["port"]}/{app["dbconn"]}'


class engineconn:
    def __init__(self):
        self.engine = create_engine(conn_string, pool_recycle=500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def connection(self):
        conn = self.engine.connect()
        return conn


