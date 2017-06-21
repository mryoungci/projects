## use *args to put a list or  tuple into a function ##
def powersum(power,*args):
    total = 0
    for i in args:
        total+= pow(i,power)
    print(total)

# a = input("Please input a number:")
# a = int(a)
# powersum(2,a)
powersum(2,3,4)
powersum(2,10)
#########################################################

## lambda usage ##
def make_return(n):
    return lambda s: s*2

n_2 = make_return(2)
print(n_2('yang'))
print(n_2(4))
###################

######## range over two list #######

questions = ['name','sex','age']
answers = ['yangxi','male','23']
for q , a in zip(questions,answers):
    print("what is your {0}? It is {1}".format(q,a))

####################################