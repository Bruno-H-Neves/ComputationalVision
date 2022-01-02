
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
import cv2, imutils

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(733, 544)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../Downloads/WhatsApp Image 2021-12-23 at 12.26.51 (2).jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 30, 561, 441))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 2, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 733, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOpen_File = QtWidgets.QMenu(self.menuFile)
        self.menuOpen_File.setObjectName("menuOpen_File")
        self.menuSave = QtWidgets.QMenu(self.menuFile)
        self.menuSave.setObjectName("menuSave")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionPublish = QtWidgets.QAction(MainWindow)
        self.actionPublish.setObjectName("actionPublish")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout_Us = QtWidgets.QAction(MainWindow)
        self.actionAbout_Us.setObjectName("actionAbout_Us")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionFile = QtWidgets.QAction(MainWindow)
        self.actionFile.setObjectName("actionFile")
        self.actionFolder = QtWidgets.QAction(MainWindow)
        self.actionFolder.setObjectName("actionFolder")
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionMaximize = QtWidgets.QAction(MainWindow)
        self.actionMaximize.setObjectName("actionMaximize")
        self.actionNormal = QtWidgets.QAction(MainWindow)
        self.actionNormal.setObjectName("actionNormal")
        self.actionMinimaze = QtWidgets.QAction(MainWindow)
        self.actionMinimaze.setObjectName("actionMinimaze")
        self.menuOpen_File.addAction(self.actionFile)
        self.menuOpen_File.addAction(self.actionFolder)
        self.menuSave.addAction(self.actionSave_2)
        self.menuSave.addAction(self.actionSave_As)
        self.menuFile.addAction(self.menuOpen_File.menuAction())
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionPublish)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout_Us)
        self.menuView.addAction(self.actionMaximize)
        self.menuView.addAction(self.actionNormal)
        self.menuView.addAction(self.actionMinimaze)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionMaximize.triggered.connect(MainWindow.showMaximized)
        self.actionNormal.triggered.connect(MainWindow.showNormal)
        self.actionMinimaze.triggered.connect(MainWindow.showMinimized)
        self.pushButton.clicked.connect(self.loadImage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

       
###########################################
    #function for image processing
 #   def loadImage(self):
#        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
#        self.image = cv2.imread(self.filename)
#        self.setPhoto(self.image)
######################################



    def loadImage(self):
        self.started = False
        self.temp=None


        vid = cv2.VideoCapture(0)                                       # Read Webcam
        while (vid.isOpened()):                                         # Infinite Loop: Read video          
            ctrl, self.image = vid.read()                               # Read frames
            self.image  = imutils.resize(self.image ,height = 480 )     # Resize
            self.image = imutils.resize(self.image,width=640)
            frame = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            self.image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))

            key=cv2.waitKey(5)                
            if key==27  or key==ord('q'):
                break
        vid.release()
	
    def setPhoto(self,image):
        self.tmp = image
        image = imutils.resize(image,width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))
    



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bruno-H-Neves Computational Vision"))
        MainWindow.setStatusTip(_translate("MainWindow", "https://github.com/Bruno-H-Neves/ComputationalVision"))
        self.label.setText(_translate("MainWindow", "Image_RGB"))
        self.pushButton.setText(_translate("MainWindow", "Open/Close"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOpen_File.setTitle(_translate("MainWindow", "Open"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.statusbar.setStatusTip(_translate("MainWindow", "https://github.com/Bruno-H-Neves/ComputationalVision"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Click to Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setStatusTip(_translate("MainWindow", "Click to Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setStatusTip(_translate("MainWindow", "Click to Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setStatusTip(_translate("MainWindow", "Click to Print"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionPublish.setText(_translate("MainWindow", "Publish"))
        self.actionPublish.setStatusTip(_translate("MainWindow", "Click to Publish"))
        self.actionPublish.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setStatusTip(_translate("MainWindow", "Click to Help"))
        self.actionHelp.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionAbout_Us.setText(_translate("MainWindow", "About Us..."))
        self.actionAbout_Us.setStatusTip(_translate("MainWindow", "Click to About Us"))
        self.actionAbout_Us.setShortcut(_translate("MainWindow", "Ctrl+U, Ctrl+S"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setStatusTip(_translate("MainWindow", "Click to Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionFile.setText(_translate("MainWindow", "File"))
        self.actionFile.setStatusTip(_translate("MainWindow", "Click to Open File"))
        self.actionFile.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.actionFolder.setText(_translate("MainWindow", "Folder"))
        self.actionFolder.setStatusTip(_translate("MainWindow", "Click to Open Folder"))
        self.actionFolder.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.actionSave_2.setText(_translate("MainWindow", "Save"))
        self.actionSave_2.setStatusTip(_translate("MainWindow", "Click to Save"))
        self.actionSave_2.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionSave_As.setStatusTip(_translate("MainWindow", "Click to Save As"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionMaximize.setText(_translate("MainWindow", "Maximize"))
        self.actionMaximize.setStatusTip(_translate("MainWindow", "Click to Maximize Window"))
        self.actionMaximize.setShortcut(_translate("MainWindow", "Shift+M"))
        self.actionNormal.setText(_translate("MainWindow", "Normal"))
        self.actionNormal.setStatusTip(_translate("MainWindow", "Click to Normal Window"))
        self.actionNormal.setShortcut(_translate("MainWindow", "Shift+N"))
        self.actionMinimaze.setText(_translate("MainWindow", "Minimize"))
        self.actionMinimaze.setStatusTip(_translate("MainWindow", "Click to Minimize Window"))
        self.actionMinimaze.setShortcut(_translate("MainWindow", "Shift+B"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

