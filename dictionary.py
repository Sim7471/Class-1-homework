# dictionary = {"refraction":"the bending of light","reflection":"When light bounces off the surface"}
# dictionary["reflection"]
# print(dictionary["reflection"])
# dictionary["reflection"] = "light bounces off"
# print(dictionary)
# dictionary["WW2"] = "1939-1945"
# print(dictionary)
# del dictionary["refraction"]
# print(dictionary)
# for i in dictionary:
#     print(i,dictionary[i])

dictionary = {}
while True:
    print("1.add or update a word\n 2.retrieve a word's defination\n 3.delete a word\n 4.view all words\n 5.check if a word exists\n 6.clear the dicitionary\n 7.Count number of words\n 8.exit")
    option = int(input("choose from numbers (1-5):"))
    if option == 1:
        key = input("Enter word:")
        value = input("Enter value of word:")
        dictionary[key] = value
    elif option == 2:
        key =input("Enter word:")
        if key in dictionary:
            print(dictionary[key])
        else:
            print("word not found:")

    elif option == 3:
        key = input("Enter word:")
        if key in dictionary:
            del dictionary[key]
            print(dictionary)
        else:
            print("word not found:")

    elif option == 4:
        for i in dictionary:
          print(i,dictionary[i])

    elif option == 5:
        key= input("Enter word to check:")
        if key in dictionary:
            print("Yes this word exists")
        else:
            print("No,the word does not exist.")

    elif option == 6:
        dictionary.clear()
        print("Dictionary cleared.")

    elif option == 7:
        print(f"There are {len(dictionary)} words in the dictionary.")
    
    elif option == 8:
        print("Bye!")
        break
    else :
        print("option not found")

 
