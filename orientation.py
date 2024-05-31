from enum import Enum

class Orientation(Enum):
    north = "north"
    east = "east"
    south = "south"
    west = "west"

    def get_left(self):
        match self:
            case Orientation.north:
                return Orientation.east
            case Orientation.east:
                return Orientation.south
            case Orientation.south:
                return Orientation.west
            case _:
                return Orientation.north
            
    def get_right(self):
        match self:
            case Orientation.north:
                return Orientation.west
            case Orientation.west:
                return Orientation.south
            case Orientation.south:
                return Orientation.east
            case _:
                return Orientation.north
    
    def __str__(self) -> str:
        return self.value