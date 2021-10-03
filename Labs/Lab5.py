from datetime import date
    
day = 0
minute = 0
sec = 0

name = input("Enter your name : ")
year = int(input("Enter your birth year : "))
current_year = int(date.today().year)
age = current_year - year
day = age * 366
minute = day * 24 * 60
sec = minute * 60

print("Your age is : {}".format(age))
print("{} you are {} days, {} minutes and {} seconds old.".format(name, day, minute, sec))