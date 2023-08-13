a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a < b and a < c:
    print("minimum number is:" ,a)
elif b < a and b < c:
    print("minimum number is: " ,b)
else:
    print("minimum number is: " ,c) 