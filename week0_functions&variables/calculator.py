
#make them integer with int

x = float(input("What is x? "))
y = float(input("What is y? "))

#give the z round to 2 decimals after integer like 1.34, 0.14 = round(x/y, 2)



print(round(x+y))

#float 1.23


#return

def main():
    x = int(input("What is x? "))
    print("x squared is", square(x))

def square(n):
     return n * n
  #  return  pow(n, 2) possible
  #  return n ** 2 possible
