#1 + 1/2 + 1/3 +.....1/x
n = int(input("Enter a number: "))
sum = 0
for x in range(1,n+1,1):
    sum = sum + 1/x
print(sum)