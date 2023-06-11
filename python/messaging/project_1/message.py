# imports
import os 
import time


            
while True:
        def begining():
            name = input("name?: ")
            pwd = input("Message: ")
      
      # makes a file and loads it for editing
            with open ( f'message, from {name}.txt', 'w') as f:
            
   # writes the text from message and puts into file
              f.write(f'{pwd}')


            time.sleep(1)
            os.system("cls")
            time.sleep(0.5)
