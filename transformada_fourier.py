
import numpy as np
import matplotlib.pyplot as plt

Fs=1000
T=1
t=np.linspace(0,T,Fs,endpoint=False)

# Señales
f=10
seno=np.sin(2*np.pi*f*t)
pulso=np.where((t>=0.3)&(t<=0.6),1,0)
escalon=np.where(t>=0.5,1,0)

def analizar(senal,nombre):
    fft=np.fft.fft(senal)
    frec=np.fft.fftfreq(len(senal),1/Fs)
    mag=np.abs(fft)
    fase=np.angle(fft)

    plt.figure(figsize=(8,3))
    plt.plot(t,senal)
    plt.title(f"{nombre} - Dominio del tiempo")
    plt.xlabel("Tiempo (s)")
    plt.grid()

    plt.figure(figsize=(8,3))
    plt.plot(frec[:len(frec)//2],mag[:len(mag)//2])
    plt.title(f"{nombre} - Magnitud FFT")
    plt.xlabel("Frecuencia (Hz)")
    plt.grid()

    plt.figure(figsize=(8,3))
    plt.plot(frec[:len(frec)//2],fase[:len(fase)//2])
    plt.title(f"{nombre} - Fase FFT")
    plt.xlabel("Frecuencia (Hz)")
    plt.grid()

analizar(seno,"Señal senoidal")
analizar(pulso,"Pulso rectangular")
analizar(escalon,"Función escalón")

# Linealidad
suma=seno+pulso
fft_suma=np.fft.fft(suma)
fft_ind=np.fft.fft(seno)+np.fft.fft(pulso)
print("Linealidad:",np.allclose(fft_suma,fft_ind))

# Desplazamiento temporal
desplazada=np.roll(seno,100)
plt.figure(figsize=(8,3))
plt.plot(t,seno,label="Original")
plt.plot(t,desplazada,label="Desplazada")
plt.legend()
plt.title("Desplazamiento temporal")
plt.grid()

# Escalamiento en frecuencia
seno20=np.sin(2*np.pi*20*t)
fft20=np.fft.fft(seno20)
frec=np.fft.fftfreq(len(seno20),1/Fs)
plt.figure(figsize=(8,3))
plt.plot(frec[:len(frec)//2],np.abs(fft20)[:len(frec)//2])
plt.title("Escalamiento en frecuencia (20 Hz)")
plt.grid()

plt.show()
