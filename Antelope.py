import Animal


class Antelope(Animal.Animal):

    def __init__(self, world):
        super(Antelope, self).__init__(world, 4, 4,
                                       "Antelope", "Antelope", (238, 182, 95))
        self.moveRange = 2
