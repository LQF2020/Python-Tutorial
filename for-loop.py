#!/usr/local/bin/python3.9

# Example 1
phone_brand_list = ["OPPO","Realme","Iphone","Samsung","Nokia"]

for phone in phone_brand_list:
    print("")
    print("My phone is "+ phone + " !")

    
# Example 2
phone_brand_list = ["OPPO","Realme","Iphone","Samsung","Nokia"]
Hugo_phone_brand = "Samsung"

for phone in phone_brand_list:
    if phone == Hugo_phone_brand:
        print("")
        print("Hugo's phone is "+ phone + " !")
        
        
# 小测试
# 情景：六合彩抽奖（1-100），中奖号码是18
# 要求：遍历 1- 100，判断号码是否为中奖号码；若是，则打印恭喜中奖信息 "Congrats, you have won the powerball !"