# -*- coding: utf-8 -*-

import time
import paho.mqtt.client as mqtt
import csv
import json

# Define the callback function for when a message is published
def on_publish(client, userdata, mid, properties=None):
    print("Message Published")

# Create a client instance
client = mqtt.Client()

# Assign the callback function
client.on_publish = on_publish

# Connect to the broker
broker = "127.0.0.1"
port = 1883
client.connect(broker, port, 60)

def csv_to_json(csv_file_path, json_file_path):
    data = []
    
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

csv_file_path1 = 'Sonoma_WML.csv'
json_file_path1 = 'Sonoma_WML.json'
csv_file_path2 = 'Oroville_WML.csv'
json_file_path2 = 'Oroville_WML.json'
csv_file_path3 = 'Shasta_WML.csv'
json_file_path3 = 'Shasta_WML.json'
csv_to_json(csv_file_path1, json_file_path1)
csv_to_json(csv_file_path2, json_file_path2)
csv_to_json(csv_file_path3, json_file_path3)

# Read the written JSON file
with open(json_file_path1, mode='r', encoding='utf-8') as json_file:
    Sonoma_json_data = json.load(json_file)

with open(json_file_path2, mode='r', encoding='utf-8') as json_file:
    Oroville_json_data = json.load(json_file)

with open(json_file_path3, mode='r', encoding='utf-8') as json_file:
    Shasta_json_data = json.load(json_file)

# Publish a message
topics = ["SONOMA/WML" ,"OROVILLE/WML","SHASTA/WML"]
json_data = [Sonoma_json_data, Oroville_json_data, Shasta_json_data]
# Start the loop to process callbacks
client.loop_start()

for i in range(3):
    for list_item in json_data[i]:
        msg = json.dumps(list_item).encode('utf-8')
        info = client.publish(
            topics[i],
            payload=msg,
            qos=0,
        )
    
    info.wait_for_publish()
    print(info.is_published(), "for WML data of", topics[i])


client.loop_stop()
    
    