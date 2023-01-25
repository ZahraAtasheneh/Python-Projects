import random





class Dog:
    info = 'the cutest animal on earth'

    def __init__(self, name):
        print('I\'m HAPPY!')
        self.favourite_number = random.randint(1,25)
        self.name = name
    
    def bark(self):
        print(f'Heya! I\'m {self.name} and my favorite number is {self.favourite_number}!')


dog1 = Dog('Harry')
dog2 = Dog('Sally')


dog1.bark()
dog2.bark()
