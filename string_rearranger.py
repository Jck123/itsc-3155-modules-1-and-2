strIn = input("Enter a string: ")

lowerC = list()
upperC = list()

for c in strIn:
    if c.isalpha():
        if c.isupper():
            upperC.append(c)
        else:
            lowerC.append(c)
    else:
        continue

print("".join(lowerC) + "".join(upperC))