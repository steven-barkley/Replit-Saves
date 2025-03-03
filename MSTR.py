day-1-printing-end

# input() will get user input in console
# Then print() will print the word "Hello" and the user input
print("Hello " + input("What is your name?"))

async-1

// How to control 3 promises

//parallel done 
//sequencial
// race

const promisify = ( item, delay ) =>
    new Promise( ( resolve ) =>
        setTimeout( () =>
            resolve( item ), delay ) );

const a = () => promisify( 'a', 100 );
const b = () => promisify( 'b', 5000 );
const c = () => promisify( 'c', 3000 );
/* console.log( a, b, c )
console.log(a(),b(),c()) */

async function parallel() {
    const promises = [ a(), b(), c() ];
    const [ output1, output2, output3 ] = await Promise.all( promises );
    return `parallel is done: ${ output1 } ${ output2 } ${ output3 }`
}

/* parallel().then(console.log); */


async function race() {
    const promises = [ a(), b(), c() ];
    const output1 = await Promise.race( promises );
    return `race is done: ${ output1 }`;
}

/* race().then(console.log) */

async function sequence() {
  const output1 = await a();
  const output2 = await b();
  const output3 = await c();
  return `sequence is done ${output} ${output2} ${output3}`
}

sequence().then(console.log)

tesla

def checkDriverAge(age = 0):
  # age = input("What is your age?: ")

  if int(age) < 18:
    print("Sorry, you are too young to drive this car. Powering off")
  elif int(age) > 18:
    print("Powering On. Enjoy the ride!")
  elif int(age) == 18:
    print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge()
#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

GUI exercise

#Exercise!
#Display the image below to the right-hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# new_picture = []
# for picture_row in range(len(picture)):
#     new_pixel = []
#     for pixel in picture[picture_row]:
#       if pixel == 0:
#         new_pixel.append(' ')
#       elif pixel == 1:
#         new_pixel.append('*')
#     new_picture.append(new_pixel)
#     print(new_pixel)

for pic_row in picture:
  for pixel in pic_row:
    if pixel == 0:
      print(' ', end='')
    elif pixel == 1:
      print('*', end='')
  print('')
#print(new_picture)


# new_picture = []
# for list_row in picture:
# #  print(list_row)
#   new_row = []
#   for list in list_row:
#     if list == 0:
#       new_row += " "
#     elif list == 1:
#       new_row += "*"
#   new_picture += new_row
# print(new_picture)
# converted_picture = []
# converted_row = []
# for pixel_row in picture:
#   for pixel in pixel_row:
#     if pixel == 0:
#       converted_row.append(' ')
#     elif pixel == 1:
#       converted_row.append('*')
#   converted_picture.append(converted_row)
# print(converted_picture)

# num_list = []
# for number in list(range(15)):
#   num_list.append(number)
# print(num_list)


# How to add a list to a list

# list_library = []

# for i in range(20):
#     for y in range(5):
#       list_library.append(i)
# print(list_library)

# list1 = [[],[],[],[]]
# list2 = [1]

# for i in range(len(list1)):
#     list1 += list2
# print(list1)

# Exercise Dictionary Methods
# Scroll to see answers.

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

# 2 iterate and print all the keys in the above user.

# 3 Add a new weapon to your user

# 4 Add a new key to include 'is_banned'. Set it to false

# 5 Ban the user by setting the previous key to True

# 6 create a new user2 my copying the previous user and update the age value and username value.


#ANSWERS BELOW:

# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'
user_profile = {
    'age': 0,
    'username': ' ',
    'weapons': None,
    'is_active': False,
    'clan': None
}

# 2 iterate and print all the keys in the above user.
print(user_profile.keys())

# 3 Add a new weapon to your user
user_profile['weapons'] = 'Katana'

# 4 Add a new key to include 'is_banned'. Set it to false
user_profile.update({'is_banned': False})

# 5 Ban the user by setting the previous key to True
user_profile['is_banned'] = True

# 6 create a new user2 my copying the previous user and update the age value and username value.
user2 = user_profile.copy()
user2.update({'age': 50, 'username': 'User2'})
print(user_profile)
print(user2)

Dict

# Dictionary

# Dict 

dictionary = {
  'a' : 1,
  'b' : 2,
  'x' : 3,
  'c' : 6,
  'y' : 2
}

print(dictionary['c'])
print(dictionary)

Operator Precedence

# Guess the output of each answer before you click RUN
# Try to write down your answer before and see how you do... keep it mind I made it a little tricky for you :)

print((5 + 4) * 10 / 2)
# 9 * 10 / 2 
# 90 / 2 
# 45.0
print(((5 + 4) * 10) / 2)
# (9 * 10) / 2 
# 90 / 2
# 45.0
print((5 + 4) * (10 / 2))
# 9 * 5
# 45.0
print(5 + (4 * 10) / 2)
# 5 + 40 / 2 
# 5 + 20
# 25.0
print(5 + 4 * 10 // 2)
# 25


day-10-start

# Write a function that converts user name input into proper capitalization

# Logic
# user_name_format is function name
# user_name is separated by space " "
# Single string is converted into two strings
# Each string is lower() to all lowercase
# Each string first [0] is converted to upper()
# Combine the two strings

def user_name_format(f_name, l_name):

caesar-cipher-1-start

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text_param, shift_param):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    if text_param == 'encode':
      for i in len(alphabet):
        print(alphabet[i])
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(text, shift)
  

