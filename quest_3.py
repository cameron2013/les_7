class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if (self.cell - other.cell) >= 0:
            return Cell(self.cell - other.cell)
        else:
            print("Вычитание клеток дает отрицательный результат")

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        if other.cell != 0:
            return Cell(round(self.cell / other.cell))  # Или //
        else:
            return Cell(round(0))
            print("Деление на ноль невозможно")

    def make_order(self, number):
        s = ""
        for i in range(1, self.cell + 1):
            s = s + "*"
            if i % number == 0:
                s = s + "\n"
        s = s + '\n'
        print(s)


cell_1 = Cell(9)
cell_1.make_order(5)
cell_2 = Cell(5)
cell_2.make_order(4)
cell_3 = cell_1 + cell_2
cell_3.make_order(6)
cell_3 = cell_1 - cell_2
cell_3.make_order(6)
cell_3 = cell_1 * cell_2
cell_3.make_order(6)
cell_3 = cell_1 / cell_2
cell_3.make_order(6)
