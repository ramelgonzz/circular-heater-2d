#Heat propagation example of a circular shaped heater on a square plate
#v1
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

dx=0.1
dt=0.1
L=50
W=50

#circle heater
r=10 #radius of heater
def circle_heater(r):
    d=2*r+2
    rx,ry=d/2,d/2
    x,y=np.indices((d,d))
    return (np.abs(np.hypot(rx-x,ry-y)-r)<0.5).astype(int)
gr=4000*circle_heater(r)

def assert_heater(M, gr):
    M[14:36,14:36] = np.where(gr > 0, gr, M[14:36,14:36])

M=np.zeros([L,W])   #matrix LenghtxWidth
assert_heater(M, gr)

T=np.arange(0,10,dt)
MM=[] #matrices per dt step
for i in range(len(T)):
    for j in range(1,L-1):
        for i in range(1,W-1):
            k=2.0
            if 24<j<28:
                if 29<i<32 or 23<i<20: k=0
            M[i,j] = (M[i-1,j] + M[i+1,j] + M[i,j-1] + M[i,j+1])/4

    assert_heater(M, gr)

    MM.append(M.copy())

fig = plt.figure()
pcm = plt.pcolormesh(MM[0])
plt.colorbar()

#update animation
def step(i):
    if i >= len(MM): return
    pcm.set_array(MM[i].ravel())
    plt.draw()

anim = FuncAnimation(fig, step, interval=1)
plt.show()
