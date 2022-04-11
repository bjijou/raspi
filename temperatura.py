# Sensor de temperature ref: 3c01f0953f5c
# Ejecutar solo con Python3

from w1thermsensor import W1ThermSensor, Sensor

def Temperatura():
    sensor = W1ThermSensor(Sensor.DS18B20, "3c01f0953f5c")
    temperature_in_celsius = sensor.get_temperature()
    #print("Temperature %.2f" % (temperature_in_celsius))  
    return (temperature_in_celsius)

''' Busca todos los sensores coenctados
for sensor in W1ThermSensor.get_available_sensors():
    print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))
'''



