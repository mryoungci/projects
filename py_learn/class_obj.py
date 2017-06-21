class person:

    number = 0
    list = []
    def __init__(self,name):
        self.name = name
        person.number += 1
        print("initializing")
        person.list.append(self.name)
    def __del__(self):
        person.number -= 1

        if person.number ==1:
            print("I am the only person!")

        else:
            print("There are still %d people existing" %(person.number))

    def sayhi(self):
        print("My name is :",self.name)


    def saybye(self):

        print("%s quit" %(self.name))
        person.list.remove(self.name)
        person.number -= 1

    def howmany(self):
        if person.number == 1 :
            print("I am the only person!")

        else:
            print("There are still %d people existing" % (person.number))
        print("current person name list:%s " % (person.list))

yangxi = person("yangxi")
yangxi.sayhi()
yangxi.howmany()

huchao = person("huchao")
huchao.sayhi()
huchao.howmany()
huchao.saybye()
huchao.howmany()
