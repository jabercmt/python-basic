my_info = []
n = int(input("Enter a number: "))
my_info = list(map(int, input().split(" ")))
my_info.sort(reverse=True)
print(my_info)