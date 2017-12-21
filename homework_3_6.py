class Animal:
    calories = 0

    def move(self):
        if (self.calories > 0):
            self.calories -= 1
        else:
            raise Exception("No calories - no move")

    def eat(self, food_type, calories):
        self.calories += calories
        print ("Am-nam-nam")

    def song(self):
        print ("Default song")


class Mammal(Animal):
    def walk(self):
        try:
            Animal.move(self)
        except Exception as ex:
            print (ex)
        print ("Mammal walk, calories {0}".format(self.calories))

    def eat(self, food_type, cals):
        if (food_type == 'grass'):
            Animal.eat(self, food_type, cals)

        else:
            print ("A mammal does not eat " + food_type)


class Bird(Animal):
    def fly(self):
        try:
            Animal.move(self)
        except Exception as ex:
            print (ex)
        print ("Bird fly, calories {0}".format(self.calories))

    def eat(self, food_type, cals):
        if food_type == 'millet':
            Animal.eat(self, food_type, cals)
        else:
            print ("A bird does not eat " + food_type)


class Cow(Mammal):
    def song(self):
        print ("Muu-Muu")


class Goat(Mammal):
    def song(self):
        print ("Meeee")


class Sheep(Mammal):
    def song(self):
        print ("Beeee")


class Pig(Mammal):
    pass


class Duck(Bird):
    def song(self):
        print ("Krya")


class Chicken(Bird):
    pass


class Gees(Bird):
    def song(self):
        print ("Ga-ga-ga")


farm = [Cow(), Goat(), Sheep(), Pig(), Duck(), Chicken(), Gees()]
cals = 3

for pet in farm:
    print (pet.__class__)
    pet.eat("grass", 3)
    pet.eat("millet", 3)
    for c in range(0, cals + 1):
        try:
            pet.fly()
        except Exception as ex:
            print (ex)
        try:
            pet.walk()
        except Exception as ex:
            print (ex)
    pet.song()
