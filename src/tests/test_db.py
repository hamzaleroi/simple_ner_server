import sys
import unittest

import mysql.connector
from fastapi.testclient import TestClient

sys.path.append("..")
from db_utils import PARAMS, get_ner_logs, log_ners
from main import app

client = TestClient(app)


class TestDBMethods(unittest.TestCase):
    @classmethod
    def create_test_table(cls, conn):
        sql = """
        CREATE TABLE IF NOT EXISTS test_logs(
        id INT PRIMARY KEY AUTO_INCREMENT,
        request_query TEXT,
        nes TEXT,
        execution_time FLOAT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
        with conn.cursor() as cursor:
            cursor.execute(sql)

    @classmethod
    def truncate_table(cls, conn):
        sql = f"truncate table test_logs"
        with conn.cursor() as cursor:
            cursor.execute(sql)

    @classmethod
    def drop_table(cls, conn):
        sql = f"drop table test_logs"
        with conn.cursor() as cursor:
            cursor.execute(sql)

    def test_log_ners(self):
        conn = mysql.connector.connect(
            user=PARAMS["user"],
            password=PARAMS["password"],
            host=PARAMS["host"],
            database=PARAMS["database"],
        )
        TestDBMethods.create_test_table(conn)
        TestDBMethods.truncate_table(conn)
        log_ners(
            conn,
            table="test_logs",
            nes=(
                "I am Hamza",
                '{"Hamza": "PERSON"}',
                "0.05",
            ),
        )
        results = get_ner_logs(conn, table="test_logs", limit=1)
        TestDBMethods.drop_table(conn)
        conn.close()
        self.assertEqual(
            list(results[0].values())[:-1], ["I am Hamza", {"Hamza": "PERSON"}, 0.05]
        )


if __name__ == "__main__":
    unittest.main()
