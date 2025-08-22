a=int(input("Enter first angle: "))
b=int(input("Enter second angle: "))
c=int(input("Enter third angle: "))
if a==90 or b==90 or c==90:
    print("The triangle is a Right triangle.")
elif a>90 or b>90 or c>90:
    print("The triangle is an Obtuse triangle.")
else:
    print("The triangle is an Acute triangle.")