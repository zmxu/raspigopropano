# Raspberry PI GoPro Pano WiFi option Python file
import time
import urllib2
import {stitch.py}
import RPi.GPIO
#replace PASSWORD by the camera wifi password
{move servo 45 degrees}
urllib2.urlopen("http://10.5.5.9/camera/SH?t=PASSWORD&p=%02")
time.sleep(2)
{move servo 45 degrees}
urllib2.urlopen("http://10.5.5.9/camera/SH?t=PASSWORD&p=%02")
time.sleep(2)
{move servo 45 degrees}
urllib2.urlopen("http://10.5.5.9/camera/SH?t=PASSWORD&p=%02")
time.sleep(2)
{move servo 45 degrees}
urllib2.urlopen("http://10.5.5.9/camera/SH?t=PASSWORD&p=%02")
time.sleep(2)
{move servo 45 degrees}
urllib2.urlopen("http://10.5.5.9/camera/SH?t=PASSWORD&p=%02")
time.sleep(2)
{move servo 45 degrees}
urllib2.urlopen("http://10.5.5.9/camera/SH?t=PASSWORD&p=%02")
time.sleep(3)
urllib2.urlretrieve("http://10.5.5.9:8080/videos/DCIM/XXXGOPRO") # XXX is the number of the folder your gopro creates
-------------
| Stitch:
| SRC: usr/downloads
| Target: usr/downloads/raspigopropano
| Degrees: 270
| Number of pics: 6
-------------
time.sleep(4)
print("Pano finished, be a hero.")
