#from picamera2 import Picamera2
from io import BytesIO
from event.event_bus import EventBus
import cv2
class Camera:
    def __init__(self, cameraQueue) -> None:
        self.video = cv2.VideoCapture(0) 
        # self.camera  = Picamera2()
        # self.camera.configure(self.camera.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
        # self.camera.start()
        # self.stream = BytesIO()
        self.cameraQueue = cameraQueue
        

    def stream(self):

        while True:
            ret, frame = self.video.read()
            self.cameraQueue.put(frame.tobytes()) 
            # im = self.camera.capture_array()
            # self.cameraQueue.append(im)
            # EventBus.publish('stream', {'streaming': True})