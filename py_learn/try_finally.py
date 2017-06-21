import time

try:
    f = open('note.txt')
    line = f.readline()
    while True:
        if len(line) == 0:
            break
        time.sleep(2)
        print(line)
except:
    print('finally in exception')

finally:
        f.close()
        print("Cleaning  up  and closing file")