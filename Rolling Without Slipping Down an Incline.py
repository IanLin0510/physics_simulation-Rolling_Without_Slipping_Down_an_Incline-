#!/usr/bin/env python
# coding: utf-8

# In[1]:

#simulate the motion
from vpython import *
dict={'Ktran':[],'Krot':[],'U':[],'Emech':[],'time':[]}
#creat
scene=canvas(width=900, length=600, center=vec(0.2,0.25,0), background=color.purple,range=0.5)
floor = box(pos=vec(0,0,0),length=0.8, height=0.005, width=0.05,texture=textures.metal)
base_side=float(input("please input the length of base-side:"))
height_leg=float(input("please input the length of height-leg:"))
choose = int(input('please choose:1.disk 2.sphere 3.hoop'))
translation_height=height_leg*(floor.length/2)/sqrt(base_side**2+height_leg**2)
translation_length=base_side*(floor.length/2)/sqrt(base_side**2+height_leg**2)-0.02
#set
angular = (atan(height_leg/base_side))*57.2957795
arc = (atan(height_leg/base_side))
#creat
incline = box(pos=vec(0,translation_height,0),length=0.8, height=0.0015, width=0.05, axis = vec(-base_side,height_leg,0),texture=textures.metal)
#demonstrate angular
msg = label(text=angular,pos=vec(0.2,0.03,0))
m=2#all mass
g=9.8#gravity
r=0.03#all radius
t=0#initial time
dt=0.001#interval time
a=0
w=30#angular velocity
#plot the graph
gd = graph(title="Ktrans,Krot,Ugrav", width=600, height=450, xtitle="t(s)", ytitle="Ktrans,Krot,Ugrav", align = 'left')
Ktrans = gcurve(graph=gd, color=color.blue)
Krot = gcurve(graph=gd, color=color.green)
Ugrav = gcurve(graph=gd, color=color.black)
gde = graph(title="E", width=600, height=450, xtitle="t(s)", ytitle="E", align = 'left')
E= gcurve(graph=gde, color=color.black)
if choose == 1:
    rate(100)#Halts computations until 1.0(frequency/seconds) after the previous call to rate()
    #creat
    disk = cylinder(pos=vec(-translation_length,2*translation_height+r,0),radius=r,length=0.01, axis=vec(0,0,0.1),texture='https://stickershop.line-scdn.net/stickershop/v1/product/8649/LINEStorePC/main.png?v=2')
    I=1/2*m*r**2#interia of disk
    disk.v=vec(0,0,0)
    while disk.pos.y>=0.036 and w>0:#higher than floor and angular frequency greater than zero
        rate(100)#Halts computations until 1.0(frequency/seconds) after the previous call to rate()
        disk.rotate(angle=w*0.01,origin=disk.pos,axis=vec(0,0,1))# rotate counterclockwise
        fs=(m*g*sin(arc))/((m*r**2)/I+1)# calculate the friction
        taw=fs*r#calculate the torque
        w=w-(taw/I)*dt#refresh the angular frequency
        f_net=(m*g*sin(arc))#calculate the net force
        disk.a=vec(cos(arc)*(f_net/m),sin(arc)*(-f_net/m),0)#a=F/m
        disk.v=disk.v+disk.a*dt#v=at
        Kt=(1/2*m*(disk.v.x**2))#calculate the kinetic of translation
        dict['Ktran'].append(Kt)
        Kr=(1/2)*I*((disk.v.x/r)**2)#calculate the kinetic of rotation
        dict['Krot'].append(Kr)
        Ue=m*g*disk.pos.y#calculate the potential energy
        dict['U'].append(Ue)
        Em=(1/2*m*(disk.v.x**2)+(1/2)*I*((disk.v.x/r)**2)+m*g*disk.pos.y)#calculate the kinetic of mechenic
        dict['Emech'].append(Em)
        #plot the graph
        Ktrans.plot(pos=(t,(1/2*m*(disk.v.x**2))))
        Krot.plot(pos=(t, (1/2)*I*((disk.v.x/r)**2)))
        Ugrav.plot(pos=(t,m*g*disk.pos.y))        
        E.plot(pos=(t,((1/2*m*(disk.v.x**2)+(1/2)*I*((disk.v.x/r)**2)+m*g*disk.pos.y))))
        disk.pos=disk.pos+disk.v*dt#x=vt
        dict['time'].append(t)
        msg = label(text="t="+str(round(t,3)),pos=vec(0.4,0.4,0))#label time
        t=t+dt#refresh the time
    while disk.pos.y>=0.036 and w<=0:
        rate(100)#Halts computations until 1.0(frequency/seconds) after the previous call to rate()
        disk.rotate(angle=-w*0.01,origin=disk.pos,axis=vec(0,0,-1))#rotate clockwise
        fs=(m*g*sin(arc))/((m*r**2)/I+1)# calculate the friction
        taw=fs*r#calculate the torque
        w=w-(taw/I)*dt#refresh the angular frequency
        f_net=(m*g*sin(arc))#calculate the net force
        disk.a=vec(cos(arc)*(f_net/m),sin(arc)*(-f_net/m),0)#a=F/m
        disk.v=disk.v+disk.a*dt#v=at
        Kt=(1/2*m*(disk.v.x**2))#calculate the kinetic of translation
        dict['Ktran'].append(Kt)
        Kr=(1/2)*I*((disk.v.x/r)**2)#calculate the kinetic of rotation
        dict['Krot'].append(Kr)
        Ue=m*g*disk.pos.y#calculate the potential energy
        dict['U'].append(Ue)
        Em=(1/2*m*(disk.v.x**2)+(1/2)*I*((disk.v.x/r)**2)+m*g*disk.pos.y)#calculate the kinetic of mechenic
        dict['Emech'].append(Em)
        #plot the graph
        Ktrans.plot(pos=(t,(1/2*m*(disk.v.x**2))))
        Krot.plot(pos=(t, (1/2)*I*((disk.v.x/r)**2)))
        Ugrav.plot(pos=(t,m*g*disk.pos.y))        
        E.plot(pos=(t,((1/2*m*(disk.v.x**2)+(1/2)*I*((disk.v.x/r)**2)+m*g*disk.pos.y))))
        disk.pos=disk.pos+disk.v*dt#x=vt
        dict['time'].append(t)
        msg = label(text="t="+str(round(t,3)),pos=vec(0.4,0.4,0))#label time
        t=t+dt#refresh the time
