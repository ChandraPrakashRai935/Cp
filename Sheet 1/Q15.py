num1=int(input("Enter A number: "))
num2=int(input("Enter B number: "))
num3=int(input("Enter C number: "))
if(num1<num2 and num1<num3):
    print("A is smallest number")
elif(num2<num1 and num2<num3):
    print("B is smallest number")
else:
    print("C is smallest number")