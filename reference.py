print('arr of el')
shoplist = ['Apples', 'mango', 'caret', 'banana']
mylist = shoplist #not clone, it`s reference

del shoplist[0]
print('shoplist', shoplist)
print('shoplist', mylist)

print('copy')
mylist = shoplist[:]
del mylist[0]

print(mylist)
print(shoplist)
