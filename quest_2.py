from abc import ABC, abstractmethod


class MyABC(ABC):
    @abstractmethod
    def material(self):
        pass


class Clothe():
    def __init__(self, name, H, V):
        self.name = name
        self.H = H
        self.V = V


class Coat(Clothe, MyABC):
    def __init__(self, name, V):
        super().__init__(name, None, V)

    @property
    def material(self):
        return self.V / 6.5 + 0.5

    def __add__(self, other):
        return self.material + other.material


class Suit(Clothe, MyABC):
    def __init__(self, name, H):
        super().__init__(name, H, None)

    @property
    def material(self):
        return 2 * self.H + 0.3

    def __add__(self, other):
        return self.material + other.material


a = Coat("Fd", 5)
print(f'{a.material:.2f}')
b = Suit("Df", 8)
print(f'{b.material:.2f}')
c = Suit("DF", 4)
print(f'{c.material:.2f}')
print(f'{a + b:.2f}')
