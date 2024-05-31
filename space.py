from agent import Agent
from coordinates import Coordinates
from ctf_object import CTFObject

class Space():

    def __init__(self, coordinates:Coordinates):
        self.agent = None
        self.object = None
        self.coordinates = coordinates
    
    def set_object(self,obj:CTFObject):
        self.object = obj
    
    def get_object(self):
        return self.object

    def set_agent(self,agent:Agent):
        self.agent = agent
        agent.space = self
    
    def remove_agent(self):
        self.agent = None

    def get_agent(self):
        return self.agent