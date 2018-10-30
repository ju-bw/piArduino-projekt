#!/usr/bin/python3
import picamera

camera = picamera.PiCamera()
#camera.capture('image.jpg')
camera.capture('image.jpg', resize=(1920,1080), use_video_port=True, quality=100)
camera.close()