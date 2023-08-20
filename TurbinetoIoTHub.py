import paho.mqtt.client as mqtt
import json
from azure.iot.device import IoTHubDeviceClient, Message

# Azure IoT Hub connection string
connection_string = "your device connection string"

# MQTT Broker details
BROKER_ADDRESS = ""
BROKER_PORT = 

# This is the Subscriber for wind turbine generator and weather station
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker" + str(rc))
    client.subscribe("wt/generator")
    client.subscribe("wt/ws3")

def on_message(client, userdata, message):
    topic = message.topic
    data = json.loads(message.payload)
    # Prepare the dictionary to hold the message data
    message_data = {}

    # Update the corresponding attributes
    if topic == "wt/generator":
        message_data["Current"] = data["current"]
        message_data["Power"] = data["power"]

    elif topic == "wt/ws3":
        message_data["windSpeed"] = data.get("wind_speed", 0.0)
        message_data["windDirection"] = data.get("wind_dir", 0.0)

    send_to_iot_hub(message_data)

def send_to_iot_hub(data):
    try:
        # Create a connection to Azure IoT Hub
        client = IoTHubDeviceClient.create_from_connection_string(connection_string)

        # Create a JSON message with the received data and set the device_id
        message = {
        "windSpeed": data.get("windSpeed", 0.0),
        "windDirection": data.get("windDirection", 0.0),
        "Power": data.get("Power", 0.0),
        "Current": data.get("Current", 0.0),
         }
        # Send the message to Azure IoT Hub
        client.send_message(Message(json.dumps(message)))
        print("Message sent to Azure IoT Hub:", message)

    except Exception as e:
        print("Error sending data to Azure IoT Hub:", str(e))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_ADDRESS, BROKER_PORT, 60)
client.loop_forever()
