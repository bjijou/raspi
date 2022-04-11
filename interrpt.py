import time
import os
import keyboard

os.system("clear" ) 
def menu():
 print('Menu:')
 print('- OP 1 : 1')
 print('- OP 2 : 2')
 print('- To exit : 0')
 
menu()
option = int(input("Option? ------>:"))

while option !=0:
 if (option == 1):
    print("To leave option 1, press 'q'")
    while True:
     # operaciones a ejecutar .....
     #    
     if keyboard.is_pressed('q'):  # 
        print('You are out of option ')
        break  # finishing the loop
    option=''


 elif (option == 2):
    print("has puesto 2")
    option=''
 else:
    print("option not available.")
    option=''
 time.sleep(0.5)
 menu()
 option = int(input("Option? ------>:"))


'''
if keyboard.is_pressed('0'):  # if key '0' is pressed 
            print('You Pressed Loop !')
        # Bucle 2 menu, salir --> 0        
            while True:
                print('Esperando..')
                 
                if keyboard.is_pressed('a'):  # 
                 print('Salir dl loop')
                 break  # finishing the loop
'''

  
