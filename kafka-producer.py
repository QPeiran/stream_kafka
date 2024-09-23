from kafka import KafkaProducer, KafkaClient, KafkaAdminClient
import json 

my_client = KafkaClient(bootstrap_servers = 'localhost:9092') ## the default server
print('Kafka Client connected:'+ str(my_client.bootstrap_connected()))

admin_client = KafkaAdminClient(bootstrap_servers = 'localhost:9094') ## the external server
topic_list = admin_client.list_topics()
print(topic_list)

# print("Topics in the Kafka cluster:")
# for topic in topic_list:
#     print(topic)

## add topic if not exists
# my_client.add_topic("talking_from_python")
# data = { 'tag ': 'dummy',
#   'name' : 'Jane',
#   'score': 
#     {'row1': 100,
#       'row2': 200
#      }
# }

# # # To send messages synchronously
# my_producer = KafkaProducer() ## default as bootstrap_servers='localhost:9092'
# print('Producer connected:'+ str(my_producer.bootstrap_connected()))

# jd = json.dumps(data)
# producer.send(b'my-test-topic','msg123456')