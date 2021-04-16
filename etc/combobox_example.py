import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

test_list = [ '선택1' , '선택2', '선택3', '선택4', '선택5' , '선택6' ]

class combobox_example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def makeComboBox(self):
		self.labelSelectComboExample = QComboBox(self)
		self.labelSelectComboExample.resize(110, 24)
		self.labelSelectComboExample.move(75, 55)
		self.labelSelectComboExample.addItem('--선택--')
		for val in test_list:
			self.labelSelectComboExample.addItem(val)

	def initUI(self):
		self.setWindowTitle('ComboBox Example')

		self.setFixedSize(600, 500)
		self.move(100, 100)

		frameGm = self.frameGeometry()
		screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
		centerPoint = QApplication.desktop().screenGeometry(screen).center()
		frameGm.moveCenter(centerPoint)
		self.move(frameGm.topLeft())
		
		status = self.statusBar()
		status.setStyleSheet(
			'''
			QStatusBar
			{
				background-color: rgb(214, 214, 214);
				color: black;
				border-top: 1px solid gray;
			}
			'''
		)

		exitAction = QAction(QIcon('image/icon/image1.png'), '종료', self)
		exitAction.setShortcut('ctrl+Q')
		exitAction.setStatusTip('프로그램 종료')
		exitAction.triggered.connect(qApp.quit)

		menubar = self.menuBar()
		menubar.setStyleSheet(
			'''
			QMenuBar
			{
				background-color: rgb(214, 214, 214);
				color: black;
				padding-top: 3px;
				border-bottom: 1px solid gray;
			}
			'''
		)
		menubar.setNativeMenuBar(True)
		filemenu = menubar.addMenu('파일')
		filemenu.addAction(exitAction)

		self.makeComboBox()

		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = combobox_example()
	sys.exit(app.exec_())
