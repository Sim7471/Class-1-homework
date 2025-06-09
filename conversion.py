def convert_grams(cups,conversion_rate):
    return cups * conversion_rate

def convert_cups(grams,conversion_rate):
    return grams / conversion_rate

def convert_teaspoon(table):
    return table * 3 

while True:
    print("1.convert cups to grams\n 2. convert grams to cups\n 3.Convert tablespoon to teaspoon\n 4. exit:")
    option = int(input("choose option from 1-4:"))
    if option ==1:
        cups = float(input("Enter the amount of cups:"))
        conversion_rate = float(input("how much can your cup hold?:"))
        grams = convert_grams(cups,conversion_rate)
        print(grams)
    elif option ==2:
        grams = float(input("Enter the amount of grams:"))
        conversion_rate2 = float(input("how many grams in a cup?:"))
        cups = convert_grams(grams,conversion_rate2)
        print(cups)
    elif option ==3:
        table = float(input("Enter the number of tablespoons:"))
        tea = convert_teaspoon(table)
        print(tea)
    elif option ==4:
        print("Okay exiting")
        break
    else:
        print("Invalid option")