fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.split()
    for words in line:
        words.rstrip()
        if words not in lst:
            lst.append(words)
lst.sort()
print(lst)
