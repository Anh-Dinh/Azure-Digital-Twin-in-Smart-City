import os
import random
import time
from datetime import date, datetime
import json
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=firsthub.azure-devices.net;DeviceId=windturbine1;SharedAccessKey=lFXb5ZDDEYTv36VLKOOfva422EIgJUzpkVW+Bl07VpU="

MSG_TXT = '{{"windSpeed": {windSpeed},"windDirection": {windDirection},"Power": {Power},"Current": {Current}}}'


def simulate_turbine(client):
    print('IoT Hub device sending periodic messages')
    client.connect()

    while True:

        current = random.randint(0, 2)
        power  = random.randint(0, 5)
        wind_dir = random.randint(0, 360)
        wind_speed = random.randint(0, 10)
        # print(str(current) + " " + str(power))
        data = {
            "current": current, 
            "power": power,
            "wind_dir": wind_dir,
            "wind_speed": wind_speed
        }

        msg_txt_formatted= MSG_TXT.format(
            windSpeed=wind_speed,
            windDirection=wind_dir,
            Power=power,
            Current=current
        )
        message = Message(msg_txt_formatted, content_encoding="utf-8", content_type="application/json")

        client.send_message(message)

        print(f"Sent message: {message}")
        time.sleep(10)

def main():
    print("Simulated wind turbine device")
    print("Press Ctrl-C to exit")

    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    try:
        simulate_turbine(client)
    except KeyboardInterrupt:
        print("IoTHubClient sample stopped by user")
    finally:
        print("Shutting down IoTHubClient")
        client.shutdown()  

if __name__ == "__main__":
    main()
