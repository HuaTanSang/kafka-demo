# A Kafka demo using Docker 
## Overview 
This repository is that creating a demo of Kafka producer and Kafka consumer with Docker. Kafka-producer will send lines of data in `data.csv` file, which was created by `csv_generator.py`. The consumer will receive data and save as DataFrame. 
## Prerequistes
- Docker 
- Docker Compose 
- Ubuntu 24.04.5 LTS 
## Installation 
- Clone this repository 
```bash
git clone https://github.com/HuaTanSang/kafka-demo.git
``` 
- Go to repository's folder 
```bash
cd kafka-demo
``` 
- Build the docker compose 
```bash
docker compose up --build -d
``` 
- To view what are printing in producer, run this command
```bash 
docker compose logs -f producer 
``` 
- To view what are printing in consumer, run this command
```bash 
docker compose logs -f consumer
```
- To stop containers and clean up 
```bash 
docker compose down -v
```