if choose == 2:
    #creat
    rate(100)#Halts computations until 1.0(frequency/seconds) after the previous call to rate()
    ball = sphere(pos=vec(-translation_length,2*translation_height+r,0),radius=r,length=0.01, axis=vec(0,0,0.1),texture='https://media.istockphoto.com/id/538449165/zh/%E7%85%A7%E7%89%87/beautiful-cloudscape-over-the-sea-sunset-shot.jpg?s=612x612&w=0&k=20&c=fjqKanHhGOw5MEbu3xckBf4PqN2bY6aOTQYrDlDDth4=')
    I=2/5*m*r**2#interia of ball
    ball.v=vec(0,0,0)
    while ball.pos.y>=0.036 and w>0:
        rate(100)#Halts computations until 1.0(frequency/seconds) after the previous call to rate()
        ball.rotate(angle=w*0.01,origin=ball.pos,axis=vec(0,0,1))# rotate counterclockwise
        fs=(m*g*sin(arc))/((m*r**2)/I+1)# calculate the friction
        taw=fs*r#calculate the torque
        w=w-(taw/I)*dt#refresh the angular frequency
        f_net=(m*g*sin(arc))#calculate the net force
        ball.a=vec(cos(arc)*(f_net/m),sin(arc)*(-f_net/m),0)#a=F/m
        ball.v=ball.v+ball.a*dt#v=at
        Kt=(1/2*m*(ball.v.x**2))#calculate the kinetic of translation
        dict['Ktran'].append(Kt)
        Kr=(1/2)*I*((ball.v.x/r)**2)#calculate the kinetic of rotation
        dict['Krot'].append(Kr)
        Ue=m*g*ball.pos.y#calculate the potential energy
        dict['U'].append(Ue)
        Em=(1/2*m*(ball.v.x**2)+(1/2)*I*((ball.v.x/r)**2)+m*g*ball.pos.y)#calculate the kinetic of mechenic
        dict['Emech'].append(Em)
        #plot the graph
        Ktrans.plot(pos=(t,(1/2*m*(ball.v.x**2))))
        Krot.plot(pos=(t, (1/2)*I*((ball.v.x/r)**2)))
        E.plot(pos=(t,(1/2*m*(ball.v.x**2)+(1/2)*I*((ball.v.x/r)**2)+m*g*ball.pos.y)))        
        ball.pos=ball.pos+ball.v*dt#x=vt
        Ugrav.plot(pos=(t,m*g*ball.pos.y ))
        dict['time'].append(t)
        msg = label(text="t="+str(round(t,3)),pos=vec(0.4,0.4,0))#label time
        t=t+dt#refresh the time
    while ball.pos.y>=0.036 and w<=0:
        rate(100)#Halts computations until 1.0(frequency/seconds) after the previous call to rate()
        ball.rotate(angle=-w*0.01,origin=ball.pos,axis=vec(0,0,-1))#rotate clockwise
        fs=(m*g*sin(arc))/((m*r**2)/I+1)# calculate the friction
        taw=fs*r#calculate the torque
        w=w-(taw/I)*dt#refresh the angular frequency
        f_net=(m*g*sin(arc))#calculate the net force
        ball.a=vec(cos(arc)*(f_net/m),sin(arc)*(-f_net/m),0)#a=F/m
        ball.v=ball.v+ball.a*dt#v=at
        Kt=(1/2*m*(ball.v.x**2))#calculate the kinetic of translation
        dict['Ktran'].append(Kt)
        Kr=(1/2)*I*((ball.v.x/r)**2)#calculate the kinetic of rotation
        dict['Krot'].append(Kr)
        Ue=m*g*ball.pos.y#calculate the potential energy
        dict['U'].append(Ue)
        #plot the graph
        Em=(1/2*m*(ball.v.x**2)+(1/2)*I*((ball.v.x/r)**2)+m*g*ball.pos.y)#calculate the kinetic of mechenic
        dict['Emech'].append(Em)
        Ktrans.plot(pos=(t,(1/2*m*(ball.v.x**2))))
        Krot.plot(pos=(t, (1/2)*I*((ball.v.x/r)**2)))
        Ugrav.plot(pos=(t,m*g*ball.pos.y))        
        E.plot(pos=(t,((1/2*m*(ball.v.x**2)+(1/2)*I*((ball.v.x/r)**2)+m*g*ball.pos.y))))
        ball.pos=ball.pos+ball.v*dt#x=vt
        dict['time'].append(t)
        msg = label(text="t="+str(round(t,3)),pos=vec(0.4,0.4,0))#label time
        t=t+dt#refresh the time
