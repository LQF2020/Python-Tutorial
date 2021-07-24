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
    
# After
for invoice in invoice_records:
    print(invoice)
print("")
    