import thread
from event.event_bus import EventBus
from controller.mqtt_controller import MQTTController
from mqtt.client import Client
from camera.camera import Camera
import queue

def main():
     cameraQueue = queue.Queue()
     camera = Camera(cameraQueue = cameraQueue)
     mqttController = MQTTController(mqttClient=Client(), cameraQueue = cameraQueue)
     EventBus.subscribe('stream', mqttController)
     camera.stream()
    

if __name__ == "__main__":
    main()

