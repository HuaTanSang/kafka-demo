import socket
import time
import csv
import json
import logging
from kafka import KafkaProducer
# from kafka.errors import NoBrokersAvailable

# Logger setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

# Wait for Kafka broker to be ready
def wait_for_kafka(host, port, retries=10, delay=3):
    for i in range(retries):
        try:
            with socket.create_connection((host, port), timeout=5):
                logger.info("Kafka broker is ready!")
                return
        except Exception:
            logger.warning(f"Kafka not ready, retry {i+1}/{retries}. Waiting {delay}s...")
            time.sleep(delay)
    raise RuntimeError("Kafka broker is not available after retries.")

wait_for_kafka('kafka', 9092)

# Kafka producer setup
producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Đọc file CSV và gửi lên Kafka
data_file = 'data.csv'
with open(data_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        logger.info(f"Sending row: {row}")
        producer.send('my_topic', value=row)
        producer.flush()
        time.sleep(1)

producer.close()