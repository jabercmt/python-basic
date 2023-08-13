a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a > b and a > c:
    print("Largest number is:" ,a)
elif b > a and b > c:
    print("Largest number is: " ,b)
else:
    print("Largest number is: " ,c)