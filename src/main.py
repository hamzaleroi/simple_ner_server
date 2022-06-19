import json
import time
from typing import Dict

import mysql.connector
import spacy
import uvicorn
from fastapi import FastAPI, HTTPException

from db_utils import PARAMS
from db_utils.crud import get_ner_logs, log_ners
from ml_utils.ner_extractor import extract_named_entities

app = FastAPI(host="0.0.0.0", port=8000, reload=True)
nlp = spacy.load("en_core_web_md")


@app.get("/ner_extract/{query}")
async def root(query: str) -> Dict:
    """
    Extract named entities from a text.
    query: The text from which to extract named entities.

    - Returns a dictionary of word and its equivalent named entity.
    """
    try:
        conn = mysql.connector.connect(
            user=PARAMS["user"],
            password=PARAMS["password"],
            host=PARAMS["host"],
            database=PARAMS["database"],
        )
        start_time = time.time()
        nes = extract_named_entities(nlp, query)
        log_list = (
            query,
            json.dumps(nes),
            time.time() - start_time,
        )
        log_ners(conn, nes=log_list)
        conn.close()
        return nes
    except:
        raise HTTPException(status_code=503, detail="Error! Try again in a while")


@app.get("/logs/{limit}")
async def root(limit: int = 1):
    """
    Fetches logs from the database.
    limit: The number of log items to fetch.

    - Returns a list of logged items.s
    """
    try:
        conn = mysql.connector.connect(
            user=PARAMS["user"],
            password=PARAMS["password"],
            host=PARAMS["host"],
            database=PARAMS["database"],
        )
        results = get_ner_logs(conn, limit=limit)
        conn.close()
        return results
    except:
        raise HTTPException(status_code=503, detail="Error! Try again in a while")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
