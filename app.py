from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap
import sys
import calculation

class Transformer_app(QMainWindow):
    def __init__(self):
        super(Transformer_app, self).__init__()
        self.setGeometry(200, 220, 650, 650)
        self.setWindowTitle("Transformer data!")
        self.initUI()

    def initUI(self):
        self.transformer_picture = QtWidgets.QLabel(self)
        self.transformer_picture.setGeometry(0,0,641,474)
        picture = QPixmap("1280px-Transformer3d_col3.svg.png")
        self.transformer_picture.setPixmap(picture)
        self.transformer_picture.move(5, 20)

        self.label_Ip = QtWidgets.QLabel(self)
        self.label_Ip.setText("Ip curren: ")
        self.label_Ip.move(25, 495)

        self.label_Is = QtWidgets.QLabel(self)
        self.label_Is.setText("Is curren: ")
        self.label_Is.move(25, 520)

        self.label_resistance_primary = QtWidgets.QLabel(self)
        self.label_resistance_primary.setText("Rp: ")
        self.label_resistance_primary.move(150, 495)

        self.label_resistance_secondary = QtWidgets.QLabel(self)
        self.label_resistance_secondary.setText("Rs: ")
        self.label_resistance_secondary.move(150, 520)

        self.label_reactance_primary = QtWidgets.QLabel(self)
        self.label_reactance_primary.setText("XLp: ")
        self.label_reactance_primary.move(275, 495)

        self.label_reactance_secondary = QtWidgets.QLabel(self)
        self.label_reactance_secondary.setText("XLs: ")
        self.label_reactance_secondary.move(275, 520)

        self.label_impedance_primary = QtWidgets.QLabel(self)
        self.label_impedance_primary.setText("Zp: ")
        self.label_impedance_primary.move(400, 495)

        self.label_impedance_secondary = QtWidgets.QLabel(self)
        self.label_impedance_secondary.setText("Zs: ")
        self.label_impedance_secondary.move(400, 520)

        self.label_phase_angle = QtWidgets.QLabel(self)
        self.label_phase_angle.setText("Φ: ")
        self.label_phase_angle.move(525, 495)

        self.linetext_SN = QtWidgets.QLineEdit(self)
        self.linetext_SN.setText("Sn kVA")
        self.linetext_SN.move(25, 550)

        self.linetext_U1 = QtWidgets.QLineEdit(self)
        self.linetext_U1.setText("Up kV")
        self.linetext_U1.move(150, 550)

        self.linetext_ek = QtWidgets.QLineEdit(self)
        self.linetext_ek.setText("Enter Value %")
        self.linetext_ek.move(275, 550)

        self.linetext_Pcu = QtWidgets.QLineEdit(self)
        self.linetext_Pcu.setText("Pcu kW")
        self.linetext_Pcu.move(400, 550)

        self.linetext_U2 = QtWidgets.QLineEdit(self)
        self.linetext_U2.setText("Us V")
        self.linetext_U2.move(525, 550)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Calculate")
        self.b1.move(275, 600)
        self.b1.clicked.connect(self.clicked)

    def clicked(self):       
        Sn = self.linetext_SN.text()
        Sn_user_input = float(Sn)
        a = Sn_user_input * 10**3

        U1 = self.linetext_U1.text()
        U1_user_input = float(U1)
        b = U1_user_input * 10**3

        ek = self.linetext_ek.text()
        ek_user_input = float(ek)
        c = ek_user_input

        Pcu = self.linetext_Pcu.text()
        Pcu_user_input = float(Pcu)
        d = Pcu_user_input * 10**3

        U2 = self.linetext_U2.text()
        U2_user_input = float(U2)
        e = U2_user_input

        calculation.values[0] = a
        calculation.values[1] = b
        calculation.values[2] = c
        calculation.values[3] = d
        calculation.values[4] = e
        calculation.Sn = a
        calculation.U1 = b
        calculation.ek = c
        calculation.Pcu = d
        calculation.U2 = e 
        calculation.Transformer(calculation.values[0],calculation.values[1],calculation.values[2],calculation.values[3],calculation.values[4])
        Gui_values = calculation.print_calculation()

        self.label_Ip.setText(str(Gui_values[0]))
        self.label_Is.setText(str(Gui_values[1]))
        self.label_resistance_primary.setText(str(Gui_values[2]))
        self.label_resistance_secondary.setText(str(Gui_values[3]))
        self.label_reactance_primary.setText(str(Gui_values[4]))
        self.label_reactance_secondary.setText(str(Gui_values[5]))
        self.label_impedance_primary.setText(str(Gui_values[6]))
        self.label_impedance_secondary.setText(str(Gui_values[7]))
        self.label_phase_angle.setText(str(Gui_values[8]))


def window():
    app = QApplication(sys.argv)
    win = Transformer_app()
    win.show()
    sys.exit(app.exec_())

window()