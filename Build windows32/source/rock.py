import time_manager

class rock:
    def __init__(self,x,y,image_):
        self.x = x
        self.y = y
        self.delta = 0
        self.size_ = 50
        self.image = image_
    def assign_function(self,function_str):
        self.function = function_str
    def eval_function(self):
        t = (float(time_manager.frames_not_paused)/60)
        return eval(self.function)
    def update(self):
        self.y -= self.delta
        self.delta = self.eval_function()
        self.y += self.delta
    def show(self):
        fill(255)
        image(self.image,self.x,self.y,self.size_,self.size_)
    
        
        
        
