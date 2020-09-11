from time import sleep
from ina219 import INA219

ina = INA219(shunt_ohms=0.1,
             max_expected_amps = 0.6,
             address=0x40)

ina.configure(voltage_range=ina.RANGE_16V,
              gain=ina.GAIN_AUTO,
              bus_adc=ina.ADC_128SAMP,
              shunt_adc=ina.ADC_128SAMP)

try:
    while 1:
        v = ina.voltage()
        #i = ina.current()
        #p = ina.power()
        print("Voltage =",v)
	#Battery Level with 20% rule (3.2V min)
        level = (v-9.6) / 3 * 100
        print("Level {:.2f}".format(level),"%\n")
        sleep(1)
except KeyboardInterrupt:
    print ("\nCtrl-C pressed.  Program exiting...")
