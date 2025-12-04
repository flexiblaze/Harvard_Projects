# +
#-
#*
#/
#%

#x = int(input("x: "))

#if x % 2 == 0:
#    print("x is even") # Cleanly divided by 2
#else:
  #  print("x is odd") # not cleanly

def main():
    x = int(input("Whats x: "))
    if is_even(x):
        print("x is even")
    else:
        print("x is odd")

def is_even(n):
    return n % 2 == 0
   # if n % 2 == 0:
   #     return True
   # else:
   #     return False

main()