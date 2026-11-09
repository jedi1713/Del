age = int(input("your age please?"))

if (age >= 18):
    print ("you are an adult") 
else:
        print("you are a kid")
        
num = int(input("enter a number"))
if (num > 0):
    print ("positive number ")
else:
    print (no)


numb = int(input("enter a number"))
if (numb % 2 == 0):
    print ("even numbers")
else: 
    print("fish") 

ages = int(input("how old are you"))
if (ages > 18 ):
    print("you can vote ")
else:
    print("you cannot vote")

score = int(input("enter a number"))
if (score >=50):
    print("pass")
else:
    print("fail")

number =int(input("add anumber"))
if (number>100):
    print("big number")
else:
    print("small number")

names = input("add your name")
if (names=="admin"):
    print("welcome admin")
else:
    print("welcome guest")

password = input("add your password")
if (password =="1234"):
    print("access granted")
else:
    print ("access denied")

# 9. Ask the user for a number. If the number is less than 0, print “Negative”, otherwise print “Not negative”.
num = float(input("Enter a number: "))
if num < 0:
    print("Negative")
else:
    print("Not negative")
# 9. Ask the user for a number. If the number is less than 0, print “Negative”, otherwise print “Not negative”.
num = float(input("Enter a number: "))
if num < 0:
    print("Negative")
else:
    print("Not negative")

# 10. Ask the user for the temperature. If the temperature is above 30, print “It’s hot”, otherwise print “It’s not hot”.
temp = float(input("Enter the temperature: "))
if temp > 30:
    print("It’s hot")
else:
    print("It’s not hot")




# 11. Compare two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print("First is larger")
else:
    print("Second is larger or equal")

# 12. Child age check
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
else:
    print("Not a child")

# 13. Divisibility by 5
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

# 14. Ticket entry check
ticket = input("Do you have a ticket? (yes/no): ").strip().lower()
if ticket == "yes":
    print("You may enter")
else:
    print("No entry")

# 15. Mark pass/fail
mark = float(input("Enter your mark: "))
if mark >= 40:
    print("You passed")
else:
    print("You failed")                              

# 16. Zero check
num = float(input("Enter a number: "))
if num == 0:
    print("Zero")
else:
    print("Not zero")

# 17. Gender greeting
gender = input("Enter your gender (male/female): ").strip().lower()
if gender == "male":
    print("Hello Sir")
else:
    print("Hello Madam")

# 18. Day of the week check
day = input("Enter the day of the week: ").strip().capitalize()
if day == "Sunday":
    print("Holiday")
else:
    print("Working day")

# 19. Range check (using only one if-else)
num = float(input("Enter a number: "))
if 50 < num < 100:
    print("In range")
else:
    print("Out of range")

# 20. Salary level check
salary = float(input("Enter your salary: "))
if salary > 30000:
    print("High salary")
else:
    print("Low salary")


    