# Animal abstract data type:
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age
    
    def set_name(self, name=''):
        self.name = name

    def __str__(self):
        return 'Animal: ' + str(self.name) + ', ' + str(self.age) + ' years old.'

# Inheritance example 1:
class Cat(Animal):
    def speak(self):
        print('meow')
    
    def __str__(self):
        return 'Cat: ' + str(self.name) + ', ' + str(self.age) + ' years old.'

# Inheritance example 2:
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friends(self, friend_name):
        if friend_name not in self.friends:
            self.friends.append(friend_name)
    
    def speak(self):
        print(f'Hello! I am {self.name}!')
    
    def age_diff(self, other):
        diff = self.age - other.age
        print(f'{abs(diff)} year difference..')

    def __str__(self):
        return 'Person: ' + str(self.name) + ', ' + str(self.age) + ' years old.'

# Inheritance example 3:
from random import random

class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    
    def change_major(self, major):
        self.major = major

    def speak(self):
        rand = random()
        if rand < 0.25:
            print('I have homework')
        elif 0.25 <= rand < 0.5:
            print('I need a sleep')
        elif 0.5 <= rand < 0.75:
            print('I should eat')
        else:
            print('I am watching TV')
    
    def __str__(self):
        return 'Student: ' + str(self.name) + ', ' + str(self.age) + ' years old and major ' + str(self.major)

# Use of class variables:
class Rabbit(Animal):
    tag = 1

    def __init__(self, age, parent_1=None, parent_2=None):
        Animal.__init__(self, age)
        self.parent_1 = parent_1
        self.parent_2 = parent_2
        self.rabbit_id = Rabbit.tag
        Rabbit.tag += 1

    def get_rabbit_id(self):
        return str(self.rabbit_id).zfill(3)

    def get_parent_1(self):
        return self.parent_1

    def get_parent_2(self):
        return self.parent_2

    def __add__(self, other):
        return Rabbit(0, self, other)
    
    def __str__(self):
        return 'Rabbit: ' + self.get_rabbit_id()


if __name__ == '__main__':
    # Animal abstract data type:
    animal = Animal(3)
    animal.set_name('Conda')
    print('Age of', animal.get_name(), 'is', animal.get_age())
    print(animal)

    # Inheritance example 1:
    cat = Cat(1)
    print(cat)

    # Inheritance example 2:
    person_1 = Person('John', 25)
    person_2 = Person('Jim', 27)
    person_2.age_diff(person_1)

    # Inheritance example 3:
    student_1 = Student('Alice', 20, 'CS')
    student_2 = Student('Beth', 19)
    print(student_1)
    student_1.speak()
    student_2.speak()
    
    # Use of class variables:
    rabbit_1 = Rabbit(3)
    rabbit_2 = Rabbit(4)
    rabbit_3 = Rabbit(5)
    print('Rabbit 1:', rabbit_1)
    print('Rabbit 2:', rabbit_2)
    print('Rabbit 3:', rabbit_3)
    
    rabbit_4 = rabbit_1 + rabbit_2
    print('Rabbit 4:', rabbit_4)