from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Connection
class Conn():
    engine_psg = create_engine('postgresql://********')
    engine_mysql = create_engine('mysql+pymysql://********/')
    # Connection PostgreSQL
    def conn_psg(self):
        return Conn.engine_psg.connect()
    # Conncection MySQL
    def conn_mysql(self): 
        return Conn.engine_mysql.connect()

# Session
class Sess(Conn):
    # Session PostgreSQL
    def session_psg(self):
        return Session(Conn.engine_psg)
    # Session MySQL
    def session_mysql(self):
        return Session(Conn.engine_mysql)
    
