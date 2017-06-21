import sys
try:
   s = input('Please input someting -->')

except EOFError:
    print('Why did you do an EOF on me?')

# except:
#     print("Some other unknow error occurred!")

print('Input Success!' )
print(s)