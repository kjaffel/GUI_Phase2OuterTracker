# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModuleNavigator/browsemodules.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BrowseModules(object):
    def setupUi(self, BrowseModules):
        BrowseModules.setObjectName("BrowseModules")
        BrowseModules.setEnabled(True)
        BrowseModules.resize(1560, 706)
        BrowseModules.setProperty("rec", QtCore.QRectF(0.0, 0.0, 0.0, 0.0))
        self.centralwidget = QtWidgets.QWidget(BrowseModules)
        self.centralwidget.setStyleSheet("font: 25 12pt \"Ubuntu\";")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 330, 1561, 301))
        self.frame.setMinimumSize(QtCore.QSize(1541, 0))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 200, 1541, 91))
        self.frame_2.setMinimumSize(QtCore.QSize(1511, 71))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 1521, 71))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 190, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 12pt \"Ubuntu Condensed\";\n"
"background-color: rgb(238, 238, 236);")
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1541, 171))
        self.tableWidget.setStyleSheet("font: 75 11pt \"Ubuntu Condensed\";")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 270, 1461, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 269, 51, 21))
        self.label_2.setStyleSheet("font: 75 12pt \"Ubuntu Condensed\";\n"
"background-color: rgb(238, 238, 236);\n"
"")
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(90, 290, 41, 25))
        self.radioButton.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(340, 290, 175, 25))
        self.radioButton_2.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(160, 290, 155, 25))
        self.radioButton_3.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(540, 290, 108, 25))
        self.radioButton_4.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.radioButton_4.setObjectName("radioButton_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(660, 290, 251, 27))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 40, 151, 25))
        self.comboBox_2.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 40, 61, 21))
        self.label_3.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 40, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(430, 40, 201, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 80, 611, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 80, 251, 21))
        self.label_5.setStyleSheet("font: 75 12pt \"Ubuntu Condensed\";\n"
"background-color: rgb(238, 238, 236);\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 140, 61, 21))
        self.label_6.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 180, 61, 21))
        self.label_7.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.label_7.setObjectName("label_7")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(140, 140, 151, 25))
        self.comboBox_3.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(140, 180, 151, 25))
        self.comboBox_4.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 220, 81, 21))
        self.label_9.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.label_9.setObjectName("label_9")
        self.comboBox_6 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_6.setGeometry(QtCore.QRect(140, 220, 151, 25))
        self.comboBox_6.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setItemText(1, "")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(650, 10, 901, 261))
        self.widget.setObjectName("widget")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(320, 180, 61, 21))
        self.label_8.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.label_8.setObjectName("label_8")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(370, 150, 121, 25))
        self.radioButton_5.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(370, 180, 121, 25))
        self.radioButton_6.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(370, 210, 121, 25))
        self.radioButton_7.setStyleSheet("font: 12pt \"Ubuntu Condensed\";")
        self.radioButton_7.setObjectName("radioButton_7")
        self.frame.raise_()
        self.line.raise_()
        self.radioButton.raise_()
        self.radioButton_3.raise_()
        self.radioButton_2.raise_()
        self.radioButton_4.raise_()
        self.comboBox.raise_()
        self.label_2.raise_()
        self.comboBox_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.line_2.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.comboBox_3.raise_()
        self.comboBox_4.raise_()
        self.label_9.raise_()
        self.comboBox_6.raise_()
        self.widget.raise_()
        self.label_8.raise_()
        self.radioButton_5.raise_()
        self.radioButton_6.raise_()
        self.radioButton_7.raise_()
        BrowseModules.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BrowseModules)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1560, 22))
        self.menubar.setObjectName("menubar")
        self.menuConnection = QtWidgets.QMenu(self.menubar)
        self.menuConnection.setObjectName("menuConnection")
        self.menuDescription = QtWidgets.QMenu(self.menubar)
        self.menuDescription.setGeometry(QtCore.QRect(404, 127, 190, 50))
        self.menuDescription.setObjectName("menuDescription")
        self.menuAssembly_Status = QtWidgets.QMenu(self.menubar)
        self.menuAssembly_Status.setGeometry(QtCore.QRect(500, 127, 190, 50))
        self.menuAssembly_Status.setObjectName("menuAssembly_Status")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        BrowseModules.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(BrowseModules)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.toolBar.setFont(font)
        self.toolBar.setAcceptDrops(False)
        self.toolBar.setMovable(True)
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        BrowseModules.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(BrowseModules)
        self.toolBar_2.setObjectName("toolBar_2")
        BrowseModules.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.statusBar = QtWidgets.QStatusBar(BrowseModules)
        self.statusBar.setObjectName("statusBar")
        BrowseModules.setStatusBar(self.statusBar)
        self.Quit = QtWidgets.QAction(BrowseModules)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icons/Action-exit-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Quit.setIcon(icon)
        self.Quit.setShortcutVisibleInContextMenu(True)
        self.Quit.setObjectName("Quit")
        self.actionOpen = QtWidgets.QAction(BrowseModules)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Icons/Open-Folder-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(BrowseModules)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Icons/Programming-Save-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionScan = QtWidgets.QAction(BrowseModules)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Icons/scan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScan.setIcon(icon3)
        self.actionScan.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionScan.setObjectName("actionScan")
        self.actionPrint = QtWidgets.QAction(BrowseModules)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Icons/Very-Basic-Print-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon4)
        self.actionPrint.setObjectName("actionPrint")
        self.actionSearch = QtWidgets.QAction(BrowseModules)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Icons/zoom_place-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSearch.setIcon(icon5)
        self.actionSearch.setObjectName("actionSearch")
        self.actionSQL = QtWidgets.QAction(BrowseModules)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../Icons/sql-database-icon-png-21.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSQL.setIcon(icon6)
        self.actionSQL.setObjectName("actionSQL")
        self.actionGet = QtWidgets.QAction(BrowseModules)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../Icons/get.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGet.setIcon(icon7)
        self.actionGet.setObjectName("actionGet")
        self.actionUpdate = QtWidgets.QAction(BrowseModules)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../Icons/update_file-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUpdate.setIcon(icon8)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionUndo = QtWidgets.QAction(BrowseModules)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../Icons/undo-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon9)
        self.actionUndo.setObjectName("actionUndo")
        self.actionUser = QtWidgets.QAction(BrowseModules)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../Icons/login-background-images-clipart-1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUser.setIcon(icon10)
        self.actionUser.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionUser.setPriority(QtWidgets.QAction.HighPriority)
        self.actionUser.setObjectName("actionUser")
        self.menubar.addAction(self.menuConnection.menuAction())
        self.menubar.addAction(self.menuDescription.menuAction())
        self.menubar.addAction(self.menuAssembly_Status.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.Quit)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPrint)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionGet)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUpdate)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionScan)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSearch)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSQL)
        self.toolBar.addSeparator()

        self.retranslateUi(BrowseModules)
        QtCore.QMetaObject.connectSlotsByName(BrowseModules)

    def retranslateUi(self, BrowseModules):
        _translate = QtCore.QCoreApplication.translate
        BrowseModules.setWindowTitle(_translate("BrowseModules", "BrowseModules"))
        self.label.setText(_translate("BrowseModules", " Console"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("BrowseModules", "QUANTITY"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("BrowseModules", "TYPE"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("BrowseModules", "LOCATION"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("BrowseModules", "STATUS"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("BrowseModules", "LAST ACTION"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("BrowseModules", "OPERATOR"))
        self.label_2.setText(_translate("BrowseModules", "  Status"))
        self.radioButton.setText(_translate("BrowseModules", "All"))
        self.radioButton_2.setText(_translate("BrowseModules", "Without known problems"))
        self.radioButton_3.setText(_translate("BrowseModules", "With known problems"))
        self.radioButton_4.setText(_translate("BrowseModules", "Concerned by:"))
        self.comboBox.setItemText(0, _translate("BrowseModules", "      Bad DAQ test performance "))
        self.comboBox_2.setItemText(0, _translate("BrowseModules", "    2S"))
        self.comboBox_2.setItemText(1, _translate("BrowseModules", "    PS"))
        self.label_3.setText(_translate("BrowseModules", "Module :"))
        self.label_4.setText(_translate("BrowseModules", "    OR Enter BarCode:"))
        self.label_5.setText(_translate("BrowseModules", "  Selection Criteria and showing proprties "))
        self.label_6.setText(_translate("BrowseModules", "Location:"))
        self.label_7.setText(_translate("BrowseModules", "Status:"))
        self.comboBox_3.setItemText(0, _translate("BrowseModules", "    LOUVAIN"))
        self.comboBox_4.setItemText(0, _translate("BrowseModules", "     RUNNING"))
        self.comboBox_4.setItemText(1, _translate("BrowseModules", "     FAULTY"))
        self.label_9.setText(_translate("BrowseModules", "Last action:"))
        self.comboBox_6.setItemText(0, _translate("BrowseModules", "     VALIDATION"))
        self.label_8.setText(_translate("BrowseModules", "Show:"))
        self.radioButton_5.setText(_translate("BrowseModules", "Module Count"))
        self.radioButton_6.setText(_translate("BrowseModules", "Module ID"))
        self.radioButton_7.setText(_translate("BrowseModules", "Module History"))
        self.menuConnection.setTitle(_translate("BrowseModules", "Connection"))
        self.menuDescription.setTitle(_translate("BrowseModules", "Description "))
        self.menuAssembly_Status.setTitle(_translate("BrowseModules", "Assembly Status"))
        self.menuHelp.setTitle(_translate("BrowseModules", "Help"))
        self.toolBar.setWindowTitle(_translate("BrowseModules", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("BrowseModules", "toolBar_2"))
        self.Quit.setText(_translate("BrowseModules", "Quit"))
        self.actionOpen.setText(_translate("BrowseModules", "Open"))
        self.actionSave.setText(_translate("BrowseModules", "Save"))
        self.actionScan.setText(_translate("BrowseModules", "Scan"))
        self.actionPrint.setText(_translate("BrowseModules", "Print"))
        self.actionSearch.setText(_translate("BrowseModules", "Query"))
        self.actionSQL.setText(_translate("BrowseModules", "SQL"))
        self.actionGet.setText(_translate("BrowseModules", "Get"))
        self.actionUpdate.setText(_translate("BrowseModules", "Update"))
        self.actionUndo.setText(_translate("BrowseModules", "Undo"))
        self.actionUser.setText(_translate("BrowseModules", "User"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BrowseModules = QtWidgets.QMainWindow()
    ui = Ui_BrowseModules()
    ui.setupUi(BrowseModules)
    BrowseModules.show()
    sys.exit(app.exec_())
