from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np
time_points=np.linspace(1,50,500)
t_span=(1,50)
init_condition=[1,2]
def system(t,r):
    x,y=r
    fx=np.cos(x)
    fy=np.sin(y)
    return [fx,fy]
sol=solve_ivp(system,t_span,y0=init_condition,t_eval=time_points)
print(sol)
t=sol.t
#y=sol.y
x=sol.y[0]
y=sol.y[1]
fig,axis=plt.subplots()
axis.set_xlim([0,2])
axis.set_ylim([-2,2])
plt.xlabel("wise")
plt.ylabel("nice")
#plt.legend()
mass,=axis.plot([],[],markersize=30,marker="o",linestyle="-")
spring,=axis.plot([],[],linewidth=3,linestyle="--")
def lap(frames):
    current_x=x[frames]
    print(current_x)
    mass.set_data([current_x],[0])
    spring.set_data([-2,current_x],[0,0])
    return mass,spring

animate=FuncAnimation(fig,lap,frames=len(time_points),interval=25)
plt.show()



