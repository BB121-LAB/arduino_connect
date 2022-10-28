# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 191)
        MainWindow.setMinimumSize(QtCore.QSize(481, 191))
        MainWindow.setMaximumSize(QtCore.QSize(481, 191))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 251, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.dropdown_port = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.dropdown_port.setObjectName("dropdown_port")
        self.verticalLayout.addWidget(self.dropdown_port)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_connect = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_connect.setObjectName("button_connect")
        self.horizontalLayout.addWidget(self.button_connect)
        self.button_refresh = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_refresh.setObjectName("button_refresh")
        self.horizontalLayout.addWidget(self.button_refresh)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.raw_out_checkbox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.raw_out_checkbox.setObjectName("raw_out_checkbox")
        self.verticalLayout.addWidget(self.raw_out_checkbox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 130, 251, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.status_line = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.status_line.setReadOnly(True)
        self.status_line.setObjectName("status_line")
        self.verticalLayout_2.addWidget(self.status_line)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(270, 10, 201, 91))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.dropdown_key = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.dropdown_key.setObjectName("dropdown_key")
        self.verticalLayout_3.addWidget(self.dropdown_key)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.frame_run_pause = QtWidgets.QFrame(self.centralwidget)
        self.frame_run_pause.setEnabled(False)
        self.frame_run_pause.setGeometry(QtCore.QRect(270, 110, 201, 71))
        self.frame_run_pause.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_run_pause.setObjectName("frame_run_pause")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_run_pause)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.button_run = QtWidgets.QPushButton(self.frame_run_pause)
        self.button_run.setObjectName("button_run")
        self.verticalLayout_4.addWidget(self.button_run)
        self.button_pause = QtWidgets.QPushButton(self.frame_run_pause)
        self.button_pause.setObjectName("button_pause")
        self.verticalLayout_4.addWidget(self.button_pause)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Port"))
        self.button_connect.setText(_translate("MainWindow", "Connect"))
        self.button_refresh.setText(_translate("MainWindow", "Refresh"))
        self.raw_out_checkbox.setText(_translate("MainWindow", "Raw Output Mode"))
        self.label_2.setText(_translate("MainWindow", "Status"))
        self.label_3.setText(_translate("MainWindow", "Key"))
        self.button_run.setText(_translate("MainWindow", "Run"))
        self.button_pause.setText(_translate("MainWindow", "Pause"))
