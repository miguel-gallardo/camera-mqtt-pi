
class MQTTController:
     def __init__(self, mqttClient, cameraQueue) -> None:
         self.mqttClient = mqttClient
     
     def handle_event(self, event_type, data=None):
        if event_type == 'stream':
            if data:
                self.mqttClient.publish(cameraQueue.get())
