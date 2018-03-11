print(1)

def currency_converter(rate, euros):
    dollars = euros * rate
    return dollars
r=input("Enter rate: ")
e=input("Enter the euros: ")
print(currency_converter(float(r),float(e)))
#print(currency_converter(100, 1000))

#functions=[currency_converter(100, 1000), currency_converter(100, 2000)]
#print(functions)
