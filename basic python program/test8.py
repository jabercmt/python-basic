# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
lines = []
while True:
    print(f"if you want to break,press only b: ",end='')
    line = input()
    if line == "b":
        break
    else:
        lines.append(line.upper())
for line in lines:
    print(lines)