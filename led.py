import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module



def led(pinout,times,duration):

    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(pinout, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
    for x in range(times):
      GPIO.output(pinout, GPIO.HIGH) # Turn on
      sleep(duration) # Sleep for 1 second
      GPIO.output(pinout, GPIO.LOW) # Turn off
      sleep(duration) # Sleep for 1 second
           
      


