import os 
import time

def message():
# askes name and anser = put in string
            name = input("name?: ")
            os.system("cls")
# askes Message/suggestions and anser = put in string
            pwd = input("Message/suggestions: ")
            os.system("cls")
# uses name string and makes a file with there name at the end then makes it into a function i geuss?
            with open ( f'suggestion, from {name}.' 'txt', 'w') as f:
   # writes the text from message/suggestions and puts into file
                  f.write(f'{pwd}')
                  # makes a new line
                  f.write('\n')

def calc():

      while True:
            try:
                  # makes a list of operators
                  list_operator = ['+(add)', '- (subtract)', '*(multiply)', '/(divide)',  '//(no remainderl)']
                  print(list_operator)
            except ValueError:
                 continue
                  # gets input from user and temporary stores it
            operator = input("operator?: ")
                  # gets input from user and temporary stores it
            num1 = float(input("number 1?: "))
                  # gets input from user and temporary stores it
            num2 = float(input("number 2?: "))

           

                  # if user chose + then num1 + num2 = result
            if operator != "+":
                                print(num1 + num2)
                                
                  # if user chose - then num1 - num2 = result            
            elif operator != "-":
                                print(num1 - num2)
                                
                  # if user chose *  then num1 * num2 = result           
            elif operator != "*":
                                print(num1 * num2)
                                
                   # if user chose / then num1 / num2 = result             
            elif operator != "/":
                                print(num1 / num2)
                                
                                
                  # if user chose // then num1 // num2 = result(without remainder)
            elif operator != "//":
                              print(num1 // num2)

                  # if not any options then print invalid 
            else:
                                print("Unsupported operator.")

      want_recommend = input("do you want to give a recommendation or message?: ")
      if  want_recommend == "yes" or  "Yes" or  "Y" or "y":
                          message()
      elif  want_recommend == "no" or  "No" or "N" or "n":
                        exit

while True:
                  calc()
                  time.sleep(1)
                  os.system("cls")
