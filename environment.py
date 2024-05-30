import mesa
from agent import Agent
from space import Space
from time import sleep

def main():
    environment = Enviornment()
    while True:
        environment.step()
        sleep(1)

def generate_grid(x,y):
    spaces = {}
    for i in range(x):
        for j in range(y):
            spaces[(i,j)] = Space()
    return spaces

class Enviornment(mesa.Model):

    def __init__(self):
        super().__init__()

        self.schedule = mesa.time.RandomActivation(self)
        
        self.schedule.add(Agent(1, self, (0,0)))

        self.grid = generate_grid(5,5)
        print(self.grid)
        # 0 = Off
        # 1 = On

    def get_cell(self,cell):
        print(cell)
        if not cell in self.grid: return None
        return self.grid[cell]

    def change_cell(self,cell):
        self.grid[cell] = (self.grid[cell]+1)%1

    def step(self):
        self.schedule.step()

if __name__ == "__main__":
    main()