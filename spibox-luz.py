import time
import datetime
import subprocess
import os
import RPi.GPIO as GPIO

def get_file_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

PIR = 4
LUZ = 26

# Tiempo de espera
T_LUZ = 60

def luz_ON():
	GPIO.output(LUZ,GPIO.HIGH)
	
def luz_OFF():
        GPIO.output(LUZ,GPIO.LOW)

def photo():
    for i in range(1,4): # Determina el numero de fotos ???
        capturename = get_file_name()
        print('Motion detected! Taking snapshot')
        cmd="raspistill -w 640 -h 480 -n -t 100 -q 65 -e jpg -th none -o /home/pi/spibox/capture/" + capturename+"_%d.jpg" % (i)
        camerapid = subprocess.call(cmd,shell=True)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(LUZ, GPIO.OUT)
try:
    print "Esperando la senyal del sensor de movimiento..."
 
    # Loop until PIR indicates nothing is happening
    while GPIO.input(PIR)==1:
        Current_State  = 0
 
    print "  Sensor listo"
 
    while True:
        print('Sin actividad...')
        GPIO.wait_for_edge(PIR,GPIO.RISING)
	luz_ON()
#	time.sleep(1) # En principio el programa para sacar la foto ya tiene un tiempo de espera
        photo()
	time.sleep(T_LUZ)
	luz_OFF()

except KeyboardInterrupt:
  print "  Bye for now"
  # Reset GPIO
  GPIO.cleanup()

