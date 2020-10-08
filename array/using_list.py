shoplist = ['Apples', 'mango', 'caret', 'banana']

print('i mast do', len(shoplist), 'bay')

print(' now in my bag', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\n And need bay coffee')
shoplist.append('coffee')
print('now my list views like this', shoplist)

print('first what i need bay ', shoplist[0])
oldItem = shoplist[0]
del shoplist[0]
print('i bay', oldItem)

print('now my shopping list view', shoplist)
