import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd     
from numpy.fft import fft    

T=2.5
fm = 8000
fx=440
A=4
pi=np.pi
L=int(fm*T)
Tm=1/fm
t=Tm*np.arange(L)
x=A*np.cos(2*pi*fx*t)
sf.write('so_ex3.wav',x,fm)

Tx=1/fx                                   
Ls=int(fm*5*Tx)                           

plt.figure(0)                             
plt.plot(t[0:Ls], x[0:Ls])                
plt.xlabel('t en segons')                 
plt.title('5 periodes de la sinusoide')   
plt.show()                                