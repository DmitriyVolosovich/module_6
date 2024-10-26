
class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible is True:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        elif food.edible is False:
            self.alive = False
            print(f'{self.name} не стал есть {food.name}')

class Plant:
    def __init__(self, name):
        self.name = name
    edible = False

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    edible = False

class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)