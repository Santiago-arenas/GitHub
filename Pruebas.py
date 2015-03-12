# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PROJECTS/Pruebas.ui'
#
# Created: Thu Mar 12 11:44:38 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(800, 480)
        Dialog.setMaximumSize(QtCore.QSize(800, 480))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(270, 10, 277, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.btnGPIO = QtGui.QPushButton(Dialog)
        self.btnGPIO.setGeometry(QtCore.QRect(40, 160, 181, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnGPIO.setFont(font)
        self.btnGPIO.setObjectName(_fromUtf8("btnGPIO"))
        self.btnADC = QtGui.QPushButton(Dialog)
        self.btnADC.setGeometry(QtCore.QRect(570, 160, 201, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnADC.setFont(font)
        self.btnADC.setObjectName(_fromUtf8("btnADC"))
        self.btnPWM = QtGui.QPushButton(Dialog)
        self.btnPWM.setGeometry(QtCore.QRect(310, 160, 181, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnPWM.setFont(font)
        self.btnPWM.setObjectName(_fromUtf8("btnPWM"))
        self.lblProceso = QtGui.QLabel(Dialog)
        self.lblProceso.setGeometry(QtCore.QRect(300, 360, 191, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Candara"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblProceso.setFont(font)
        self.lblProceso.setAlignment(QtCore.Qt.AlignCenter)
        self.lblProceso.setObjectName(_fromUtf8("lblProceso"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "PRUEBA DE PLANTA", None))
        self.btnGPIO.setText(_translate("Dialog", "SALIDAS DIGITALES", None))
        self.btnADC.setText(_translate("Dialog", "ENTRADAS ANALOGAS", None))
        self.btnPWM.setText(_translate("Dialog", "PWM", None))
        self.lblProceso.setText(_translate("Dialog", "Paso", None))

