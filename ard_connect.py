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

VERSION = "v1.1.0-a.4"
LOG_LEVEL = logging.DEBUG


class ArdConnect(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(ArdConnect, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/icon/icon.png'))

        # Button choices
        self.current_key = None
        self.button_choices = {
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
        for i in self.button_choices.keys():
            self.dropdown_key.addItem(i)
        self.kb = pynput.keyboard.Controller()
        self.mouse = pynput.mouse.Controller()
        self.keysend = self._kb_send
        self.ui_change_key(0)
        self.setWindowTitle("Arduino Connect - " + VERSION) 
        
        # connect buttons to methods
        self.button_connect.clicked.connect(self.ui_com_connect)
        self.button_refresh.clicked.connect(self.ui_com_refresh)
        self.dropdown_key.currentIndexChanged.connect(self.ui_change_key)
        self.button_run.clicked.connect(self.ui_run)
        self.button_pause.clicked.connect(self.ui_pause)
        
        # connection status
        self.ser: serial.Serial = serial.Serial(baudrate = 115200, timeout = 1, write_timeout = 1)
        self.com_port = ''
        
        # disable controls until connected
        self.frame_run_pause_2.setEnabled(False)
        
        # perform an initial port check
        self.ui_com_refresh()
        
        # serial update timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.serial_update)
        self.timer.stop()
        
        # port update timer
        self.port_timer = QtCore.QTimer()
        self.port_timer.timeout.connect(self.ui_com_refresh)
        self.port_timer.start(10000)

        # graph timer
        self.graph_timer = QtCore.QTimer()
        self.graph_timer.timeout.connect(self.draw_graphs)
        self.graph_frame_rate = 30
        self.graph_timer_ms = int(1 / (self.graph_frame_rate / 1000))

        # graph properties
        self.graph.showGrid(True, True, alpha = 0.5)
        self.graph_padding_factor = 0.667
        self.green_pen = pg.mkPen('g', width = 2)

        # graph data
        self._graph_max_size = 250
        self._data_index = 0
        self._data = numpy.zeros(self._graph_max_size)
        
        # set curve
        self.graph_reset()
        self.graph.disableAutoRange()

        
    def ui_com_connect(self):
        if not self.ser.isOpen():
            try:
                self.ui_status_update("Connecting...")
                self.com_port = self.dropdown_port.currentText()
                self.ser = serial.Serial(self.com_port, 115200)
                self.button_connect.setText("Disconnect")
                self.dropdown_port.setEnabled(False)
                self.button_refresh.setEnabled(False)
                self.button_pause.setEnabled(False)
                self.button_run.setEnabled(True)
                self.port_timer.stop()
                self.radioButton_graph.setEnabled(False)
                self.ui_status_update("Connected")
                self.ser.flush()
                logging.info(f"Device connected: {self.com_port}")
                if self.radioButton_graph.isChecked():
                    self.graph_timer.start(self.graph_timer_ms)      
                else:
                    self.frame_run_pause_2.setEnabled(True)              
                connect_attempts = 3
                time.sleep(2)
                while True:
                    self.ser.flushInput()
                    print("Sending mode...")
                    if self.radioButton_graph.isChecked():
                        self.ser.write('$WAVE\n'.encode('UTF-8'))
                        self.ser.flushOutput()                  
                        time.sleep(1)
                    else:
                        self.ser.write('$NORMAL\n'.encode('UTF-8'))
                        self.ser.flushOutput()
                        time.sleep(1)
                    if self.ser.in_waiting:
                        response = self.ser.read_all().decode('UTF-8').strip('\r\n')
                        print(response)
                        if "INVALID" in response:
                            continue
                        break
                    connect_attempts -= 1
                    if connect_attempts <= 0:
                        print("Resetting serial device...")
                        self.ser.close()
                        self.ser = serial.Serial(self.com_port, 115200)
                        connect_attempts = 3
                        time.sleep(2)
                        continue
                if self.radioButton_graph.isChecked():
                    self.ui_run()
                    self.graph_zoom_frame.setEnabled(True)

            except Exception as e:
                self.com_port = ''
                logging.warning(f"Connection Error: {e}")
                self.ui_status_update("Connection Error")
                self.ui_display_error_message("Connection Error", f"{e}")
                self.button_connect.setText("Connect")
                self.dropdown_port.setEnabled(True)
                self.button_refresh.setEnabled(True) 
                self.frame_run_pause_2.setEnabled(False)   
                self.radioButton_graph.setEnabled(True)
                self.port_timer.start(10000)
                self.ui_com_refresh()     
        else:
            self.graph_timer.stop()
            if self.timer.isActive():
                self.ui_pause()
                self.graph_zoom_frame.setEnabled(False)
            self.ser.close()
            self.dropdown_port.setEnabled(True)
            self.button_refresh.setEnabled(True) 
            self.frame_run_pause_2.setEnabled(False)   
            self.radioButton_graph.setEnabled(True)
            self.port_timer.start(10000) 
            self.ui_com_refresh()     
            self.ui_status_update("Disconnected")    
            self.button_connect.setText("Connect")                            
    
    def ui_change_key(self, i):
        key = list(self.button_choices.keys())[i]
        self.ui_status_update("Key changed to " + key.lower())
        self.current_key = self.button_choices[key]
        if key.find("Click") >= 0:
            self.keysend = self._mouse_send
        else:
            self.keysend = self._kb_send
       
    def ui_com_refresh(self):
        self.dropdown_port.clear()
        self.available_ports = serial.tools.list_ports.comports()
        for i in self.available_ports:
            self.dropdown_port.addItem(i.device)  
        com_count = self.dropdown_port.count()
        if com_count == 0:
            self.ui_status_update("No ports found!")
            self.dropdown_port.setEnabled(False)
            self.button_connect.setEnabled(False)
            return
        self.ui_status_update("Select port and click connect")
        self.dropdown_port.setEnabled(True)
        self.button_connect.setEnabled(True)
        for i in self.available_ports:
            logging.debug(f"USB device detected: {i.device}")
            if i.description.find('Arduino') == 0:
                self.com_port = i.device
                self.ui_status_update("Arduino detected")
                index = self.dropdown_port.findText(self.com_port)
                self.dropdown_port.setCurrentIndex(index)
                break
            
    def ui_display_error_message(self, title: str, msg: str) -> None:
        """Display a generic error message to the user."""
        error_message = QtWidgets.QMessageBox()
        error_message.setWindowTitle(title)
        error_message.setText(str(msg))
        error_message.exec_()  
        
    def ui_status_update(self, string):
        #self.status_line.setText(string)
        self.statusBar.showMessage(string)
        
    def serial_update(self):
        try:
            if not self.radioButton_graph.isChecked():
                if self.ser.in_waiting:
                    i = self.ser.readline().decode('UTF-8').strip('\n')
                    if i == 'T':
                        self.keysend()
            else:
                self.ser.write('\n'.encode())

                # get response from Arduino, terminated by newline character
                buf = ''

                # read and discard incoming bytes until the start character is found
                while self.ser.inWaiting() > 0:
                    chr = str(self.ser.read().decode())
                    if chr == '$':
                        break

                # read characters until newline is detected, this is faster than serial's read_until
                while self.ser.inWaiting() > 0:
                    chr = str(self.ser.read().decode())
                    if chr == '\n':
                        break
                    buf = buf + chr
                if len(buf) != 3:
                    return
                current_reading = int(buf)
                self.add_data(current_reading)

        except OSError as e:
            logging.warning(e)
            self.ui_display_error_message("Device Disconnected", f"The USB device has been disconnected.\n{e}")
            self.ui_com_connect()

    def ui_run(self):
        self.button_pause.setEnabled(True)
        self.button_run.setEnabled(False)
        #self.dropdown_key.setEnabled(False)
        self.ui_status_update("Running")
        self.timer.start(25)
    
    def ui_pause(self):
        self.button_pause.setEnabled(False)
        self.button_run.setEnabled(True)
        #self.dropdown_key.setEnabled(True)
        self.ui_status_update("Paused")
        self.timer.stop()
    
    def _kb_send(self):
        self.kb.press(self.current_key)
        self.kb.release(self.current_key)
    
    def _mouse_send(self):
        self.mouse.press(self.current_key)
        self.mouse.release(self.current_key)

    def add_data(self, value):
        self._data[self._data_index] = value
        self._data_index = (self._data_index + 1) % self._graph_max_size
        if self._data_index == 0 and self.checkBox_auto_scale.isChecked():
            self.graph.enableAutoRange()
            self.graph.disableAutoRange()
    def draw_graphs(self):
        self.curve.setData(numpy.arange(self._data.size), self._data, skipFiniteCheck = True)  
    def graph_reset(self):
        self.graph.clear()
        self.curve = self.graph.plot(numpy.arange(self._graph_max_size), self._data, pen = self.green_pen, skipFiniteCheck = True)
       

if __name__ == "__main__":
    log_system.init_logging(LOG_LEVEL)
    app = QtWidgets.QApplication(sys.argv)
    window = ArdConnect()
    window.show()
    app.exec_()
