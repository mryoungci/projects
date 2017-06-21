# -*- coding: utf-8 -*-
import pickle as p

shoplistname = 'shoplist.data'

shoplist = ['apple','orange','mango']

f = open(shoplistname,'wb')
p._dump(shoplist,f)
f.close()
del shoplist

f = open(shoplistname)
list = p.load(f)
print(list)

