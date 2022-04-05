import time
import RPi.GPIO as gpio

#gpio.setwarnings(False)
#gpio.setmode(gpio.BOARD)
#gpio.setup(19,gpio.OUT)


def beep(pinout,tiempoon,tiempooff):
        gpio.setwarnings(False)
        gpio.setmode(gpio.BOARD) 
        gpio.setup(pinout,gpio.OUT)

        gpio.output(pinout,0)
        time.sleep(tiempoon)
        gpio.output(pinout,1)
        time.sleep(tiempooff)
        gpio.output(pinout,0)     
        gpio.cleanup()
        return "Beep"
