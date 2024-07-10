from picamera2 import Picamera2
from io import BytesIO
from event.event_bus import EventBus
class Camera:
    def __init__(self, cameraQueue) -> None:
        self.camera  = Picamera2()
        self.stream = BytesIO()
        self.cameraQueue = cameraQueue
        

    def stream(self):
        self.camera .resolution = (100, 60)
        self.camera .framerate = 30
        while True:
            self.camera.capture(self.stream, format='jpeg', use_video_port=True)
            self.cameraQueue.append(self.stream.getvalue())
            EventBus.publish('stream', {'streaming': True})