import machine
import utime

# ADC on channel 4 is connected to the internal temperature sensor
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

def get_temperature():
    # Read raw ADC value
    reading = sensor_temp.read_u16() * conversion_factor
    
    # Convert the ADC reading to a temperature
    temperature = 27 - (reading - 0.706) / 0.001721
    return temperature
