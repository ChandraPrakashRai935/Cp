num=int(input("Enter a number: "))
if(num <= 0):
    print("Please enter a positive number")
else:
    for i in range(num, 0, -1):
        print(i, end=" ")

