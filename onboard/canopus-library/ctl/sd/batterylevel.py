from time import sleep
from ina219 import INA219

class CanBatLev():
  def __init__(self,address = 0x40):
    self.address = address
    try:
      self.ina = INA219(shunt_ohms=0.1, #maybe ina
                        max_expected_amps = 0.6,
                        address=self.address)
      self.ina.configure(voltage_range=self.ina.RANGE_16V,
                         gain=self.ina.GAIN_AUTO,
                         bus_adc=self.ina.ADC_128SAMP,
                         shunt_adc=self.ina.ADC_128SAMP)
    except:
      self.ina = None
  def battery_level_voltage(self):
    try:
      voltage = self.ina.voltage()
      return "{:.2f}".format((voltage-9.6) / 3 * 100), voltage
    except:
      return None, None
