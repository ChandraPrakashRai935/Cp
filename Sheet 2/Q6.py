num=int(input("Enter a number: "))
sum=0
if num< 1:
    print("Enter a positive number")
else:
    for i in range(1,num+1):
        if i%2==0:
            sum += i
    print(sum)