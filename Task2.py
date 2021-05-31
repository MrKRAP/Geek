class Clothes:

    summary_rate = 0

    def __init__(self, id, v, h):
        self.id = id
        self.v = v
        self.h = h

    @property
    def thread_length(self):
        return 2 * (self.v + self.h)


class Coat(Clothes):

    def rate(self):
        rate = self.v / 6.5 + 0.5
        Clothes.summary_rate += rate
        return rate

    @property
    def cost(self):
        return self.rate() * 100

class Suit(Clothes):

   def rate(self):
        rate = 2 * self.h + 0.3
        Clothes.summary_rate += rate
        return rate

   @property
   def cost(self):
       return self.rate() * 130

class Trousers(Clothes):

    def rate(self):
        rate = self.v / 3.5 + 0.25 # расчет расхода ткани
        Clothes.summary_rate += rate
        return rate

    @property
    def cost(self):
        return self.rate() * 80


coat_1 = Coat(152, 48, 190)
suit_1 = Suit(113, 82, 176)
trousers_1 = Trousers(114, 46, 178)


print(coat_1.id,coat_1.rate(),suit_1.thread_length)
