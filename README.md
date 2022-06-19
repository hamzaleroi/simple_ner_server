# Simple NER extractor
This is a simple project for extracting named entities. It uses FastAPI and Spacy.
## How to run the project ?  
To run the project, run the following commands:  
First copy and modify the environment variables to include MYSQL credentials:  
```bash
cp .env.example .env
# Modify .env
```
Then, simply run Docker Compose:  
```bash
[sudo] docker-compose -f docker-compose[-prod].yml up --build
````  

### Optional arguments 
* [sudo]: Depends on your docker installation. If docker is installed sudo-less, you can omit it.
* [-prod]: Add it if you want to run the code in production.

Note that in order to to run the project, you have to have docker and docker-compose installed.

## Program endpoints:  
To preview the endpoints simply visit: `localhost:8000/docs`. There are two endpoints implemented:  
1. Extracting the named entities: /ner_extract/{query}
2. Getting logs up to a limit: logs/{limit}

## Examples: 
The following are examples on the use case of the two endpoints:  

### NER endpoint: 
Let's take the following simple examples and the expected output:  
#### Sentence 1: "I am Hamza"  

Command:  
```bash
curl -X 'GET' \
  'http://localhost:8000/ner_extract/I%20am%20Hamza' \
  -H 'accept: application/json'
````
Expected output:  
```JSON
{
  "Hamza": "PERSON"
}
```

#### Sentence 2: "I am from Algeria"  

Command:  
```bash
curl -X 'GET' \
  'http://localhost:8000/ner_extract/I%20am%20from%20Algeria' \
  -H 'accept: application/json'
````
Expected output:  
```JSON
{
  "Algeria": "GPE"
}
```

#### Sentence 2: "Einstein is from Germany."  

Command:  
```bash
curl -X 'GET' \
  'http://localhost:8000/ner_extract/Einstein%20is%20from%20Germany.' \
  -H 'accept: application/json'
````
Expected output:  
```JSON
{
  "Einstein": "PERSON",
  "Germany": "GPE"
}
```

### Log endpoint: 
After the requests above, we can visualize the logs with a limit of 3. 
Command:  
```bash
curl -X 'GET' \
  'http://localhost:8000/logs/3' \
  -H 'accept: application/json'
````
Expected output (without the timestamp information):  
```JSON
[
    {
    "query": "I am Hamza",
    "named_entities": {
      "Hamza": "PERSON"
    },
    "execution_time": 0.0300872,
    "timestamp": "2022-06-19T16:12:59"
  },
  {
    "query": "I am from Algeria",
    "named_entities": {
      "Algeria": "GPE"
    },
    "execution_time": 0.0186865,
    "timestamp": "2022-06-19T16:15:16"
  },
  {
    "query": "Einstein is from Germany.",
    "named_entities": {
      "Einstein": "PERSON",
      "Germany": "GPE"
    },
    "execution_time": 0.0273702,
    "timestamp": "2022-06-19T16:16:15"
  }
]
```