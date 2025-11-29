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

#Collections

# collection = single "variable" used to store multiple values
# List  = [] ordered and changeable. Duplicates OK
# Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# Fruits  = ['Banana', 'Coconut', 'Orang', 'Grapes', 'Apple' ]
# print(dir(Fruits)) #This will return all the possible operations which can be performed on list
# print(help(Fruits)) #This will return How to use each function

# Shopping Cart Project ----------------------------------------------------

# foods = []
# prices = []
# total = 0
# while True :
#     food = input("Enter a food to buy (q to quit): ").lower()
#     if food == 'q':
#         break
#     else :
#         price = float(input(f"Enter the price of a {food} : "))
#         foods.append(food)
#         prices.append(price)
# print("------------- Your cart -------------")
# for food in foods :
#     print(food, end="\n")
# for price in prices :
#     total += price
# print("------------- Your Total -------------")
# print(f"Your total is : ${total}")

#----------------------------------------------------------------------------

# 2 - D Lists

# fruits =     ['apple', 'orange', 'banana', 'coconut']
# vegetables = ['celery', 'carrots', 'potatoes']
# meats =      ['chicken', 'fish', 'turkey']
#
# groceries = [fruits, vegetables, meats]

# fruits[0] = 'pineapple'
# print(fruits)
# print(groceries)
# for items in groceries :
#     for item in items :
#         print(item, end=' ')
#     print()

# print(groceries[0])    # ['apple', 'orange', 'banana', 'coconut']
# print(groceries[0][1]) # orange
# print(groceries[2])    # ['chicken', 'fish', 'turkey']


# groceries = [['apple', 'orange', 'banana', 'coconut'],
#              ['celery', 'carrots', 'potatoes'],
#              ['chicken', 'fish', 'turkey']]
#
# groceries = [('apple', 'orange', 'banana', 'coconut'),
#              ('celery', 'carrots', 'potatoes'),
#              ('chicken', 'fish', 'turkey')]
#
# groceries = [{'apple', 'orange', 'banana', 'coconut'},
#              {'celery', 'carrots', 'potatoes'},
#              {'chicken', 'fish', 'turkey'}]
#
# groceries = ({'apple', 'orange', 'banana', 'coconut'},
#              {'celery', 'carrots', 'potatoes'},
#              {'chicken', 'fish', 'turkey'})


# Quiz - Game ---------------------------------------------------------

# questions = ("How many elements are in the periodic table ?:" ,
#              "Which animal lays the largest eggs ?: ",
#              "What is the most abundant gas in Earth's atmosphere? : ",
#              "How many bones are in the human body ?: ",
#              "Which planet in the solar system is the hottest ?:")
#
# options = (("A. 116", "B. 117", "C. 118", "D. 119"),
#            ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
#            ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
#            ("A. 206", "B. 207", "C. 208", "D. 209"),
#            ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))
# answers = ("C", "D", "A", "A", "B")
# guesses = []
# score = 0
# question_num = 0
#
# for question in questions :
#     print("-----------------------")
#     print(question)
#     for option in options[question_num] :
#         print(option)
#
#     guess = input("Enter your answer : ").upper()
#     guesses.append(guess)
#     if guess ==answers[question_num] :
#         score =+ 1
#         print("CORRECT")
#     else:
#         print("INCORRECT")
#         print(f"{answers[question_num]} is the correct answer")
#     question_num = question_num + 1
#
# print("-----------------------")
# print("        RESULTS        ")
# print("-----------------------")
#
# print("answers : ", end="")
# for answer in answers :
#     print(answer,end=" | ")
# print()
#
# print("guesses : ", end="")
# for guess in guesses :
#     print(guess, end=" | ")
# print()
# score = int(score / len(questions) * 100)
# print(f"Your score is : {score}%")
#
#----------------------------------------------------------------------------

#Dictionary : a collection of {key : value} pairs
#             ordered and changeable. No duplicates

