class Cell:

    def __init__(self, nums: int):
        self.nums = nums # колличество клеток

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        if self.nums > other.nums:
            return Cell(self.nums - other.nums)
        else:
            return 'Результат - ноль или отрицательное число'

    def __mul__(self, other):
        return Cell(self.nums * other.nums)

    def __truediv__(self, other):
        return Cell(self.nums // other.nums)


    def make_order(self, n):
        result = ''
        for i in range(self.nums):
            if i % n != 0 or i == 0:
                result += '*'
            else:
                result += '\n*'
        return result

cell_01 = Cell(5)
cell_02 = Cell(9)

print(cell_01 + cell_02)
print(cell_01 - cell_02)
print(cell_01 * cell_02)
print(cell_01 / cell_02)

print(cell_02.make_order(5))