
class Stationery:

    def title(self,title):
        print(title)

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):

    def draw(self):
        print("Ну тут мы рисуем ручкой ")

class Pencil(Stationery):

    def draw(self):
        print("Ну тут мы рисуем карандашом ")

class Handle(Stationery):

    def draw(self):
        print("Ну тут мы рисуем Маркером ")



st = Stationery()
st.draw()

pn = Pen()
pn.draw()

pc = Pencil()
pc.draw()

hn = Handle()
hn.draw()