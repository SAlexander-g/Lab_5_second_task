class Point():

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __repr__(self):
        return f"X:{self.__x} Y:{self.__y}"