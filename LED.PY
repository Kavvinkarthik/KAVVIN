1. import RPi.GPIO as GPIO
2. from time import sleep
3. GPIO.setwarnings(False)
4. GPIO.setmode(GPIO.BCM)
5. GPIO.setup(18,GPIO.OUT)
6. while True:
.....GPIO.output(18,GPIO.HIGH)
.....print ("LED ON")
.....sleep(1)
....GPIO.output(18,GPIO.LOW)
....print ("LED OFF")
....sleep(1)
