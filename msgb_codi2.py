import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft     


x_r,fm=sf.read('so_exemple2.wav') # Agafem el so creat en el cas 1 del ex1
#Importem la info del 'so_exemple2.wav'
Tm =1/fm
t=Tm*np.arange(len(x_r))
sf.write('so_ex2.wav',x_r,fm) #Creem un nou so per l'ex2

fx=4000
Tx=1/fx                                   # Període del senyal
Ls=int(fm*5*Tx)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(21)                             
plt.plot(t[0:Ls], x_r[0:Ls])                
plt.xlabel('t en segons')              
plt.title('5 periodes de la sinusoide, Ex 2')   
plt.show()    

#Per poder fer la transformada:
N=5000
XR =fft(x_r[0:Ls],N)
k=np.arange(N)                        

plt.figure(1)                         
plt.subplot(211)                      
plt.plot(k,abs(XR))                    
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   
plt.ylabel('|X[k]|')                  
plt.subplot(212)                      
plt.plot(k,np.unwrap(np.angle(XR)))    
plt.xlabel('Index k')                 
plt.ylabel('$\phi_x[k]$')             
plt.show()                            