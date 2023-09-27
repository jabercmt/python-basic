#2 * 4 * 6 * ........n
n = int(input("Enter a number: "))
mul = 1
for x in range(2,n+1,2):
    mul = mul * x
print(mul)