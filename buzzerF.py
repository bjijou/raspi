import time
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
#gpio.setup(19,gpio.OUT)


def beep(pinout,tiempoon,tiempooff):
 
        gpio.setup(pinout,gpio.OUT)

        gpio.output(pinout,0)
        time.sleep(tiempoon)
        print ("Beeeep") 
        gpio.output(pinout,1)
        time.sleep(tiempooff)
        gpio.output(pinout,0)        
        
        return "Beep1111"


try:
    beep(19,0.1,0.1)
    beep(19,0.1,0.1)
    beep(19,0.1,0.1)
    time.sleep(1)
    beep(19,2,0.1)
    beep(19,2,0.1)
    beep(19,2,0.1)
 
 # Reset by pressing CTRL + C
except KeyboardInterrupt:
     print("Measurement stopped by User")
     GPIO.cleanup()


