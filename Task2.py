
class Road:

    # __weight = 25
    # __sqrt = 5

    def __init__(self,length,width):
        self.__length = length
        self.__width = width

#вариант когда изначально извезтно о весе и толщине 
    # def final(self):
    #     print("Нужно:",(self.__width*self.__length*self.__sqrt*self.__weight)//1000)

    def final(self,sqrt,weight):
        print("Нужно:",(self.__width*self.__length*sqrt*weight)//1000)


road_1  = Road(20,5000)

road_1.final(25,5)