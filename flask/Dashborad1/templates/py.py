file = open('tc','r')

st = ''

for i in file:
    for j in i:
        if j != '\n':
            st += i
print(st)