from .crud import *
import os

MYSQL_SERVER=os.getenv("MYSQL_SERVER") if os.getenv("MYSQL_SERVER")  else "db"
try:
    MYSQL_PORT=int(os.getenv("MYSQL_SERVER")) if os.getenv("MYSQL_SERVER")  else 3306
except:
    MYSQL_PORT=3306
MYSQL_USER=os.getenv("MYSQL_USER") if os.getenv("MYSQL_USER")  else "user"
MYSQL_PASSWORD=os.getenv("MYSQL_PASSWORD") if os.getenv("MYSQL_PASSWORD")  else "password"
MYSQL_DB=os.getenv("MYSQL_DB") if os.getenv("MYSQL_DB")  else "logs"

PARAMS = {
    "host":MYSQL_SERVER,
    "port":MYSQL_PORT,
    "user":MYSQL_USER,
    "password":MYSQL_PASSWORD,
    "database":MYSQL_DB,
}