# Created by Qiucheng Su on 2021
# Revised by Hao Jin on 2022/04/08

from ast import Global
import os
import sys
import math
import time
import datetime
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import serial
import serial.tools.list_ports
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QProgressBar,
    QFileDialog
)
import pyqtgraph as pg
from saw_single_ui import Ui_MainWindow

# import serial_comm as comm

# for pyinstaller to include local assets
basedir = os.path.dirname(__file__)

# ONLY used for initializing config json file, if it does not exist
# should modify these values in .json file once it is created
init_dict = {
    "start_freq": 428,
    "stop_freq": 429,
    "threshold": 14000,
    "thresholdRange": 3000,
    "freqRange": 0.5,
    "intercept": 2281472.055,
    "slope_1": -1.07016075e-02,
    "slope_2": 1.25492074e-11,
}
json_file = "config.json"
try:
    with open(json_file) as f_obj:
        json_dict = json.load(f_obj)
except FileNotFoundError:
    with open(json_file, 'w') as f_obj:
        json.dump(init_dict, f_obj, indent=4)
        json_dict = init_dict
    print("\nConfiguration file not found! \nInitialized with initial values.")

# 创建数据文件夹
if not os.path.exists("data"):
    os.mkdir("data")

time_stamp = str(datetime.date.today())+"-"+str(time.strftime("%H-%M-%S"))

# 创建连续测试数据保存文件，每次打开app都新建一个，以防文件size过大
with open("data/auto-" + time_stamp + ".csv","w") as f:
    f.write("time, freq, temperature\n")
# 创建单次测试数据保存文件，每次打开app都新建一个，以防文件size过大
with open("data/manual-"+ time_stamp + ".csv","w") as f:
    f.write("time, freq, temperature\n")

# “频率--温度” 拟合初始参数
# temp = intercept + slope_1*freq + slope_2*freq**2
intercept = json_dict["intercept"]
slope_1 = json_dict["slope_1"]
slope_2 = json_dict["slope_2"]

# start and stop frequency
startFreq = json_dict["start_freq"]
endFreq = json_dict["stop_freq"]

# RSSI 阈值，峰值超过该阈值才有效
threshold = json_dict["threshold"]

# 阈值范围，从峰值RSSI往下取该阈值范围的数据点作曲线拟合
thresholdRange = json_dict["thresholdRange"]

# 扫频跟随谐振频率变化的范围，span
freqRange = json_dict["freqRange"]

# # 最大数据点
# number_of_plot = json_dict["number_of_plot"]

# 步进是0.01MHz，如果是其他的阅读器需要更改这个代码
stepFreq = 0.01

# 表示第一个接收的数是起始频率
flag = False  

# 接收的数据
receiveData = {}

# 当前频率
freq = 0

# 当前的温度
currentTemperature = 0

#工作的谐振频率都存在这里
freqList = []

# 工作的谐振频率和温度存在这里，key为时间，value为谐振频率和温度
dicTimeAndTAndF = {}

# 工作的温度都存在这里
temperatureList = []

# 画图时候的最小温度和最大温度值
minTemperature= 0
maxTemperature=100

