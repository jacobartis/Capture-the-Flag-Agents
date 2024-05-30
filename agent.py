import mesa

class Agent(mesa.Agent):

    def __init__(self, unique_id, model, start_pos=(0,0)):
        super().__init__(unique_id, model)
        self.set_coordinates(start_pos)

    def get_coordinates(self):
        return (self.__x,self.__y)

    def set_coordinates(self,coords):
        self.__x = coords[0]
        self.__y = coords[1]

    def step(self):
        observations = self.observe()
        print(observations)
        print(f"{str(self.unique_id)} stepped, pos:{str(self.get_coordinates())}")
        
        if (self.__x+1,self.__y+1) in self.model.grid:
            self.move()

    def move(self):
        grid = self.model.grid
        assert (self.__x,self.__y+1) in grid, "Trying to move to an invalid space"
        self.set_coordinates((self.__x,self.__y+1))
    
    def observe(self):
        return {
            'front':self.model.get_cell((self.__x,self.__y+1)),
            'back':self.model.get_cell((self.__x,self.__y-1)),
            'left':self.model.get_cell((self.__x-1,self.__y)),
            'back':self.model.get_cell((self.__x+1,self.__y)),
        }