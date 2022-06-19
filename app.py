import json
import time
from typing import Dict

import mysql.connector
import spacy
import uvicorn
from fastapi import FastAPI

from db_utils.crud import get_ner_logs, log_ners

app = FastAPI(host="0.0.0.0", port=8000, reload=True)
nlp = spacy.load("en_core_web_md")


@app.get("/ner_extract/{query}")
async def root(query: str) -> Dict:
    """
    Extract named entities from a text.
    query: The text from which to extract named entities.

    - Returns a dictionary of word and its equivalent named entity.
    """
    conn = mysql.connector.connect(
        user="user", password="password", host="db", database="logs"
    )
    start_time = time.time()
    doc = nlp(query)
    ners = dict([(item.text, item.label_) for item in doc.ents])
    log_list = (
        query,
        json.dumps(ners),
        time.time() - start_time,
    )
    log_ners(conn, ners=log_list)
    conn.close()
    return ners


@app.get("/logs/{limit}")
async def root(limit: int = 1):
    """
    Fetches logs from the database.
    limit: The number of log items to fetch.

    - Returns a list of logged items.s
    """
    conn = mysql.connector.connect(
        user="user", password="password", host="db", database="logs"
    )
    results = get_ner_logs(conn, limit=limit)
    conn.close()
    return results


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
