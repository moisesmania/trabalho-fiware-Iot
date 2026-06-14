import paho.mqtt.client as mqtt
import json
import time
import random

client = mqtt.Client()

client.connect("localhost", 1883, 60)

client.loop_start()

try:
    while True:

        sensor001 = {
            "temperature": round(20 + random.uniform(0, 10), 2),
            "humidity": round(50 + random.uniform(0, 20), 2)
        }

        sensor002 = {
            "co2": random.randint(350, 800),
            "pm25": round(random.uniform(5, 30), 2)
        }

        client.publish("/iot/sensor001", json.dumps(sensor001))
        client.publish("/iot/sensor002", json.dumps(sensor002))

        print("Sensor001:", sensor001)
        print("Sensor002:", sensor002)

        time.sleep(5)

except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
    