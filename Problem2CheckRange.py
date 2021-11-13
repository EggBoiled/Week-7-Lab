#Check the range if the entered number is in range(1, 10)

X = range(1, 11,)
Number = int(input("Enter number: "))

if Number in X:
    print("Number is in range")
else:
    print("Number is not in range")