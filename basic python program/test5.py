# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
num = input()
l = num.split(", ")
t=tuple(l)
print(l)
print(t)
