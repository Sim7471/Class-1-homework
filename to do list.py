task = []
while True:
    print("Welcome to the TO DO list app:")
    print("1.view task\n 2.Add task\n 3.Remove task\n 4.Edit list\n 5.Exit")

    answer = int(input("Chose your option(1-5):"))
    if answer ==1:
        for i in task:
            print(i)
    elif answer ==2:
        option = input("Enter your new task:")
        task.append(option)
        print(option +" got added")
    elif answer ==3:
        name = input("Enter the task you want to be removed:")
        task.remove(name)
        print(name + " got removed")
    elif answer ==4:
        index = int(input("Enter index number to edit list:"))
        new = (input("Enter the new value:"))
        task[index] = new
        print("Updated list:",task)
    elif answer ==5:
        print("Exiting from TO DO list")
        break
    else:
        print("Invalid option")
