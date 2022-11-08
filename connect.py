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
        MainWindow.resize(1045, 344)
        MainWindow.setMinimumSize(QtCore.QSize(1045, 344))
        MainWindow.setMaximumSize(QtCore.QSize(9999, 9999))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setMaximumSize(QtCore.QSize(404, 16777215))
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.vertframe = QtWidgets.QFrame(self.horizontalFrame)
        self.vertframe.setMinimumSize(QtCore.QSize(384, 90))
        self.vertframe.setMaximumSize(QtCore.QSize(384, 90))
        self.vertframe.setFrameShape(QtWidgets.QFrame.Box)
        self.vertframe.setObjectName("vertframe")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.vertframe)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.vertframe)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.frame_run_pause_2 = QtWidgets.QFrame(self.vertframe)
        self.frame_run_pause_2.setEnabled(True)
        self.frame_run_pause_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_run_pause_2.setObjectName("frame_run_pause_2")
        self.frame_run_pause = QtWidgets.QHBoxLayout(self.frame_run_pause_2)
        self.frame_run_pause.setObjectName("frame_run_pause")
        self.button_run = QtWidgets.QPushButton(self.frame_run_pause_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_run.sizePolicy().hasHeightForWidth())
        self.button_run.setSizePolicy(sizePolicy)
        self.button_run.setMinimumSize(QtCore.QSize(50, 10))
        self.button_run.setMaximumSize(QtCore.QSize(99999, 99999))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_run.setFont(font)
        self.button_run.setObjectName("button_run")
        self.frame_run_pause.addWidget(self.button_run)
        self.button_pause = QtWidgets.QPushButton(self.frame_run_pause_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_pause.sizePolicy().hasHeightForWidth())
        self.button_pause.setSizePolicy(sizePolicy)
        self.button_pause.setMinimumSize(QtCore.QSize(50, 10))
        self.button_pause.setMaximumSize(QtCore.QSize(99999, 99999))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_pause.setFont(font)
        self.button_pause.setObjectName("button_pause")
        self.frame_run_pause.addWidget(self.button_pause)
        self.verticalLayout_4.addWidget(self.frame_run_pause_2)
        self.gridLayout.addWidget(self.vertframe, 2, 0, 1, 1)
        self.verticalFrame_4 = QtWidgets.QFrame(self.horizontalFrame)
        self.verticalFrame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.verticalFrame_4.setObjectName("verticalFrame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalFrame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.verticalFrame_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_norm = QtWidgets.QRadioButton(self.verticalFrame_4)
        self.radioButton_norm.setChecked(True)
        self.radioButton_norm.setObjectName("radioButton_norm")
        self.horizontalLayout_2.addWidget(self.radioButton_norm)
        self.radioButton_graph = QtWidgets.QRadioButton(self.verticalFrame_4)
        self.radioButton_graph.setObjectName("radioButton_graph")
        self.horizontalLayout_2.addWidget(self.radioButton_graph)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.gridLayout.addWidget(self.verticalFrame_4, 0, 0, 1, 1)
        self.verticalFrame = QtWidgets.QFrame(self.horizontalFrame)
        self.verticalFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalFrame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.dropdown_port = QtWidgets.QComboBox(self.verticalFrame)
        self.dropdown_port.setObjectName("dropdown_port")
        self.verticalLayout.addWidget(self.dropdown_port)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_connect = QtWidgets.QPushButton(self.verticalFrame)
        self.button_connect.setObjectName("button_connect")
        self.horizontalLayout.addWidget(self.button_connect)
        self.button_refresh = QtWidgets.QPushButton(self.verticalFrame)
        self.button_refresh.setObjectName("button_refresh")
        self.horizontalLayout.addWidget(self.button_refresh)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.verticalFrame, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout)
        self.horizontalLayout_3.addWidget(self.horizontalFrame)
        self.verticalFrame_3 = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame_3.setMinimumSize(QtCore.QSize(208, 0))
        self.verticalFrame_3.setMaximumSize(QtCore.QSize(208, 16777215))
        self.verticalFrame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.verticalFrame_3.setObjectName("verticalFrame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalFrame_3)
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalFrame1 = QtWidgets.QFrame(self.verticalFrame_3)
        self.verticalFrame1.setFrameShape(QtWidgets.QFrame.Box)
        self.verticalFrame1.setObjectName("verticalFrame1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalFrame1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalFrame1)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.dropdown_key = QtWidgets.QComboBox(self.verticalFrame1)
        self.dropdown_key.setObjectName("dropdown_key")
        self.verticalLayout_2.addWidget(self.dropdown_key)
        self.verticalLayout_3.addWidget(self.verticalFrame1)
        self.graph_zoom_frame = QtWidgets.QFrame(self.verticalFrame_3)
        self.graph_zoom_frame.setEnabled(True)
        self.graph_zoom_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.graph_zoom_frame.setObjectName("graph_zoom_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.graph_zoom_frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.graph_zoom_frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.graph_zoom_frame)
        self.label_6.setMinimumSize(QtCore.QSize(188, 60))
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.checkBox_auto_scale = QtWidgets.QCheckBox(self.graph_zoom_frame)
        self.checkBox_auto_scale.setChecked(True)
        self.checkBox_auto_scale.setObjectName("checkBox_auto_scale")
        self.verticalLayout_6.addWidget(self.checkBox_auto_scale)
        self.label_7 = QtWidgets.QLabel(self.graph_zoom_frame)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.pushButton = QtWidgets.QPushButton(self.graph_zoom_frame)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_6.addWidget(self.pushButton)
        self.verticalLayout_3.addWidget(self.graph_zoom_frame)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3.addWidget(self.verticalFrame_3)
        self.graph = PlotWidget(self.centralwidget)
        self.graph.setObjectName("graph")
        self.horizontalLayout_3.addWidget(self.graph)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(_translate("MainWindow", "Step 3: If in Key Mode, click run to start emulating key presses."))
        self.button_run.setText(_translate("MainWindow", "Run"))
        self.button_pause.setText(_translate("MainWindow", "Pause"))
        self.label_4.setText(_translate("MainWindow", "Step 1: choose operation mode."))
        self.radioButton_norm.setText(_translate("MainWindow", "Key Mode"))
        self.radioButton_graph.setText(_translate("MainWindow", "Graph mode"))
        self.label.setText(_translate("MainWindow", "Step 2: Choose port and click connect."))
        self.button_connect.setText(_translate("MainWindow", "Connect"))
        self.button_refresh.setText(_translate("MainWindow", "Refresh"))
        self.label_3.setText(_translate("MainWindow", "Key press to emulate. This can be changed any time when in Key Mode."))
        self.label_2.setText(_translate("MainWindow", "Graph Options"))
        self.label_6.setText(_translate("MainWindow", "You can zoom in and out with the scroll wheel and click and drag to pan the graph.\n"
""))
        self.checkBox_auto_scale.setText(_translate("MainWindow", "Auto scale graph"))
        self.label_7.setText(_translate("MainWindow", "Export Data"))
        self.pushButton.setText(_translate("MainWindow", "PNG"))
from pyqtgraph import PlotWidget
