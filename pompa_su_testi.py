import datetime
import time
import Jetson.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
RELAIS_1_GPIO = 17
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode


try:
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
    print("başlıyor")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("başladı")
    ilk = datetime.datetime.now()
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
    time.sleep(100)


except:
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
    son = datetime.datetime.now()
    sayac = son - ilk
    print(son, "\n\n\n" , ilk , "\n\n\n" , sayac)

