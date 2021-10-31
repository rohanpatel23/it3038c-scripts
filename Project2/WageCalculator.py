name = input(" Name of Employee ")

wage = int(input(" Hourly Wage of Employee "))
hoursWorked = int(input(" How many hours did this" + name + " work this week"))

pay = wage * hoursWorked

overTime = input("If" + name + " worked over time this week please say yes")
overTimeTax = input("If" + name + "Would like to know pay after taxes please say tax")

if overTime == "yes":
    overTime = int(input("How many hours of overtime did they work"))
    overTimePay = (wage * 1.5) * overTime
    total = overTimePay + pay
    print("Total pay is " + str(pay) + " The total amount of hours work is " + str(hoursWorked))

elif overTimeTax == "tax":
    overTimeTax = int(input("How many hours of overtime did they work"))
    overTimePay = (wage * 1.5) * overTimeTax
    total = overTimePay + pay
    totalTax = (total / .14)
    totalOverall = total - totalTax
    print(" Total pay is " + str(pay) + " The total pay with taxes taken is " + str(totalOverall))


else:
    print("Total pay is " + str(pay) + " The total amount of hours work is " + str(hoursWorked))