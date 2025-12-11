

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollar_without = d.replace("$", "")
    number = float(dollar_without)
    return number

def percent_to_float(p):
    percent_without = p.replace("%", "")
    percent_number = float(percent_without) /100 # we got a foult cyz u cant deel the string
    return percent_number



main()