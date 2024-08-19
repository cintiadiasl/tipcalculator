'''
Cíntia Dias Lindolfo
Tip Calculator
'''

print("**************************************")
print("            Tip Calculator            ")
print("**************************************")

#Questions
print("Welcome to the tip calculator!")
total_bill = float(input("Whats was the total bill? € "))
percent_tip = int(input("How much tip would you like to give? \n10, 12 or 15: "))
people = int(input("How many people to split the bill? "))

#Calculation
#pay = (percent_tip / 100 * total_bill + total_bill) / people
#pay = (total_bill * (1 + percent_tip/100)) / people
increase = percent_tip / 100
pay = ((total_bill * increase) + total_bill) / people

#return

#print("The total for person is = " + str(round(pay, 2)) + "€")
# or using f string
pay = round(pay, 2)
print(f"The total for person is = {pay}")
print("**************************************")
