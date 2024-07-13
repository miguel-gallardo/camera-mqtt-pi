import paho.mqtt.client as mqtt
import config.settings as settings


class Client:
    def __init__(self, cameraQueue) -> None:
        self.cameraQueue = cameraQueue
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
        self.client.connect(settings.SERVER_MQTT, settings.SERVER_MQTT_PORT)
        self.topic = settings.STREAM_TOPIC
    
    def publish(self):
        while True:
            if  self.cameraQueue.empty() == False:
                data = self.cameraQueue.get()
                self.client.publish(topic = self.topic,payload = data)
            