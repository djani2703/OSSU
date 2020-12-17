# -*- coding: utf-8 -*-

# A sample class:
class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

an = PartyAnimal()

an.party()
PartyAnimal.party(an)

# Playing with dir() and type()
x = list()
type_x = type(x)
dir_x = dir(x)

print('Type:', type_x)
print('Dir:', dir_x)

# Constructor and destructor:
class PartyAnimal2:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal2()
an.party()
PartyAnimal2.party(an)

an = 42
print('an contains', an)

# Additional parameters for constructor:
class PartyAnimal3:
    x = 0
    name = ''
    def __init__(self, name):
        self.name = name
        print(self.name, 'constructed!')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)

s = PartyAnimal3('Sally')
s.party()

j = PartyAnimal3('Jim')
j.party()

# Inheritance:
class FootballFan(PartyAnimal3):
    points = 0

    def touch_down(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)

ff = FootballFan('Alex')
ff.party()
ff.touch_down()
