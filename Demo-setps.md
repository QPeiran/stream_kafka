
1. Create my test topic
```
docker compose exec kafka-0 /opt/bitnami/kafka/bin/kafka-topics.sh \
    --create \
    --bootstrap-server kafka-0:9092,kafka-1:9092 \
    --replication-factor 1 \
    --partitions 1 \
    --topic my-test-topic
```

2. Validate the topic is created
```
docker compose exec kafka-0 /opt/bitnami/kafka/bin/kafka-topics.sh \
    --describe --topic my-test-topic \
    --bootstrap-server kafka-0:9092,kafka-1:9092
```

3. Mimic the producer on node 0(from a new ternimal)
```
docker compose exec kafka-0 /opt/bitnami/kafka/bin/kafka-console-producer.sh \
  --bootstrap-server kafka-0:9092,kafka-1:9092 \
  --producer.config /opt/bitnami/kafka/config/producer.properties \
  --topic my-test-topic
```

4. Mimic the consumer on node 1(from a new ternimal)
```
docker compose exec kafka-1  /opt/bitnami/kafka/bin/kafka-console-consumer.sh \
  --bootstrap-server kafka-0:9092,kafka-1:9092 \
  --consumer.config /opt/bitnami/kafka/config/consumer.properties \
  --topic my-test-topic \
  --from-beginning
```


5. Enable the Kafaka UI on port 8080