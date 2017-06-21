import os
note = "learn python and tensorflow,makes you a good job!"

f = open('note.txt','w')
f.write(note)
f.close()

f = open('note.txt')

while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)
f.close()