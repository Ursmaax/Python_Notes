# num = int(input("Enter a number:"))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
# message = "Even" if num % 2 == 0 else "Odd"
# print(message)

#H O M E W O R K #

# Q . Write a program that can tell you your BMI Category.
#
# 1. Ask user to enter height in Meter
#
# 2. Ask user to enter weight in KG
#
# 3. Calculate the BMI(Body Mass Index) = weight /(height)**2 and store it in a variable
#
# 4. If the BMI is 30 or greater, print “Obesity”
#
# 5. If the BMI is in between 25 and 29, print “Overweight”
#
# 6. If the BMI is in between 18.5 and 25, print “Normal”
#
# 7. If the BMI is less than 18.5, print “Underweight”

#Solution

# Height = int(input("Enter your height in m  : "))
# Weight = int(input("Enter your weight in Kg : "))
# BMI = Weight / Height ** 2
# if BMI >= 30 :
#     print("Obesity")
# elif  BMI >= 25 and BMI <= 29 :
#     print("Overweight")
# elif  BMI >= 18.5 and BMI < 25 :
#     print("Normal")
# elif BMI < 18.5 :
#     print("Underweight")

# Q.  Using the following list of cities per country,
#
# India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
#  USA = ["New York","Chicago","Las Vegas", "San Francisco"]
#  UK = ["London", "Manchester", "Liverpool", "Nottingham"]
# 1. Write a program that asks the user to enter a city name, and it should tell which country the city belongs to
#
# 2. Write a program that asks users to enter two cities, and it tells you if they both are in the same country or nor />
# For example:
#If I enter Mumbai and Chennai, it will print "Both cities are in India" -
#- but if I enter Mumbai and New York it should print "They don't belong to the same country"

#Solution
# India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
# USA = ["New York","Chicago","Las Vegas", "San Francisco"]
# UK = ["London", "Manchester", "Liverpool", "Nottingham"]
 #1
# city = input("Enter the city name : ").title()
# if city in India :
#     print(f"{city} is in India")
# elif city in USA :
#     print(f"{city} is in USA")
# elif city in UK :
#     print(f"{city} is in UK")
# else :
#     print(f"{city} is not in our county list")
#2
# city1 = input("Enter the city name : ").title()
# city2 = input("Enter the city name : ").title()
# if city1 and city2 in India :
#     print(f"{city1} and {city2} is in India")
# elif city1 in USA :
#     print(f"{city1} and {city2} is in the USA")
# elif city1    in UK :
#     print(f"{city1} and {city2} is in the UK")
# else :
#     print(f"{city1} and {city2}  is not in our county list / not located in same country")

# For Loop

# expanses = [1000 ,1000, 1000, 2000, 3000]
# total = 0
# for expanse in expanses :
#     total += expanse # total = total + expanse
# print(total)

# print(list(range(0,5))) #[0, 1, 2, 3, 4]

# expanses = [1000 ,1000, 1000, 2000, 3000]
# total = 0
# for i, expanse in enumerate(expanses) :
#     print(f"Month : {i+1} -->  Expanse : {expanse}")
#     total = total +  expanse
# print(f"Total Expanses : {total}")

# expanses = [1900 ,1708, 1000, 2050, 3700]
# for i,expanse in enumerate(expanses) :
#     if expanse >= 1800 :
#         print(f"Month : {i+1}  Expanses :{expanse} ")

# places = ['Sofa', 'Bed Room', 'Kitchen', 'Hall']
# key_location = 'Bed Room'
# for location in places :
#     if location == key_location:
#         print('Key is found :' ,location)
#         break
#     else :
#         print('Key is not found at ' ,location)

# for i in range(1 , 11) :
#     if i % 2 != 0 :
#         print(i , end=" ")

# for i in range(1 , 11) :
#      if i % 2 == 0 :
#          continue
#      print(i)

# for i in range(1,-6,-2) :
#     print(i)


# rows
# n = 6
# for i in range(n, 1, -1):
#
#     # columns
#     for j in range(1, i):
#         print(j, end=" ")
#
#     # print new line after each row
#     print()

# Q. Write a Python program to find the sum of all the numbers except odd numbers
#    between 1 and 20 using a loop. Can you also do this using a while loop?

#Solution

# total = 0
# for i in range(1,21):
#     if i % 2 == 0:
#         total += i
#     else :
#         continue
# print("Sum of all the numbers except odd numbers = ", total)


# %%
# Using While loop

# sum_ = 0
# num = 1
# while num <= 20:
#
#     if num % 2 == 0:
#         sum_ += num
#
#     num = num + 1
#
# print(sum_)


# Q. After throwing the dice several times, you got this result,
#
# dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
# Using a for loop find out the followings:
#
# 1. How many times have you got 6s
#
# 2. How many times have you got 1s
#
# 3. How many times have you got 6s two times in a row

#Solution

# dice_result  = [5,6,4,2,5,4,4,5,3,3,2,6,1,2,1,1,6,5]
# times = 0
# for result  in dice_result :
#     if result == 6 :  #insted of 6 place 1 to get 2nd answer
#         times += 1
#     else:
#         continue
# print(times)

# %%
# two_6s = 0
# l = len(dice_result)
#
# for i in range(l - 1):
#     if dice_result[i] == 6 and dice_result[i + 1] == 6:
#         two_6s += 1
#
# print(two_6s)


# Q.  Let's say you are doing push-ups, and you have to complete 50 push-ups daily, write a program that,
#
# Upon completing 10 push-ups in a go, asks you, “Are you tired?”
#
# If you reply “yes” or “y” then it should break and print “You did total push-ups.”
#
# For example: If you did only 30  push-ups and answered “yes” to your program. It will break the loop and print “You did a total of 30 push-ups
#
# If you reply “no” or “n” then it should continue and display how many push-ups are remaining  now after that ask you again “Are you tired?”
#
# For Example: if you answered “no” then it should display that 20 push-ups are remaining and ask you again “Are you tired?”
#
# If you complete all 50 push-ups, then it should print the “Congratulations! You made it” and stopped the program.

#Solution

# pushups = 0
# answer = ""
# while True:
#     print("Doing push up.")
#     pushups += 1
#     if pushups == 50:
#         print("Congratulations! You made it")
#         break
#
#     elif pushups % 10 == 0:
#         answer = input("Are you tired? (yes/no)")
#         if answer[0].lower() == 'y':
#             break
#         else:
#             print(f"{50 - pushups} push-ups are remaining today.")
#
# print(f"You did total {pushups} Push-ups today.")

# import time
# my_time = int(input("Enter your time in seconds : "))
# for x in range(my_time, 0 , -1) :
#     seconds = x % 60
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("TIME'S UP!")


# for i in range(3):
#     for j in range(10,0,-1) :
#         print(j, end=" ")
#     print()

