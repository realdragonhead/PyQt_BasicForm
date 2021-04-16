import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic

# read csv file
header_list = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten' ]
content_list = [ [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '10' ], [ '11', '12', '13', '14', '15', '16', '17', '18', '19', '20' ]]

class tableWidgetView(QMainWindow):
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

		self.createTable()

		self.show()

	def createTable(self):
		self.tableWidget = QTableWidget(self)
		header_label = []

		self.tableWidget.setColumnCount(10)
		self.tableWidget.setRowCount(20)
		self.tableWidget.setGeometry(10, 10, 580, 450)
		self.tableWidget.setHorizontalHeaderLabels(header_list)
		
		for col, lists in enumerate(content_list):
			for row, val in enumerate(lists):
				try:
					self.tableWidget.setItem(row , col, QTableWidgetItem(val))
				except:
					continue

		self.tableWidget.repaint()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = tableWidgetView()
	sys.exit(app.exec_())
