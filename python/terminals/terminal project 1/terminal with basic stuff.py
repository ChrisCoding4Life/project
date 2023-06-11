# command import from hidden file

from commands import *

#time imports 

from datetime import datetime
import pytz

# clear imports

from os import system as sys
from os import *

# title

print("CCT terminal")

# loop

while True:
  
  # input for commands to work
  
    code = input(">>>")
    
  # display the usrs typed text
  
    if code == "echo":
      echo()
    
  # diplay the current time for new york/amarica and london/eerope
  
    if code == "time":
        time()
  
  # display commands
  
    if code == "command -ls":
      command_accses_ls = input("do you want a list of the commands type command ls again for yes for no do nothing and enter?")


    if command_accses_ls == "command -ls":
        print("the regular commands are", commands)
      

    if code == "su -c -ls":
        print(command_secret)

    # displays the command thay need to type to get help
    if code == "command_help":
        print("command -ls use in terminal for a list of commands")

    if code == "math -a":
          num1 = float(input("number1?: "))


    if code != "echo" or "time" or "su -c -ls" or "command -ls" or "command_help":
        print("invalid command")
