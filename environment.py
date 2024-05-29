from agent import Agent
from time import sleep

def main():
    environment = Enviornment([Agent])
    while True:
        environment.cycle()
        sleep(1)

class Enviornment():
    grid = {
        (0,0):0,(1,0):0,(2,0):0,(3,0):0,(4,0):0,
        (0,1):0,(1,1):0,(2,1):0,(3,1):0,(4,1):0,
        (0,2):0,(1,2):0,(2,2):0,(3,2):0,(4,2):0,
        (0,3):0,(1,3):0,(2,3):0,(3,3):0,(4,3):0,
        (0,4):0,(1,4):0,(2,4):0,(3,4):0,(4,4):0,
    }
    # 0 = Off
    # 1 = On

    agents: list[Agent] = []

    def __init__(self,agents) -> None:
        self.agents = agents

    def move_agent(self, agent, new_coordinates):
        assert agent.coordinates in self.grid and new_coordinates in self.grid
        agent.coordinates = new_coordinates
        print(agent.coordinates)

    def cycle(self):
        for agent in self.agents:
            self.move_agent(agent=agent,new_coordinates=(agent.coordinates[0]+1,agent.coordinates[1]))

if __name__ == "__main__":
    main()