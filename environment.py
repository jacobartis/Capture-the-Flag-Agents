import mesa
from agent import Agent
from time import sleep

def main():
    environment = Enviornment()
    while True:
        environment.step()
        sleep(1)

class Enviornment(mesa.Model):

    def __init__(self):
        super().__init__()

        self.schedule = mesa.time.RandomActivation(self)
        
        self.schedule.add(Agent(1, self, (0,0)))

        self.grid = {
            (0,0):0,(1,0):0,(2,0):0,(3,0):0,(4,0):0,
            (0,1):0,(1,1):0,(2,1):0,(3,1):0,(4,1):0,
            (0,2):0,(1,2):0,(2,2):0,(3,2):0,(4,2):0,
            (0,3):0,(1,3):0,(2,3):0,(3,3):0,(4,3):0,
            (0,4):0,(1,4):0,(2,4):0,(3,4):0,(4,4):0,
        }
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