# print("Hello World")

# #VARIABLES
# my_name = ("Soumya")
# age = (23)
# print("name")
# print(my_name , age)
# print(type(my_name))

# #learning how to take input-in Python

# name = input("Enter your-name: ")
# print("Hello" + name) #concatenation

# ###########EXERCISE-1############
# first_name = "Tony"
# last_name = "Stark"
# age = 53
# height = 1.85
# is_superhero = True

# # Ask the user for Tony's superhero name
# superhero_name = input("Enter Tony's superhero name: ")

# #superhero_name = input("Tell us your Superhero identity: ")
# #print("Hello " + superhero_name)

# # Print all the details
# print("--- Person Details ---")
# print("First name:", first_name)
# print("Last name:", last_name)
# print("Age:", age)
# print("Height:", height, "m")
# print("Is a superhero:", is_superhero)
# print("Superhero name:", superhero_name)


# #Type Conversion and Type Casting
# print (1 + 2.5) # implicit
# print(1 + int(2.999)) # explicit

#Sum Program--> a,b--sum
# a = int(input("Enter a:"))
# b = int(input("Enter b:"))
# sum = a + b
# print("sum:" , sum)


# name = "Tony Stark"
# grade = 'B'

# #string operations
# print (name. upper())
# print (name) #string is immutable--> can't be changed from the original form
# print (name.find("ark")) #0 index => position
# print (name.find ("T")) 
# print (name.find("X")) 
# # replace
# print(name. replace("Tony Stark", "Ironman"))
# print(name. replace("Stark", "Ironman"))
# print(name. replace("T", "Ph"))


# name = "Tony Stark"
# # check for presence
# print('X' in name) # False
# print('S' in name) # True
# #reserved words --> True, in, False, while, for, break, continue
# abcd = "abc"


###########EXERCISE 2#############
#Question-1
# p_1 = float(input("Enter the price of 1:"))
# p_2 = float(input("Enter the price of 2:"))
# p_3 = float(input("Enter the price of 3:"))

# total_bill_amt = p_1 + p_2 + p_3
# avg_amt = total_bill_amt/3
# print("Total Amount: ", total_bill_amt)
# print("Average Amount: ", avg_amt)

#Question-2
# superhero_name = input("Enter a superhero name: ")
# starts_with_s = superhero_name.lower().startswith("s")
# print("Does the name start with S or s?", starts_with_s)

# arithmetic operators
# print(5 + 3)
# print(5 - 3)
# print (5* 3)
# print (5 / 3)
# print (5 // 3)
# print (5 % 3) #modulo-> remainder
# print (5 ** 3) #power_operator


#assignment operators

# x = 2
# # x = 2 * 5
# x *= 5
# print(x)
# x /= 5, x %= 5

# OPERATOR PRECENDENCE
# ans = (2 + 5) * 3
# print(ans)

# comparison operators
# >, <, >=, <=, ==, !=
# print(2 != 2)


#conditional statements

# age = 16
# # indentation ---> proper tab spacing
# if age >= 18:
#     print ("you can an adult")
#     print ("you can drive / vote")
# elif age < 18:
#     print ("you can't vote or drive")

# print("end of code")


# marks = float(input("Enter student's marks:"))

# if 80 <= marks <= 100:
#     print("Grade = A")
# elif 60 <= marks <= 80:
#     print("Grade = B")
# elif marks <= 60:
#     print("Grade = C")


#######EXERCISE 3#############
#CALCULATOR
# a = float(input("First number:"))
# b = float(input("Second number:"))
# operations = input("operation to be performed:")

# if operations == "+" :
#     print(a + b)
# elif operations == "-" :
#     print(a - b)
# elif operations == "*" :
#     print(a * b)
# elif operations == "%" :
#     print(a % b)
# elif operations == "**" :
#     print(a ** b)
# else:
#     print("undefined")


#LOOPS:

#WHILE LOOPS:
#counter: 1, 2, 3, 4, 5, 6
# i = 1
# while i <= 5:
#     print("Soumya")
#     i += 1
# print("END OF CODE")

#FOR LOOPS:
# 0 to 4
# for i in range(5):
#     print(i)
# 1 to 5
# for i in range(1, 6):
#     print(i)

# for i in range(15, 0, -1):
#     print(i * "*")

# 1 to 10--> even nums
# for i in range(0, 11, 2):
#     print(i)

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i)



#break and continue
# print multiples of 3(1, 51) till 21

# multiples of 3 [1 to 50] => 21 skip
# for i in range (1, 51):
#     if(i == 21):
#         break
#     if (i % 3 == 0): 
#         print (i)

# print("out of loop")


#multiples of 3 except 21(skip) till 51
# for i in range (1, 51):
#     if(i == 21):
#         continue
#     if (i % 3 == 0): 
#         print (i)

# print("out of loop")

#EXERCISE 3#
#Print all odd numbers from 1 to 20.
# for i in range(1, 20):
#     if(i % 2 != 0):
#         print(i)

#Print the table of 57.
# for i in range(1, 571):
#     if(i % 57 == 0):
#         print(i)

#Print all multiples of 3 from 1 to 50 but skip 15.
# for i in range (1, 51):
#     if(i == 15):
#         continue
#     if (i % 3 == 0): 
#         print (i)

#Take two integers a and b as input.
#Find and print the first number between 1 and 1000 
#that is divisible by both numbers.
# a = float(input("Enter the first number:"))
# b = float(input("Enter the second number:"))
# numberOfPrintedValues = 0
# for i in range(1, 1000):
#     if(i % a == 0 and i % b == 0):
#         print(i)
#         numberOfPrintedValues = numberOfPrintedValues + 1
#         if(numberOfPrintedValues == 3):
#             break

# print(numberOfPrintedValues)

# a = float(input("Enter the first number:"))
# b = float(input("Enter the second number:"))
# numberOfPrintedValues = 0
# for i in range(1000, 1, -1):
#     if(i % a == 0 and i % b == 0):
#         print(i)
#         numberOfPrintedValues = numberOfPrintedValues + 1
#         if(numberOfPrintedValues == 3):
#             break

#EXERCISE 4#
# roll_numbers = [101, 105, 102, 101, 108, 105, 110]
# unique_roll_numbers = set(roll_numbers)
# print("Unique roll numbers:", unique_roll_numbers)

employees = [
    (101, "Alice", 50000),
    (102, "Bob", 65000),
    (103, "Charlie", 45000)
]
search_id = int(input("Enter Employee ID: "))
found = False
for employee in employees:
    employee_id = employee[0]
    if employee_id == search_id:
        print("Employee found!")
        print("Employee ID:", employee[0])
        print("Employee Name:", employee[1])
        print("Salary:", employee[2])
        found = True
        break

if found == False:
    print("Employee not found.")
