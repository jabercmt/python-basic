lo = 1
hi = 1000

l=[]
for i in range(lo, hi + 1):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(', '.join(l))
