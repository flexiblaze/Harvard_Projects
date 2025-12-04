name = input("Name: ")

match name:
    case "A"  |  "B": # or means | dik cizgi
        print("A and b")
    case "C":
        print("C")
    case _: # if its not mentioned say this
        print("I don't know")

#match key world for long strings for long things  if else is  to many for this problem