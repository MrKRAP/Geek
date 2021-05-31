class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        new_matrix = []
        matrix_1 = []
        if len(self.matrix) != len(other.matrix):
            print("Так нельзя?")
        else:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):
                    new_matrix.append(self.matrix[i][j] + other.matrix[i][j])

                print(new_matrix)
                matrix_1.append(new_matrix)
                new_matrix.clear() # Почему при вызове очистки листа, он удаляет его из другого листа тоже?

        return matrix_1

    def __str__(self):
        for row in self.matrix:
            for el in row:
                print(el, end=' ')
            print()


A = [[2, 3, 4, 5], [2, 7, 4, 5]]
a = Matrix([[2, 3, 4, 5], [2, 7, 4, 5]])
b = Matrix([[2, 3, 8, 5], [2, 7, 4, 5]])

print(a + b)

a.__str__()
