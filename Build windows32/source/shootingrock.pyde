#imports
from rock import *
from targetrock import *
from shooter import *
from properoties import *
import time_manager
# global
main_rock = None
shooters = []
target_rocks = []
prp = None
shooter_sprite = None
background_image = None
edditable = None
play_pause_button = None
pre_millis = 0
levels = ("50*cos(t)","50*cos(2*t)","50*cos(sin(t))+50*sin(cos(t))","50*sin(t*sin(t))","sum(1/i*sin(t) for i in range(1,10))")
level_index = 0 
small_runs_sprites = None
shooting_score = 0
shooters_count = 0
def setup():
    
    global main_rock,target_rocks,shooters,prp,shooter_sprite,play_pause_button,background_image,small_runs_sprites
    size(800,500)
    textFont(createFont("Nirmala UI Bold", 24))
    shooter_sprite = loadImage("data/Sprites/shooter.png")
    background_image = loadImage("data/Sprites/background.jpg")
    small_runs_sprites = tuple(loadImage("data/Sprites/"+str(i+1)+".png")for i in range(7))

    main_rock = rock(width-220,height/2,small_runs_sprites[int(random(0,7))])
    main_rock.assign_function("50*cos(t)")
    play_pause_button = button(width/2-50,height-55,100,50,"Play",pause_play)
    target_rocks = [
                    targetrock(main_rock,100+random(0,80),random(0,360),random(0.3,0.5),small_runs_sprites[int(random(0,7))]) 
                    for i in range(8)
                    ]
    target_rocks.sort(key=lambda x:-x.radius)
    prp = properoties(0,0,320,100,spawn_shooter,change_function,change_shoot_function)
    
def draw():
    
    global main_rock,a_rock,target_rocks,shooters,edditable,shooting_score
    background("#51A3A3")
    fill(255)
    textAlign(RIGHT,BOTTOM)
    textSize(20)
    text(frameRate,width-20,height-20)
    textAlign(RIGHT,TOP)
    text("Level : "+str(level_index+1),width-20,20)
    play_pause_button.check()
    play_pause_button.show()
    main_rock.update()
    main_rock.show()
    for target in target_rocks:
        target.update()
        target.show()
    for shooter_ in shooters:
        shooter_.update(target_rocks,main_rock)
        shooter_.show()
        if shooter_.shooting:shooting_score+=0.1
        if not shooter_.dropped_recently() and not edditable and shooter_.check():
            edditable = shooter_
            shooter_.pickup()
            print("picked up")
    if edditable:
        if mousePressed and prp.no_recent_interactions() and not(edditable.pick_up_recently()):
            edditable.stop_moving()
            print("drooped")
            edditable = None
            

                
    prp.update(shooters)
    prp.show()
    if not time_manager.game_paused:
        time_manager.frames_not_paused += 1
    if len(target_rocks)==0:
        next_level()
    print(target_rocks)
# callbacks of buttons
def spawn_shooter():
    global shooters,edditable,shooters_count
    shooters.append(shooter(mouseX,0, [0,320],len(shooters),shooter_sprite))
    shooters[-1].assign_function("self.free_move()")
    edditable = shooters[-1]
    shooters_count += 1
def change_function():
    answer = prp.input("Move function")
    if not shooters:return
    if answer:
        t=0
        result = eval(answer)
        if type(result) in[float,int,bool] :
            shooters[prp.shooter_index].assign_function(answer)
        else:
            print("function should return a float")
def change_shoot_function():
    answer = prp.input("Shoot function")
    if not shooters:return
    if answer:
        t=0
        result = eval(answer)
        if type(result) in[float,int,bool] :
            shooters[prp.shooter_index].assign_shooting_function(answer)
        else:
            print("function should return a float")
def pause_play():
    if time_manager.game_paused:
        play_pause_button.text = "Pause"
        time_manager.game_paused = False
    else:
        play_pause_button.text = "Play"
        time_manager.game_paused = True
        
def next_level():
    global level_index,levels,target_rocks,shooters,main_rock,small_runs_sprites,shooting_score,shooters_count
    level_index+=1
    if level_index > len(levels)-1:
        background(0)
        textSize(100)
        fill(255)
        text("your score is: "+str(shooter_count+shooting_score))
    else:
        main_rock = rock(width-220,height/2,small_runs_sprites[int(random(0,7))])
        main_rock.assign_function(levels[level_index])
        target_rocks += [
                        targetrock(main_rock,100+random(0,80),random(0,360),random(0.3,0.5),small_runs_sprites[int(random(0,7))]) 
                        for i in range(8)
                        ]
        shooters = []
        pause_play()
        print(level_index)
                     
def end_of_game(frameCount):
    pass
       
