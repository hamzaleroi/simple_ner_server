
import mysql.connector
from typing import Tuple

def log_ners(conn,ners: Tuple):
    sql = "INSERT INTO logs (request_query, ners, execution_time) VALUES (%s, %s, %s);"
    with conn.cursor() as cursor:
        cursor.execute(sql, ners)
        conn.commit()

def get_ner_logs(conn, limit: int):
    sql = f"SELECT * from logs LIMIT {limit}"
    with conn.cursor() as cursor:
        cursor.execute(sql)
        results = cursor.fetchall() 
    return results