pip install kafka-python
import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json

producer = KafkaProducer(bootstrap_servers=[':0001'], #change ip here
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
producer.send('demo_test', value={'surnasdasdame':'parasdasdmar'})
df = pd.read_csv("data/dataSet.csv")
df.head()

while True:
    sample_data = df.sample(1).to_dict(orient="records")[0]
    producer.send('demo_test', value=sample_data)
    sleep(1)

producer.flush()