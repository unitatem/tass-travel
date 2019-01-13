# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tass_travel/application/gui.ui'
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
        self.filterBtn = QtWidgets.QPushButton(self.centralwidget)
        self.filterBtn.setGeometry(QtCore.QRect(530, 10, 161, 61))
        self.filterBtn.setObjectName("filterBtn")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 80, 681, 80))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.types = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.types.setContentsMargins(0, 0, 0, 0)
        self.types.setObjectName("types")
        self.radioButton_1 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_1.setObjectName("radioButton_1")
        self.types.addWidget(self.radioButton_1, 0, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_4.setObjectName("radioButton_4")
        self.types.addWidget(self.radioButton_4, 0, 3, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_3.setObjectName("radioButton_3")
        self.types.addWidget(self.radioButton_3, 0, 2, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_2.setObjectName("radioButton_2")
        self.types.addWidget(self.radioButton_2, 0, 1, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_5.setObjectName("radioButton_5")
        self.types.addWidget(self.radioButton_5, 0, 4, 1, 1)
        self.dropDown = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.dropDown.setObjectName("dropDown")
        self.types.addWidget(self.dropDown, 0, 5, 1, 1)
        self.types.setColumnStretch(5, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 511, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.dates = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.dates.setContentsMargins(0, 0, 0, 0)
        self.dates.setObjectName("dates")
        self.endDate = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.endDate.setDate(QtCore.QDate(2008, 1, 1))
        self.endDate.setObjectName("endDate")
        self.dates.addWidget(self.endDate, 1, 1, 1, 1)
        self.startDate = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.startDate.setCalendarPopup(False)
        self.startDate.setDate(QtCore.QDate(2005, 1, 1))
        self.startDate.setObjectName("startDate")
        self.dates.addWidget(self.startDate, 1, 0, 1, 1)
        self.endDateLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.endDateLabel.setObjectName("endDateLabel")
        self.dates.addWidget(self.endDateLabel, 0, 1, 1, 1)
        self.startDateLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.startDateLabel.setObjectName("startDateLabel")
        self.dates.addWidget(self.startDateLabel, 0, 0, 1, 1)
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 170, 681, 391))
        self.table.setColumnCount(3)
        self.table.setObjectName("table")
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setDefaultSectionSize(200)
        self.table.horizontalHeader().setSortIndicatorShown(False)
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
        self.filterBtn.setText(_translate("MainWindow", "Filter"))
        self.radioButton_1.setText(_translate("MainWindow", "leisure"))
        self.radioButton_4.setText(_translate("MainWindow", "building"))
        self.radioButton_3.setText(_translate("MainWindow", "tourism"))
        self.radioButton_2.setText(_translate("MainWindow", "historic"))
        self.radioButton_5.setText(_translate("MainWindow", "aeroway"))
        self.endDateLabel.setText(_translate("MainWindow", "End date"))
        self.startDateLabel.setText(_translate("MainWindow", "Start date"))
        self.table.setSortingEnabled(False)
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "City"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Population"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Normalized POIs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

