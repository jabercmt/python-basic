words = list(map(str, input("Enter words: ").split(',')))
words.sort()
print(','.join(words))
