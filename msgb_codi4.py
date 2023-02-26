import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd     
from numpy.fft import fft 

x_r,fm=sf.read('luzbel44.wav') 
T= 0.025                                                                 
Ls = int(fm * T)                      
Tm=1/fm                              
t=Tm*np.arange(Ls)                    
sf.write('so_exercici4.wav', x_r, fm)   
                                 
plt.figure(0)                            
plt.plot(t[0:Ls], x_r[0:Ls])              
plt.xlabel('t en segons')                 
plt.title('Gràfica ex4')   
plt.show() 

N=5000                       
X=fft(x_r[0 : Ls], N)          

k=np.arange(N)                        

sd.play(x_r, fm) 

N=5000                       
X=fft(x_r[0 : Ls], N) 
k=np.arange(N)   
Xdb=20*np.log10(np.abs(X)/max(np.abs(X)))                     
fk = k[0:N//2+1]*fm/N  #Trobem fk per a l'eix d'abscisses de la gràfica
plt.figure(1)                         
plt.subplot(211)                      
plt.plot(fk,Xdb[0:N//2+1])   # Representem el mòul de la Transformada tal i com se'ns demana (0 a fk/2) i en dB                 
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|en dB')                  
plt.subplot(212)                      
plt.plot(fk,np.unwrap(np.angle(X[0:N//2+1])))    
plt.ylabel('$\phi_x[k]$')             
plt.show()                           