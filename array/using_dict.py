ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("address Swaroop'a: ", ab['Swaroop'])
#delete element
del ab['Spammer']

print('\nIn Address book {0} contacts\n'.format(len(ab)))

for name, address in ab.items():
    print('contact {0} with address {1}'.format(name, address))

#add element kay value
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nAddress Guido:", ab['Guido'])
