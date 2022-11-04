class vessel :
    def __init__(self, coordinates ,int max_hits ,weapon) :
        self.coordinates = coordinates 
        self.max_hits = max_hits
        self.weapon = weapon

    def go_to(self,x,y,z) :

    def get_coordinates(self) :
        x= self.coordinates(0)
        y= self.coordinates(1)
        z= self.coordinates(2)
        print (x,y,z)
     
    def fire_at(self,x,y,z) :
    
