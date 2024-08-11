class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f'Название: {self.name}, Количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if not isinstance(other, (int, House)):
            raise ArithmeticError
        return self.number_of_floors == other

    def __lt__(self, other):
        if not isinstance(other, (int, House)):
            raise ArithmeticError
        return self.number_of_floors < other

    def __le__(self, other):
        if not isinstance(other, (int, House)):
            raise ArithmeticError
        return self.number_of_floors <= other

    def __gt__(self, other):
        if not isinstance(other, (int, House)):
            raise ArithmeticError
        return self.number_of_floors > other

    def __ge__(self, other):
        if not isinstance(other, (int, House)):
            raise ArithmeticError
        return self.number_of_floors >= other

    def __ne__(self, other):
        if not isinstance(other, (int, House)):
            raise ArithmeticError
        return self.number_of_floors != other

    def __add__(self, other):
        if not isinstance(other, (int, House)):
            raise ArithmeticError
        self.number_of_floors += other
        return self.number_of_floors

    def __iadd__(self, other):
        if not isinstance(other, (int, House)):
            raise ArithmeticError
        self.number_of_floors += other
        return self.number_of_floors

    def __radd__(self, other):
        if not isinstance(other, (int, House)):
            raise ArithmeticError
        self.number_of_floors += other
        return self.number_of_floors


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)

h1 = h1 + 10
print(h1)
print(h1 == h2)

h1 += 10
print(h1)

h2 = 10 + h2
print(h2)

print(h1 > h2)
print(h1 >= h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 != h2)

