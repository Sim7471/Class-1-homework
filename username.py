import random
def generate_username(name):
    store_name = name.split()
    if len(store_name) <2:
        print("Enter BOTH your last and first name:")
    else:
        first_name = store_name[0].lower()
        second_name = store_name[1].lower()
        U_N1 = first_name[0:2] + second_name[-1]
        U_N2 = first_name[1:3] + second_name[0] 
        U_N3 = first_name[0:3] + second_name[-1:-5:-1] + str(random.randint(0,7))
        U_N4 = first_name[1:2] + second_name[0:2] + str(random.randint(10,20))
        U_N5 = first_name[0:4] + second_name[-1:-3:-1] + str(random.randint(80,100))
        usernames = [U_N1,U_N2,U_N3,U_N4,U_N5]
        return random.choice(usernames)

while True:

    name = input("Enter your first and last name or type exit to quit:")
    if name.lower() == "exit":
        print("Okay, try again next time")
        break
    else:
        name_generate =  generate_username(name)
        print(name_generate)

    

