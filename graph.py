import numpy
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets
import graph_ui

class GraphWindow(QtWidgets.QDialog, graph_ui.Ui_Graph):
    def __init__(self, *args, obj=None, **kwargs):
        super(GraphWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/icon/icon.png'))
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        # graph timer
        self.graph_timer = QtCore.QTimer()
        self.graph_timer.timeout.connect(self.draw_graphs)
        self.graph_frame_rate = 30
        self.graph_timer_ms = int(1 / (self.graph_frame_rate / 1000))

        # graph properties
        self.graph.disableAutoRange()
        self.graph.showGrid(True, True, alpha = 0.5)
        self.graph_padding_factor = 0.667
        self.green_pen = pg.mkPen('g', width = 2)

        # graph data
        self._graph_max_size = 1000
        self._data_index = 0
        self._data = numpy.zeros(self._graph_max_size)
        
        # set curve
        self.graph_reset()

        # start timer
        self.graph_timer.start(self.graph_timer_ms)

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, value):
        self._data[self._data_index] = value
        self._data_index = (self._data_index + 1) % self._graph_max_size
        if self._data_index == 0:
            self.graph.enableAutoRange()
            self.graph.disableAutoRange()

    def draw_graphs(self):
        self.curve.setData(numpy.arange(self._data.size), self._data, skipFiniteCheck = True)  
    def graph_reset(self):
        self.graph.clear()
        self.curve = self.graph.plot(numpy.arange(self._graph_max_size), self._data, pen = self.green_pen, skipFiniteCheck = True)
       