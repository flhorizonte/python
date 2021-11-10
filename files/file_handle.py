xfile = open('file.txt')
count = 0
for cheese in xfile:
    count = count + 1
    print(chesse)


print('Line count: ', count)


fhand = open('big_file.txt')
inp = fhand.read()

print(len(inp))

#searching through a file

for line in xfile:
    line = line.rstrip()
    if line.startswith('From:'):
        print line

#skiping withg continue

for line in xfile:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

#using 'in' to select lines
for line in xfile:
    line = line.rstrip()
    if not 'uct.ac.az' in line:
        continue
    print(line)
