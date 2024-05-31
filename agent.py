import mesa
from coordinates import Coordinates
from orientation import Orientation

class Agent(mesa.Agent):

    def __init__(self, unique_id, model, start_space):
        super().__init__(unique_id, model)
        self.orientation = Orientation.north
        self.space = start_space
    
    #Called every cycle for the environment
    def step(self):
        observations = self.observe()
        if observations['center']:
            if observations['center'].get_object():
                observations['center'].get_object().interact()
        
        if observations['forward'] is None:
            self.turn_left()
        else:
            self.move()
        print(f"{str(self.unique_id)} pos:{str(self.space.coordinates)} ori:{str(self.orientation)}")

    def turn_left(self):
        self.orientation = self.orientation.get_left()

    def move(self):
        #assert  in grid, "Trying to move to an invalid space"
        self.model.move_agent(self,self.space.coordinates.forward(self.orientation))
    
    def observe(self):
        current_coords = self.space.coordinates
        return {
            'center':self.model.get_cell(current_coords),
            'forward':self.model.get_cell(current_coords.forward(self.orientation)),
            'forward left':self.model.get_cell(current_coords.forward_left(self.orientation)),
            'left':self.model.get_cell(current_coords.left(self.orientation)),
            'forward right':self.model.get_cell(current_coords.forward_right(self.orientation)),
            'right':self.model.get_cell(current_coords.right(self.orientation)),
        }