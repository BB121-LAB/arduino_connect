# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graph_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Graph(object):
    def setupUi(self, Graph):
        Graph.setObjectName("Graph")
        Graph.resize(592, 493)
        Graph.setMinimumSize(QtCore.QSize(412, 289))
        self.verticalLayout = QtWidgets.QVBoxLayout(Graph)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graph = PlotWidget(Graph)
        self.graph.setObjectName("graph")
        self.verticalLayout.addWidget(self.graph)
        self.label = QtWidgets.QLabel(Graph)
        self.label.setMaximumSize(QtCore.QSize(400, 50))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Graph)
        QtCore.QMetaObject.connectSlotsByName(Graph)

    def retranslateUi(self, Graph):
        _translate = QtCore.QCoreApplication.translate
        Graph.setWindowTitle(_translate("Graph", "Raw Data"))
        self.label.setText(_translate("Graph", "This graph is displaying the raw output of the primary amplifier. \n"
"Press \'Run\' on the main window to start capturing data."))
from pyqtgraph import PlotWidget
