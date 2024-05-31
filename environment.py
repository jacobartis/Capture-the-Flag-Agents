import mesa
from agent import Agent
from space import Space
from time import sleep
from coordinates import Coordinates
from ctf_object import Flag 

def main():
    environment = Enviornment()
    while True:
        environment.step()
        sleep(1)

def generate_grid(x,y):
    spaces = {}
    for i in range(x):
        for j in range(y):
            spaces[Coordinates(i,j)] = Space(Coordinates(i,j))
            if i%2 or j%2:
                spaces[Coordinates(i,j)].set_object(Flag("blue"))
    return spaces

class Enviornment(mesa.Model):

    def __init__(self):
        super().__init__()

        self.schedule = mesa.time.RandomActivation(self)
        
        self.grid = generate_grid(5,5)

        self.schedule.add(Agent(1, self, self.grid[Coordinates(0,0)]))
        # 0 = Off
        # 1 = On

    def get_cell(self,coordinates):
        if not coordinates in self.grid: return None
        return self.grid[coordinates]

    def move_agent(self, agent:Agent, to_coord:Coordinates):
        assert agent in self.schedule.agents
        assert agent.space
        from_coord = agent.space.coordinates

        assert from_coord in self.grid and to_coord in self.grid
        assert self.grid[to_coord].get_agent() == None
        
        self.grid[from_coord].remove_agent()
        self.grid[to_coord].set_agent(agent)

    def turn_agent(self, coord, direction):
        assert coord in self.__grid and self.__grid[coord].has_actor()

    def step(self):
        self.schedule.step()

if __name__ == "__main__":
    main()