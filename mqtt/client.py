import logging
import paho.mqtt.client as mqtt
import config.settings as settings

logging.basicConfig(level=logging.DEBUG)
class Client:
    def __init__(self) -> None:
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.connect(settings.SERVER_MQTT, settings.SERVER_MQTT_PORT)
        self.client.loop_start()
        self.topic = settings.STREAM_TOPIC
    
    def publish(self, data):
        self.client.publish(topic = self.topic,payload = data)