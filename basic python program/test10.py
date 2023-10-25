# Write a program, which will find all numbers between 100 and 300 (both included) such that each digit of the number is an even number.

# The numbers obtained should be printed in a comma-separated sequence on a single line.
even = []
lo = 100
hi = 300
for number in range(lo,hi):
    number = str(number)
    a = int(number[0]) % 2 == 0
    b = int(number[1]) % 2 == 0
    c = int(number[2]) % 2 == 0 
    if a and b and c:
        even.append(number)
print(','.join(even))
