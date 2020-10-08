import random

f = ['s', 'g']
s = ['s', 's']
t = ['g', 'g']
r = random.randrange(1, 2)
if r == 1:
    print(f[0])
    print(s[0])
    print(t[0])
else:
    print(f[1])
    print(s[1])
    print(t[1])