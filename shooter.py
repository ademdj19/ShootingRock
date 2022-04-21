import time_manager
class shooter:
    def __init__(self,x,y,zone,index,image_):
        self.index = index
        self.x = x
        self.y = y
        self.zone = zone
        self.w = 50
        self.h = 50
        self.delta = 0
        self.pre_function = "0"
        self.function = "0"
        self.pre_shooting_function = "0"
        self.shooting_function = "0"
        self.shooting = False
        self.pick_up_time = 0 # in frames
        self.dropped_time = 0 # in frames
        self.image = image_
    def assign_function(self,function_str):
        self.pre_function = self.function
        self.function = function_str
        
    def eval_function(self):
        t = (float(time_manager.frames_not_paused)/60)
        return eval(self.function)
    
    def assign_shooting_function(self,function_str):
        self.pre_shooting_function = self.shooting_function
        self.shooting_function = function_str
        
    def eval_shooting_function(self):
        t = (float(time_manager.frames_not_paused)/60)*(not time_manager.game_paused)
        return eval(self.shooting_function)
            
    def free_move(self):
        self.delta = 0
        self.x = mouseX
        return mouseY
    def stop_moving(self):
        self.y = mouseY
        self.x = mouseX
        self.function = self.pre_function
        self.delta = 0
        self.dropped_time = frameCount
    def update(self,targets,main):
        self.y -= self.delta
        self.delta = self.eval_function()
        self.y += self.delta
        self.x = min(max(self.zone[0],self.x),self.zone[1])
        if self.eval_shooting_function()>0:
            self.shoot(targets,main)
            self.shooting = True
        else:
            self.shooting = False
        
    def show(self):
        if self.shooting:
            strokeWeight(5)
            stroke(255,120,2)
            line(self.x+self.w/2,self.y,width,self.y)
        noStroke()
        rectMode(CENTER)
        fill("#EAD94C")
        rect(self.x,self.y,self.w,self.h,10)
        
        fill(255)
        textSize(self.w/2)
        textAlign(CENTER,CENTER)
        text(self.index,self.x,self.y)
            
        
    def shoot(self,targets,main):
        if main.y+main.size_ > self.y > main.y:
            print("main destroyed")
        else:
            for target in targets:
                if target.y+target.size_ > self.y > target.y:
                    targets.remove(target)
    def check(self):
        if mousePressed and self.x+self.w/2>mouseX>self.x-self.w/2 and self.y+self.h/2>mouseY>self.y-self.h/2:
            self.pick_up_time = frameCount
            return True
        return False
    def pick_up_recently(self):
        return frameCount-self.pick_up_time<40
    def dropped_recently(self):
        return frameCount-self.dropped_time<40
    def pickup(self):
        self.y = 0
        self.pick_up_time = frameCount
        self.assign_function("self.free_move()")
        
                
    
    
        