day-8-start

# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#   print("1\n")
#   print("2\n")
#   print("3\n")

# def greet_with_name(name_parameter):
#   print(f"Hello {name_parameter}.")
#   print(f"How do you do {name_parameter}?")

# name_argument = input("What is your name? ")
# greet_with_name(name_argument)

# Functions with more than one input
# Greet with name and location

user_name_arg = input("What is your name?")
user_location_arg = input("What is your location?")

def greet_with(parameter1 = user_name_arg, parameter2 = user_location_arg):
  print(f"{parameter1} how is the weather in {parameter2}?")

greet_with(user_name_arg, user_location_arg)

Day-7-Hangman-3-Start

#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
guess_count = 10
while guess_count > 0:
  guess = input("Guess a letter: ").lower()
  guess_count -=1
  #Check guessed letter
  for position in range(word_length):
      letter = chosen_word[position]
      #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
      if letter == guess:
          display[position] = letter
  print(display)


class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


#1 Add another Cat

class Tikachu(Cat):
    def sing(self,sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = []
cat1 = Simon('Simon', 10)
cat2 = Sally('Sally', 15)
cat3 = Tikachu('Tikachu', 5)

my_cats.append(cat1)
my_cats.append(cat2)
my_cats.append(cat3)

#OR my_cats = [Simon('Simon', 10), Sally('Sally', 15), Tikachu('Tikachu', 5)]

#3 Instantiate the Pet class with all your cats use variable my_pets

my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance

my_pets.walk()

# New code 1/31

# Fundamental Data types
#integers 2, 4, 5, 100, 10000,

print(2+4)
print(2-4)
print(2*4)
print(2/4)
# find the data type using "type"

print(type(6))
# result <class 'int'>

print(type(5.003))
# result <class 'float'>

# Data is stored in binary "000" and "111"

# We can do math operation in pythons

# "**" is the power operation
print(2**9)
# "// is divided into without the remainder" 
print(500//3)
# '% or modulo operation' for the remainder only
print(20%3) 
# "round" is a operation
print(round(30.23))
# "abs" is absolute vale operation

print(abs(-422))
# New code

# operator precedence 

print(20 + 3 * 4)

#1 ()
#2 **
#3 /
#4 -+

# Guess the output of each answer before you click RUN
# Try to write down your answer before and see how you do... keep it mind I made it a little tricky for you :)

print((5 + 4) * 10 / 2)
# guess 45
print(((5 + 4) * 10) / 2)
# guess 45
print((5 + 4) * (10 / 2))
# guess 45
print(5 + (4 * 10) / 2)
# guess 25
print(5 + 4 * 10 // 2)
# guess 25

print(bin(9))
print(int('0b101', 2))
print(int('0b10001',2))

#New code variables and rules to creating them 

# int 
# float 
# complex 


# variables
# text used to store values in memory
IQ = 190

print(IQ)

rules for variables

# snake_case
# Start with lowercase or underscore
# contain letters, numbers or underscores only
# Case sensitive 
# Dont overwrite keywords (reused variable in memory)

#underscore in python signals a private variable 
_myIQ = 120 #"private"

avgIQ = 100 #"public"

#Statements and expressions

iq = 100

user_age = iq/5

# A statement is simply a line of code
# i.e iq = 100

# An expression produces a value "iq/5" = 20

# print(type('hi hello there 24!'))
# username = 'supercoder'
# password = 'supersecret'
# long_string = '''
# WOW
# 0 0
# ---
# '''

# print(long_string)

first_name = "Steven"
last_name = "Barkley"
full_name = first_name + " " + "last_name"

print(full_name)


# for example "str" is a keyword

print(str(100))

print(type(str(100)))

print(type(int(str(100))))

# above is type conversion

# for example "str" is a keyword

print(str(100))

print(type(str(100)))

print(type(int(str(100))))

# above is type conversion


# Escape Sequence

# \ is a special character to denote ignoring string syntax

# \t
# \n 
# \d
# \'
# \f etc. 

# Tuples

# formatted strings 

name = "David"
age = 29 

print('hi {1}. You are {0} years old'.format(name, age))

# formatting strings

# indexing into strings

selfish = 'me me me'

print(selfish[0:-1])
#stepover
print(selfish[0:8:2])
print(selfish[1:])

#[start:stop:step]

#Will continue Python Zero to Mastery tomorrow. I did not do anything.

Today I am finally remaking my resume using AI.
Maybe start by building something simple and using the CD/CI method to extend the function and uses.

Another day of no studying but at least I got some rest!
