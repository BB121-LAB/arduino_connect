#!/usr/bin/python3

#       Arduino Connect
#   Written by Kevin Williams
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  


from PyQt5 import QtCore, QtGui, QtWidgets
from connect import Ui_MainWindow
import serial, pynput, sys
import serial.tools.list_ports
import logging
import time
import numpy
import pyqtgraph as pg
import pyqtgraph.exporters

try:
    # manual includes to fix occasional compile problem
    from pyqtgraph.graphicsItems.ViewBox.axisCtrlTemplate_pyqt5 import *
    from pyqtgraph.graphicsItems.PlotItem.plotConfigTemplate_pyqt5 import *
    from pyqtgraph.imageview.ImageViewTemplate_pyqt5 import *
    from pyqtgraph.console.template_pyqt5 import *
except:
    pass

# local includes
import images_qr
import log_system

VERSION = "v1.1.0-a.5"
LOG_LEVEL = logging.DEBUG

class ArdConnect(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(ArdConnect, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/icon/icon.png'))

        # Button choices
        self._current_key = None
        self._button_choices = {
            "Spacebar (default)"    : pynput.keyboard.Key.space,
            "Left Click"  : pynput.mouse.Button.left,
            "Right Click" : pynput.mouse.Button.right,
            "Arrow Up"    : pynput.keyboard.Key.up,
            "Arrow Down"  : pynput.keyboard.Key.down,
            "Arrow Left"  : pynput.keyboard.Key.left,
            "Arrow Right" : pynput.keyboard.Key.right,
            "W"           : 'w',
            "A"           : 'a',
            "S"           : 's',
            "D"           : 'd',
            }
        for i in self._button_choices.keys():
            self.dropdown_key.addItem(i)
        self._kb = pynput.keyboard.Controller()
        self._mouse = pynput.mouse.Controller()
        self._keysend = self._kb_send
        self._ui_change_key(0)
        self.setWindowTitle("Arduino Connect - " + VERSION) 
        
        # connect buttons to methods
        self.button_connect.clicked.connect(self._ui_com_connect)
        self.button_refresh.clicked.connect(self._ui_com_refresh)
        self.dropdown_key.currentIndexChanged.connect(self._ui_change_key)
        self.button_run.clicked.connect(self._ui_run)
        self.button_pause.clicked.connect(self._ui_pause)
        self.button_png_export.clicked.connect(self._ui_export_data_png)
        
        # connection status
        self._ser: serial.Serial = serial.Serial(baudrate = 115200, timeout = 1, write_timeout = 1)
        self._com_port = ''
        
        # disable controls until connected
        self.frame_run_pause_2.setEnabled(False)
        
        # perform an initial port check
        self._ui_com_refresh()
        
        # serial update timer
        self._capture_timer = QtCore.QTimer()
        self._capture_timer.timeout.connect(self._serial_update)
        self._capture_timer.stop()
        
        # port update timer
        self._port_timer = QtCore.QTimer()
        self._port_timer.timeout.connect(self._ui_com_refresh)
        self._port_timer.start(10000)

        # graph timer
        self._graph_timer = QtCore.QTimer()
        self._graph_timer.timeout.connect(self._draw_graphs)
        self._graph_frame_rate = 30
        self._graph_timer_ms = int(1 / (self._graph_frame_rate / 1000))

        # graph properties
        self._graph.showGrid(True, True, alpha = 0.5)
        self._graph_padding_factor = 0.667
        self._green_pen = pg.mkPen('g', width = 2)

        # graph data
        self._graph_max_size = 250
        self._data_index = 0
        self._data = numpy.zeros(self._graph_max_size)
        
        # set curve
        self._graph_reset()
        self._graph.disableAutoRange()

    def _ui_com_connect(self) -> None:
        """
        Called when the 'connect' button is pressed. This function is a bit
        complex: the program needs to connect to and then send a operation mode
        to the arduino. The process of connecting to the arduino is a bit finnicky,
        so it will automatically resend and reset the arduino if needed.
        """

        if not self._ser.isOpen():
            try:
                self._ui_status_update("Connecting...")
                self._com_port = self.dropdown_port.currentText()
                self._ser = serial.Serial(self._com_port, 115200)
                self.button_connect.setText("Disconnect")
                self.dropdown_port.setEnabled(False)
                self.button_refresh.setEnabled(False)
                self.button_pause.setEnabled(False)
                self.button_run.setEnabled(True)
                self._port_timer.stop()
                self.radioButton_graph.setEnabled(False)
                self._ui_status_update("Connected")
                self._ser.flush()
                logging.info(f"Device connected: {self._com_port}")
                if self.radioButton_graph.isChecked():
                    self._graph_timer.start(self._graph_timer_ms)      
                else:
                    self.frame_run_pause_2.setEnabled(True)              
                connect_attempts = 3
                time.sleep(2)
                while True:

                    # Begin attempting the connection to the arduino
                    # This normally takes several tries to work.
                    self._ser.flushInput()
                    print("Sending mode...")
                    if self.radioButton_graph.isChecked():
                        self._ser.write('$WAVE\n'.encode('UTF-8'))
                        self._ser.flushOutput()                  
                        time.sleep(1)
                    else:
                        self._ser.write('$NORMAL\n'.encode('UTF-8'))
                        self._ser.flushOutput()
                        time.sleep(1)
                    if self._ser.in_waiting:
                        response = self._ser.read_all().decode('UTF-8').strip('\r\n')
                        print(response)
                        if "INVALID" in response:
                            continue
                        break
                    connect_attempts -= 1
                    if connect_attempts <= 0:
                        print("Resetting serial device...")
                        self._ser.close()
                        self._ser = serial.Serial(self._com_port, 115200)
                        connect_attempts = 3
                        time.sleep(2)
                        continue
                if self.radioButton_graph.isChecked():
                    self._ui_run()
                    self.graph_zoom_frame.setEnabled(True)

            except Exception as e:
                self._com_port = ''
                logging.warning(f"Connection Error: {e}")
                self._ui_status_update("Connection Error")
                self._ui_display_error_message("Connection Error", f"{e}")
                self.button_connect.setText("Connect")
                self.dropdown_port.setEnabled(True)
                self.button_refresh.setEnabled(True) 
                self.frame_run_pause_2.setEnabled(False)   
                self.radioButton_graph.setEnabled(True)
                self._port_timer.start(10000)
                self._ui_com_refresh()     
        else:
            self._graph_timer.stop()
            if self._capture_timer.isActive():
                self._ui_pause()
                self.graph_zoom_frame.setEnabled(False)
            self._ser.close()
            self.dropdown_port.setEnabled(True)
            self.button_refresh.setEnabled(True) 
            self.frame_run_pause_2.setEnabled(False)   
            self.radioButton_graph.setEnabled(True)
            self._port_timer.start(10000) 
            self._ui_com_refresh()     
            self._ui_status_update("Disconnected")    
            self.button_connect.setText("Connect")

    def _ui_change_key(self, i: str) -> None:
        """When the dropdown choice has changed, update the key to output."""
        key = list(self._button_choices.keys())[i]
        self._ui_status_update("Key changed to " + key.lower())
        self._current_key = self._button_choices[key]
        if key.find("Click") >= 0:
            self._keysend = self._mouse_send
        else:
            self._keysend = self._kb_send

    def _ui_com_refresh(self) -> None:
        """
        Clear the dropdown menu, detect all serial ports, and populate
        the dropdown with the results. Unfortunately, Arduinos may
        or may not show the correct USB descriptor to the operating system.
        It will try to default to any USB descriptor named "Arduino," but
        it's 100% Arduino dependant whether this works or not. 
        """

        self.dropdown_port.clear()
        self.available_ports = serial.tools.list_ports.comports()
        for i in self.available_ports:
            self.dropdown_port.addItem(i.device)  
        com_count = self.dropdown_port.count()
        if com_count == 0:
            self._ui_status_update("No ports found!")
            self.dropdown_port.setEnabled(False)
            self.button_connect.setEnabled(False)
            return
        self._ui_status_update("Select port and click connect")
        self.dropdown_port.setEnabled(True)
        self.button_connect.setEnabled(True)
        for i in self.available_ports:
            logging.debug(f"USB device detected: {i.device}")
            if i.description.find('Arduino') == 0:
                self._com_port = i.device
                self._ui_status_update("Arduino detected")
                index = self.dropdown_port.findText(self._com_port)
                self.dropdown_port.setCurrentIndex(index)
                break

    def _ui_display_error_message(self, title: str, msg: str) -> None:
        """Display a generic error message to the user."""
        error_message = QtWidgets.QMessageBox()
        error_message.setWindowTitle(title)
        error_message.setText(str(msg))
        error_message.exec_()   

    def _ui_status_update(self, message: str) -> None:
        """Update status bar message."""
        self.statusBar.showMessage(message)

    def _serial_update(self) -> None:
        """
        Called via QTimer defined in __init__. 
        Polls the Arduino for an update depending on which
        mode the Arduino is running in.
        """

        try:
            # if in Key Mode, expect a single character input for a trigger
            if not self.radioButton_graph.isChecked():
                if self._ser.in_waiting:
                    i = self._ser.readline().decode('UTF-8').strip('\n')
                    if i == 'T':
                        self._keysend()

            # if in Graph Mode, expect a packet containing the current analog reading.
            # Packet format: $NNN\n
            #   Where $ is the start character
            #   NNN are three numbers ranging from 0-9
            #   \n as the packet terminator
            else:
                self._ser.write('\n'.encode())

                # get response from Arduino, terminated by newline character
                buf = ''

                # read and discard incoming bytes until the start character is found
                while self._ser.inWaiting() > 0:
                    chr = str(self._ser.read().decode())
                    if chr == '$':
                        break

                # read characters until newline is detected, this is faster than serial's read_until
                while self._ser.inWaiting() > 0:
                    chr = str(self._ser.read().decode())
                    if chr == '\n':
                        break
                    buf = buf + chr
                if len(buf) != 3:
                    return
                current_reading = int(buf)
                self._add_data(current_reading)
        except OSError as e:
            logging.warning(e)
            self._ui_display_error_message("Device Disconnected", f"The USB device has been disconnected.\n{e}")
            self._ui_com_connect()

    def _ui_run(self):
        """Starts capture mode."""
        self.button_pause.setEnabled(True)
        self.button_run.setEnabled(False)
        self._ui_status_update("Running")
        self._capture_timer.start(25)

    def _ui_pause(self):
        """Stops capture mode."""
        self.button_pause.setEnabled(False)
        self.button_run.setEnabled(True)
        self._ui_status_update("Paused")
        self._capture_timer.stop()

    def _kb_send(self):
        """Sends keycode on call"""
        self._kb.press(self._current_key)
        self._kb.release(self._current_key)

    def _mouse_send(self):
        """Sends mousepress on call"""
        self._mouse.press(self._current_key)
        self._mouse.release(self._current_key)

    def _add_data(self, value):
        """Adds data to the graphing dataset"""
        self._data[self._data_index] = value
        self._data_index = (self._data_index + 1) % self._graph_max_size
        if self._data_index == 0 and self.checkBox_auto_scale.isChecked():
            self._graph.enableAutoRange()
            self._graph.disableAutoRange()

    def _draw_graphs(self):
        """Called via QTimer, updates the graph curve data"""
        self._curve.setData(numpy.arange(self._data.size), self._data, skipFiniteCheck = True) 

    def _graph_reset(self):
        """Clear and redraw curve on graph."""
        self._graph.clear()
        self._curve = self._graph.plot(numpy.arange(self._graph_max_size), self._data, pen = self._green_pen, skipFiniteCheck = True)

    def _ui_export_data_png(self):
        """Exports a PNG file of the current graph data. Stops and resumes capture after running."""
        capture_running = self._capture_timer.isActive()
        self._ui_pause()
        default_filename = str(time.time()).split('.', maxsplit=1)[0] + '.png'
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", directory = default_filename)[0]
        if filename:
            try:
                QtCore.QCoreApplication.processEvents()
                exporter = pg.exporters.ImageExporter(self._graph.getPlotItem())
                exporter.export(filename)
            except Exception as e:
                self._ui_display_error_message("Export Error", e)
                logging.warn(e)
        if capture_running:
            self._ui_run()

if __name__ == "__main__":
    log_system.init_logging(LOG_LEVEL)
    app = QtWidgets.QApplication(sys.argv)
    window = ArdConnect()
    window.show()
    app.exec_()
