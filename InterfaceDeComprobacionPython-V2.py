# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InterfaceDeComprobacion.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!
import os
from PyQt5 import QtCore, QtGui, QtWidgets
def validacionPing():
    ArduinoGas="8.8.8.8" #ARDUINO DEL GAS
    ArduinoIluminacion = "192.168.1.20" #Arduino de iluminacion
    ArduinoPuertas = "192.168.1.30" #Arduino Puertas
    ArduinoAlarma="192.168.1.40" # Arduino de alerta Medica
    GasPing = os.system("ping -n 1 " + ArduinoGas)
    IluminacionPing = os.system("ping -n 1 " + ArduinoIluminacion)
    PuertasPing = os.system("ping -n 1 " + ArduinoPuertas)
    AlarmasPing = os.system("ping -n 1 " + ArduinoAlarma)
    print("VALIDANDO")
    #INCIO DE PRUEBAS
    if GasPing == 0:
        print( 'Funciona GAS')
        #self.Gasbox.setStyleSheet("background-color: rgb(0, 255, 0);")
    else:
        print('GAS no funciona')
    
    if IluminacionPing == 0:
        print( 'Funciona ILUMINACION')
        #self.IluminacionBox.setStyleSheet("background-color: rgb(0, 255, 0);")
    else:
        print('ILUMINACION no funciona')
    
    if PuertasPing == 0:
        print( 'Funciona PUERTAS')
        #self.PuertasBox.setStyleSheet("background-color: rgb(0, 255, 0);")
    else:
        print('PUERTAS no funciona')

    if AlarmasPing == 0:
        print( 'Funciona ALARMAS')
        #self.AlertaBox.setStyleSheet("background-color: rgb(0, 255, 0);")
    else:
        print('ALARMAS no funciona')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 795)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Validador = QtWidgets.QPushButton(self.centralwidget)
        self.Validador.setGeometry(QtCore.QRect(360, 540, 291, 101))
        self.Validador.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.Validador.setObjectName("Validador")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 170, 181, 61))
        self.label.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.Gasbox = QtWidgets.QFrame(self.centralwidget)
        self.Gasbox.setGeometry(QtCore.QRect(50, 230, 181, 191))
        self.Gasbox.setAutoFillBackground(False)
        self.Gasbox.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Gasbox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Gasbox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Gasbox.setObjectName("Gasbox")
        self.IluminacionBox = QtWidgets.QFrame(self.centralwidget)
        self.IluminacionBox.setGeometry(QtCore.QRect(300, 230, 181, 191))
        self.IluminacionBox.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.IluminacionBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.IluminacionBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.IluminacionBox.setObjectName("IluminacionBox")
        self.PuertasBox = QtWidgets.QFrame(self.centralwidget)
        self.PuertasBox.setGeometry(QtCore.QRect(560, 230, 181, 191))
        self.PuertasBox.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.PuertasBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PuertasBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PuertasBox.setObjectName("PuertasBox")
        self.AlertaBox = QtWidgets.QFrame(self.centralwidget)
        self.AlertaBox.setGeometry(QtCore.QRect(810, 230, 181, 191))
        self.AlertaBox.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.AlertaBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AlertaBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AlertaBox.setObjectName("AlertaBox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 170, 241, 61))
        self.label_2.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(550, 170, 211, 61))
        self.label_4.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(830, 130, 181, 61))
        self.label_3.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(860, 170, 181, 61))
        self.label_5.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 10, 701, 91))
        self.label_6.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 26))
        self.menubar.setObjectName("menubar")
        self.menudsasda = QtWidgets.QMenu(self.menubar)
        self.menudsasda.setObjectName("menudsasda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionVerificacion = QtWidgets.QAction(MainWindow)
        self.actionVerificacion.setObjectName("actionVerificacion")
        self.menudsasda.addAction(self.actionVerificacion)
        self.menubar.addAction(self.menudsasda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VerificacionEstado"))
        self.Validador.setText(_translate("MainWindow", "Validar"))
        self.label.setText(_translate("MainWindow", "Sensores de Gas"))
        self.label_2.setText(_translate("MainWindow", "Sensores de Iluminacion"))
        self.label_4.setText(_translate("MainWindow", "Sensores de Puertas"))
        self.label_3.setText(_translate("MainWindow", "Sistema Alerta "))
        self.label_5.setText(_translate("MainWindow", "Medica"))
        self.label_6.setText(_translate("MainWindow", "ESTADO DE LOS SISTEMAS DOMOTICOS DEL HOGAR 25 DE MAYO-SUCRE"))
        self.menudsasda.setTitle(_translate("MainWindow", "Verificacion"))
        self.actionVerificacion.setText(_translate("MainWindow", "Verificacion"))
        self.Validador.clicked.connect(validacionPing)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
