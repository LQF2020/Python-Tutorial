def my_first_function():
  print("Hello, this is my first function.")

def function_with_param(variable):
	print("Hello, this is my variable: " + variable)

def function_with_multiple_params(variable1, variable2):
	print("Hello, this is my first variable: " + variable1)
	print("Hello, this is my second variable: " + variable2)

def print_name_and_age(name, gender):
	print("My name is" + name+",  and my gender is "+gender+".")

## Running Program
my_first_function()

variable = "a"
function_with_param(variable)

variable1 = "a"
variable2 = "b"
function_with_multiple_params(variable1, variable2)

name = "Jola"
gender = "female"
print_name_and_age(name, gender)
