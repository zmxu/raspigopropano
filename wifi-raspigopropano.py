# Raspberry PI GoPro Pano WiFi option Python file
import time
import urllib2
import {stitch.py}
import RPi.GPIO
def set(property, value):
 try:
 f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
 f.write(value)
 f.close() 
 except:
 print("Error writing to: " + property + " value: " + value)
def setServo(angle):
 set("servo", str(angle))
set("delayed", "0")
set("mode", "servo")
set("servo_max", "180")
set("active", "1")
delay_period = 0.01
#replace PASSWORD by the camera wifi password
for angle in range(0, 45):
setServo(45)
urllib2.urlopen("http://10.5.5.9/bacpac/SH?t=password&p=%01")
time.sleep(2)
for angle in range(45, 90):
setServo(90)
urllib2.urlopen("http://10.5.5.9/bacpac/SH?t=password&p=%01")
time.sleep(2)
for angle in range(90, 135):
setServo(135)
urllib2.urlopen("http://10.5.5.9/bacpac/SH?t=password&p=%01")
time.sleep(2)
for angle in range(135, 180):
setServo(180)
urllib2.urlopen("http://10.5.5.9/bacpac/SH?t=password&p=%01")
time.sleep(2)
for angle in range(180, 225):
setServo(225)
urllib2.urlopen("http://10.5.5.9/bacpac/SH?t=password&p=%01")
time.sleep(2)
for angle in range(225, 270):
setServo(270)
urllib2.urlopen("http://10.5.5.9/bacpac/SH?t=password&p=%01")
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
