
import mysql.connector

def log_ners(conn,ners):
    sql = "INSERT INTO logs (request_query, ners, execution_time) VALUES (%s, %s, %s);"
    with conn.cursor() as cursor:
        cursor.execute(sql, ners)
        conn.commit()
