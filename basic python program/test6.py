# You are given two number n and m. You have to made a 2D matrix where each index contains the multiple of i*j, where i means row number and j means column numbers. 

# constraints: 0 ≤ i ≤ n, 0 ≤ j ≤ m
rows, cols = map(int, input("Enter the value of n & m: ").split())
row = []

for i in range(rows):
    col = []
    for j in range(cols):
        col.append(i * j)
    row.append(col)
for i in range(rows):
    print(row[i])

