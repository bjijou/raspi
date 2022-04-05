import os
import time
from buzzer import beep
from distancia import distance
from datetime import datetime
from led import led


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

welcome = "[[red]]****** Welcome [[blue]]* Welcome [[yellow]]* Welcome [[red]]* Welcome [[green]]* Welcome ******"
emoj = "\U0001f600   " + "\U0001F606   " + "\U0001F440   " + "\U0001F441   " + "\U0001F6A8   " + "\U0001F515   "
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
        print(emoj)
#        print("beep")
#        beep(19,1,0.1)
        led(18,3,1)
#        beep(19,1,0.8)  

        ladistancia = str("{0:.2f}".format(distance()))

         
#        print ("La distancia: "+ ladistancia)
        #Escribir log
        log(dt_string + " - " + ladistancia + " cm.")
  
        while True:
            if distance() < 25.00 :
 #             print ("Distancia:"+ str("{0:.2f}".format(distance())))
              beep(19,0.1,0.1)
            elif (distance() > 25.00 and distance() < 35.00) :
              print ("Distancia:"+ str("{0:.2f}".format(distance())))         
#              beep(19,0.5,0.1)  
#            elif distance() > 40 :
#               print ("Distancia:"+ str("{0:.2f}".format(distance())))
            else:
               print ("nada")
#            print ("Distancia:"+ str("{0:.2f}".format(distance())))
            time.sleep(0.7)
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print(salto)
        print("Service stopped by User")

