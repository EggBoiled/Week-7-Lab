# A function that multiple all numbers in a list

def multiplyList(Numbers):

    total = 1
    for x in Numbers:
        total *= x
    return total
print(multiplyList((5, 2, 7, -1)))




