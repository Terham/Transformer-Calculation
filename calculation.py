import math
import numpy as np

values = ["0", "0", "0", "0", "0"]

Sn = float
U1 = float
ek = float
Pcu = float
U2 = float

class Transformer():
    def __init__(self, Sn, U1, ek, Pcu, U2):
        self.Sn = Sn
        self.U1 = U1
        self.ek = ek
        self.Pcu = Pcu
        self.U2 = U2
             
    def resitance_primary(self):
        R_primary = Pcu / (3 * data.current_primary()**2)
        return R_primary

    def reactance_primary(self):
        XL_primary = math.sqrt(data.impedance_primary()**2 - data.resitance_primary()**2)
        return XL_primary

    def impedance_primary(self):
        Z_primary = (U1**2 * ek) / (Sn * 100)
        return Z_primary

    def current_primary(self):
        I1 = Sn / (U1 * math.sqrt(3))
        return I1

    def resitance_secondary(self):
        R_secondary = Pcu / (3 * data.current_secondary()**2)
        return R_secondary

    def reactance_secondary(self):
        XL_secondary = math.sqrt(data.impedance_secondary()**2 - data.resitance_secondary()**2)
        return XL_secondary

    def impedance_secondary(self):
        Z_secondary = (U2**2 * ek) / (Sn * 100)
        return Z_secondary

    def current_secondary(self):
        I2 = Sn / (U2 * math.sqrt(3))
        return I2

    def phase_angle(self):
        phase_angle = math.degrees(math.atan(1 / (data.resitance_primary() / data.reactance_primary())))
        return phase_angle

data = Transformer(values[0], values[1], values[2], values[3], values[4])

def print_calculation():
    
    current_primary_result = "Ip current: %s A" % data.current_primary()
    print(current_primary_result)
    current_secondary_result = "Is current: %s A" % data.current_secondary()
    print(current_secondary_result)
    resistance_primary_result = "Rp: %s Ω" % data.resitance_primary()
    print(resistance_primary_result)
    resistance_secondary_result = "Rs: %s Ω" % data.resitance_secondary()
    print(resistance_secondary_result)
    reactance_primary_result = "XLp: %s Ω" % data.reactance_primary()
    print(reactance_primary_result)
    reactance_secondary_result = "XLs: %s Ω" % data.reactance_secondary()
    print(reactance_secondary_result)
    impadance_primary_result = "Zs: %s Ω" % data.impedance_primary()
    print(impadance_primary_result)
    impadance_secondary_result = "Zs: %s Ω" % data.impedance_secondary()
    print(impadance_secondary_result)
    phase_angle_result = "Φ: %s" % data.phase_angle()
    print(phase_angle_result)

    return current_primary_result, current_secondary_result, resistance_primary_result, resistance_secondary_result, reactance_primary_result, reactance_secondary_result, impadance_primary_result, impadance_secondary_result, phase_angle_result