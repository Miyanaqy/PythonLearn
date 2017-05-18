import sys
from PyQt4 import QtCore, QtGui, uic

from_class = uic.loadUiType("CelToFah.ui")[0]

class MyWindowClass(QtGui.QMainWindow, from_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.ctoF.clicked.connect(self.ctoF_clicked)
        self.ftoC.clicked.connect(self.ftoC_clicked)
        self.actionCtoF.triggered.connect(self.ctoF_clicked)
        self.actionFtoC.triggered.connect(self.ftoC_clicked)
        self.actionExit.triggered.connect(self.menuExit)

    def ftoC_clicked(self):
        cel = float(self.celsius.toPlainText())
        fahr = cel*9/5.0+32
        fahr_text = "%.2f" % fahr
        self.fahrenheit.setText(fahr_text)

    def ctoF_clicked(self):
        fahr = float(self.fahrenheit.toPlainText())
        cel = (fahr-32)*5/9.0
        cel_text = "%.2f" % cel
        self.celsius.setText(cel_text)

    def menuExit(self):
        self.close()

app = QtGui.QApplication(sys.argv)
myClass = MyWindowClass()
myClass.show()
app.exec_()