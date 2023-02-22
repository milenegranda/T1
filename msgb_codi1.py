import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd     
from numpy.fft import fft     

T=2.5
fm=8000
A=4
pi=np.pi
L=int(fm*T)
Tm=1/fm
t=Tm*np.arange(L)

##Exercici 1
#Prova 1 amb Fx = 4kHz
fx2 = 4000
x2 = A * np.cos(2 * pi * fx2 * t)      
sf.write('so_exemple2.wav', x2, fm)   #Creacio del nou so amb Fx=4kHz

Tx2=1/fx2                                  # Període del senyal amb fx= 4kHz
Ls=int(fm*5*Tx2)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x2[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide amb Fx=4kHz')   # Títol del gràfic
plt.show() 

sd.play(x2, fm)   #Reproducció so 

N=5000                        # Dimensió de la transformada discreta
X2=fft(x2[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(1)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X2))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X2)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics

#Prova 2 amb Fx = 40Hz
fx3 = 40 #Nova freq Fx= 40Hz
x3 = A * np.cos(2 * pi * fx3 * t)      
sf.write('so_exemple3.wav', x3, fm)   #Creació del fitxer wav amb Fx=40Hz

Tx3=1/fx3                                 # Període del senyal
Ls=int(fm*5*Tx3)                           # Nombre de mostres corresponents a 5 períodes de la sinusoide

plt.figure(0)                             # Nova figura
plt.plot(t[0:Ls], x3[0:Ls])                # Representació del senyal en funció del temps
plt.xlabel('t en segons')                 # Etiqueta eix temporal
plt.title('5 periodes de la sinusoide amb Fx=40Hz')   # Títol del gràfic
plt.show() 

sd.play(x3, fm)  #Reproducció del nou so

X3=fft(x2[0 : Ls], N)           # Càlcul de la transformada de 5 períodes de la sinusoide

k=np.arange(N)                        # Vector amb els valors 0≤  k<N

plt.figure(2)                         # Nova figura
plt.subplot(211)                      # Espai per representar el mòdul
plt.plot(k,abs(X3))                    # Representació del mòdul de la transformada
plt.title(f'Transformada del senyal de Ls={Ls} mostres amb DFT de N={N}')   # Etiqueta del títol
plt.ylabel('|X[k]|')                  # Etiqueta de mòdul
plt.subplot(212)                      # Espai per representar la fase
plt.plot(k,np.unwrap(np.angle(X3)))    # Representació de la fase de la transformad, desenroscada
plt.xlabel('Index k')                 # Etiqueta de l'eix d'abscisses 
plt.ylabel('$\phi_x[k]$')             # Etiqueta de la fase en Latex
plt.show()                            # Per mostrar els grafics



