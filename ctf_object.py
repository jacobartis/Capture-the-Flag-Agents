
class CTFObject():

    def __init__(self) -> None:
        return

    def interact(self):
        print("interaction")

class Flag(CTFObject):

    def __init__(self,colour:str) -> None:
        self.colour = colour
    
    def interact(self):
        print(self.colour)