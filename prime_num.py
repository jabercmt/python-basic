n = int(input("Enter a number: "))
for x in range(1,n+1):
    if x > 1:
        for i in range(2,x):
            if (x % 2) == 0:
                break
        else:
            print(x)
