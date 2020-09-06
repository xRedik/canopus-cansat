from time import sleep
from ina219 import INA219

class CanBatLev():
  def __init__(self,address = 0x40):
    self.address = address
    self.ina = INA219(shunt_ohms=0.1, #maybe ina
                 max_expected_amps = 0.6,
                 address=self.address)
    self.ina.configure(voltage_range=ina.RANGE_16V,
                  gain=ina.GAIN_AUTO,
                  bus_adc=ina.ADC_128SAMP,
                  shunt_adc=ina.ADC_128SAMP)
  def battery_level_voltage():
    return "{:.2f}".format((v-9.6) / 3 * 100), self.ina.voltage()
