handle = open("mbox-short.txt")

counts = dict()

for line in handle:
    wds = line.split()
    if len(wds) < 2 : continue
    if wds[0] != "From" : continue
    email = wds[1]
    counts[email] = counts.get(email,0) + 1
    
bigcount = None
bigname = None
for name,count in counts.items():
    if bigname is None or count > bigcount:
        bigname = name
        bigcount = count
print bigname, bigcount