No wahala, this one na the *mumu-simple noob version* - as if na you just learn Python yesterday. No big grammar, no f-string too much.

Copy am:
# 1
name = "Jedidiah"
age = 17
height = 1.75
student = True
print(name)
print(age)
print(height)
print(student)

# 2
a = 10
b = 5
c = 2.5
d = 1.5
print(a + b)
print(a - b)
print(c * d)
print(c / d)

# 3
name = input("Enter your name: ")
age = input("Enter your age: ")
colour = input("Enter your favourite colour: ")
print("My name is", name, "I am", age, "my favourite colour is", colour)

# 4
a = 10
b = 2.5
c = "hello"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 5
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1 + num2)
print(num1 * num2)
print(num1 - num2)

# 6
name = "Jedidiah"
s1 = 80
s2 = 90
s3 = 70
s4 = 85
s5 = 95
status = True
total = s1 + s2 + s3 + s4 + s5
average = total / 5
print(name)
print(s1, s2, s3, s4, s5)
print(status)
print(total)
print(average)

# 7
fruits = ["apple", "mango", "orange", "banana", "pineapple", "grapes", "pawpaw", "watermelon", "pear", "guava"]
print(fruits[0])
print(fruits[9])
print(len(fruits))

# 8
students = ["John", "Mary", "David", "Samuel", "James"]
new = input("Enter name: ")
students.append(new)
print(students)

# 9
numbers = [10, 15, 22, 33, 40, 51, 60, 71, 82, 93]
for n in numbers:
    if n % 2 == 0:
        print(n)

# 10
numbers = [15, 8, 25, 40, 12, 30, 5, 18]
big = numbers[0]
small = numbers[0]
total = 0
for n in numbers:
    if n > big:
        big = n
    if n < small:
        small = n
    total = total + n
print(big)
print(small)
print(total)

# 11
shopping = ["rice", "beans", "yam", "oil", "tomato"]
a = input("Add one: ")
shopping.append(a)
b = input("Add two: ")
shopping.append(b)
print(shopping)
c = input("Remove one: ")
shopping.remove(c)
print(shopping)

# 12
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
find = int(input("Enter number: "))
if find in numbers:
    print("It is there")
    print(numbers.index(find))
else:
    print("Not there")

# 13
student = {"name": "Jedidiah", "age": 17, "gender": "Male", "department": "Software", "matric": "123"}
print(student["name"])
print(student["age"])
print(student["gender"])
print(student["department"])
print(student["matric"])

# 14
products = {"Rice": 50000, "Beans": 30000, "Yam": 5000, "Oil": 15000, "Tomato": 2000}
print(products)

# 15
student = {"name": "John", "age": 17, "score": 85}
new_score = int(input("Enter new score: "))
student["score"] = new_score
print(student)

# 16
scores = {"John": 85, "Mary": 92, "Victor": 78, "David": 88, "James": 90}
big_name = ""
big_score = 0
for name in scores:
    if scores[name] > big_score:
        big_score = scores[name]
        big_name = name
print(big_name)
print(big_score)

# 17
account = {"name": "Jedidiah", "number": "123456", "balance": 50000}
print(account)
choice = input("deposit or withdraw: ")
amount = int(input("amount: "))
if choice == "deposit":
    account["balance"] = account["balance"] + amount
if choice == "withdraw":
    account["balance"] = account["balance"] - amount
print(account["balance"])

# 18
numbers = {10, 20, 30, 10, 40, 20, 50, 30}
print(numbers)
# set removes duplicate so 10 and 20 and 30 will show once

# 19
class1 = {"John", "Mary", "David"}
class2 = {"Mary", "David", "Peter"}
print(class1.intersection(class2))

# 20
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

# 21
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(days[0])
print(days[6])
print(len(days))
print("Saturday" in days)

# 22
students = ("John", "Mary", "David", "Samuel", "James")
temp = list(students)
temp.append("Victor")
temp.append("Sarah")
temp.remove("David")
students = tuple(temp)
print(students)

# 23
file = open("students.txt", "w")
file.write("Jedidiah\n17\nSoftware\n")
file.close()

# 24
file = open("students.txt", "w")
file.write("John\nMary\nDavid\nSamuel\nJames\n")
file.close()

# 25
file = open("students.txt", "a")
file.write("Victor\nSarah\nPeter\n")
file.close()

# 26
file = open("students.txt", "r")
print(file.read())
file.close()

# 27
file = open("diary.txt", "w")
file.write("Today is good\n")
file.write("I like Python\n")
file.write("I am learning\n")
file.write("It is fun\n")
file.write("I will try more\n")
file.close()
file = open("diary.txt", "r")
print(file.read())
file.close()

# 28
name = input("Enter name: ")
lang = input("Enter language: ")
file = open("profile.txt", "a")
file.write(name + " " + lang + "\n")
file.close()

# 29
file = open("numbers.txt", "w")
file.write("10\n20\n30\n40\n50\n")
file.close()
file = open("numbers.txt", "r")
total = 0
for line in file:
    total = total + int(line)
print(total)
file.close()

# 30
name = input("Enter name: ")
age = input("Enter age: ")
score = input("Enter score: ")
file = open("records.txt", "a")
file.write(name + " " + age + " " + score + "\n")
file.close()

file = open("records.txt", "r")
count = 0
for line in file:
    print(line)
    count = count + 1
print("Total records:", count)
file.close()
