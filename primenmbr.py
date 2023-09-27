n = int(input("Enter a number: "))
for x in range(2,n+1,1):
    if n % x == 0: 
        break
if x == n:
    print("prime number")
else:
    print("not prime number  ")