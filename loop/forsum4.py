#4 + 8 + 12 +......n
n = int(input("Enter a number: "))
sum = 0
for x in range(4,n+1,4):
    sum = sum + x
print(sum)