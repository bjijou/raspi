from time import sleep
import sys



def TypingText(text,delay):

     for letter in text+"\n":
       sleep(delay) # In seconds
       sys.stdout.write(letter)
       sys.stdout.flush()
     return "Ok"
