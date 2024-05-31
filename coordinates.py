from orientation import Orientation

class Coordinates():

    def __init__(self,x,y) -> None:
        self.__x = x
        self.__y = y
    
    def get_coords(self):
        return (self.__x,self.__y)

    def __add__(self,coords:tuple[int, int]):
        return Coordinates(self.__x+coords[0],self.__y+coords[1])

    def __sub__(self,coords):
        return Coordinates(self.__x-coords[0],self.__y-coords[1])
    
    def __str__(self) -> str:
        return str(f"({self.__x}, {self.__y})")
    
    def forward(self, orientation:Orientation):
        assert orientation in [Orientation.north, Orientation.south, Orientation.west, Orientation.east]
        match orientation:
            case Orientation.north:
                return Coordinates(self.__x,self.__y-1)
            case Orientation.south:
                return Coordinates(self.__x,self.__y+1)
            case Orientation.east:
                return Coordinates(self.__x+1,self.__y)
            case _:
                return Coordinates(self.__x-1,self.__y)
    
    def backward(self, orientation:Orientation):
        assert orientation in [Orientation.north, Orientation.south, Orientation.west, Orientation.east]
        match orientation:
            case Orientation.north:
                return Coordinates(self.__x,self.__y+1)
            case Orientation.south:
                return Coordinates(self.__x,self.__y-1)
            case Orientation.east:
                return Coordinates(self.__x-1,self.__y)
            case _:
                return Coordinates(self.__x+1,self.__y)

    def left(self, orientation:Orientation):
        assert orientation in [Orientation.north, Orientation.south, Orientation.west, Orientation.east]
        match orientation:
            case Orientation.north:
                return Coordinates(self.__x-1,self.__y)
            case Orientation.south:
                return Coordinates(self.__x+1,self.__y)
            case Orientation.east:
                return Coordinates(self.__x,self.__y-1)
            case _:
                return Coordinates(self.__x,self.__y+1)

    def right(self, orientation:Orientation):
        assert orientation in [Orientation.north, Orientation.south, Orientation.west, Orientation.east]
        match orientation:
            case Orientation.north:
                return Coordinates(self.__x+1,self.__y)
            case Orientation.south:
                return Coordinates(self.__x-1,self.__y)
            case Orientation.east:
                return Coordinates(self.__x,self.__y+1)
            case _:
                return Coordinates(self.__x,self.__y-1)
    
    def forward_left(self, orientation:Orientation):
        assert orientation in [Orientation.north, Orientation.south, Orientation.west, Orientation.east]
        match orientation:
            case Orientation.north:
                return Coordinates(self.__x-1,self.__y-1)
            case Orientation.south:
                return Coordinates(self.__x+1,self.__y+1)
            case Orientation.east:
                return Coordinates(self.__x+1,self.__y-1)
            case _:
                return Coordinates(self.__x-1,self.__y+1)

    def forward_right(self, orientation:Orientation):
        assert orientation in [Orientation.north, Orientation.south, Orientation.west, Orientation.east]
        match orientation:
            case Orientation.north:
                return Coordinates(self.__x+1,self.__y-1)
            case Orientation.south:
                return Coordinates(self.__x-1,self.__y+1)
            case Orientation.east:
                return Coordinates(self.__x+1,self.__y+1)
            case _:
                return Coordinates(self.__x-1,self.__y-1)