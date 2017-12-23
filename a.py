PATH = '/home/user/q1.py'   
f = open( PATH, 'r')
def filter(line):
    line = list(line)
    for x in line:
        if x == '\'' or x == '\"' :
            line.remove(x)
    s = ''
    for x in line:
        s = s + x

    s = int(s)
    return s

line_list = []

for line in f:
    line,z = line.split('\n')
    if line:
        line = filter(line)
        line_list.append(line)

line_list.sort()
print line_list
