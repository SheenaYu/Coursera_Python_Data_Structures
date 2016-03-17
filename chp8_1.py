fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.strip()
    words = line.split()
    # remove duplicative words
    for word in words:
        if word not in lst:
            lst.append(word)

# sort the list of words alphabetically    
lst.sort()
print lst
