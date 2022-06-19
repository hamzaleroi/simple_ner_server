from fastapi import FastAPI
import mysql.connector
import spacy
import uvicorn
from db_utils.crud import log_ners, get_ner_logs
import json
import time

app = FastAPI(host="0.0.0.0", port=8000, reload=True)
nlp = spacy.load("en_core_web_md")




@app.get("/ner_extract/{query}")
async def root(query:str):
    conn = mysql.connector.connect(user='user', password='password', host='db', database='logs')
    start_time = time.time()
    doc = nlp(query)
    ners = dict( [(item.text, item.label_) for item in doc.ents])
    log_list = (query,json.dumps(ners),time.time() - start_time,)
    log_ners(conn,ners=log_list)
    conn.close()
    return ners

@app.get("/logs/{limit}")
async def root(limit:int):
    conn = mysql.connector.connect(
    user='user', password='password', host='db', database='logs'
    )
    results = get_ner_logs(conn, limit=limit)
    conn.close()
    return results


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)