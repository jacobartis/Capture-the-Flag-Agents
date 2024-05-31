from agent import Agent
from coordinates import Coordinates

class Space():

    def __init__(self, coordinates:Coordinates):
        self.agent = None
        self.coordinates = coordinates

    def add_agent(self,agent):
        self.agent = agent
    
    def get_agent(self):
        return self.agent
    