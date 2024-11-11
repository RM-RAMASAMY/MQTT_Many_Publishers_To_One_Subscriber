import paho.mqtt.client as mqtt
import json
import csv
import os
# Delete the CSV file if it exists
if os.path.exists("aggregated_data.csv"):
    os.remove("aggregated_data.csv")
# Define the callback function for when a message is received
def on_message(client, userdata, msg):
    message = json.loads(msg.payload.decode('utf-8'))
    message['topic'] = msg.topic  # Add the topic to the JSON data
    # Open the CSV file in append mode
    with open("aggregated_data.csv", "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=message.keys())
        # Write the header if the file is empty
        if file.tell() == 0:
            writer.writeheader()
        # Write the JSON data to the CSV file
        writer.writerow(message)

# Define the callback function for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    topics = ["SONOMA/WML" ,"OROVILLE/WML","SHASTA/WML"]
    for topic in topics:
        client.subscribe(topic)

# Create a client instance
client = mqtt.Client()

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
broker = "127.0.0.1"
port = 1883
client.connect(broker, port, 60)

# Start the loop to process callbacks
client.loop_forever()