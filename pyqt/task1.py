import sys
from PyQt4 import QtCore, QtGui, uic

form_class = uic.loadUiType("MyFirstGUI.ui")[0]

class MyWindowClass(QtGui.QMainWindow, form_class):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.spushButton.clicked.connect(self.button_clicked)
	def button_clicked(self):
		x = self.spushButton.x()
		y = self.spushButton.y()
		x += 50
		y += 50
		self.spushButton.move(x, y)
app = QtGui.QApplication(sys.argv)
myWindow = MyWindowClass()
myWindow.show()
app.exec_()
