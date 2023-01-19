#James Kelly

def charCounter(strIn):
    outDict = dict()
    for c in strIn:
        if not c.isalpha():
            continue
        c = c.lower()
        if c in outDict:
            outDict[c] += 1
        else:
            outDict[c] = 1
    return outDict

string_input = input("Enter a string: ")
print(charCounter(string_input))