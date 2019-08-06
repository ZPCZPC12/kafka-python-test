import pandas as pd
import os
import time

from kafka import KafkaConsumer, KafkaProducer
from kafka.errors import KafkaError

class dataHandle():
    def __init__(self):
        self.serverIP = input("Pleae put KAFKA broker IP: ")
        self.topic = input("Please put topic: ")

    def input_file_path(self, file_name):
        return './SampleRaw/' + file_name

    def number_of_files(self):
        self.file_list = os.listdir('./SampleRaw/')
        self.number_files = len(self.file_list)
        print ("Number of files: %d" % (self.number_files,))

    def send_data_KAFKA(self):
        self.broker_servers = [self.serverIP]
        self.topic = self.topic

        producer = KafkaProducer(bootstrap_servers=self.broker_servers, api_version=(0, 10))

        producer.send(self.topic, bytes(self.read_data, encoding = 'utf-8'))

        producer.close()
        print("Send {} datas to producer".format(self.read_data))

    def generate_data(self):
        self.number_of_files()
        for i in self.file_list:
            print ("input file path: {}".format(self.input_file_path(i)))
            total_read = pd.read_csv(self.input_file_path(i), sep=',', header = None, error_bad_lines=False)
            print ("row count: %d" % (len(total_read),))
            for row in range(len(total_read)):
                self.starttime = time.time()
                self.read_data = str(list(total_read.iloc[row]))
                self.send_data_KAFKA()
                time.sleep(0.75 - ((time.time() - self.starttime) % 0.75)) #every 0.75sec, send data

    def __del__(self):
        print ("delete object")

# Main
if __name__ == '__main__':
    root = dataHandle()
    root.generate_data()
