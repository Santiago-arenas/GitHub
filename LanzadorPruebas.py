import sys
import Adafruit_BBIO.GPIO as GPIO
import time
from Pruebas import *

class Pruebas(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.btnGPIO, QtCore.SIGNAL('clicked()'), self.digitalOut)

    def digitalOut(self):
        ports = ["P8_7", "P8_8", "P8_9", "P8_10", "P8_11", "P8_12", "P8_14", "P8_15", "P8_16", "P8_17", "P8_18"]
        self.ui.lblProceso.clear()
        for x in ports:
            self.ui.lblProceso.setText(x)
            GPIO.setup(x, GPIO.OUT)
            GPIO.output(x, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(x, GPIO.LOW)
            self.ui.lblProceso.repaint()

if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        myapp = Pruebas()
        myapp.show()
        sys.exit(app.exec_())