#1*1 * 2*2 * 3*3 * ........n
n = int(input("Enter a number: "))
mul = 1
for x in range(1,n+1,1):
    mul = mul * x*x
print(mul)