# Form implementation generated from reading ui file 'D:\KTLT_NGUYENVONHUNGOC_EXERCISE\MODULE3\Exercise63\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 452)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 651, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 255);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 241, 321))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 221, 281))
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 201, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 60, 411, 221))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 120, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.radioButtonOfficial = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButtonOfficial.setGeometry(QtCore.QRect(150, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButtonOfficial.setFont(font)
        self.radioButtonOfficial.setChecked(True)
        self.radioButtonOfficial.setObjectName("radioButtonOfficial")
        self.lineEditName = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditName.setGeometry(QtCore.QRect(150, 60, 251, 20))
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditPrice = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditPrice.setGeometry(QtCore.QRect(150, 90, 251, 20))
        self.lineEditPrice.setObjectName("lineEditPrice")
        self.lineEditDiscount = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditDiscount.setGeometry(QtCore.QRect(150, 120, 251, 20))
        self.lineEditDiscount.setObjectName("lineEditDiscount")
        self.lineEditId = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.lineEditId.setGeometry(QtCore.QRect(150, 30, 251, 20))
        self.lineEditId.setObjectName("lineEditId")
        self.radioButtonNotOfficial = QtWidgets.QRadioButton(parent=self.groupBox_2)
        self.radioButtonNotOfficial.setGeometry(QtCore.QRect(270, 150, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButtonNotOfficial.setFont(font)
        self.radioButtonNotOfficial.setCheckable(False)
        self.radioButtonNotOfficial.setChecked(False)
        self.radioButtonNotOfficial.setObjectName("radioButtonNotOfficial")
        self.pushButtonSave = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonSave.setGeometry(QtCore.QRect(150, 190, 81, 21))
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.pushButtonRemove = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.pushButtonRemove.setGeometry(QtCore.QRect(260, 190, 121, 21))
        self.pushButtonRemove.setObjectName("pushButtonRemove")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(260, 290, 411, 91))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButtonSearchName = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonSearchName.setGeometry(QtCore.QRect(30, 40, 171, 31))
        self.pushButtonSearchName.setObjectName("pushButtonSearchName")
        self.pushButtonFilterPrice = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.pushButtonFilterPrice.setGeometry(QtCore.QRect(230, 40, 171, 31))
        self.pushButtonFilterPrice.setObjectName("pushButtonFilterPrice")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Product Managements"))
        self.groupBox.setTitle(_translate("MainWindow", "Products:"))
        self.pushButton_2.setText(_translate("MainWindow", "112- Thuốc trị hôi nách - 100"))
        self.pushButton_5.setText(_translate("MainWindow", "98 - Thuốc trị ngáo - 23"))
        self.pushButton_4.setText(_translate("MainWindow", "113- Thuốc tăng tự tin - 113"))
        self.pushButton_3.setText(_translate("MainWindow", "114 - Thuốc trị lác - 154"))
        self.pushButton.setText(_translate("MainWindow", "117 - Thuốc trị lười - 159"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Product Details:"))
        self.label_3.setText(_translate("MainWindow", "Id:"))
        self.label_4.setText(_translate("MainWindow", "Name:"))
        self.label_5.setText(_translate("MainWindow", "Price:"))
        self.label_6.setText(_translate("MainWindow", "Discount:"))
        self.radioButtonOfficial.setText(_translate("MainWindow", "Official"))
        self.radioButtonNotOfficial.setText(_translate("MainWindow", "Not Official"))
        self.pushButtonSave.setText(_translate("MainWindow", "Save"))
        self.pushButtonRemove.setText(_translate("MainWindow", "Remove"))
        self.groupBox_3.setTitle(_translate("MainWindow", "More functions:"))
        self.pushButtonSearchName.setText(_translate("MainWindow", "Search Name"))
        self.pushButtonFilterPrice.setText(_translate("MainWindow", "Filter Price"))
