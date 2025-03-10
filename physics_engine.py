import pygame
import time
import random
class circle(object):
    def __init__(self,loc_x,loc_y,radius):
        self.x=loc_x
        self.y=loc_y
        self.radius=radius
        self.color=[255,255,255]
        self.uy=400
        self.vy=0
        self.ux=300
        self.vx=0
        self.halt=0
        
    def draw(self,screen):
        pygame.draw.circle(screen, (self.color[0],self.color[1],self.color[2]), (self.x, self.y), self.radius)
    def update(self,x_inc,y_inc):
        self.x+=x_inc
        self.y+=y_inc

class virtual_border(object):
    def __init__(self,loc_x,loc_y,width,height):
        self.x=loc_x
        self.y=loc_y
        self.color=[255,255,255]
        self.width=width
        self.height=height

    def draw(self,screen):
        pygame.draw.rect(screen,(self.color[0],self.color[1],self.color[2]),pygame.Rect((self.x-self.width/2),(self.y-self.height/2),self.width,self.height))

class physics_engine(object):
    def __init__(self,gravity:float,friction:float,width:float,height:float):
        self.g=gravity
        self.friction=friction
        self.width=width
        self.height=height
        self.reflect_factor=0.75
        
    def manage_actor(self,actor,v_border,s_time):
        if(((actor.y-actor.radius <= v_border.y+v_border.height/2 and actor.y-actor.radius >= v_border.y-v_border.height/2) or (actor.y+actor.radius <= v_border.y+v_border.height/2 and actor.y+actor.radius >= v_border.y-v_border.height/2)) and actor.x+actor.radius <= v_border.x+v_border.width/2 and actor.x+actor.radius >= v_border.x-v_border.width/2):#and actor.x+actor.radius <= v_border.x+v_border.width/2 and actor.x+actor.radius >= v_border.x-v_border.width/2
            print("in range")
            actor.color[0]=random.randint(0.0,255.0)
            actor.color[1]=random.randint(0.0,255.0)
            actor.color[2]=random.randint(0.0,255.0)
            actor.uy=-1*self.reflect_factor*actor.uy
            t_delta=time.time()-s_time
            if(actor.halt == True):
                pass
            else:
                actor.vx=actor.ux+(self.friction*t_delta)
                sx_delta=((actor.vx**2)-(actor.ux**2))/(2*self.friction)
                if(-1<actor.ux<=0):
                    actor.halt=True
                actor.ux=actor.vx
                actor.vy=actor.uy
                sy_delta=actor.vy*t_delta
                actor.update(sx_delta,(sy_delta))
        
        
        if(actor.x+actor.radius >= self.width or actor.x-actor.radius <= 0):
            print("hit border")
            actor.ux=-1*self.reflect_factor*actor.ux
            t_delta=time.time()-s_time
            sx_delta=actor.ux*t_delta
            actor.vy=actor.uy+(self.g*t_delta)
            sy_delta=((actor.vy**2)-(actor.uy**2))/(2*self.g)
            actor.update(sx_delta,(sy_delta))
            actor.uy=actor.vy
            actor.color[0]=random.randint(0.0,255.0)
            actor.color[1]=random.randint(0.0,255.0)
            actor.color[2]=random.randint(0.0,255.0)
            
        if(actor.y+actor.radius >= self.height):
            #actor.update(0,0)
            print("hit ground")
            actor.color[0]=random.randint(0.0,255.0)
            actor.color[1]=random.randint(0.0,255.0)
            actor.color[2]=random.randint(0.0,255.0)
            actor.uy=-1*self.reflect_factor*actor.uy
            t_delta=time.time()-s_time
            if(actor.halt == True):
                pass
            else:
                actor.vx=actor.ux+(self.friction*t_delta)
                sx_delta=((actor.vx**2)-(actor.ux**2))/(2*self.friction)
                if(-1<actor.ux<=0):
                    actor.halt=True
                actor.ux=actor.vx
                actor.vy=actor.uy+(self.g*t_delta)
                sy_delta=((actor.vy**2)-(actor.uy**2))/(2*self.g)
                actor.update(sx_delta,(sy_delta))
                actor.uy=actor.vy
        else:
            if(s_time==0):
                pass
            else:
                #print(actor.uy)
                t_delta=time.time()-s_time
                sx_delta=actor.ux*t_delta
                actor.vy=actor.uy+(self.g*t_delta)
                sy_delta=((actor.vy**2)-(actor.uy**2))/(2*self.g)
                actor.update(sx_delta,(sy_delta))
                actor.uy=actor.vy
            #v=u+at
            #v2=u2+2as -> (v2-u2)/2a = s
            #10.093    

pygame.init()
pygame.display.set_caption("Physics Engine")
width=500
height=500
screen=pygame.display.set_mode([width,height])
#pygame.time.wait(4000)
running=True
circle_o=circle(150,150,20)
v_border_o = virtual_border(250,290,350,5)
physics = physics_engine(90.8,-10,width,height)
start_time=0
while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running=False
        if(event.type == pygame.KEYDOWN):
            if(event.key==pygame.K_ESCAPE):
                running=False
    screen.fill((0,0,0))
    physics.manage_actor(circle_o,v_border_o,start_time)
    start_time=time.time()
    circle_o.draw(screen)
    v_border_o.draw(screen)
    pygame.display.flip()
    
pygame.quit()
