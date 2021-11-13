# Taking a list of number and return a new list with elements

def unique_list(L):
    x = []
    for a in L:
        if a not in x:
            x.append(a)
    return x

print(unique_list([1, 3, 4, 5, 6, 2, 3, 5]))