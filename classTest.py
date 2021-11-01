class Things:
    def tobe(self):
        pass


class Inanimate(Things):
    pass


class Animate(Things):
    pass


class Animals(Animate):
    def breath(self):
        pass

    def move(self):
        pass

    def eat_food(self):
        pass


class Mammals(Animals):
    def eat_milk(self):
        pass


class Giraffes(Mammals):
    def eat_trees(self):
        pass


animal = Giraffes()
animal.eat_food()
