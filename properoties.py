from ui_widgets import *
class properoties:
    def __init__(self,x,y,w,h,spawn_callback,changing_function,changing_shoot_function):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.create_button = button(self.x+self.w-105,self.y+self.h-25,100,20,"Spawn shooter",spawn_callback)
        self.function_button = button(self.x+self.w-210,self.y+self.h-25,100,20,"Move function",changing_function)
        self.shoot_function_button = button(self.x+self.w-315,self.y+self.h-25,100,20,"Shoot function",changing_shoot_function)
        self.right_button = button(self.x+self.w-25,self.y+5,20,self.h-30,">",self.increment_shooter_index)
        self.right_button.text_size(20)
        self.left_button = button(self.x+5,self.y+5,20,self.h-30,"<",self.decrement_shooter_index)
        self.left_button.text_size(20)
        self.function_text = ""
        self.shooting_function_text = ""
        self.shooter_index = 0
        self.shooters_count = 0

        self.edditable_active = False
    def show(self):
        noStroke()
        fill(0,0,0,150);
        rectMode(CORNER);
        rect(self.x,self.y,self.w,self.h,10);
        self.create_button.show()
        self.function_button.show()
        self.shoot_function_button.show()  
        self.right_button.show()
        self.left_button.show()

        textSize(self.w/20)
        fill(255,125,75)
        if (self.shooting_function_text or self.function_text )and not("self" in self.function_text or "self" in self.shooting_function_text) :
            textAlign(LEFT,TOP)
            text("Shooter : "+str(self.shooter_index),self.x+30,self.y)
            fill(255)
            text("Move(t) = "+self.function_text,self.x+30,self.y+self.w/20)
            text("Shoot(t) = "+self.shooting_function_text,self.x+30,self.y+self.w/10)
        else:
            textAlign(CENTER,CENTER)
            text("No Shooters Available",self.x+self.w/2,self.y+self.h/2)
            
    def update(self,shooters):
        if shooters :
            self.shooting_function_text = shooters[self.shooter_index].shooting_function
            self.function_text = shooters[self.shooter_index].function
            self.shooters_count = len(shooters)
        self.create_button.check()
        self.function_button.check()
        self.shoot_function_button.check()
        self.right_button.check()
        self.left_button.check()

        
    def input(self,message):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message+"")
        
    def no_recent_interactions(self):
        return self.create_button.colddown == 0
    def increment_shooter_index(self):
        self.shooter_index += 1
        try:
            self.shooter_index %= self.shooters_count
        except ZeroDivisionError:
            pass
    def decrement_shooter_index(self):
        self.shooter_index -= 1
        try:
            self.shooter_index %= self.shooters_count
        except ZeroDivisionError:
            pass

        
