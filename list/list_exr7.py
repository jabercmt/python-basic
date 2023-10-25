#Built in functiion all().

list = [1,3,4,5]
print(all(list))

#all values false.

list = [0,False]
print(all(list))

#one false value
list = [5,False,5]
print(all(list))

#empty iterable
list = []
print(all(list))