import time_manager
class targetrock:
    def __init__(self,orbit,radius,phase,speed,image_):
        self.orbit = orbit
        self.radius = radius
        self.phase = phase
        self.speed = speed
        self.angle = self.phase
        self.size_ = 35
        self.image = image_
        self.update_cords()
    def update_cords(self):
        self.x = self.orbit.x + cos(radians(self.angle))*self.radius
        self.y = self.orbit.y + sin(radians(self.angle))*self.radius
    def update(self):
        self.angle += self.speed*(not time_manager.game_paused)
        self.update_cords()
    def show(self):
        noStroke()
        #fill(255,0,0)
        #ellipse(self.x,self.y,self.size_,self.size_);
        image(self.image,self.x,self.y,self.size_,self.size_)
        
        
        
        
    
        
