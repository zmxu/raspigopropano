# Raspberry PI GoPro Pano No WiFi option Python file.
# Make sure your GoPro has autoexec.ash
import time
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
delay_period = 0.001

time.sleep(6)
 for angle in range(0, 45):
 setServo(45)
time.sleep(6)
 for angle in range(45, 90):
 setServo(90)
time.sleep(6)
 for angle in range(90, 135):
 setServo(135)
time.sleep(6)
 for angle in range(135, 180):
 setServo(180)
time.sleep(6)
 for angle in range(180, 225):
 setServo(225)
time.sleep(6)
 for angle in range(225, 270):
 setServo(270)
