import re
x = open("regex_sum_1014917.txt")
n=0
sumlist=list()
for line in x:
    line=line.rstrip()
    #print(line)
    y = re.findall('[0-9]+', line)
    for i in y:
        n+=int(i)
    

print(n)
