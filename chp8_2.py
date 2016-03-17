fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0

for line in fh:
    if len(line) < 1 : continue
    if not line.startswith('From ') : continue
    word = line.split()
    print word[1]
    count += 1

print "There were", count, "lines in the file with From as the first word"
