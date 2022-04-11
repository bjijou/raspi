import os
import time
from buzzer import beep
from distancia import distance
from datetime import datetime
from led import led
from temperatura import Temperatura


COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
          }

# variables

welcome = "[[red]]****** [[blue]]Welcome [[red]]****** [[green]] "
salto = "\n"

# get date time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


# Funciones
def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

def log(text):
    f = open("guard.log", "a")
    f.write(text+"\n")
    f.close 


if __name__ == '__main__':
    try:
        os.system("clear" )  #use this for windows. change to os.system("clear") for linux
        print(salto + salto)
        print(colorText(welcome))
        print("**********  Guard Armed ************")         
        beep(19,1,0.05)
        led(18,1,1)

        ladistancia = str("{0:.2f}".format(distance()))
        temperatura = str("{0:.2f}".format(Temperatura()))

        #Escribir log
        log(dt_string + " - " + ladistancia + " cm. Temp:" + temperatura + " °C")
  
        while True:
            if distance() < 20.00 :
             print ("Distancia:"+ str("{0:.2f}".format(distance())))
             beep(19,0.1,0.02)              
            elif (distance() > 20.00 and distance() < 35.00) :
              print ("Distancia:"+ str("{0:.2f}".format(distance())))         
              beep(19,0.5,0.1)            
            else:
              print ("Temperatura:"+ str("{0:.2f}".format(Temperatura())))
            time.sleep(0.1)
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print(salto)
        print("Service stopped by User")

