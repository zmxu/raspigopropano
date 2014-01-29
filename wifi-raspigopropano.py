# Raspberry PI GoPro Pano WiFi option Python file
import time
import urllib2
import {stitch.py}
import RPi.GPIO
#replace PASSWORD by the camera wifi password
{move servo 45 degrees}
urllib2.urlopen("http://10.5.5.9/camera/SH?t=PASSWORD&p=%02")
time.sleep(2)
