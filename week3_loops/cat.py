
b = 1.34

print(round(b,2))

#print("meaow")
#print("meaow")
#print("meaow")

#loops while

i = 0
while i <3:
    print("meauw")
    i += 1

#loop for
#list things
#for in
#for in range
#if u dont use i use _
for _ in range(100):
    print("ali")

print("meow\n" * 3, end="" ) # end it when finished

#while True:
#    n = int(input("What's n ?"))
 #   if n > 0:
 #       break

#for _ in range(n):
#    print("ahmet")


def main():
    number = getnumber()
    meouw(number)

def getnumber():
    while True:
        n  = int(input("What's n ?"))
        if n >0 :
            break
    return n

def meouw(n):
    for _ in range(n):
        print("meaouw")


if __name__ == '__main__':
    main()