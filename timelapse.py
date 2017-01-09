from time import sleep
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()
camera.resolution = (1280, 720)
camera.hflip = True
camera.vflip = True
file = open("log.txt", mode='a')

for filename in camera.capture_continuous("img{counter:04d}.jpg"):
    time_now = datetime.now()
    print("Captured {} at {}".format(filename, time_now))
    file.write("Captured {} at {}\n".format(filename, time_now))
    sleep(10)
