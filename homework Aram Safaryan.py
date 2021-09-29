# 1. Enter your name, then find the sum of the ASCII values of the letters in your name. If that number is larger than
# 500, print "I've got a great name!", and "I've got a fancy name!" otherwise.


Aram = ord('A') + ord('r') + ord('a') + ord('m')

if Aram > 500:
    print("I've got a great name!")
else:
    print("I've got a fancy name!")

# 2. Ask the user for a movie title. If the title starts with a capital letter, print "Great title!", otherwise print
# "Titles start with capital letters...". If the input is not a string, print "Why are you doing this to me?".

x = input(" ENTER movie title:")

y = x.lower()
z = x.upper()

if x[0] == z[0]:
    print("Great title!")
if x[0] == y[0]:
    print ("Titles start with capital letters...")
else:
    print ("Why are you doing this to me?")




# # 3. Ask the user to input his/her age. If the user is older than 18, than tell them they're eligible to vote. If they
# # are younger than 18, tell them how many years do they have to wait.

x = int(input(" ENTER your age:"))
if x > 18:
    print("You are eligible to vote")
if x < 18:
    y = 18 - x
    text = 'You must wait {} years'.format(y)
    print(text)



# 4. Write a program that will tell us whether a given year is a leap year or not.

x = 2022
if (2020-x)%4==0:
    text1 = '{} is a leap year'.format(x)
    print(text1)
else:
    text2 = '{} is not a leap year'.format(x)
    print (text2)



# 5. Using 'random' module, generate a random number between -1000 and 1000. If the number is positive, print positive.
# If it's negative, print negative along with the absolute value of the num

import random
x = random.randint(-1000, 1000)
print (x)

if x>0:
    print ('positive')
if x<0:
    y=x*-1
    print (y)