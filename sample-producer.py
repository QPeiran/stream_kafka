from kafka import SimpleProducer, KafkaClient
import json 

data = { 'tag ': 'dummy',
  'name' : 'Jane',
  'score': 
    {'row1': 100,
      'row2': 200
     }
}

# To send messages synchronously
kafka = KafkaClient('localhost:9092')
producer = SimpleProducer(kafka)
jd = json.dumps(data)
producer.send_messages(b'my-test-topic',jd)