import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

class basicWindowFrame(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('Program\'s title')
		# Set Icon
		# self.setWindowIcon(QIcon('image/icon.png')

		self.setFixedSize(600, 500)
		self.move(100, 100)
		# Main Window center position
		# self.center()

		frameGm = self.frameGeometry()
		screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
		centerPoint = QApplication.desktop().screenGeometry(screen).center()
		frameGm.moveCenter(centerPoint)
		self.move(frameGm.topLeft())

		# Status Bar
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

		# Exit Action
		exitAction = QAction(QIcon('image/icon/image1.png'), '종료', self)
		exitAction.setShortcut('ctrl+Q')
		exitAction.setStatusTip('프로그램 종료')
		exitAction.triggered.connect(qApp.quit)

		# MenuBar
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
		# Option for Windows type menu bar for Windows and Mac type menu bar for Mac
		menubar.setNativeMenuBar(True)
		filemenu = menubar.addMenu('파일')
		filemenu.addAction(exitAction)
		
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = basicWindowFrame()
	sys.exit(app.exec_())
