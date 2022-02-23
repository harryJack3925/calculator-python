#Calculator Code With Harry
from ast import operator
import art
from os import system, name

#Add the Number
def add_number(number1, number2):
    return number1 + number2

#Subtract the number
def subtract_number(number1, number2):
    return number1 - number2

#Multiply the number
def multiply_number(number1, number2):
    return number1 * number2

#Divide the number
def divide_number(number1, number2):    
    return number1 / number2

#Exponentiation	the two numbers
def exponentiation_number(number1, number2):
    return number1 ** number2

#Creating clear functions
def clear():  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

logo = art.logo

operations = {
    "+" : add_number,
    "-" : subtract_number,
    "*" : multiply_number,
    "/" : divide_number,
    "**" : exponentiation_number
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()