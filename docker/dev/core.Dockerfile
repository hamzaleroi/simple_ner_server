FROM continuumio/miniconda3:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app

COPY environment.yml .
RUN conda env create -f environment.yml

RUN echo "conda activate spacy_env" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

RUN spacy download en_core_web_md

COPY . /app
EXPOSE 8000
CMD ["bash","entrypoint_dev.sh"]
