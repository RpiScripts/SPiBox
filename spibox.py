# Activa el detector de movimiento de SPiBox en el PIN 4
# Conecta el relé al PIN 26 de la Raspberry
# Al recibir aviso de movimiento saca una foto y activa el interruptor o luz

# PENDIENTE
# 

import time
import datetime
import subprocess
import os
import RPi.GPIO as GPIO

def get_file_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

PIR = 4
LUZ = 26
def photo():
    for i in range(1,2):
        capturename = get_file_name()
        print('Motion detected! Taking snapshot')
        cmd="raspistill -w 640 -h 480 -n -t 10 -q 10 -e jpg -th none -o /home/pi/spibox/capture/" + capturename+"_%d.jpg" % (i)
        camerapid = subprocess.call(cmd,shell=True)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR, GPIO.IN, GPIO.PUD_DOWN)
#GPIO.setup(LUZ, GPIO.OUT)
GPIO.setup(LUZ, GPIO.OUT, initial=1)    # set initial value option (1 or 0)  
try:
    print "Turning on motion sensor..."
 
    # Loop until PIR indicates nothing is happening
    while GPIO.input(PIR)==1:
        Current_State  = 0
 
    print "  Sensor ready"
 
    while True:
        print('Waiting for movement')
        GPIO.wait_for_edge(PIR,GPIO.RISING)
        photo()
	# Enciendo la luz -> puedo llamar a una fucncion
	GPIO.output(LUZ, GPIO.LOW)		# De momento no funciona

except KeyboardInterrupt:
  print "  Bye for now"
  # Reset GPIO
  GPIO.cleanup()
