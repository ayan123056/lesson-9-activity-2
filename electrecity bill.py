unit = int(input("enter the units(that was not a question)"))
if unit <50:
    amount = unit*2.6
    tax = 25
elif unit<=100:
    Amount = 130+((unit-50)*3.25)
    tax = 35
elif unit<=200:
    Amount =130+162.5+((unit-100)*5.26)
    tax = 45 
else:
    amount = 130+162.5+526+((unit-200)*8.45)
    tax = 75
total_amount = amount+tax
print("electricity bill = ",total_amount)