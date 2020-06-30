# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'motorui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 785)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_graph = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_graph.setGeometry(QtCore.QRect(360, 50, 791, 531))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_graph.sizePolicy().hasHeightForWidth())
        self.groupBox_graph.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_graph.setFont(font)
        self.groupBox_graph.setObjectName("groupBox_graph")
        self.tabWid = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWid.setGeometry(QtCore.QRect(50, 60, 291, 521))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.tabWid.setFont(font)
        self.tabWid.setObjectName("tabWid")
        self.tab_Serial = QtWidgets.QWidget()
        self.tab_Serial.setObjectName("tab_Serial")
        self.baund_rate = QtWidgets.QComboBox(self.tab_Serial)
        self.baund_rate.setGeometry(QtCore.QRect(10, 50, 180, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baund_rate.sizePolicy().hasHeightForWidth())
        self.baund_rate.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.baund_rate.setFont(font)
        self.baund_rate.setObjectName("baund_rate")
        self.baund_rate.addItem("")
        self.baund_rate.addItem("")
        self.baund_rate.addItem("")
        self.baund_rate.addItem("")
        self.baund_rate.addItem("")
        self.open_serial = QtWidgets.QPushButton(self.tab_Serial)
        self.open_serial.setGeometry(QtCore.QRect(200, 10, 75, 75))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_serial.sizePolicy().hasHeightForWidth())
        self.open_serial.setSizePolicy(sizePolicy)
        self.open_serial.setMinimumSize(QtCore.QSize(56, 56))
        self.open_serial.setMaximumSize(QtCore.QSize(100, 201))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.open_serial.setFont(font)
        self.open_serial.setObjectName("open_serial")
        self.port_select = QtWidgets.QComboBox(self.tab_Serial)
        self.port_select.setGeometry(QtCore.QRect(10, 10, 180, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.port_select.sizePolicy().hasHeightForWidth())
        self.port_select.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.port_select.setFont(font)
        self.port_select.setObjectName("port_select")
        self.textBrowser_RecText = QtWidgets.QTextBrowser(self.tab_Serial)
        self.textBrowser_RecText.setGeometry(QtCore.QRect(10, 130, 261, 331))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowser_RecText.setFont(font)
        self.textBrowser_RecText.setObjectName("textBrowser_RecText")
        self.textBrowser_SentText = QtWidgets.QTextBrowser(self.tab_Serial)
        self.textBrowser_SentText.setGeometry(QtCore.QRect(10, 90, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowser_SentText.setFont(font)
        self.textBrowser_SentText.setObjectName("textBrowser_SentText")
        self.tabWid.addTab(self.tab_Serial, "")
        self.tab_Ctrl = QtWidgets.QWidget()
        self.tab_Ctrl.setObjectName("tab_Ctrl")
        self.lineEdit_F_SetPoint = QtWidgets.QLineEdit(self.tab_Ctrl)
        self.lineEdit_F_SetPoint.setGeometry(QtCore.QRect(130, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_F_SetPoint.setFont(font)
        self.lineEdit_F_SetPoint.setText("")
        self.lineEdit_F_SetPoint.setObjectName("lineEdit_F_SetPoint")
        self.label_Temperature = QtWidgets.QLabel(self.tab_Ctrl)
        self.label_Temperature.setGeometry(QtCore.QRect(0, 190, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_Temperature.setFont(font)
        self.label_Temperature.setObjectName("label_Temperature")
        self.label_Force = QtWidgets.QLabel(self.tab_Ctrl)
        self.label_Force.setGeometry(QtCore.QRect(30, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_Force.setFont(font)
        self.label_Force.setObjectName("label_Force")
        self.lineEdit_T_SetPoint = QtWidgets.QLineEdit(self.tab_Ctrl)
        self.lineEdit_T_SetPoint.setGeometry(QtCore.QRect(130, 190, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_T_SetPoint.setFont(font)
        self.lineEdit_T_SetPoint.setText("")
        self.lineEdit_T_SetPoint.setObjectName("lineEdit_T_SetPoint")
        self.label_Mode = QtWidgets.QLabel(self.tab_Ctrl)
        self.label_Mode.setGeometry(QtCore.QRect(10, 10, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_Mode.setFont(font)
        self.label_Mode.setObjectName("label_Mode")
        self.label_Position = QtWidgets.QLabel(self.tab_Ctrl)
        self.label_Position.setGeometry(QtCore.QRect(20, 140, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_Position.setFont(font)
        self.label_Position.setObjectName("label_Position")
        self.lineEdit_P_SetPoint = QtWidgets.QLineEdit(self.tab_Ctrl)
        self.lineEdit_P_SetPoint.setGeometry(QtCore.QRect(130, 140, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_P_SetPoint.setFont(font)
        self.lineEdit_P_SetPoint.setText("")
        self.lineEdit_P_SetPoint.setObjectName("lineEdit_P_SetPoint")
        self.mode_select = QtWidgets.QComboBox(self.tab_Ctrl)
        self.mode_select.setGeometry(QtCore.QRect(10, 30, 101, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mode_select.sizePolicy().hasHeightForWidth())
        self.mode_select.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.mode_select.setFont(font)
        self.mode_select.setObjectName("mode_select")
        self.mode_select.addItem("")
        self.mode_select.addItem("")
        self.mode_select.addItem("")
        self.lineEdit_SamplePeriod = QtWidgets.QLineEdit(self.tab_Ctrl)
        self.lineEdit_SamplePeriod.setGeometry(QtCore.QRect(130, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_SamplePeriod.setFont(font)
        self.lineEdit_SamplePeriod.setText("")
        self.lineEdit_SamplePeriod.setObjectName("lineEdit_SamplePeriod")
        self.label_Speriod = QtWidgets.QLabel(self.tab_Ctrl)
        self.label_Speriod.setGeometry(QtCore.QRect(130, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_Speriod.setFont(font)
        self.label_Speriod.setObjectName("label_Speriod")
        self.StartSample = QtWidgets.QPushButton(self.tab_Ctrl)
        self.StartSample.setGeometry(QtCore.QRect(10, 240, 120, 56))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartSample.sizePolicy().hasHeightForWidth())
        self.StartSample.setSizePolicy(sizePolicy)
        self.StartSample.setMinimumSize(QtCore.QSize(56, 56))
        self.StartSample.setMaximumSize(QtCore.QSize(120, 201))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.StartSample.setFont(font)
        self.StartSample.setObjectName("StartSample")
        self.CtrlStart = QtWidgets.QPushButton(self.tab_Ctrl)
        self.CtrlStart.setGeometry(QtCore.QRect(150, 240, 120, 56))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CtrlStart.sizePolicy().hasHeightForWidth())
        self.CtrlStart.setSizePolicy(sizePolicy)
        self.CtrlStart.setMinimumSize(QtCore.QSize(56, 56))
        self.CtrlStart.setMaximumSize(QtCore.QSize(120, 201))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.CtrlStart.setFont(font)
        self.CtrlStart.setObjectName("CtrlStart")
        self.Clear = QtWidgets.QPushButton(self.tab_Ctrl)
        self.Clear.setGeometry(QtCore.QRect(10, 310, 120, 56))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Clear.sizePolicy().hasHeightForWidth())
        self.Clear.setSizePolicy(sizePolicy)
        self.Clear.setMinimumSize(QtCore.QSize(56, 56))
        self.Clear.setMaximumSize(QtCore.QSize(120, 201))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Clear.setFont(font)
        self.Clear.setObjectName("Clear")
        self.Send = QtWidgets.QPushButton(self.tab_Ctrl)
        self.Send.setGeometry(QtCore.QRect(150, 310, 120, 56))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Send.sizePolicy().hasHeightForWidth())
        self.Send.setSizePolicy(sizePolicy)
        self.Send.setMinimumSize(QtCore.QSize(56, 56))
        self.Send.setMaximumSize(QtCore.QSize(120, 201))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Send.setFont(font)
        self.Send.setObjectName("Send")
        self.Save = QtWidgets.QPushButton(self.tab_Ctrl)
        self.Save.setGeometry(QtCore.QRect(10, 380, 261, 56))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Save.sizePolicy().hasHeightForWidth())
        self.Save.setSizePolicy(sizePolicy)
        self.Save.setMinimumSize(QtCore.QSize(56, 56))
        self.Save.setMaximumSize(QtCore.QSize(300, 201))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.Save.setFont(font)
        self.Save.setObjectName("Save")
        self.tabWid.addTab(self.tab_Ctrl, "")
        self.tab_para = QtWidgets.QWidget()
        self.tab_para.setObjectName("tab_para")
        self.groupBox_Tpid = QtWidgets.QGroupBox(self.tab_para)
        self.groupBox_Tpid.setGeometry(QtCore.QRect(30, 10, 231, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupBox_Tpid.setFont(font)
        self.groupBox_Tpid.setObjectName("groupBox_Tpid")
        self.lineEdit_T_Kp = QtWidgets.QLineEdit(self.groupBox_Tpid)
        self.lineEdit_T_Kp.setGeometry(QtCore.QRect(60, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_T_Kp.setFont(font)
        self.lineEdit_T_Kp.setText("")
        self.lineEdit_T_Kp.setObjectName("lineEdit_T_Kp")
        self.lineEdit_T_Ti = QtWidgets.QLineEdit(self.groupBox_Tpid)
        self.lineEdit_T_Ti.setGeometry(QtCore.QRect(60, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_T_Ti.setFont(font)
        self.lineEdit_T_Ti.setText("")
        self.lineEdit_T_Ti.setObjectName("lineEdit_T_Ti")
        self.label_T_Ti = QtWidgets.QLabel(self.groupBox_Tpid)
        self.label_T_Ti.setGeometry(QtCore.QRect(20, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_T_Ti.setFont(font)
        self.label_T_Ti.setObjectName("label_T_Ti")
        self.lineEdit_T_Td = QtWidgets.QLineEdit(self.groupBox_Tpid)
        self.lineEdit_T_Td.setGeometry(QtCore.QRect(60, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_T_Td.setFont(font)
        self.lineEdit_T_Td.setText("")
        self.lineEdit_T_Td.setObjectName("lineEdit_T_Td")
        self.label_T_Td = QtWidgets.QLabel(self.groupBox_Tpid)
        self.label_T_Td.setGeometry(QtCore.QRect(20, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_T_Td.setFont(font)
        self.label_T_Td.setObjectName("label_T_Td")
        self.label_T_Kp = QtWidgets.QLabel(self.groupBox_Tpid)
        self.label_T_Kp.setGeometry(QtCore.QRect(20, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_T_Kp.setFont(font)
        self.label_T_Kp.setObjectName("label_T_Kp")
        self.groupBox_F_PID = QtWidgets.QGroupBox(self.tab_para)
        self.groupBox_F_PID.setGeometry(QtCore.QRect(30, 170, 231, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupBox_F_PID.setFont(font)
        self.groupBox_F_PID.setObjectName("groupBox_F_PID")
        self.lineEdit_F_Kp = QtWidgets.QLineEdit(self.groupBox_F_PID)
        self.lineEdit_F_Kp.setGeometry(QtCore.QRect(60, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_F_Kp.setFont(font)
        self.lineEdit_F_Kp.setText("")
        self.lineEdit_F_Kp.setObjectName("lineEdit_F_Kp")
        self.lineEdit_F_Ti = QtWidgets.QLineEdit(self.groupBox_F_PID)
        self.lineEdit_F_Ti.setGeometry(QtCore.QRect(60, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_F_Ti.setFont(font)
        self.lineEdit_F_Ti.setText("")
        self.lineEdit_F_Ti.setObjectName("lineEdit_F_Ti")
        self.label_F_Ti = QtWidgets.QLabel(self.groupBox_F_PID)
        self.label_F_Ti.setGeometry(QtCore.QRect(20, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_F_Ti.setFont(font)
        self.label_F_Ti.setObjectName("label_F_Ti")
        self.lineEdit_F_Td = QtWidgets.QLineEdit(self.groupBox_F_PID)
        self.lineEdit_F_Td.setGeometry(QtCore.QRect(60, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_F_Td.setFont(font)
        self.lineEdit_F_Td.setText("")
        self.lineEdit_F_Td.setObjectName("lineEdit_F_Td")
        self.label_F_Td = QtWidgets.QLabel(self.groupBox_F_PID)
        self.label_F_Td.setGeometry(QtCore.QRect(20, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_F_Td.setFont(font)
        self.label_F_Td.setObjectName("label_F_Td")
        self.label_F_Kp = QtWidgets.QLabel(self.groupBox_F_PID)
        self.label_F_Kp.setGeometry(QtCore.QRect(20, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_F_Kp.setFont(font)
        self.label_F_Kp.setObjectName("label_F_Kp")
        self.groupBox_P_PID = QtWidgets.QGroupBox(self.tab_para)
        self.groupBox_P_PID.setGeometry(QtCore.QRect(30, 330, 231, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupBox_P_PID.setFont(font)
        self.groupBox_P_PID.setObjectName("groupBox_P_PID")
        self.lineEdit_P_Kp = QtWidgets.QLineEdit(self.groupBox_P_PID)
        self.lineEdit_P_Kp.setGeometry(QtCore.QRect(60, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_P_Kp.setFont(font)
        self.lineEdit_P_Kp.setText("")
        self.lineEdit_P_Kp.setObjectName("lineEdit_P_Kp")
        self.lineEdit_P_Ti = QtWidgets.QLineEdit(self.groupBox_P_PID)
        self.lineEdit_P_Ti.setGeometry(QtCore.QRect(60, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_P_Ti.setFont(font)
        self.lineEdit_P_Ti.setText("")
        self.lineEdit_P_Ti.setObjectName("lineEdit_P_Ti")
        self.label_P_Ti = QtWidgets.QLabel(self.groupBox_P_PID)
        self.label_P_Ti.setGeometry(QtCore.QRect(20, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_P_Ti.setFont(font)
        self.label_P_Ti.setObjectName("label_P_Ti")
        self.lineEdit_P_Td = QtWidgets.QLineEdit(self.groupBox_P_PID)
        self.lineEdit_P_Td.setGeometry(QtCore.QRect(60, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lineEdit_P_Td.setFont(font)
        self.lineEdit_P_Td.setText("")
        self.lineEdit_P_Td.setObjectName("lineEdit_P_Td")
        self.label_P_Td = QtWidgets.QLabel(self.groupBox_P_PID)
        self.label_P_Td.setGeometry(QtCore.QRect(20, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_P_Td.setFont(font)
        self.label_P_Td.setObjectName("label_P_Td")
        self.label_P_Kp = QtWidgets.QLabel(self.groupBox_P_PID)
        self.label_P_Kp.setGeometry(QtCore.QRect(20, 30, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_P_Kp.setFont(font)
        self.label_P_Kp.setObjectName("label_P_Kp")
        self.tabWid.addTab(self.tab_para, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWid.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_graph.setTitle(_translate("MainWindow", "Graph"))
        self.tabWid.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>s</p></body></html>"))
        self.baund_rate.setItemText(0, _translate("MainWindow", "1382400"))
        self.baund_rate.setItemText(1, _translate("MainWindow", "115200"))
        self.baund_rate.setItemText(2, _translate("MainWindow", "38400"))
        self.baund_rate.setItemText(3, _translate("MainWindow", "19200"))
        self.baund_rate.setItemText(4, _translate("MainWindow", "9600"))
        self.open_serial.setText(_translate("MainWindow", "打开\n"
"串口"))
        self.tabWid.setTabText(self.tabWid.indexOf(self.tab_Serial), _translate("MainWindow", "串口"))
        self.label_Temperature.setText(_translate("MainWindow", "Temperature"))
        self.label_Force.setText(_translate("MainWindow", "Force"))
        self.label_Mode.setText(_translate("MainWindow", "Mode"))
        self.label_Position.setText(_translate("MainWindow", "Position"))
        self.mode_select.setItemText(0, _translate("MainWindow", "等温"))
        self.mode_select.setItemText(1, _translate("MainWindow", "等张"))
        self.mode_select.setItemText(2, _translate("MainWindow", "恒定位置"))
        self.label_Speriod.setText(_translate("MainWindow", "Sample Period"))
        self.StartSample.setText(_translate("MainWindow", "Start"))
        self.CtrlStart.setText(_translate("MainWindow", "Ctrl"))
        self.Clear.setText(_translate("MainWindow", "Clear"))
        self.Send.setText(_translate("MainWindow", "Send"))
        self.Save.setText(_translate("MainWindow", "Save"))
        self.tabWid.setTabText(self.tabWid.indexOf(self.tab_Ctrl), _translate("MainWindow", "控制"))
        self.groupBox_Tpid.setTitle(_translate("MainWindow", "Temperature PID"))
        self.label_T_Ti.setText(_translate("MainWindow", "Ti"))
        self.label_T_Td.setText(_translate("MainWindow", "Td"))
        self.label_T_Kp.setText(_translate("MainWindow", "Kp"))
        self.groupBox_F_PID.setTitle(_translate("MainWindow", "Force PID"))
        self.label_F_Ti.setText(_translate("MainWindow", "Ti"))
        self.label_F_Td.setText(_translate("MainWindow", "Td"))
        self.label_F_Kp.setText(_translate("MainWindow", "Kp"))
        self.groupBox_P_PID.setTitle(_translate("MainWindow", "Position PID"))
        self.label_P_Ti.setText(_translate("MainWindow", "Ti"))
        self.label_P_Td.setText(_translate("MainWindow", "Td"))
        self.label_P_Kp.setText(_translate("MainWindow", "Kp"))
        self.tabWid.setTabText(self.tabWid.indexOf(self.tab_para), _translate("MainWindow", "参数"))
