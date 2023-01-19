#James Kelly

intList = list()
while len(intList) < 5:
    intIn = input("Enter int #" + str(len(intList) + 1) + ":")
    if intIn.lstrip('-').isdigit() and int(intIn) % 1 == 0:
        intList.append(int(intIn))
    else:
        print("Invalid input. Please enter an int.")

print(sum(intList))