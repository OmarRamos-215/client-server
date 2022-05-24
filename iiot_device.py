from random import randint
import psutil
import wmi

#POO en Python
#Definición de la clase
class Sensor:

    # Constructor de la clase
    def __init__(self):
        # Funciona para Linux y unas cosas para Windows
        self._sensor= psutil.cpu_count()
        # Funciona para Windows 'talvez'. No funcionó
        #self._wmi= wmi.WMI(namespace='root\OpenHardwareMonitor')

    def get_temp(self):
        return self._sensor

    # Simular 'la toma de algún valor de otro sensor'
    def get_random_number(self):
        return randint(0,99)

    #Para Windows. No funciona (:
    def get_temp_for_windows(self):
        return self._wmi.SensorType['Temperature']

    # Simular 'la toma de un sensor de inclinación'
    def get_random_inclination(self):
        rand= randint(0, 90)
        if rand > 15:
            print(f"Advertencia, inclinación de {rand}°".center(50,'-'))