# 温度的校准值
calibration = 0

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 测试flag，测试中为1，未测试为0
        self.measureFlag = 0

        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))

        # sweep mode: 
        # 0 - 初始化扫描
        # 1 - 连续扫描
        self.sweepMode = 0

        # 初始化设置编辑框
        self.textEditStartFreq.setText(str(startFreq))
        self.textEditEndFreq.setText(str(endFreq))
        self.textEditEndFreq_2.setText(str(threshold))  # rssi 阈值
        self.rssiThreshold_2.setText(str(thresholdRange))  # rssi 阈值范围 
        self.freqChange.setText(str(freqRange))  # freq span
        self.intercept_a.setText(f"{intercept:.4e}")
        self.slope_1_a.setText(f"{slope_1:.4e}")
        self.slope_2_a.setText(f"{slope_2:.4e}")
        self.save2FileRealTime.setChecked(True)
        self.hex_send.setChecked(True)
        # self.spinBox.setValue(number_of_plot)
        # self.spinBox.setMaximum(number_of_plot*2)

        # 使用pyqtgraph画图，将图绑定在这个组件上
        self.plot = pg.PlotWidget(enableAutoRange=True)
        self.plotDataViewVerticalLayout.addWidget(self.plot)
        # 如果重新设置了起始频率和终止频率，这个也要更新
        # self.plot.setYRange(startFreq, endFreq)
        self.plot.setYRange(minTemperature, maxTemperature)
        self.plot.setTitle("实时温度曲线")
        self.curve = self.plot.plot()
        
        # for pyinstaller
        self.label.setPixmap(QtGui.QPixmap(os.path.join(basedir, "logo_343x60.png"))) 

        # status bar
        self.statusBar().showMessage('Ready')

        self.setWindowTitle("无源无线温度传感器系统 v.2022.4.3")
        self.ser = serial.Serial()

        # 初始化按钮使能
        self.open_button.setEnabled(False)
        self.close_button.setEnabled(False)
        self.testButton.setEnabled(False)
        self.monitorButton.setEnabled(False)
        self.stopMonitorButton.setEnabled(False)

        # 串口检测按钮
        self.s1__box_1.clicked.connect(self.port_check)

        # 串口信息显示
        self.s1__box_2.currentTextChanged.connect(self.port_imf)

        # 打开串口按钮
        self.open_button.clicked.connect(self.port_open)

        # 关闭串口按钮
        self.close_button.clicked.connect(self.port_close)

        # 发送数据按钮
        self.s3__send_button.clicked.connect(self.data_send)

        # 定时发送数据
        self.timer_send = QTimer()
        self.timer_send.timeout.connect(self.data_send)
        self.timer_send_cb.stateChanged.connect(self.data_send_timer)

        # 定时接收数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.data_receive)

        # 清除发送窗口
        self.s3__clear_button.clicked.connect(self.send_data_clear)

        # 清除接收窗口
        self.s2__clear_button.clicked.connect(self.receive_data_clear)

        # 设置起始频率和终止频率
        self.sendFreqButton.clicked.connect(self.set_freq)

        # 初始化扫描
        self.testButton.clicked.connect(self.start_process_mode_0)

        # 连续监测
        self.monitorButton.clicked.connect(self.start_process_mode_1)
        self.stopMonitorButton.clicked.connect(self.stop_monitor)

        # debug button
        self.debugButton.clicked.connect(self.start_process_mode_0)

        # 模型参数写入
        self.pushButton_a.clicked.connect(self.writeModelParameters_a)
        self.pushButton_b.clicked.connect(self.writeModelParameters_b)

        # 定时器刷新数据
        self.plotData = QTimer(self)
        self.plotData.timeout.connect(self.plotDataView)
        self.plotData.start(100)

        # 设置span范围
        self.sendFreqRangeButton.clicked.connect(self.set_freq_range)

        # # 设置校准值
        # self.sendCalibration.clicked.connect(self.buttonCalibration)

        # # 将温度和谐振频率保存为文件
        self.saveTempAndFreq.clicked.connect(self.saveTAndFToFile)
        # self.selectFileButton.clicked.connect(self.selectSavedFile)

        # 简易模型拟合
        self.evalModelButton.clicked.connect(self.simpleFitting)

        # # 最大数据点
        # self.spinBox.valueChanged.connect(self.spinValueChange)


    # 串口检测
    def port_check(self):
        # 检测所有存在的串口，将信息存储在字典中
        self.Com_Dict = {}
        port_list = list(serial.tools.list_ports.comports())
        # print(port_list)
        self.s1__box_2.clear()
        for port in port_list:
            print(port)
            self.Com_Dict["%s" % port[0]] = "%s" % port[1]
            self.s1__box_2.addItem(port[0])
        if len(self.Com_Dict) == 0:
            self.state_label.setText("未发现串口")

    # 串口信息
    def port_imf(self):
        # 显示选定的串口的详细信息
        imf_s = self.s1__box_2.currentText()
        if imf_s != "":
            self.state_label.setText(self.Com_Dict[self.s1__box_2.currentText()])
            self.open_button.setEnabled(True)
    
    # 打开串口
    def port_open(self):
        self.ser.port = self.s1__box_2.currentText()
        self.ser.baudrate = int(self.s1__box_3.currentText())
        self.ser.bytesize = int(self.s1__box_4.currentText())
        self.ser.stopbits = int(self.s1__box_6.currentText())
        self.ser.parity = self.s1__box_5.currentText()

        try:
            self.ser.open()
        except:
            QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
            return None

        # 打开串口接收定时器，周期为2ms， 115200波特率传输每Byte的时间约87us
        self.timer.start(2)

        if self.ser.isOpen():
            self.open_button.setEnabled(False)
            self.close_button.setEnabled(True)
            # self.formGroupBox1.setTitle("串口状态（已开启）")
            self.statusbar.showMessage(f"Connected to {self.state_label.text()}")
            self.testButton.setEnabled(True)

            self.set_freq_1(startFreq, endFreq)

    # 关闭串口
    def port_close(self):
        global flag
        flag = False
        self.timer.stop()
        self.timer_send.stop()
        try:
            self.ser.close()
        except:
            pass
        self.open_button.setEnabled(True)
        self.close_button.setEnabled(False)
        self.lineEdit_3.setEnabled(True)
        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))
        # self.formGroupBox1.setTitle("串口状态（已关闭）")
        self.statusbar.showMessage(f"Disconnected from {self.state_label.text()}")
        self.testButton.setEnabled(False)

    # 设置扫频范围
    def set_freq_1(self, start, end):
        global startFreq, endFreq, flag
        flag = False
        startFreq = start
        startFreq = round(startFreq, 2)
        endFreq = end
        endFreq = round(endFreq, 2)
        print(f"set start freq: {startFreq}")
        print(f"set stop freq: {endFreq}")
        self.textEditStartFreq.setText(str(startFreq))
        self.textEditEndFreq.setText(str(endFreq))

        # self.data_send_string("AA 07 00", True)

        s = "AA 05 " + hex(int(startFreq * 100))[2:4].upper() + " " + hex(int(startFreq * 100))[
                                                                  4:6].upper() + " " + hex(int(endFreq * 100))[
                                                                                       2:4].upper() + " " + hex(
            int(endFreq * 100))[4:6].upper() + " 01"
        self.data_send_string(s, True)
        # self.plot.setYRange(start, end)
        # self.curve = self.plot.plot()
    
    # 设置扫频及阈值范围
    def set_freq(self):
        global threshold, thresholdRange
        self.set_freq_1(round(float(self.textEditStartFreq.text()), 2), round(float(self.textEditEndFreq.text()), 2))
 
        # threshold parameters are not writen to MCU
        threshold = int(self.textEditEndFreq_2.text())
        thresholdRange = int(self.rssiThreshold_2.text())
 

    # 发送数据,s表示发送的数据，isHexSend表示是否按照十六进制发送
    def data_send_string(self, s, isHexSend):
        if self.ser.isOpen():
            input_s = s
            print(input_s)
            if input_s != "":
                # 非空字符串
                if isHexSend:
                    # hex发送
                    input_s = input_s.strip()
                    send_list = []
                    while input_s != '':
                        try:
                            num = int(input_s[0:2], 16)
                        except ValueError:
                            QMessageBox.critical(self, 'wrong data', '请输入十六进制数据，以空格分开!')
                            return None
                        input_s = input_s[2:].strip()
                        send_list.append(num)
                    input_s = bytes(send_list)
                else:
                    # ascii发送
                    input_s = (input_s + '\r\n').encode('utf-8')

                print(input_s)
                num = self.ser.write(input_s)
                self.data_num_sended += num
                self.lineEdit_2.setText(str(self.data_num_sended))
        else:
            pass

    # 发送数据
    def data_send(self):
        input_s = self.s3__send_text.toPlainText()
        self.data_send_string(input_s, self.hex_send.isChecked())


    # 定时发送数据
    def data_send_timer(self):
        if self.timer_send_cb.isChecked():
            self.timer_send.start(int(self.lineEdit_3.text()))
            self.lineEdit_3.setEnabled(False)
        else:
            self.timer_send.stop()
            self.lineEdit_3.setEnabled(True)
    
    # 初始化扫描
    def start_process_mode_0(self):
        self.timer.stop()
        self.timer.start(2)
        self.sweepMode = 0
        self.start_process()

    # 连续扫描
    def start_process_mode_1(self):
        global freqRange
        self.timer.stop()
        self.sweepMode = 1
        self.checkBox.setChecked(True)  # 频率跟随
        self.freqChange.setText(str(0.5))  # 连续扫描时，span自动设为0.5MHz
        freqRange = 0.5
        self.timer.start(2)
        self.start_process()
        self.monitorButton.setEnabled(False)
        self.stopMonitorButton.setEnabled(True)
    
    def stop_monitor(self):
        self.timer.stop()
        self.sweepMode = 0
        self.monitorButton.setEnabled(True)
        self.stopMonitorButton.setEnabled(False)

    # 开始工作
    # def start_process(self):
    #     if self.testButton.text() == "开始测试":
    #         self.testButton.setText("结束测试")
    #         self.debugButton.setText("测试中...")
    #         if "单天线" in self.comboBox.currentText():
    #             self.data_send_string("AA 06 01", True)
    #             print("写入一次检波（单天线）模式")
    #         elif "双天线" in self.comboBox.currentText():
    #             self.data_send_string("AA 06 02", True)
    #             print("写入二次检波（双天线）模式")
    #     else:
    #         # self.testButton.setText("开始测试")
    #         # self.debugButton.setText("调试")
    #         pass
    def start_process(self):
        # 上升沿触发写入命令
        if self.measureFlag == 0: # 未在测试中
            # self.testButton.setText("结束测试")
            self.debugButton.setText("测试中...")
            if "单天线" in self.comboBox.currentText():
                self.data_send_string("AA 06 01", True)
                print("写入一次检波（单天线）模式")
            elif "双天线" in self.comboBox.currentText():
                self.data_send_string("AA 06 02", True)
                print("写入二次检波（双天线）模式")
            self.measureFlag = 1
        else:
            # self.testButton.setText("开始测试")
            # self.debugButton.setText("调试")
            pass

    # 接收数据
    def data_receive(self):
        global flag, receiveData, startFreq, endFreq, freq, stepFreq
        try:
            num = self.ser.inWaiting()
            # print(f"num: {num}")
        except:
            self.port_close()
            return None
        if num > 0:
            # data = self.ser.read(num)
            data = self.ser.readline()
            print(data)
            num = len(data)

            tempData = data
            tempData = tempData.decode("iso-8859-1").strip()
            row = tempData.split(" ")
            if len(row) == 2:
                
                if self.sweepMode == 0: 
                    progressValue = int((float(row[0]) - startFreq)/(endFreq - startFreq)*100)
                    # print(progressValue)
                    self.progressBar.setValue(progressValue)
                
                # print(f"row[0]: {row[0]}")
                # print(f"startFreq: {startFreq}")
                if float(row[0]) == startFreq:
                    receiveData = {}

                if float(row[0])>=startFreq and float(row[0])<=endFreq:  # key: freq; value: rssi
                    receiveData[float(row[0])] = float(row[1])

                if math.isclose(float(row[0]), endFreq, rel_tol=1e-5):  # 一次扫频结束，进行数据处理
                # if float(row[0]) == startFreq:
                #     receiveData = {}
                #     flag = True
                # if flag == True:
                #     if float(row[0]) >= startFreq:
                #         receiveData[float(row[0])] = float(row[1])
                # if flag and float(row[0]) == endFreq:
                    # 对得到的数据处理，因为有一部分数据的rssi值是残缺的
                    self.deleteMutationValue(5000)  # delete the outlier (delta rssi > 5000)

                    self.data_process()
                    if self.measureFlag == 1:  # 若在测试中
                        flag = False

                        self.ser.close()
                        self.ser.open()
                        # self.ser.flush()

                        # self.set_freq_1(startFreq, endFreq)
                        if self.checkBox.isChecked():
                            print("频率跟随，改变测试频率范围...")
                            print(freq - freqRange/2, freq + freqRange/2)
                            # print(freqRange)
                            self.set_freq_1(freq - freqRange/2, freq + freqRange/2)
                            time.sleep(0.1)

                        if self.sweepMode == 1:  # 连续监测
                            if self.comboBox.currentText() == "单天线功率检波":
                                # self.ser.close()
                                # self.ser.open()
                                self.data_send_string("AA 06 01", True)
                            elif self.comboBox.currentText() == "双天线功率检波":
                                # self.ser.close()
                                # self.ser.open()
                                self.data_send_string("AA 06 02", True)
                        else:  #  单次测试
                            self.measureFlag = 0  # 单次模式，则测一次后标志位置 0
                            self.testButton.setText("开始测试")
                            self.debugButton.setText("单次测试")

                            # if self.comboBox.currentText() == "单天线功率检波":
                            #     # self.ser.close()
                            #     # self.ser.open()
                            #     # pg.plot(list(receiveData.keys()), list(receiveData.values()))
                               
                            # elif self.comboBox.currentText() == "双天线功率检波":
                            #     # self.ser.close()
                            #     # self.ser.open()
                            #     # pg.plot(list(receiveData.keys()), list(receiveData.values()))

                    else:
                        # self.ser.close()
                        # self.ser.open()
                        pass
            # hex显示
            if self.hex_receive.isChecked():
                # print("=== marker1 ===")
                out_s = ''
                for i in range(0, len(data)):
                    out_s = out_s + '{:02X}'.format(data[i]) + ' '
                self.s2__receive_text.insertPlainText(out_s)
            else:
                # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
                # self.s2__receive_text.insertPlainText(data.decode('iso-8859-1'))
                self.s2__receive_text.append(data.decode('iso-8859-1'))
                # print("=== marker2 ===")

            # 统计接收字符的数量
            self.data_num_received += num
            self.lineEdit.setText(str(self.data_num_received))

            # # 获取到text光标
            # textCursor = self.s2__receive_text.textCursor()
            # # 滚动到底部
            # textCursor.movePosition(textCursor.End)
            # # 设置光标到text中去
            # self.s2__receive_text.setTextCursor(textCursor)
        else:
            pass

    # 将串口得到的值RSSI中的突变值删掉
    def deleteMutationValue(self, valueRange):
        global receiveData
        f = list(receiveData.keys())
        rssi = list(receiveData.values())
        for i in range(1, len(rssi) - 1):
            if abs(rssi[i] - rssi[i - 1]) >= valueRange:
                receiveData.pop(f[i])

    def data_process(self):
        global threshold, flag, startFreq, endFreq, receiveData, freq, freqList, currentTemperature, dicTimeAndTAndF
        global minTemperature, maxTemperature
        global intercept, slope_1, slope_2
        global time_stamp
        indexList = set()

        f = list(receiveData.keys())
        rssi = list(receiveData.values())

        maxRssi = max(rssi)  # no curve fitting, use the max value simply
        maxIndex = rssi.index(maxRssi)
        freq = 0

        if maxRssi < threshold:
            self.receiveText_2.setText(f"{freq*1e6:,.0f}")
            QMessageBox.critical(self, "warning", "信号弱，请调整天线位置 或 扩大扫频范围")
            self.monitorButton.setEnabled(False)
        else:
            checkThreshold = maxRssi - thresholdRange

            for i in range(maxIndex, 0, -1):
                if rssi[i] >= checkThreshold:
                    indexList.add(f[i])
                else:
                    break

            for i in range(maxIndex, len(rssi), 1):
                if rssi[i] >= checkThreshold:
                    indexList.add(f[i])
                else:
                    break

            if len(indexList) != 0:
                # # simple algorithm
                # freq = np.mean(list(indexList))

                # === start curve fitting by polynominal regression ===
                df = pd.DataFrame({
                    "freq": f,
                    "rssi": rssi
                })
                mask = df["rssi"] >= checkThreshold
                df2 = df[mask]

                x = df2["freq"].values.reshape((-1, 1))
                y = df2["rssi"].values

                transformer = PolynomialFeatures(degree=2, include_bias=False)
                x_new = transformer.fit_transform(x)

                model = LinearRegression().fit(x_new, y)
                r_sq = model.score(x_new, y)
                print(f'coefficient of determination (R^2): {r_sq:.2f}')
                print(f"intercept: {model.intercept_:.3f}")
                print(f"slope: {model.coef_}")

                y_pred = model.predict(x_new)
                # number of points for 1 Hz resolution
                num_1Hz = int((len(x) - 1)*1e4 + 1)
                print(f"length of x is {len(x)}")
                print(f"length of x (1 Hz) is {num_1Hz}")
                x2 = np.linspace(x[0], x[-1], num_1Hz).reshape((-1, 1))  # improve the resolution from 10 kHz to 1 Hz
                x2_new = transformer.fit_transform(x2)
                y2_pred = model.predict(x2_new)
                
                freq = x2[np.argmax(y2_pred)][0]
                freq = round(freq, 6)
                print(f"frequency is {freq*1e6:,.0f}")
                print(f"fitting score is {r_sq:.3f}")
                # === end 
                
                if self.sweepMode == 0:
                    fig, ax = plt.subplots()
                    ax.scatter(f, rssi, label="measured")
                    ax.scatter(df2["freq"].values, df2["rssi"].values, label="selected for fitting")
                    # ax.scatter(x, y_pred, color='red', marker="s")
                    ax.plot(x2, y2_pred, color='red', label=f"fitted ($R^2$: {r_sq:.3f})")
                    ax.axvline(x = freq, color='blue', linestyle='--')
                    ax.annotate(f" {freq*1e6:,.0f} Hz", xy=(freq, np.min(rssi)+500), color='blue')
                    ax.legend()
                    fig.show()
        
                    if r_sq < 0.9:
                        QMessageBox.warning(self, "warning", "频率拟合失败，请减小阈值范围 或 扩大扫频范围")
                        self.monitorButton.setEnabled(False)
                    else:
                        QMessageBox.information(self, "", "传感器信号强，可进行连续监测")
                        self.monitorButton.setEnabled(True)

                # currentTemperature = (self.lookUpMethod(originData1_x,originData1_y,freq)+self.lookUpMethod(originData2_x,originData2_y,freq))/2
                currentTemperature = intercept + slope_1*freq*1e6 + slope_2*(freq*1e6)**2
                currentTemperature = round(currentTemperature, 1)
                # freq = round(freq, 2)
                # currentTemperature = round(currentTemperature,1)
                # 如果跟随温度变化按钮被选中了，那么这个就会工作，设置频率
            
            self.receiveText_2.setText(f"{freq*1e6:,.0f}")
            self.receiveText.setText(f"{currentTemperature:.1f}")
            self.s2__receive_text.setText("")  # 清空接收区显示数据，以免文本框内容过多
            # 将工作得到的结果保存在freqlist和dicTimeAndTAndF中
            key = time.strftime("%H:%M:%S")
            dicTimeAndTAndF[key] = [freq, currentTemperature]
            freqList.append(freq)
            temperatureList.append(currentTemperature)
            # print(len(freqList), len(temperatureList))

            # 限制数据存储列表最大点数
            if len(temperatureList) >= self.spinBox.value():
                freqList.pop(0)
                temperatureList.pop(0)

            # print(temperatureList)
            # print(len(temperatureList))

            # 实时保存文件
            if self.save2FileRealTime.isChecked() and self.sweepMode == 1:
                QApplication.processEvents()
                dataRealTime = str(key)+", "+str(dicTimeAndTAndF[key][0])+", "+str(dicTimeAndTAndF[key][1])+"\n"
                with open("data/auto-" + time_stamp + ".csv","a") as f:
                    f.write(dataRealTime)

            # 画图
            minTemperature = min(temperatureList)-1
            maxTemperature = max(temperatureList)+1
            self.plot.setYRange(minTemperature, maxTemperature)
            # self.curve = self.plot.plot()

    # 清除发送区数据
    def send_data_clear(self):
        self.s3__send_text.setText("")

    # 清除接收区数据
    def receive_data_clear(self):
        global receiveData, freqList, dicTimeAndTAndF, temperatureList
        self.s2__receive_text.setText("")
        receiveData = {}
        freqList = []
        dicTimeAndTAndF = {}
        temperatureList=[]
        self.plot.close()
        self.plot = pg.PlotWidget(enableAutoRange=True)
        self.plotDataViewVerticalLayout.addWidget(self.plot)
        # 如果重新设置了起始频率和中止频率，这个也要更新
        self.plot.setYRange(startFreq, endFreq)
        self.curve = self.plot.plot()
        
    # 设置频率变化的范围
    def set_freq_range(self):
        global freqRange
        freqRange = float(self.freqChange.text())

    # 保存文件
    def saveTAndFToFile(self):
        global dicTimeAndTAndF, time_stamp
        QApplication.processEvents()
        key = list(dicTimeAndTAndF.keys())
        with open("data/manual-"+ time_stamp + ".csv","a") as f:
            f.write(str(key[-1]))
            f.write(", ")
            f.write(str(dicTimeAndTAndF[key[-1]][0]))
            f.write(", ")
            f.write(str(dicTimeAndTAndF[key[-1]][1]))
            f.write("\n")
            

   

    # def selectSavedFile(self):
    #     global savedFile, file
    #     tempFile = QFileDialog.getOpenFileNames(self,
    #         "getOpenFileNames", "./",
    #         "All Files (*);;Text Files (*.txt)")
    #     if(len(tempFile)==2 and len(tempFile[0])!=0 and tempFile[0][0].endswith(".txt")):
    #         savedFile = tempFile[0][0]
    #         file = None
    #         # self.s2__receive_text.insertPlainText("保存文件选择完成")
    #         self.statusBar().showMessage("保存文件选择完成")

    #     else:
    #         # self.s2__receive_text.insertPlainText("保存文件选择错误，请选择以.txt结尾的文件")
    #         # self.statusBar().showMessage("保存文件选择错误，请选择以.txt结尾的文件")
    #         QMessageBox.critical(self, "File Type Error", "保存文件选择错误，请选择以.txt结尾的文件！")
    
    # 写入模型参数
    def writeModelParameters_a(self):
        global intercept, slope_1, slope_2
        intercept = float(self.intercept_a.text())
        slope_1 = float(self.slope_1_a.text())
        slope_2 = float(self.slope_2_a.text())

    def writeModelParameters_b(self):
        global intercept, slope_1, slope_2
        intercept = float(self.intercept_b.text())
        slope_1 = float(self.slope_1_b.text())
        slope_2 = float(self.slope_2_b.text())

    # 画图
    def plotDataView(self):
        global temperatureList
        # print("len: {len(temperatureList)}")
        # self.plot.clear()
        if self.measureFlag == 1:  # 若在测试中
            self.plot.clear()
            self.curve = self.plot.plot()
            self.curve.setData(temperatureList)
        
    # 简易模型拟合
    def simpleFitting(self):
        if self.firstFreq.text() == "" or \
            self.secondFreq.text() == "" or \
            self.thirdFreq.text() == "" or \
            self.fourthFreq.text() == "" or \
            self.fifthFreq.text() == "" or \
            self.firstTemp.text() == "" or \
            self.secondTemp.text() == "" or \
            self.thirdTemp.text() == "" or \
            self.fourthTemp.text() == "" or \
            self.fifthTemp.text() == "":
            QMessageBox.warning(self, "warning", "请完整输入 5 组数据")
        else:
            x = np.array([
                float(self.firstFreq.text()),
                float(self.secondFreq.text()),
                float(self.thirdFreq.text()),
                float(self.fourthFreq.text()),
                float(self.fifthFreq.text()),
                ]).reshape((-1, 1))
            y = np.array([
                float(self.firstTemp.text()),
                float(self.secondTemp.text()),
                float(self.thirdTemp.text()),
                float(self.fourthTemp.text()),
                float(self.fifthTemp.text()),
                ])
            print(x)
            print(y)

            # === start curve fitting by polynominal regression ===
            transformer = PolynomialFeatures(degree=2, include_bias=False)
            x_new = transformer.fit_transform(x)

            model = LinearRegression().fit(x_new, y)
            r_sq = model.score(x_new, y)

            self.R2Text.setText(f"{r_sq:.3f}")
            self.intercept_b.setText(f"{model.intercept_:.4e}")
            self.slope_1_b.setText(f"{model.coef_[0]:.4e}")
            self.slope_2_b.setText(f"{model.coef_[1]:.4e}")

            y_pred = model.predict(x_new)
            y_pred_model = model.intercept_ + model.coef_[0]*freq + model.coef_[1]*freq**2

            # extend the prediction range to see the fitting quality
            x2 = np.linspace(x[0] - (x[-1] - x[0]), x[-1] + (x[-1] - x[0]), 1601).reshape((-1, 1))
            x2_new = transformer.fit_transform(x2)
            y2_pred = model.predict(x2_new)

            fig, ax = plt.subplots()
            ax.scatter(x, y, color="blue", label="measured")
            ax.scatter(x, y_pred, color='red', marker="s")
            ax.plot(x2, y2_pred, color='red', label=f"fitted ($R^2$: {r_sq:.3f})")
            ax.legend()
            fig.show()
            # === end 


if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    sys.argv += ['--style', 'fusion']
    app = QApplication(sys.argv)
    # app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec() 