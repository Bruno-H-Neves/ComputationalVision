# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'p5menus_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 322, 392))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(350, 30, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.treeView = QtWidgets.QTreeView(self.tab)
        self.treeView.setGeometry(QtCore.QRect(320, 80, 91, 101))
        self.treeView.setObjectName("treeView")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_7.setGeometry(QtCore.QRect(10, 80, 82, 17))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_8.setGeometry(QtCore.QRect(10, 100, 82, 17))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_9.setGeometry(QtCore.QRect(10, 120, 82, 17))
        self.radioButton_9.setObjectName("radioButton_9")
        self.spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox.setGeometry(QtCore.QRect(190, 40, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.radioButton_10 = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton_10.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButton_10.setObjectName("radioButton_10")
        self.radioButton_11 = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton_11.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_11.setObjectName("radioButton_11")
        self.radioButton_12 = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton_12.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_12.setObjectName("radioButton_12")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.radioButton_13 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_13.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButton_13.setObjectName("radioButton_13")
        self.radioButton_14 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_14.setGeometry(QtCore.QRect(10, 30, 82, 17))
        self.radioButton_14.setObjectName("radioButton_14")
        self.radioButton_15 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_15.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.radioButton_15.setObjectName("radioButton_15")
        self.radioButton_16 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_16.setGeometry(QtCore.QRect(10, 70, 82, 17))
        self.radioButton_16.setObjectName("radioButton_16")
        self.radioButton_17 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_17.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.radioButton_17.setObjectName("radioButton_17")
        self.radioButton_18 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_18.setGeometry(QtCore.QRect(10, 110, 82, 17))
        self.radioButton_18.setObjectName("radioButton_18")
        self.radioButton_19 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_19.setGeometry(QtCore.QRect(10, 130, 82, 17))
        self.radioButton_19.setObjectName("radioButton_19")
        self.radioButton_20 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_20.setGeometry(QtCore.QRect(10, 150, 82, 17))
        self.radioButton_20.setObjectName("radioButton_20")
        self.radioButton_21 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_21.setGeometry(QtCore.QRect(10, 170, 82, 17))
        self.radioButton_21.setObjectName("radioButton_21")
        self.radioButton_22 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_22.setGeometry(QtCore.QRect(10, 190, 82, 17))
        self.radioButton_22.setObjectName("radioButton_22")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.verticalSlider = QtWidgets.QSlider(self.tab_5)
        self.verticalSlider.setGeometry(QtCore.QRect(340, 190, 19, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.dial = QtWidgets.QDial(self.tab_5)
        self.dial.setGeometry(QtCore.QRect(360, 30, 50, 64))
        self.dial.setObjectName("dial")
        self.tabWidget.addTab(self.tab_5, "")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(320, 20, 696, 513))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../Desktop/images/Detect_RGB.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalSlider_3 = QtWidgets.QSlider(self.layoutWidget)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.horizontalLayout.addWidget(self.verticalSlider_3)
        self.verticalSlider_2 = QtWidgets.QSlider(self.layoutWidget)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.horizontalLayout.addWidget(self.verticalSlider_2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSave = QtWidgets.QMenu(self.menuFile)
        self.menuSave.setObjectName("menuSave")
        self.menuEdit_2 = QtWidgets.QMenu(self.menubar)
        self.menuEdit_2.setObjectName("menuEdit_2")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSave_3 = QtWidgets.QAction(MainWindow)
        self.actionSave_3.setObjectName("actionSave_3")
        self.actionSave_As_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_As_2.setObjectName("actionSave_As_2")
        self.actionMaximaze = QtWidgets.QAction(MainWindow)
        self.actionMaximaze.setObjectName("actionMaximaze")
        self.actionNormal = QtWidgets.QAction(MainWindow)
        self.actionNormal.setObjectName("actionNormal")
        self.menuSave.addAction(self.actionSave_3)
        self.menuSave.addAction(self.actionSave_As_2)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuView.addAction(self.actionMaximaze)
        self.menuView.addAction(self.actionNormal)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit_2.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionMaximaze.triggered.connect(MainWindow.showMaximized)
        self.actionNormal.triggered.connect(MainWindow.showNormal)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Computational Vision "))
        MainWindow.setStatusTip(_translate("MainWindow", "https://github.com/Bruno-H-Neves"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "GrayScale"))
        self.radioButton_4.setText(_translate("MainWindow", "Gaussian"))
        self.radioButton_5.setText(_translate("MainWindow", "SepFilter2D"))
        self.radioButton_6.setText(_translate("MainWindow", "Blur"))
        self.radioButton_7.setText(_translate("MainWindow", "Median Blur"))
        self.radioButton_8.setText(_translate("MainWindow", "Bilateral"))
        self.radioButton_9.setText(_translate("MainWindow", "2D"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "LBF"))
        self.radioButton_10.setText(_translate("MainWindow", "Sobel"))
        self.radioButton_11.setText(_translate("MainWindow", "Canny"))
        self.radioButton_12.setText(_translate("MainWindow", "Laplacian"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "HBF"))
        self.radioButton_13.setText(_translate("MainWindow", "Dilate"))
        self.radioButton_14.setText(_translate("MainWindow", "Erode"))
        self.radioButton_15.setText(_translate("MainWindow", "Open"))
        self.radioButton_16.setText(_translate("MainWindow", "Close"))
        self.radioButton_17.setText(_translate("MainWindow", "Gradient"))
        self.radioButton_18.setText(_translate("MainWindow", "Top Hat"))
        self.radioButton_19.setText(_translate("MainWindow", "Black Hat"))
        self.radioButton_20.setText(_translate("MainWindow", "Rect"))
        self.radioButton_21.setText(_translate("MainWindow", "Ellipse"))
        self.radioButton_22.setText(_translate("MainWindow", "Cross"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Morphologic"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Threshold"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.pushButton_2.setText(_translate("MainWindow", "Save"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.menuEdit_2.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Click to Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionSave_3.setText(_translate("MainWindow", "Save"))
        self.actionSave_As_2.setText(_translate("MainWindow", "Save As"))
        self.actionMaximaze.setText(_translate("MainWindow", "Maximize"))
        self.actionMaximaze.setShortcut(_translate("MainWindow", "Shift+M"))
        self.actionNormal.setText(_translate("MainWindow", "Normal"))
        self.actionNormal.setShortcut(_translate("MainWindow", "Shift+N"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

