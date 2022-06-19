import json
from typing import Tuple

import mysql.connector


def log_ners(conn, nes: Tuple, table: str = "logs"):
    sql = (
        f"INSERT INTO {table} (request_query, nes, execution_time) VALUES (%s, %s, %s);"
    )
    with conn.cursor() as cursor:
        cursor.execute(sql, nes)
        conn.commit()


def get_ner_logs(conn, limit: int, table: str = "logs"):
    sql = f"SELECT * from {table} LIMIT {limit}"
    with conn.cursor() as cursor:
        cursor.execute(sql)
        results = cursor.fetchall()
    return [
        {
            "query": result[1],
            "named_entities": json.loads(result[2]),
            "execution_time": result[3],
            "timestamp": result[4],
        }
        for result in results
    ]
