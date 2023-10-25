# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sort them alphanumerically.

words = list(map(str, input().split()))
uniques = []
for word in words:
    if word not in uniques:
        uniques.append(word)
    uniques.sort()
    for unique_word in uniques:
        print(unique_word,end='')