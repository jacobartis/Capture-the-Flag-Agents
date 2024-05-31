import mesa
from agent import Agent
from space import Space
from time import sleep
from coordinates import Coordinates

def main():
    environment = Enviornment()
    while True:
        environment.step()
        sleep(1)

def generate_grid(x,y):
    spaces = {}
    for i in range(x):
        for j in range(y):
            spaces[(i,j)] = Space(Coordinates(i,j))
    return spaces

class Enviornment(mesa.Model):

    def __init__(self):
        super().__init__()

        self.schedule = mesa.time.RandomActivation(self)
        
        self.grid = generate_grid(5,5)

        self.schedule.add(Agent(1, self, self.grid[(0,0)]))

        print(self.grid)
        # 0 = Off
        # 1 = On

    def get_cell(self,coordinates):
        print(coordinates)
        if not coordinates.get_coords() in self.grid: return None
        return self.grid[coordinates.get_coords()]

    def change_cell(self,cell):
        self.grid[cell] = (self.grid[cell]+1)%1

    def step(self):
        self.schedule.step()

if __name__ == "__main__":
    main()