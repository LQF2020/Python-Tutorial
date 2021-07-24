def print_hello_world():
	print("Hello world.")

def print_10_times_hello_world():
  for i in range(0,11):
	  print_hello_world()

def function_with_param(variable):
	print("Hello, this is my variable: " + variable)

def function_with_multiple_params(variable1, variable2):
	print("Hello, this is my first variable: " + variable1)
	print("Hello, this is my second variable: " + variable2)

def print_name_and_gender(name, gender):
	print("My name is" + name +",  and my gender is "+gender+".")


# take 2 params e.g. a and b
# return sum of a and b
def sum(part1, part2):
	return part1 + part2

# ## Running Program
# my_first_function()

# variable = "a"
# function_with_param(variable)

# variable1 = "a"
# variable2 = "b"
# function_with_multiple_params(variable1, variable2)

# name = "Jola"
# gender = "female"
# print_name_and_gender(name, gender)

# print_10_times_hello_world()

# part1 = 1
# part2 = 2
# result = sum(part1,part2)
# print(result)

# 写一个函数，计算参数1与参数2的差值（相减）
# 并且判断结果是不是大于10
# 如果是，返回true; 否，返回false

# 变量的作用域
# file 作用域： 全局作用域
# 函数作用域： 局部作用域
def minus(part1, part2):
	result = part1 - part2
	if result > 10:
		return True
	else:
		return False

part1 = 30
part2 = 14
result = minus(part1, part2) # True
result = False


# 定义一个函数，计算参数1与参数2的积（相乘）
# 定义另外一个函数，如下：
# 计算 6和7的积
# 计算 3和8的积
# 计算两个积之间的差值，如果差值小于10，则打印“积小于10”；如果大于10，则打印“大于10”10次

def multiply(part1, part2):
	return part1 * part2

	
part1 = 6
part2 = 7
result1 = multiply(part1, part2)
part1 = 4
part2 = 8
result2 = multiply(part1, part2)

def minus(result1, result2):
	minus = result1 - result2
	if minus < 10:
		print("minus < 10")
	else:
		for i in range(0,11):
			print("minus > 10")

minus(result1, result2)