# capitals = {"USA"   : "Washington D.C",
#             "India" : "New Delhi",
#             "China" : "Beijing",
#             "Russia": "Moscow" }
# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("India")) # New Delhi
# print(capitals.get("New Delhi")) # None

# if capitals.get("Russia"):
#     print("That capital exist")
# else:
#     print("That capital doesn't exist")

# capitals = {"USA"   : "Washington D.C",
#             "India" : "New Delhi",
#             "China" : "Beijing",
#             "Russia": "Moscow" }
# capitals.update({"Germany" : "Berlin"}), print(capitals)
# capitals.update({"USA" : "Detroit"}), print(capitals)
# capitals.pop("China"), print(capitals)
# capitals.popitem(), print(capitals) # removes latest updated value
# capitals.clear(), print(capitals) # {}
# keys = capitals.keys()
# print(keys) # dict_keys(['USA', 'India', 'China', 'Russia'])

# for key in capitals.keys() :
#     print(key, end=" | ")   # USA | India | China | Russia |

# for value in capitals.values() :
#     print(value, end=" | ")  # Washington D.C | New Delhi | Beijing | Moscow |

# capitals = {"USA"   : "Washington D.C",
#             "India" : "New Delhi",
#             "China" : "Beijing",
#             "Russia": "Moscow" }

# items = capitals.items()
# print(items)  # ([('USA', 'Washington D.C'), ('India', 'New Delhi'), ('China', 'Beijing'), ('Russia', 'Moscow')])

#
# for key, value in capitals.items():
#     print(f"{key}: {value}")

#    #output will look like
#     USA: Washington
#     D.C
#     India: New
#     Delhi
#     China: Beijing
#     Russia: Moscow

#Concession stand program ----------------------------------------------------------------------------
#
# menu = {"pizza": 3.00,
#         "nachos": 4.50,
#         "popcorn": 6.00,
#         "fries": 2.50,
#         "pretzel": 3.50,
#         "chips": 1.00,
#         "soda": 3.00,
#         "lemonade": 4.25}
# cart = []
# total = 0
#
# print("---------MENU--------------")
# for key, value in menu.items() :
#     print(f"{key:10}: ${value:.2f}")
# print("---------------------------")
#
# while True:
#     food = input("select an item (q to quit) : ").lower()
#     if food == "q" :
#         break
#     elif menu.get(food) is not None :
#         cart.append(food)
#
# for food in cart :
#     total = total + menu.get(food)
#     print(food,end=" ")
#
# print()
# print("----------TOTAL-----------")
# print(f"Total is : ${total:.2f}")

#----------------------------------------------------------------------------

# import random
#
# # print((help(random)))
# low = 1
# high = 100
# # number = random.randint(low, high)
# number = random.random() #radom floating point number
# print(number)

# Rock Paper Scissors Program ----------------------------------------------------------------------------

# import random
#
# options = ("rock", "paper", "scissors")
# player = None
# computer = random.choice(options)
# playing = True
# while playing :
#     player = None
#     computer = random.choice(options)
#
#     while player not in options :
#         player = input('Enter a choice (rock, paper, scissors): ').lower()
#
#     print(f"Player  : {player}")
#     print(f"Computer: {computer}")
#
#     if player == 'rock' and computer == 'scissors' :
#         print("You Win!")
#     elif player == 'paper' and computer == 'rock' :
#         print("You Win!")
#     elif player == 'scissors' and computer == 'paper' :
#         print("You Win!")
#     elif player == computer :
#         print("It's a tie!")
#     else :
#         print("You lose !")
#     if not input("Play again ? (y/n): ").lower() == 'y':
#         playing = False
#
# print("Thanks for Playing !")
#----------------------------------------------------------------------------

