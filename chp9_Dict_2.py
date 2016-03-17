# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
try:
    handle = open(name)
except:
    print "File", name, "cannot be opened."
    
counts = dict()

for line in handle:
    if len(line) < 0 : continue
    if not line.startswith("From ") : continue
    wds = line.split()
    email = wds[1]
    counts[email] = counts.get(email,0) + 1
    
bigcount = None
bigname = None
for name,count in counts.items():
    if bigname is None or count > bigcount:
        bigname = name
        bigcount = count
print bigname, bigcount
        