zoo = ('python', 'elephant', 'penguin')
print('arr', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('arr', len(new_zoo))
print('all el in arr', new_zoo)
print('3d el in arr', new_zoo[2])
print('last el in 2d arr', new_zoo[2][2])
print('count in new zoo', len(new_zoo)-1+len(new_zoo[2]))
