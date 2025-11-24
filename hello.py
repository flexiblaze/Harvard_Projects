
#Asking user for their name

name = input("Wat is jouw naam? ").strip().title()

#remove the whitespace from string str.
name = name.strip().title().capitalize()
name = name.capitalize() #capitalize user's  only first letter
name = name.title() # hepsi buyuk yapar

#split user's name into first name and last name

first, last = name.split(" ")


#i can also use + or , here
print("Hello World",first,"Bond"  )
print(f"Hello World, {first}") # format string, f string is uniek
#function =>print

#arguments input to a function => Hello World

#side effects => uitslag van function

#bug's mistake in a program code

#return values , go get that values,put it somewhere then if you want it print it

#variables .can store a value like a container right to left

#comments not for my self
#pseudocode = expressing my thoughts on how to do it
"""
Anything here is also comment
"""

#str => string type of data, \n new line
# print(*objects, sep='',end ='\n', file=sys.stdout, flush=False)
#sep means seperater tussen twee  words, end means u can add new line or something after the first variable

#parameteres =>  value in functions

print('Hello, "friend"')
print("Hello, 'friend'")
print('Hello, \"friend\"') # escaping

#int => numbers , no decimals

#def=>  define functions,  taking inputs and writing outputs, you need to call them

#def hello(to="world"): # if noone puts name it will say world
 #  print("Hello, ", to)

#name = input("Whats your name ")
#hello(name)


def main():
    name = input("Whats your name ") #omer
    hello(name)                      #hello ya gelicek input is omer

def hello(to="world"):               # hello(omer)
    print("hello,", to)              # hello omer

    main()

    # this the good way of writing functions, fix define them then call them, top to bottom

