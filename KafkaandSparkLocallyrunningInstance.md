# Kafka and Spark - Locally running Instance

1. Start Zookeeper Server

```
C:\kafkaTest\kafka_2.12-2.2.0> bin\windows\zookeeper-server-start.bat config/zookeeper.properties
```

2. Start Kafka Server in separate Powershell terminal

```
C:\kafkaTest\kafka_2.12-2.2.0> bin\windows\kafka-server-start.bat config/server.properties
```
3. Run Datasim script in separate Powershell terminal (Ensure that all python depencies have been installed with Pip)
```
C:\kafkaTest> python .\datasim.py
```
4. Run Consumer script (assuming topic is "test") in separate Powershell terminal
```
C:\kafkaTest\kafka_2.12-2.2.0> bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic test --from-beginning
```
5. Run Spark script in separate Powershell terminal
```
C:\kafkaTest\spark-2.4.3-bin-hadoop2.7> bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.2.0 ./spark-k
afka.py localhost:9092 test
```


