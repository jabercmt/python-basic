# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 1 and 1000 (both included).
lo = 1
hi = 1000
for i in range(lo,hi + 1):
    if i % 7 == 0 and i % 5 != 0:
        print(i,end=',')
