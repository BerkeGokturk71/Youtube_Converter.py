# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Youtube_Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 757)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(1000, 0))
        self.frame.setStyleSheet("\n"
"border-top-right-radius: 70px;\n"
"border-bottom-left-radius: 70px;\n"
"\n"
"background-color: rgb(12, 146, 230);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 29, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(31)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel#label_2:hover{\n"
"\n"
"color: rgb(2, 62, 138);\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(300, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"background-color: rgb(254, 250, 224);\n"
"color: rgb(43, 117, 255);\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color: rgb(37, 215, 255);\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(254, 250, 224);\n"
"border-radius: 8px;")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("Youtube Link Here")
        self.lineEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame)
        self.radioButton_2.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("background-color:rgb(173, 232, 244);\n"
"color: rgb(43, 117, 255);\n"
"")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("background-color:rgb(173, 232, 244);\n"
"color: rgb(43, 117, 255);\n"
"\n"
"")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color:rgb(173, 232, 244);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.3 rgba(85, 210, 255), stop:0.7 rgba(94, 97, 255), stop:0.8 rgba(49, 69, 255));\n"
"border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(37, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(85, 85, 255);\n"
"background-color: rgb(94, 137, 255);\n"
"border-radius: 8px;\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"color:rgba(122,191,255);\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color:rgba(122,191,155);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(163, 196, 243), stop:0.5 rgba(142, 236, 245), stop:0.7 rgba(152, 245, 225));\n"
"    \n"
"    \n"
"    \n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem5 = QtWidgets.QSpacerItem(35, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.label_3 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setStyleSheet("color: rgb(138, 240, 255);\n"
"background-color: rgb(85, 159, 255);")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_2,#pushButton_3,#pushButton_4{\n"
"background-color:rgba(0,0,0,0);\n"
"color:rgba(222,191,255);\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover,#pushButton_3:hover,#pushButton_4:hover{\n"
"color:rgba(122,191,255);\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed,#pushButton_3:pressed,#pushButton_4:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color:rgba(122,191,155);\n"
"\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ikonlar/Bokehlicia-Captiva-Web-github.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(26, 40))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_6.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_2,#pushButton_3,#pushButton_4{\n"
"background-color:rgba(0,0,0,0);\n"
"color:rgba(222,191,255);\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover,#pushButton_3:hover,#pushButton_4:hover{\n"
"color:rgba(122,191,255);\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed,#pushButton_3:pressed,#pushButton_4:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"color:rgba(122,191,155);\n"
"\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ikonlar/Bokehlicia-Captiva-Web-google-gmail.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(26, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Youtube Conventer Vol 1.1"))
        self.label.setText(_translate("MainWindow", "Youtube Link :"))
        self.radioButton_2.setText(_translate("MainWindow", "Normal Video"))
        self.radioButton.setText(_translate("MainWindow", "Playlist"))
        self.comboBox.setItemText(0, _translate("MainWindow", "144p"))
        self.comboBox.setItemText(1, _translate("MainWindow", "360p"))
        self.comboBox.setItemText(2, _translate("MainWindow", "480p"))
        self.comboBox.setItemText(3, _translate("MainWindow", "720p"))
        self.pushButton.setText(_translate("MainWindow", "İndirilecek klasor"))
        self.pushButton_2.setText(_translate("MainWindow", "İndir"))
        self.label_3.setText(_translate("MainWindow", "Mp3 İndirmeye Hazırım:)"))
        self.pushButton_4.setText(_translate("MainWindow", "Github"))
        self.pushButton_3.setText(_translate("MainWindow", "Mail"))
import icons_rc
