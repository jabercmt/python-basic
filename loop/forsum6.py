#2*2 + 4*4 + 6*6 +.....n*n
n = int(input("Enter a number: "))
sum = 0
for x in range(2,n+1,2):
    sum = sum + x*x
print(sum)