#Number Guessing Game ----------------------------------------------------------------------------
# import random
# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True
# print("Python Number Guessing game ")
# print(f"Select a number between {lowest_num} and {highest_num}")
#
# while is_running :
#     guess = input("Enter your guess: ")
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
#
#         if guess < lowest_num or guess > highest_num :
#             print("That number is out of range")
#             print(f"Select a number between {lowest_num} and {highest_num}")
#         elif guess < answer :
#             print("Too low ! Try again")
#         elif guess > answer :
#             print("Too high! Try again")
#         elif guess == answer :
#             print(f"CORRECT! The answer was {answer}")
#             print(f"Nuber of guesses: {guesses}")
#             is_running = False
#     else:
#         print("Invalid guess")
#         print(f"Please Select a number between {lowest_num} and {highest_num}")
#----------------------------------------------------------------------------
 # 3:42:03

#fuction = A block of reusable code
#          place () after the function name to invoke it

# I want to print Happy Birthday 3 times

# def My_Name():
#     print("Umamahesh")
# My_Name()
# My_Name()
# My_Name() # Whenever i call a function then that function calls once and goes inside that function then executes it once

# def My_friends(name, age):
#     print(f"One of my friends name is {name} - {age}")
# My_friends("X", 20)
# My_friends("Y", 30)
# My_friends("Z", 40)

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")
# display_invoice("Uma", 100, "12/12")
# display_invoice("Gnani", 200, "13/12")
# display_invoice("Prasanth", 540, "14/12")

#return = statement used  to end a function
#          and send a result back to the caller

# def add(x, y):
#     z = x + y
#     return z
# def subtract(x, y):
#     z = x - y
#     return z
# def product(x, y):
#     z = x * y
#     return z
# def division(x, y):
#     z = x / y
#     return z
# print(add(10, 20))
# print(subtract(10, 20))
# print(product(10, 20))
# print(division(10, 20))

# def create_name(first, last):
#     first = first.capitalize()
#     last  = last.capitalize()
#     return first + " " + last
# print(create_name("uma", "mahesh"))

#default arguments = A default value for certain parameters
#                    default is used when that argument is omitted
#                    make your functions more flexible, reduces #of
#                    1. positional, 2. default 3. keyword 4. arbitrary

# def net_price(list_price, discount = 0, tax = 0.05):
#     return list_price * (1 - discount) * (1 + tax)
#
# print(net_price(500))
# print(net_price(500, 0.1))
# print(net_price(500, 0.1, 0))

# import time
#
# def count(end, start = 0): #default value should be last otherwise it will throw error
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("DONE!")
#
# count(0, 10)

# #Keyword arguments = an argument preceded an identifier
#                      helps with readability
#                      order of arguments doesn't matter

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first}{last}")
# hello("Hello", title="Mr.", last="John", first="James")

# print("1","2","3","4","5", sep=" - ") #it seperated the strings by - , it almost works like end="-"


# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"
# phone_num = get_phone(country=1, area=123, first=456, last=7890)
# print(phone_num)

#ARBITRADRY
# 1.*args    = allows you to pass multiple non-key arguments
# 2.**kwargs = allows you to pass multiple keyword-arguments
#              * unpacking operator


# def add(*args): # converted to tuple
#     total = 0
#     for arg in args:
#         total += arg
#     return total
#
# print(add(1, 2, 4))

# def add(*nums): # converted to tuple
#     total = 0
#     for num in nums:
#         total += num
#     return total
#
# print(add(1, 2, 4))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
# display_name("Uma", "Mahesh")

# def print_address(**kwargs): #kwargs --> convert the data to dictionary
#     for key,value in kwargs.items():
#           print(key)
#           print(f"{key:10} : {value}")
#
# print_address(street="123 Fake St.",
#               city="Srikakulam",
#               state="Andhra Pradesh",
#               zip="532001")

# def shipping_label(*args, **kwargs): #*args should come first
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     for value in kwargs.values():
#         print(value, end="")
# shipping_label("D", "Uma", "Mahesh", "III",
#                    street="123 Fake St.",
#                    apt="100",
#                    city="Detroit",
#                    state="MI",
#                    zip="54321")
