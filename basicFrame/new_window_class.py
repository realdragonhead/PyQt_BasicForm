from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# Type 1 ############################################
# Inherit Parents
class newWindow1(QDialog):
	def __init__(self, parent):
		super(newWindow1, self).__init__(parent)
		self.initUI(parent)

	def initUI(self, parent):
		'''
			Make new window widget
		'''
		self.show()
# Type 2 ###########################################
# No Inherit Parents
class newWindow2(QDialog):
	def __init__(self):
		super(newWindow2, self).__init__()
		self.initUI()
	
	def initUI(self):
		'''
			Make new window widget
		'''
		self.show()

class Main(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def openNewWindow_with_P(self):
		newWindow1(self)
		'''
			Make trigger function to open new window(etc, click menu/button, start processing)
		'''
	
	def openNewWindow_with_N(self):
		newWindow2(self)
		'''
			Make trigger function to open new window(etc, click menu/button, start processing)
		'''

	def initUI(self):
		'''
			Make parents window widget
		'''
		# Button type trigger to open new window
		self.button1.clicked.connect(self.openNewWindow_with_P)
		self.button2.clicked.connect(self.openNewWindow_with_N)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Main()
	sys.exit(app.exec_())

# No Inherit Parents
