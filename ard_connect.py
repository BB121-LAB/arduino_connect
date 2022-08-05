#!/usr/bin/python3
VERSION = "v1.0.0"

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
import serial, time, pynput, sys
import serial.tools.list_ports
import images_qr

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(':/icon/icon.png'))

        # Button choices
        self.current_key = None
        self.button_choices = {
            "Spacebar"    : pynput.keyboard.Key.space,
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
        self.keysend = self.__kb_send
        self.change_key(0)
        self.setWindowTitle("Arduino Connect - " + VERSION) 
        
        # connect buttons to methods
        self.button_connect.clicked.connect(self.com_connect)
        self.button_refresh.clicked.connect(self.com_refresh)
        self.dropdown_key.currentIndexChanged.connect(self.change_key)
        self.button_run.clicked.connect(self.run)
        self.button_pause.clicked.connect(self.pause)
        
        # connection status
        self.ser = None
        self.com_port = ''
        
        # disable controls until connected
        self.frame_run_pause.setEnabled(False)
        
        # perform an initial port check
        self.com_refresh()
        
        # serial update timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.serial_update)
        self.timer.stop()
        
        # port update timer
        self.port_timer = QtCore.QTimer()
        self.port_timer.timeout.connect(self.com_refresh)
        self.port_timer.start(10000)
        
    def com_connect(self):
        if(self.ser == None):
            try:
                self.com_port = self.dropdown_port.currentText()
                self.ser = serial.Serial(self.com_port, 115200)
                self.button_connect.setText("Disconnect")
                self.dropdown_port.setEnabled(False)
                self.button_refresh.setEnabled(False)
                self.frame_run_pause.setEnabled(True)
                self.button_pause.setEnabled(False)
                self.button_run.setEnabled(True)
                self.port_timer.stop()
                self.status_update("Connected")
            except Exception as e:
                self.com_port = ''
                self.status_update("Connection Error")
                error_message = QtWidgets.QMessageBox()
                error_message.setWindowTitle("Connection Error")
                error_message.setText(str(e))
                error_message.exec_()  
                self.button_connect.setText("Connect")
                self.dropdown_port.setEnabled(True)
                self.button_refresh.setEnabled(True) 
                self.frame_run_pause.setEnabled(False)   
                self.port_timer.start(10000)
                self.com_refresh()     
        else:
            if(self.timer.isActive()):
                self.pause()
            self.ser.close()
            self.ser = None
            self.dropdown_port.setEnabled(True)
            self.button_refresh.setEnabled(True) 
            self.frame_run_pause.setEnabled(False)   
            self.port_timer.start(10000) 
            self.com_refresh()     
            self.status_update("Disconnected")    
            self.button_connect.setText("Connect")                            
    
    def change_key(self, i):
        key = list(self.button_choices.keys())[i]
        self.status_update("Key changed to " + key.lower())
        self.current_key = self.button_choices[key]
        if(key.find("Click") >= 0):
            self.keysend = self.__mouse_send
        else:
            self.keysend = self.__kb_send
       
    def com_refresh(self):
        self.dropdown_port.clear()
        self.available_ports = serial.tools.list_ports.comports()
        for i in self.available_ports:
            self.dropdown_port.addItem(i.device)  
        com_count = self.dropdown_port.count()
        if(com_count == 0):
            self.status_update("No ports found!")
            self.dropdown_port.setEnabled(False)
            self.button_connect.setEnabled(False)
            return
        self.status_update("Select port and click connect")
        self.dropdown_port.setEnabled(True)
        self.button_connect.setEnabled(True)
        for i in self.available_ports:
            if i.description.find('Arduino') == 0:
                self.com_port = i.device
                self.status_update("Arduino detected")
                index = self.dropdown_port.findText(self.com_port)
                self.dropdown_port.setCurrentIndex(index)
                break
    
    def status_update(self, string):
        self.status_line.setText(string)
        
    def serial_update(self):
        if(self.ser.in_waiting):
            i = self.ser.readline().decode('UTF-8').strip('\n')
            if i == 'T':
                self.keysend()
    
    def run(self):
        self.button_pause.setEnabled(True)
        self.button_run.setEnabled(False)
        self.dropdown_key.setEnabled(False)
        self.status_update("Running")
        self.timer.start(100)
    
    def pause(self):
        self.button_pause.setEnabled(False)
        self.button_run.setEnabled(True)
        self.dropdown_key.setEnabled(True)
        self.status_update("Paused")
        self.timer.stop()
    
    def __kb_send(self):
        self.kb.press(self.current_key)
        self.kb.release(self.current_key)
    
    def __mouse_send(self):
        self.mouse.press(self.current_key)
        self.mouse.release(self.current_key)
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec_()
