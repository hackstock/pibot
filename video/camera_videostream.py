from threading import Thread
import cv2

class CameraVideoStream(object):

    def __init__(self, src=0, name="CameraVideoStream"):
        stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.name = name 
        self.stopped = False 

    def start(self):
        t = Thread(target=self.update, name=self.name, args=())
        t.daemon = True
        t.start()

        return self

    def update(self):
        while True:
            if self.stopped:
                return

            (self.grabbed, self.frame) = self.stream.read()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True
        
