import time
import board
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219

i2c_bus = board.I2C()

ina219 = INA219(12c_bus)

ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
ina219.bus_voltage_range = BusVoltageRange.RANGE_16V

class BatLev:
  def __init__(self):
    i2c_bus=board.I2C()
    self.ina219 = INA219(i2c_bus)
    self.ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
    self.ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
    self.ina219.bus_voltage_range = BusVoltageRange.RANGE_16V
    self.voltage = 0
    self.current = 0
    self.sh_voltage = 0
  def read_voltage(self):
    self.voltage = self.ina219.bus_voltage
    self.current = self.ina219.current / 1000
    self.sh_voltage = self.ina219.shunt_voltage
    return self.voltage,"{:.2f}".format((self.voltage-9.6) / 3 * 100)
