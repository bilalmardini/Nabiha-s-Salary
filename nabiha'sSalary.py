while True:
    
        try:
            salary = float(input("Enter your salary: "))
            if salary > 0:
                break
            else:
                print("Cant be 0 or less")
        except ValueError:
            print("Enter digits only")


while True:
        month = input("Enter the name of the month: ").capitalize()
        if month == "January" or month == "February"or month == "March"or month == "April"or month == "May"or month == "June"or month == "July"or month == "August" or month == "September"or month == "October"or month == "November"or month == "December":
            break
        else:
            print("Invalid month")
    
while True:
        try:
             savings = float(input("Enter your savings: "))  
             break
        except:
            print("Invalid. Enter only numbers or decimals")

while True:
        try:
            rent = float(input("Enter your rent fees: "))
            break
        except:
            print("Invalid. Enter only numbers or decimals")
    
while True:
        try:
            electricity = float(input("Enter your electricity fees: "))
            break
        except:
            print("Invalid. Enter only numbers or decimals")

print("Savings: "+str(savings)+", Rent: "+str(rent)+", Electricity: "+str(electricity)+".")
total = savings+rent+electricity

print("Saving + rent + electricity = "+str(total))
remainder = salary - total
print("Remaider of salary: "+str(remainder))
rentElec = (rent*12) + (electricity*12)
print("Estimation of your yearly rent and electricity fees: "+str(rentElec))
salaryP2 = salary**2
print("Your total salary for the month powered by 2: "+str(salaryP2))

salary += 50
salarydiv = salary/savings

print("Adding random 50$ to total salary then dividing it by savings  is: "+str(salarydiv))
