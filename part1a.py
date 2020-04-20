import numpy as np
import matplotlib.pyplot as plt
#part(a)
g=9.8
y1=0.0
dt=0.01
vel_0 = 100.0
angle_theta=30*np.pi/180.0
t_max=2*vel_0*np.sin(angle_theta)/g
t_steps = int(t_max/dt)
t=np.arange(y1,t_max+dt,dt)
pos_x=np.zeros(t_steps+1)
pos_y=np.zeros(t_steps+1)
vel_x=np.zeros(t_steps+1)
vel_y=np.zeros(t_steps+1)
pos_y[0]=y1
vel_x[:]=vel_0*np.cos(angle_theta)
vel_y[0]=vel_0*np.sin(angle_theta)
for i in range (t_steps):
    pos_x[i+1]=pos_x[i]+dt*vel_x[i]
    vel_y[i+1]=vel_y[i]-dt*g
    pos_y[i+1]=pos_y[i]+dt*vel_y[i]
max_x=max(pos_x)
max_y=max(pos_y)
print('Maximum height: '+str(round(max_y,2))+' metres')
print('Maximum distance traveled:'+str(round(max_x,2))+'metres')
print('Total time taken: '+str(round(t_max,2))+'sec')

plt.plot(pos_x,pos_y)
plt.ylabel('y-position (meters)')
plt.xlabel('x-position (meters)')
plt.title('Projectile trajectory')
plt.grid()
plt.savefig('3ab.png')
plt.show()

#part 3c
g=9.8                # gravitational force
y1=0.0               # initial height
dt=[0.001,0.005,0.01,0.05,0.1,0.5]
vel_0= 100.0                      # initial Velocity at which projectile is launched
mass_p = 1.0                      # mass of projectile
angle_theta=30*np.pi/180.0        # angle in radians
t_max=2*vel_0*np.sin(angle_theta)/g           # flight time
t_steps = np.zeros(len(dt))                    # steps
np.divide(t_max,dt,t_steps)
t_steps=t_steps.astype(int)
t=np.zeros((max(t_steps)+1,len(dt)))
pos_x=np.zeros((max(t_steps)+1,len(dt)))         # x-axis
pos_y=np.zeros((max(t_steps)+1,len(dt)))          # y-axis position
vel_x=np.zeros((max(t_steps)+1,len(dt)))         # velocity at position x
vel_y=np.zeros((max(t_steps)+1,len(dt)))         # velocity of y
energy1= np.zeros((max(t_steps)+1,len(dt)))        # total projectile energy, PE + KE
pos_y[0,:]=y1
vel_x[:,:]=vel_0*np.cos(angle_theta)
vel_y[0,:]=vel_0*np.sin(angle_theta)
energy1[0,:]=0.5*mass_p *(vel_x[0,:]**2 + vel_y[0,:]**2)+mass_p *g*pos_y[0,:]

for j in range(len(dt)):
    for i in range(t_steps[j]):
        pos_x[i+1,j]=pos_x[i,j]+dt[j]*vel_x[i,j]
vel_y[i+1,j]=vel_y[i,j]-dt[j]*g
pos_y[i+1,j]=pos_y[i,j]+ dt[j]*vel_y[i,j]
energy1[i+1,j]=0.5*mass_p *(vel_x[i+1,j]**2 + vel_y[i+1,j]**2) + g*mass_p *pos_y[i+1,j]
t[i+1,j]=t[i,j]+dt[j]

plt.plot(t[0:t_steps[0],0],energy1[0:t_steps[0],0],label='dt=0.001')
plt.plot(t[0:t_steps[1],1],energy1[0:t_steps[1],1],label='dt=0.005')
plt.plot(t[0:t_steps[2],2],energy1[0:t_steps[2],2],label='dt=0.01')
plt.plot(t[0:t_steps[3],3],energy1[0:t_steps[3],3],label='dt=0.05')
plt.plot(t[0:t_steps[4],4],energy1[0:t_steps[4],4],label='dt=0.1')
plt.plot(t[0:t_steps[5],5],energy1[0:t_steps[5],5],label='dt=0.5')
plt.ylabel('Total Energy')
plt.xlabel('Time (Seconds)')
plt.title('Projectile Total Energy')
plt.legend()
plt.savefig('3c.png')
plt.show()