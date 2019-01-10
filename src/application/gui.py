# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/application/gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(698, 605)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 10, 161, 61))
        self.pushButton.setObjectName("pushButton")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 170, 681, 391))
        self.tableView.setObjectName("tableView")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 80, 681, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.types = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.types.setContentsMargins(0, 0, 0, 0)
        self.types.setObjectName("types")
        self.checkBox_3 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.types.addWidget(self.checkBox_3, 0, 2, 1, 1)
        self.checkBox_1 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_1.setObjectName("checkBox_1")
        self.types.addWidget(self.checkBox_1, 0, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.types.addWidget(self.checkBox_4, 0, 3, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.types.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_5.setObjectName("checkBox_5")
        self.types.addWidget(self.checkBox_5, 0, 4, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 511, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.dates = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.dates.setContentsMargins(0, 0, 0, 0)
        self.dates.setObjectName("dates")
        self.endDate = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.endDate.setObjectName("endDate")
        self.dates.addWidget(self.endDate, 1, 1, 1, 1)
        self.startDate = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.startDate.setObjectName("startDate")
        self.dates.addWidget(self.startDate, 1, 0, 1, 1)
        self.endDateLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.endDateLabel.setObjectName("endDateLabel")
        self.dates.addWidget(self.endDateLabel, 0, 1, 1, 1)
        self.startDateLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.startDateLabel.setObjectName("startDateLabel")
        self.dates.addWidget(self.startDateLabel, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 698, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Filter"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_1.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_5.setText(_translate("MainWindow", "CheckBox"))
        self.endDateLabel.setText(_translate("MainWindow", "End date"))
        self.startDateLabel.setText(_translate("MainWindow", "Start date"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

