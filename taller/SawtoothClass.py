import math
import matplotlib.pylab as plt
import numpy as np

class Sawtooth:

        def __init__(self, frecuencia, sampling, bits, time):
            self.SamplingRate = sampling
            self.NumeroBit = bits
            self.Seconds = time
            self.Frecuencia = frecuencia
            self.tamano = int(sampling * time)


        def generar(self):

            wavearray = []
            for i in range(0, self.tamano):
                    A = 0.5-(1 / math.pi)
                    datos = 0
                    for j in range (1, 100):

                        value = (1/float(j))*math.sin((j*math.pi*self.Frecuencia*i)/self.SamplingRate)
                        datos += value
                    frame = datos * A
                    wavearray.append(frame)
            FinalData = np.asarray(wavearray)

            return FinalData


        def leveladjust(self, datos, bits, level):
            peaklevel = max(abs(datos))
            valueLevel = (10**(level/20))*((2**16)/2.0)
            valueAdjust = valueLevel / float(peaklevel)
            datosAjustados = datos * valueAdjust
            return datosAjustados



        def graficar(self, array):
                plt.plot(array, color="green", linewidth=1.0, linestyle="-")
                plt.show()