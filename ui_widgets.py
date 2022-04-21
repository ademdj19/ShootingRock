
class button:
    def __init__(self,x,y,w,h,text,callback):
        self.text = text;
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.callback = callback
        self.colddown = 0
        self.colddown_time = 20 # in frames
        self.size_of_text = None
    def show(self):
        stroke(255)
        strokeWeight(2)
        fill(33,33,33)
        rect(self.x,self.y,self.w,self.h,5)
        fill(255)
        if self.size_of_text:
            textSize(self.size_of_text)
        else:
            textSize(self.w/10)
        textAlign(CENTER,CENTER)
        text(self.text,self.x+self.w/2,self.y+self.h/2)
    def text_size(self,text_size):
        self.size_of_text = text_size
    def check(self):
        if self.colddown == 0 and mousePressed and self.x+self.w>mouseX>self.x and self.y+self.h>mouseY>self.y:
            self.callback()
            self.colddown = self.colddown_time
        self.colddown = max(0,self.colddown-1)
            
    
        
        
