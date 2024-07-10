import thread
from event.event_bus import EventBus
from event.notification_subscriber import NotificationSubscriber
from camera.camera import Camera
import queue

def main():
    
    notificationSUbscriber = NotificationSubscriber()
    EventBus.subscribe('stream', notificationSUbscriber)
    cameraQueue = queue.Queue()
    camera = Camera(cameraQueue = cameraQueue)
    camera.stream()
    

if __name__ == "__main__":
    main()

