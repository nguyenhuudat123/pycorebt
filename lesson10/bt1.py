class dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

class pet:
    def __init__(self, dog1, dog2, dog3, dog4):
        self.name = [dog1.name, dog2.name, dog3.name, dog4.name]
        self.age = [dog1.age, dog2.age, dog3.age, dog4.age]

    def cz1(self):
        print(f' I have {len(self.name)} dogs.')
        for i in range(4):
            print(self.name[i], 'is', self.age[i])

dog1 = dog("Tom", 6)
dog2 = dog('Jerry', 9)
dog3 = dog('Butt', 3)
dog4 = dog('Wine', 1)
pets = pet(dog1, dog2, dog3, dog4)
pets.cz1()
print(f'and they are all {dog1.species}')