if choose == 3:
    #creat
    rate(100)#Halts computations until 1.0(frequency/seconds) after the previous call to rate()
    hoop = ring(pos=vec(-translation_length,2*translation_height+r,0),thickness=0.01,radius=r,length=0.01, axis=vec(0,0,0.1),texture='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbE8XtHD9NOSIZEanQeecsjKoDSvFEDZwEfserq74QSQ&s')
    I=1*m*r**2#interia of hoop
    hoop.v=vec(0,0,0)
    while hoop.pos.y>=0.036 and w>0:
        rate(100)#Halts computations until 1.0(frequency/seconds) after the previous call to rate()
        hoop.rotate(angle=w*0.01,origin=hoop.pos,axis=vec(0,0,1))# rotate counterclockwise
        fs=(m*g*sin(arc))/((m*r**2)/I+1)# calculate the friction
        taw=fs*r#calculate the torque
        w=w-(taw/I)*dt#refresh the angular frequency
        f_net=(m*g*sin(arc))#calculate the net force
        hoop.a=vec(cos(arc)*(f_net/m),sin(arc)*(-f_net/m),0)#a=F/m
        hoop.v=hoop.v+hoop.a*dt#v=at
        Kt=(1/2*m*(hoop.v.x**2))#calculate the kinetic of translation
        dict['Ktran'].append(Kt)
        Kr=(1/2)*I*((hoop.v.x/r)**2)#calculate the kinetic of rotation
        dict['Krot'].append(Kr)
        Ue=m*g*hoop.pos.y#calculate the potential energy
        dict['U'].append(Ue)
        Em=(1/2*m*(hoop.v.x**2)+(1/2)*I*((hoop.v.x/r)**2)+m*g*hoop.pos.y)
        dict['Emech'].append(Em)
        #plot the graph
        Ktrans.plot(pos=(t,(1/2*m*(hoop.v.x**2))))
        Krot.plot(pos=(t, (1/2)*I*((hoop.v.x/r)**2)))
        E.plot(pos=(t,(1/2*m*(hoop.v.x**2)+(1/2)*I*((hoop.v.x/r)**2)+m*g*hoop.pos.y))) #calculate the kinetic of mechenic      
        hoop.pos=hoop.pos+hoop.v*dt#x=vt
        Ugrav.plot(pos=(t,m*g*hoop.pos.y ))
        dict['time'].append(t)
        msg = label(text="t="+str(round(t,3)),pos=vec(0.4,0.4,0))#label time
        t=t+dt#refresh the time
    while hoop.pos.y>=0.036 and w<=0:
        rate(100)#Halts computations until 1.0(frequency/seconds) after the previous call to rate()
        hoop.rotate(angle=-w*0.01,origin=hoop.pos,axis=vec(0,0,-1))#rotate clockwise
        fs=(m*g*sin(arc))/((m*r**2)/I+1)# calculate the friction
        taw=fs*r#calculate the torque
        w=w-(taw/I)*dt#refresh the angular frequency
        f_net=(m*g*sin(arc))#calculate the net force
        hoop.a=vec(cos(arc)*(f_net/m),sin(arc)*(-f_net/m),0)#a=F/m
        hoop.v=hoop.v+hoop.a*dt#v=at
        Kt=(1/2*m*(hoop.v.x**2))#calculate the kinetic of translation
        dict['Ktran'].append(Kt)
        Kr=(1/2)*I*((hoop.v.x/r)**2)#calculate the kinetic of rotation
        dict['Krot'].append(Kr)
        Ue=m*g*hoop.pos.y#calculate the potential energy
        dict['U'].append(Ue)
        Em=(1/2*m*(hoop.v.x**2)+(1/2)*I*((hoop.v.x/r)**2)+m*g*hoop.pos.y)
        dict['Emech'].append(Em)
        #plot the graph
        Ktrans.plot(pos=(t,(1/2*m*(hoop.v.x**2))))
        Krot.plot(pos=(t, (1/2)*I*((hoop.v.x/r)**2)))
        Ugrav.plot(pos=(t,m*g*hoop.pos.y))       
        E.plot(pos=(t,((1/2*m*(hoop.v.x**2)+(1/2)*I*((hoop.v.x/r)**2)+m*g*hoop.pos.y))))
        hoop.pos=hoop.pos+hoop.v*dt#x=vt
        dict['time'].append(t)
        msg = label(text="t="+str(round(t,3)),pos=vec(0.4,0.4,0))#label time
        t=t+dt#refresh the time
else:
    print('wrong')


# In[2]:

#process the data
import pandas as pd


# In[3]:


import matplotlib.pyplot as plt
import numpy as np


# In[4]:


Krot=list(map(float, dict['Krot']))
Ktran=list(map(float,dict['Ktran']))
U=list(map(float,dict['U']))
Emech=list(map(float,dict['Emech']))
time=list(map(float,dict['time']))


# In[5]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.Series(Krot)


# In[6]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.Series(Ktran)


# In[7]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.Series(U)


# In[8]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.Series(Emech)


# In[9]:


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.Series(time)


# In[10]:

#plot the graph
plt.plot(time,Krot,color='blue',label='Krot-time')
plt.plot(time,Ktran,color='orange',label='Ktran-time')
plt.plot(time,U,color='green',label='U-time')
plt.title('Energy-time',loc='center')
plt.xlabel('time(s)',{'fontsize':12,'color':'black'})
plt.ylabel('Energy(J)',{'fontsize':12,'color':'black'})
plt.legend()


# In[11]:


plt.plot(time,Emech,color='purple')
plt.title('Emech-time')
plt.xlabel('time(s)')
plt.ylabel('Emech(J)')

