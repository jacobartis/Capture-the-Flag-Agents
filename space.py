from agent import Agent

class Space():

    def __init__(self):
        self.agent = None
        pass

    def add_agent(self,agent):
        self.agent = agent
    
    def get_agent(self):
        return self.agent
    