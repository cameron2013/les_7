class Matrix():

    def __init__(self, width, hight, *args):
        if len(args) == 1:
            args = args[0]
        self.hight = hight
        self.width = width
        self.horiz = []
        self.vert = []
        i = 0
        j = 0
        n = 1
        if width * hight == len(args):
            while i < hight:
                while j < len(args) // hight * n:
                    self.horiz.append(args[j])
                    j += 1
                i += 1
                self.vert.append(self.horiz)
                self.horiz = []
                n += 1
        else:
            print("Неверные данные")

    def __str__(self):
        s = ""
        for i in range(self.hight):
            s = s + "|"
            for j in range(self.width):
                if j == self.width - 1:
                    s = s + str(self.vert[i][j]) + "|"
                else:
                    s = s + str(self.vert[i][j]) + "  "
            s = s + "\n"
        return s

    def __add__(self, other):
        if self.width == other.width:
            if self.hight == other.width:
                new_matrix = []
                for i in range(self.hight):
                    for j in range(self.width):
                        new_matrix.append(self.vert[i][j] + other.vert[i][j])
            else:
                print("Неверный размер матрицы")
        else:
            print("Неверный размер матрицы")
        return Matrix(self.width, self.hight, new_matrix)


a = Matrix(3, 3, 5, 4, 7, 8, 5, 4, 8, 7, 5)
print(a)
b = Matrix(3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(b)
print(a+b)
