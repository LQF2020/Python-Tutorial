#!/usr/local/bin/python3.9

# Example

# 求和数列的最后一位
max_number = 100
# 求和结果
sum = 0
# 计数器
number_counter = 1

while number_counter <= max_number:
    sum = sum + number_counter
    number_counter += 1
 
print("1 到 %d 之和为: %d" % (max_number, sum))



# 小测试
# 求出 1~100 所有偶数之和

# 求和数列的最大位
# max_number = 100
# # 求和结果
# sum = 0
# # 计数器
# number_counter = 1

# while number_counter <= max_number:
#     # 求余
#     if number_counter % 2 == 0:
#         sum = sum + number_counter
#     number_counter += 1 
 
# print("1 到 %d 的所有偶数之和为: %d" % (max_number, sum))