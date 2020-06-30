# -*- coding: utf-8 -*-
# Author：Tang XT
# Time: 2020/6/30/18:58
# File name：myQtGraph.py

import pyqtgraph as pg
import sys
from PyQt5.QtWidgets import QGridLayout, QWidget, QApplication
from queue import Queue
import threading
from PyQt5 import QtCore
import time

class MyQtGraph():

    def __init__(self, queue, mode):
        self.grid = QGridLayout()

        self.temperaturePlot = pg.PlotWidget(title="Temperature")
        self.forcePlot = pg.PlotWidget(title="Force")
        self.positionPlot = pg.PlotWidget(title="Position")
        self.versus = pg.PlotWidget(title="Versus")

        listtemp = [self.temperaturePlot, self.forcePlot, self.positionPlot]
        for each in listtemp:
            each.showGrid(x=True, y=True)
            each.setLabel('bottom', "Time", units='s')
        del(listtemp)
        self.temp_curve_1 = self.temperaturePlot.plot()
        self.force_curve_1 = self.forcePlot.plot()
        self.pos_curve_1 = self.positionPlot.plot()
        self.versue_curve_1 = self.versus.plot()

        self.flag = 0
        self.queue = queue
        self.mode = mode

        self.time_list = []
        self.temperature_list = []
        self.force_list = []
        self.position_list = []
        self.data = [self.time_list,self.temperature_list,self.force_list,self.position_list]
        self.half_line = ""

        self.grid.addWidget(self.temperaturePlot,0,0)
        self.grid.addWidget(self.forcePlot, 0, 1)
        self.grid.addWidget(self.positionPlot,1,0)
        self.grid.addWidget(self.versus, 1, 1)

        self.time = QtCore.QTimer()
        self.time.setInterval(100)
        self.time.timeout.connect(self.update)

    def decode(self):
        new_text = ""
        full_line = ""
        while not (self.queue.empty()):
            new_text += self.queue.get()  # queue中的新文本读进来
        new_text = self.half_line + new_text  # 跟之前剩下的半行合并


        lines = new_text.split("\r\n")[:-1]  # 整个文本分割成行
        self.half_line = new_text.split("\r\n")[-1]


        for each in lines:

            data = each.split(",")  # 每行文本用逗号分割
            self.time_list.append(float(data[0]))
            self.temperature_list.append(float(data[1]))
            self.force_list.append(float(data[2]))
            self.position_list.append(float(data[3]))
    # ===================================

    def update(self):
        print("****")
        print(self.time_list)
        print("***")
        self.decode()
        self.temp_curve_1.setData(self.time_list,self.temperature_list)
        self.force_curve_1.setData(self.time_list,self.force_list)
        self.pos_curve_1.setData(self.time_list,self.position_list)
        self.versue_curve_1.setData(self.temperature_list,self.position_list)
    #=========================



    def start_plot(self):
        self.time.start()
    #=================
    def stop_plot(self):
        self.time.stop()
    #==========

    def clear(self):
        for each in self.data:
            each = []
    #=========================
#=======================

if __name__ == "__main__":

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    queue1 = Queue()
    app = QApplication(sys.argv)
    testwindow = QWidget()
    testgraph = MyQtGraph(queue1,1)
    testwindow.setLayout(testgraph.grid)
    testwindow.show()
    #testgraph.start_plot()
    count = 0
    testgraph.start_plot()


    def gen():
        count = 0
        while 1:
            count+=1
            text = "{0},{1},{2},{3},{4}\r\n".format(count,2*count,3*count,4*count,5*count)
            queue1.put(text)
            time.sleep(0.1)
            print(text)

    thread1 = threading.Thread(target = gen)
    thread1.start()








    sys.exit(app.exec_())

