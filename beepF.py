# Usar Python3

from pibeep import pulseBeep,beepDuration

beepDuration(pin=10,duration=.33) #beeper on pin 12, on for .33 sec
pulseBeep(pin=10,freq=16,duration=.5) #pulse beep at 25HZ for 1 seccond




### Informacion
''' 
Beeps

    short: duration 0.05 sec
    medium: duration 0.25 sec
    long: duration 1.00 sec
    warning: pulses 8HZ for 1.5 sec duration
    confirmed: pulses 16HZ for .5 sec duration
    brr: pulses 50HZ for .5 sec duration
Example



beep warning --pin 12 #Warning sound
beep short --pin 12 #Small beep
beep brr --pin 12 #A rumbling sound
beep confirmed --pin 12 #A sound that conveys success


 '''
