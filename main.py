from mqtt.client import Client
from camera.camera import Camera
import multiprocessing as mp

 

def main():
    queue = mp.Queue()
    camera = Camera(cameraQueue = queue)
    client = Client(cameraQueue = queue)

    processVideo = mp.Process(target=camera.stream)
    processVideo.start()

    processMessage = mp.Process(target=client.publish)
    processMessage.start()


if __name__ == "__main__":
    main()

