# EXAMPLE
invoice_records = [
{"company": "Harvay Normen","category":"","department":""},
{"company": "5G Works","category":"","department":""},
{"company": "JB HIFI","category":"","department":""},
{"company": "Optus Store","category":"","department":""}
]


mapping = {
"Harvay Normen": {"category":"Sale","department":"Marketing"},
"5G Works": {"category":"Rebate","department":"Operation"},
"JB HIFI": {"category":"Discount","department":"Account"},
"Optus Store": {"category":"Annal Bouns","department":"IT"},   
}

for invoice in invoice_records:
    # invoice = {"company": "Harvay Normen","category":"","department":""},
    
    target_company = invoice["company"]
    # >> target_company = "Harvay Normen"

    mapping_company = mapping[target_company] 
    # >> mapping_company = {"category":"Sale","department":"Marketing"}

    invoice["category"] = mapping_company["category"] 
    # >> mapping_company["category"] = "Sale"
    # >> invoice["category"] = "Sale"

    invoice["department"] = mapping_company["department"] 
    # >> mapping_company["department"] = "Marketing"
    # >> invoice["department"] = "Marketing"

    # loop 4 times until reach the end of mapping list
    
    # before:
    # invoice = {"company": "Harvay Normen","category":"","department":""},

    # After
    # >> invoice["category"] = "Sale"
    # >> invoice["department"] = "Marketing"
    # invoice = {"company": "Harvay Normen","category":"Sale","department":"Marketing"},



print("")
print("")
print("Before:")
# Before
for invoice in invoice_records:
    print(invoice)


print("")
print("")
print("After:")
# Doing mapping   
for invoice in invoice_records:
    target_company = invoice["company"]
    mapping_company = mapping[target_company] 
    invoice["category"] = mapping_company["category"] 
    invoice["department"] = mapping_company["department"] 
    

for invoice in invoice_records:
    print(invoice)
print("")
    