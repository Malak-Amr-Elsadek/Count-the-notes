Dollar=int(input("Enter payment:"))

Dollar100=Dollar//100
Dollar50=(Dollar%100)//50
Dollar10=((Dollar%100)%50)//10

print("100 dollars needed is :",Dollar100)
print("50 dollars needed is :",Dollar50)
print("10 dollars needed is :",Dollar10)