class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name} is barking.And he happens to be {self.age} years')

    def sprinting(self):
        print(f'feels awesome to sprint.I am {self.name} and i am {self.age}.Probably sprinting')


my_dog = Dog('Simba', 12)
print(f'hello !!I am {my_dog.name} and probably {my_dog.age} years old')
my_dog.bark()
my_dog.sprinting()


my_dog = Dog('\nlambosky', 12)
print(f'hello !!I am {my_dog.name} and probably {my_dog.age} years old')
my_dog.bark()
my_dog.sprinting()
