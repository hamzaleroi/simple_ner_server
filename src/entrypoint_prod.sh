source ~/.bashrc
gunicorn --bind 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker --reload main:app