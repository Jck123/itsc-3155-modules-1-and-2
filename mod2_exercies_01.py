#James Kelly

def get_unique_list(listIn):
    uniqueList = list()
    for x in my_list:
        if uniqueList.count(x) == 0:
            uniqueList.append(x)
    return uniqueList

my_list = [1, 2,  3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)