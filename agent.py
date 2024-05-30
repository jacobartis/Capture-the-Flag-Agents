import mesa

class Agent(mesa.Agent):

    def __init__(self, unique_id, model, start_pos=(0,0)):
        super().__init__(unique_id, model)
        self.coordinates = start_pos

    def step(self):
        print(f"{str(self.unique_id)} stepped, pos:{str(self.coordinates)}")
        self.move()

    def move(self):
        grid = self.model.grid
        assert (self.coordinates[0]+1,self.coordinates[1]) in grid, "Trying to move to an invalid space"
        self.coordinates = (self.coordinates[0]+1,self.coordinates[1])