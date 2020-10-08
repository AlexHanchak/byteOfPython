class Robot:
    population = 0

    def __init__(self, name):
        '''init data.'''
        self.name = name
        print('(initialization {0})'.format(self.name))

        Robot.population += 1

    def __del__(self):
        '''i dai'''
        print('{0} destroy!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{0} was last'.format(self.name))
        else:
            print('left {0:d} worked robots'.format(self.population))

    def sayHi(self):
        print('my owners names me {0}'.format(self.name))

    def howMany():
        print('we have {0:d} robots.'.format(Robot.population))

    howMany = staticmethod(howMany)


droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()
droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()
print('some action')

print('delete robots')
del droid1
del droid2

Robot.howMany()
