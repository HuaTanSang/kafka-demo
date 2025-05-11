import socket
import time
from kafka import KafkaConsumer
import pandas as pd
import json

# Wait for Kafka broker to be ready
def wait_for_kafka(host, port, retries=10, delay=3):
    for i in range(retries):
        try:
            with socket.create_connection((host, port), timeout=5):
                print("Kafka broker is ready for consumer!")
                return
        except Exception:
            print(f"Consumer waiting for Kafka, retry {i+1}/{retries}... sleeping {delay}s")
            time.sleep(delay)
    raise RuntimeError("Kafka broker is not available for consumer after retries.")

wait_for_kafka('kafka', 9092)

# Kafka consumer setup
consumer = KafkaConsumer(
    'my_topic',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

records = []
for message in consumer:
    print(f"Received: {message.value}")
    records.append(message.value)
    if len(records) >= 10:
        break

# Hiển thị DataFrame cuối cùng
df = pd.DataFrame(records)
print("Final DataFrame:")
print(df)