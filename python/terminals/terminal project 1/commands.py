# time imports

from datetime import datetime
import pytz

# commands
command_secret = ['su ls']
commands = [ 'echo', 'time', 'command -ls', 'command_help']

def time():
    
# Get the timezone object for New York
  
      tz_NY = pytz.timezone('America/New_York') 
  
# Get the current time in New York
  
      datetime_NY = datetime.now(tz_NY)
  
# Format the time as a string and print it
  
      print("NY/Amarica time:", datetime_NY.strftime("%H:%M:%S"))
   
# Get the timezone object for London
  
      tz_London = pytz.timezone('Europe/London')
  
# Get the current time in London
  
      datetime_London = datetime.now(tz_London)
  
# Format the time as a string and print it
      print("London/Eerope time:",     datetime_London.strftime("%H:%M:%S"))

def echo():
    echo = input("what would you like to display on the terminal: ")
    print(echo)
    if echo == "hello" or "hi" or "wsp guys":
         print(echo, "dummys")