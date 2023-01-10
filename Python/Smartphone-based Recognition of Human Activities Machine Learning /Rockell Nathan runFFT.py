#Maths Libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft, fftfreq
import statistics

#Length of time each recording is
recordingLength = 20
#How many values are captured per second
recordingsPerSecond = 0.25
#Activity Array
activity = ['standing', 'sitting', 'walking', 'jogging', 'running', 'cycling']

def runFFT(x, y, z):
    #Length of array 
    N = len(x)
    #Timeframe
    T = len(x)*recordingsPerSecond
    
    t = np.linspace(0, T, N)
    f = fftfreq(len(t), np.diff(t)[0])
    #Calculates FFT values for each axis
    xfft = fft(x)
    yfft = fft(y)
    zfft = fft(z) 
    # print('fft:', (xfft))
    plt.plot(t, x, label="Accel X")
    plt.plot(t, y, label="Accel Y")
    plt.plot(t, z, label="Accel Z")
    plt.legend(loc="upper right")
    plt.xlabel('t [seconds]')
    plt.ylabel('Accelerometer Value')
    plt.show()
    
    plt.plot(f[:N//2], np.abs(xfft[:N//2]), label ="Accel X FFT")
    plt.legend(loc="upper right")
    # plt.show()
    plt.plot(f[:N//2], np.abs(yfft[:N//2]), label ="Accel Y FFT")
    plt.legend(loc="upper right")
    # plt.show()
    plt.plot(f[:N//2], np.abs(zfft[:N//2]), label ="Accel Z FFT")
    plt.legend(loc="upper right")
    plt.ylabel('Frequency')
    plt.xlabel('')
    # plt.show()
    print(xfft[0])
    print("FFT Values Calculated")
    return xfft[0], yfft[0], zfft[0]