# Created by Qiucheng Su on 2021
# Revised by Hao Jin on 2022/03/26

import datetime
import math
import os
import sys
# import threading
import time
import json
from urllib import response
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import serial
import serial.tools.list_ports
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QMessageBox
)
from PyQt5.QtCore import QTimer
from outputUI4 import Ui_Form
import pyqtgraph as pg

# === start reading config === 
json_file = 'single.json'
try:
    with open(json_file) as f_obj:
        json_dict = json.load(f_obj)
except FileNotFoundError:
    temp_dict = {
        "start_freq": 453,
        "stop_freq": 454
    }
    with open(json_file, 'w') as f_obj:
        json.dump(temp_dict, f_obj, indent=4)
    print("\nConfiguration file not found! \nInitialized with default values.")
    print("Please restart the app.\n")
# === end ===    

startFreq = json_dict["start_freq"]
endFreq = json_dict["stop_freq"]
startFreq2 = json_dict["start_freq"]
endFreq2 = json_dict["stop_freq"]
startFreq3 = json_dict["start_freq"]
endFreq3 = json_dict["stop_freq"]
# 步进是0.01MHz，如果是其他的阅读器需要更改这个代码
stepFreq = 0.01

flag = False  # 表示第一个接收的数是起始频率
receiveData = {}
threshold = 14000
thresholdRange = 4000
freq = 43602 # 温度频率
freq2 = 43602 # 应变频率
freq3 = 43480 # 压力频率
threshold2 = 14000
thresholdRange2 = 4000
threshold3 = 14000
thresholdRange3 = 4000

# 设置拟合函数参数
one_stage_T=0.000104186
two_stage_T=0.0
zero_stage_T=-45401.56
one_stage_D=0.000104918
two_stage_D=0.0
zero_stage_D=-46125.3
one_stage_P=0.000117647
two_stage_P=0
zero_stage_P=-52619.82
fliter_var = 436020000
fliter_var2 = 436020000
fliter_var3 = 434800000

responseTime =  time.perf_counter() 
print(responseTime)

# 当前的温度
currentTemperature = 0
# 扫频跟随谐振频率变化的范围，span, 1 MHz
freqRange = 1
#工作的谐振频率都存在这里
freqList = []
# 工作的谐振频率和温度存在这里，key为时间，value为谐振频率和温度
dicTimeAndTAndF = {}
# 工作的温度都存在这里
temperatureList = []
# 工作的应变都存在这里
deformationList = []
# 工作的压力都存在这里
pressureList = []

freq_list = []
freq2_list = []
freq3_list = []
# 画图时候的最小温度和最大温度值
#minTemperature= 0
#maxTemperature= 100
# 温度的校准值
calibration = 0
#保存在哪个文件里，默认是这个
savedFile = "./data.txt"
file = None
# 查表法用到的原始值
# originData1_x = [424.11,424.77,425.42,426.065,426.415,427.04,427.47,427.945,428.575,429.465,429.76,430.215,430.51,431.075,431.385,431.615,431.78,432,432.22,432.61,432.935,433.38,433.57,433.81,434.15,434.285,434.475,434.645,434.7,434.895]
# originData1_y = [801,773,750,723,698,678,650,635,606,547,545,522,497,471,444,441,430,414,389,373,334,310,280,260,227,208,187,153,138,27]
# originData2_x= [424.06,424.765,425.255,425.67,426.385,426.925,427.35,427.385,427.96,428.465,428.84,429.395,429.725,430.035,430.47,430.81,431.285,431.77,432.095,432.815,433.185,433.46,433.64,433.93,434.12,434.255,434.35,434.53,434.57,434.65]
# originData2_y=[798,775,749,740,702,682,656,651,632,605,592,555,547,529,506,484,460,426,405,353,318,287,268,230,210,194,178,147,121,34]
originData1_x = [434.9,434.89,434.86,434.83,434.84,434.82,434.81,434.79,434.76,434.7,434.66,434.65,434.61,434.57,434.54,434.49,434.44,434.38,434.32,434.26,434.2,434.12,434.04,433.98,433.92,433.77,433.6,433.41,433.2,433,432.78,432.53,432.27,432,431.74,431.5,431.23,430.94,430.68,430.35,430.07,429.78,429.48,429.35]
originData1_y = [30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,335]
originData2_x = [434.72,434.71,434.7,434.68,434.65,434.62,434.58,434.55,434.51,434.46,434.41,434.36,434.3,434.25,434.18,434.12,434.04,433.96,433.89,433.79,433.72,433.61,433.52,433.46,433.36,433.19,433,432.78,432.58,432.36,432.12,431.9,431.65,431.44,431.17,430.91,430.64,430.35,430.07,429.82,429.5,429.24,429.07]
originData2_y = [30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,325]

class MainWoindow(QMainWindow, QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.setWindowTitle("无源无线温度传感器系统")
        self.ser = serial.Serial()
        self.port_check()

        self.close_button.setEnabled(False)

        # 接收数据和发送数据数目置零
        self.data_num_received = 0
        self.lineEdit.setText(str(self.data_num_received))
        self.data_num_sended = 0
        self.lineEdit_2.setText(str(self.data_num_sended))

        # 温度设置
        self.textEditStartFreq.setText(str(startFreq))
        self.textEditEndFreq.setText(str(endFreq))
        self.textEditEndFreq_2.setText(str(threshold))  # rssi 阈值
        self.rssiThreshold_2.setText(str(thresholdRange))  # rssi 阈值范围

        # 应变设置
        self.textEditStartFreq_2.setText(str(startFreq))
        self.textEditEndFreq_3.setText(str(endFreq))
        self.textEditEndFreq_4.setText(str(threshold)) 
        self.rssiThreshold_3.setText(str(thresholdRange))

        # 压力设置
        self.textEditStartFreq_3.setText(str(startFreq))
        self.textEditEndFreq_5.setText(str(endFreq))
        self.textEditEndFreq_6.setText(str(threshold)) 
        self.rssiThreshold_4.setText(str(thresholdRange))

        # 拟合函数设置
        self.freqChange.setText(str(freqRange))  # the step of frequency adjust
        self.one_stage_T.setText(str(one_stage_T)) 
        self.two_stage_T.setText(str(two_stage_T))
        self.zero_stage_T.setText(str(zero_stage_T)) 
        self.one_stage_D.setText(str(one_stage_D))
        self.two_stage_D.setText(str(two_stage_D))
        self.zero_stage_D.setText(str(zero_stage_D))
        self.one_stage_P.setText(str(one_stage_P))
        self.two_stage_P.setText(str(two_stage_P))
        self.zero_stage_P.setText(str(zero_stage_P))


        # 使用pyqtgraph画图，将图绑定在这个组件上
        self.plot = pg.PlotWidget(enableAutoRange=True)
        self.plotDataViewVerticalLayout.addWidget(self.plot)
        # 如果重新设置了起始频率和终止频率，这个也要更新
        # self.plot.setYRange(startFreq, endFreq)
        # self.plot.setYRange(minTemperature, maxTemperature)
        self.plot.setTitle("温度曲线")
        self.curve = self.plot.plot()
        

    def init(self):
        # status bar
        self.statusBar().showMessage('Ready')

        #
        # self.label_12.setText(f"$\mu \epsilon$")

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

        # 定时器接收数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.data_receive)

        # 清除发送窗口
        self.s3__clear_button.clicked.connect(self.send_data_clear)

        # 清除接收窗口
        self.s2__clear_button.clicked.connect(self.receive_data_clear)

        # 设置起始频率和终止频率
        self.sendFreqButton.clicked.connect(self.set_freq)
        # 设置起始频率和终止频率2
        self.sendFreqButton_2.clicked.connect(self.set_freq2)
        # 设置起始频率和终止频率3
        self.sendFreqButton_3.clicked.connect(self.set_freq3)

        # 开始工作
        self.testButton.clicked.connect(self.start_process)

        
        # 定时器刷新数据-温度 画图
        self.plotData = QTimer(self)
        self.plotData.timeout.connect(self.plotDataView)
        self.plotData.start(10)

        # 定时器刷新数据-应变 画图
        self.plotData = QTimer(self)
        self.plotData.timeout.connect(self.plotDataView2)
        self.plotData.start(10)

        # 定时器刷新数据-压力 画图
        self.plotData = QTimer(self)
        self.plotData.timeout.connect(self.plotDataView3)
        self.plotData.start(10)
        
        # 设置偏移的范围
        self.sendFreqRangeButton.clicked.connect(self.set_freq_range)
        # 设置校准值
        # self.sendCalibration.clicked.connect(self.buttonCalibration)
        # 将温度和谐振频率保存为文件
        self.saveTempAndFreq.clicked.connect(self.saveTAndFToFile)

        self.selectFileButton.clicked.connect(self.selectSavedFile)

        # ********** need to set **********
        # 设置拟合函数参数
        # ********** need to set **********
        self.send_para.clicked.connect(self.button_para)   

    def selectSavedFile(self):
        global savedFile, file
        tempFile = QtWidgets.QFileDialog.getOpenFileNames(self,
                                                           "getOpenFileNames", "./",
                                                           "All Files (*);;Text Files (*.txt)")
        if(len(tempFile)==2 and len(tempFile[0])!=0 and tempFile[0][0].endswith(".txt")):
            savedFile = tempFile[0][0]
            file = None
            # self.s2__receive_text.insertPlainText("保存文件选择完成")
            self.statusBar().showMessage("保存文件选择完成")

        else:
            # self.s2__receive_text.insertPlainText("保存文件选择错误，请选择以.txt结尾的文件")
            # self.statusBar().showMessage("保存文件选择错误，请选择以.txt结尾的文件")
            QMessageBox.critical(self, "File Type Error", "保存文件选择错误，请选择以.txt结尾的文件！")


        # # 获取到text光标
        # textCursor = self.s2__receive_text.textCursor()
        # # 滚动到底部
        # textCursor.movePosition(textCursor.End)
        # # 设置光标到text中去
        # self.s2__receive_text.setTextCursor(textCursor)

    # 保存文件
    def saveTAndFToFile(self):
        global dicTimeAndTAndF
        QApplication.processEvents()
        key = list(dicTimeAndTAndF.keys())
        with open(str(datetime.date.today())+"-"+str(time.strftime("%H-%M-%S"))+".txt","w") as f:
            for i in range(len(dicTimeAndTAndF)):
                f.write(str(key[i]))
                f.write("\t")
                f.write(str(dicTimeAndTAndF[key[i]][0]))
                f.write("\t")
                f.write(str(dicTimeAndTAndF[key[i]][1]))
                f.write("\n")
            f.close()

    def save2FileRealTimeFun(self,data):
        global savedFile,file
        if file==None:
            file = open(savedFile,'a')
        file.write(data)
        file.flush()


    # # 设置校准值
    # def buttonCalibration(self):
    #     global calibration
    #     calibration = 0
    #     initFreq = float(self.initFreq.toPlainText())
    #     initTemperature = float(self.initTemperature.toPlainText())
    #     tempData1 = self.lookUpMethod(originData1_x,originData1_y,initFreq)
    #     tempData2 = self.lookUpMethod(originData2_x,originData2_y,initFreq)
    #     calibration = initTemperature - (tempData1+tempData2)/2

    # 设置校准值
    def button_para(self):
        global one_stage_T,two_stage_T,zero_stage_T,one_stage_D,two_stage_D,zero_stage_D,one_stage_P,two_stage_P,zero_stage_P
        one_stage_T = float(self.one_stage_T.toPlainText())
        two_stage_T = float(self.two_stage_T.toPlainText())
        zero_stage_T = float(self.zero_stage_T.toPlainText())
        one_stage_D = float(self.one_stage_D.toPlainText())
        two_stage_D = float(self.two_stage_D.toPlainText())
        zero_stage_D = float(self.zero_stage_D.toPlainText())
        one_stage_P = float(self.one_stage_P.toPlainText())
        two_stage_P = float(self.two_stage_P.toPlainText())
        zero_stage_P = float(self.zero_stage_P.toPlainText())
        print(one_stage_T,two_stage_T,zero_stage_T)
        print(one_stage_D,two_stage_D,zero_stage_D)
        print(one_stage_P,two_stage_P,zero_stage_P)
        # print(type(one_stage_T))

    # 温度画图
    def plotDataView(self):
        global freqList,temperatureList
        if self.comboBox.currentText() == "单天线工作" or self.comboBox.currentText() == "双天线工作":
            if self.comboBox_2.currentText() == "温度测试":
                self.curve.clear()
                self.plot.setTitle("温度曲线")
                if len(temperatureList)>0:
                    minTemperature = min(temperatureList)-10
                    maxTemperature = max(temperatureList)+10
                    self.plot.setYRange(minTemperature, maxTemperature)
                    if self.testButton.text() == "结束测试":
                        self.curve.clear()
                        # self.curve.setData(freqList)
                        self.curve.setData(temperatureList)
                        # print(temperatureList)
    
    # 应变画图
    def plotDataView2(self):
        global deformationList
        if self.comboBox.currentText() == "单天线工作" or self.comboBox.currentText() == "双天线工作":
            if self.comboBox_2.currentText() == "应变测试":
                self.curve.clear()
                self.plot.setTitle("应变曲线")
                if len(deformationList)>0:
                    minTemperature = min(deformationList)-10
                    maxTemperature = max(deformationList)+10
                    self.plot.setYRange(minTemperature, maxTemperature)
                    if self.testButton.text() == "结束测试":
                        # self.curve.setData(freqList)
                        self.curve.setData(deformationList)

    # 压力画图
    def plotDataView3(self):
        global pressureList
        if self.comboBox.currentText() == "单天线工作" or self.comboBox.currentText() == "双天线工作":
            if self.comboBox_2.currentText() == "压力测试":
                self.curve.clear()
                self.plot.setTitle("压力曲线")
                if len(pressureList)>0:
                    minTemperature = min(pressureList)-10
                    maxTemperature = max(pressureList)+10
                    self.plot.setYRange(minTemperature, maxTemperature)
                    if self.testButton.text() == "结束测试":
                        # self.curve.setData(freqList)
                        self.curve.setData(pressureList)
    


    # 设置扫频范围
    def set_freq(self):
        global startFreq, endFreq, threshold, thresholdRange, flag,temperatureList,minTemperature,maxTemperature
        flag = False

        # 温度参数上传
        startFreq = float(self.textEditStartFreq.toPlainText())
        startFreq = round(startFreq,2)
        endFreq = float(self.textEditEndFreq.toPlainText())
        endFreq = round(endFreq,2)
        # threshold parameters are not writen to MCU
        threshold = int(self.textEditEndFreq_2.toPlainText())
        thresholdRange = int(self.rssiThreshold_2.toPlainText())

        s = "AA 15 01 " + hex(int(startFreq * 100))[2:4].upper() + " " + hex(int(startFreq * 100))[
                                                                      4:6].upper() + " " + hex(int(endFreq * 100))[
                                                                                           2:4].upper() + " " + hex(
            int(endFreq * 100))[4:6].upper() + " 01"

        self.data_send_string(s, True)

        # self.plot.setYRange(startFreq, endFreq)
        # self.plot.setYRange(minTemperature, maxTemperature)
        # self.curve = self.plot.plot()

# 设置扫频范围
    def set_freq2(self):
        global startFreq2, endFreq2, threshold2, thresholdRange2, flag,temperatureList,minTemperature,maxTemperature
        flag = False

        # 应变参数上传
        startFreq2 = float(self.textEditStartFreq_2.toPlainText())
        startFreq2 = round(startFreq2,2)
        endFreq2 = float(self.textEditEndFreq_3.toPlainText())
        endFreq2 = round(endFreq2,2)
        # threshold parameters are not writen to MCU
        threshold2 = int(self.textEditEndFreq_4.toPlainText())
        thresholdRange2 = int(self.rssiThreshold_3.toPlainText())


        s2 = "AA 15 02 " + hex(int(startFreq2 * 100))[2:4].upper() + " " + hex(int(startFreq2 * 100))[
                                                                      4:6].upper() + " " + hex(int(endFreq2 * 100))[
                                                                                           2:4].upper() + " " + hex(
            int(endFreq2 * 100))[4:6].upper() + " 01"
  
        self.data_send_string(s2, True)

        # self.plot.setYRange(startFreq, endFreq)
        # self.plot.setYRange(minTemperature, maxTemperature)
        # self.curve = self.plot.plot()

# 设置扫频范围
    def set_freq3(self):
        global startFreq3, endFreq3, threshold3, thresholdRange3,flag,temperatureList,minTemperature,maxTemperature
        flag = False

        # 压力参数上传
        startFreq3 = float(self.textEditStartFreq_3.toPlainText())
        startFreq3 = round(startFreq3,2)
        endFreq3 = float(self.textEditEndFreq_5.toPlainText())
        endFreq3 = round(endFreq3,2)
        # threshold parameters are not writen to MCU
        threshold3 = int(self.textEditEndFreq_6.toPlainText())
        thresholdRange3 = int(self.rssiThreshold_4.toPlainText())
        
        s3 = "AA 15 03 " + hex(int(startFreq3 * 100))[2:4].upper() + " " + hex(int(startFreq3 * 100))[
                                                                      4:6].upper() + " " + hex(int(endFreq3 * 100))[
                                                                                           2:4].upper() + " " + hex(
            int(endFreq3 * 100))[4:6].upper() + " 01"

        self.data_send_string(s3, True)
        # self.plot.setYRange(startFreq, endFreq)
        # self.plot.setYRange(minTemperature, maxTemperature)
        # self.curve = self.plot.plot()



    def set_freq_1(self, start, end):
        global startFreq, endFreq, flag
        flag = False
        startFreq = start
        startFreq = round(startFreq, 2)
        endFreq = end
        endFreq = round(endFreq, 2)

        # self.data_send_string("AA 07 00", True)

        s = "AA 05 " + hex(int(start * 100))[2:4].upper() + " " + hex(int(start * 100))[
                                                                  4:6].upper() + " " + hex(int(end * 100))[
                                                                                       2:4].upper() + " " + hex(
            int(end * 100))[4:6].upper() + " 01"
        self.data_send_string(s, True)
        self.textEditStartFreq.setText(str(startFreq))
        self.textEditEndFreq.setText(str(endFreq))
        self.plot.setYRange(start, end)
        self.curve = self.plot.plot()

    # 设置频率变化的范围
    def set_freq_range(self):
        global freqRange
        freqRange = float(self.freqChange.toPlainText())

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
        # if len(self.Com_Dict) == 0:
        #     self.state_label.setText("未发现串口")

    # 串口信息
    def port_imf(self):
        # 显示选定的串口的详细信息
        imf_s = self.s1__box_2.currentText()
        # if imf_s != "":
            # self.state_label.setText(self.Com_Dict[self.s1__box_2.currentText()])

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
            self.formGroupBox1.setTitle("串口状态（已开启）")

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
        self.formGroupBox1.setTitle("串口状态（已关闭）")

    # 发送数据
    def data_send(self):
        if self.ser.isOpen():
            input_s = self.s3__send_text.toPlainText()
            if input_s != "":
                # 非空字符串
                if self.hex_send.isChecked():
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

                num = self.ser.write(input_s)
                self.data_num_sended += num
                self.lineEdit_2.setText(str(self.data_num_sended))
        else:
            pass

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
                
                # print(input_s)
                num = self.ser.write(input_s)
                self.data_num_sended += num
                self.lineEdit_2.setText(str(self.data_num_sended))
        else:
            pass

    # 开始工作
    def start_process(self):
        global temperatureList, deformationList, pressureList
        if self.testButton.text() == "开始测试":
            self.testButton.setText("结束测试")
            if "单天线工作" in self.comboBox.currentText():
                self.data_send_string("AA 07 08 01", True)
            elif "双天线工作" in self.comboBox.currentText():
                self.data_send_string("AA 07 08 02", True)
            elif "单天线功率检波" in self.comboBox.currentText():
                self.data_send_string("AA 06 01", True)
            elif "双天线功率检波" in self.comboBox.currentText():
                self.data_send_string("AA 06 02", True)
        else:
            self.testButton.setText("开始测试")
            self.data_send_string("AA 07 00", True)
            # 清除列表
            temperatureList = []
            deformationList = []
            pressureList = []


    # 接收数据
    def data_receive(self):
        global flag, receiveData, startFreq, endFreq,freq,stepFreq,responseTime,freq_list,freq2_list,freq3_list,fliter_var,fliter_var2,fliter_var3

        try:
            num = self.ser.inWaiting()
        except:
            self.port_close()
            return None
        if num > 0:
            # data = self.ser.read(num)
            data = self.ser.readline()
            num = len(data)

            Tt = round((time.perf_counter()  -responseTime), 2)
            self.receiveText_2.setText(str(Tt))   # **********************responseTime 响应时间*********************
            responseTime =  time.perf_counter() 

            tempData = data
            tempData = tempData.decode("iso-8859-1").strip()
            row = tempData.split(" ")
            #print(row) # ['T','12345','12345','12345']
            if len(row)==4:
                freq = float(row[1])
                freq2 = float(row[2])
                freq3 = float(row[3])
                freq_list.append(freq)
                freq2_list.append(freq2)
                freq3_list.append(freq3)
                if len(freq_list)>6 or len(freq2_list)>6 or len(freq3_list)>6:

                    tempppp=round(np.mean(freq_list[-7:])*10000)    # ******************倍数*******************
                    tempppp = round(fliter_var*0.2 + tempppp*0.8)
                    fliter_var = tempppp

                    deformmm=round(np.mean(freq2_list[-7:])*10000)
                    deformmm = round(fliter_var2*0.2 + deformmm*0.8)
                    fliter_var2 = deformmm

                    presss=round(np.mean(freq3_list[-7:])*10000)
                    presss = round(fliter_var3*0.2 + presss*0.8)
                    fliter_var3 = presss

                    self.receiveText_6.setText(str(tempppp))   # ******************频率**************温度*************
                    # print(round(np.mean(freq_list[-7:])*10000))
                    self.receiveText_7.setText(str(deformmm))   # *******************频率**********应变***************
                    self.receiveText_9.setText(str(presss)) # **************频率**********压力******************

                    #currentTemperature = (self.lookUpMethod(originData1_x,originData1_y,freq)+self.lookUpMethod(originData2_x,originData2_y,freq))/2
                    currentTemperature = (self.lookUp_tem(tempppp))
                    currentDeformation = (self.lookUp_defom(deformmm))
                    currentPressure = (self.lookUp_press(presss))
                    
                    # freq = round(freq, 2)
                    currentTemperature = round(currentTemperature,1)
                    currentDeformation = round(currentDeformation, 1)
                    currentPressure = round(currentPressure, 1)

                    # # 如果跟随温度变化按钮被选中了，那么这个就会工作，设置频率(这里随应变压力未改)
                    # if self.checkBox.checkState() == QtCore.Qt.Checked:
                    #     self.set_freq_1(freq - freqRange/2, freq + freqRange/2)
                    # self.receiveText_2.setText(f"{freq*1e6:,.0f}")  
                    
                    self.receiveText.setText(str(currentTemperature))   # ********************************温度*************
                    self.receive_deform.setText(str(currentDeformation))   # *****************************应变***************
                    self.receiveText_5.setText(str(currentPressure)) # ************************压力******************

                    # 将工作得到的结果保存在freqlist和dicTimeAndTAndF中
                    key = time.strftime("%H:%M:%S")
                    dicTimeAndTAndF[key] = [freq,currentTemperature]
                    freqList.append(freq)

                    # 计算温度list
                    temperatureList.append(currentTemperature)
                    # 计算应变list
                    deformationList.append(currentDeformation)
                    # 计算压力list
                    pressureList.append(currentPressure)
            

                if self.testButton.text() == "结束测试":
                    flag = False
                    if self.comboBox.currentText() == "单天线工作":
                        self.ser.close()
                        self.ser.open()
                        #self.data_send_string("AA 07 08 01", True)
                    elif self.comboBox.currentText() == "双天线工作":
                        self.ser.close()
                        self.ser.open()
                        #self.data_send_string("AA 07 08 02", True)
                    elif self.comboBox.currentText() == "单天线功率检波":
                        self.ser.close()
                        self.ser.open()
                        # self.data_send_string("AA 06 01", True)
                        # pg.plot(list(receiveData.keys()), list(receiveData.values())) # 无限循环弹窗
                        self.testButton.setText("开始测试")
                    elif self.comboBox.currentText() == "双天线功率检波":
                        self.ser.close()
                        self.ser.open()
                        # self.data_send_string("AA 06 02", True)
                        # pg.plot(list(receiveData.keys()), list(receiveData.values())) # 无限循环弹窗
                        self.testButton.setText("开始测试")
                else:
                    #self.data_send_string("AA 07 00", True)
                    self.ser.close()
                    self.ser.open()
            
            elif len(row) == 2:

                if float(row[0]) == startFreq:
                    receiveData = {}

                if float(row[0])>=startFreq and float(row[0])<=endFreq:
                    receiveData[float(row[0])] = float(row[1])

                if math.isclose(float(row[0]), endFreq, rel_tol=1e-5):
                # if float(row[0]) == startFreq:
                #     receiveData = {}
                #     flag = True
                # if flag == True:
                #     if float(row[0]) >= startFreq:
                #         receiveData[float(row[0])] = float(row[1])
                # if flag and float(row[0]) == endFreq:
                    # 对得到的数据处理，因为有一部分数据的rssi值是残缺的
                    self.deleteMutationValue(5000)

                    self.data_process()
                    if self.testButton.text() == "结束测试":
                        flag = False
                        if self.comboBox.currentText() == "单天线工作":
                            self.ser.close()
                            self.ser.open()
                            #self.data_send_string("AA 06 01", True)
                        elif self.comboBox.currentText() == "双天线工作":
                            self.ser.close()
                            self.ser.open()
                            #self.data_send_string("AA 06 02", True)
                        elif self.comboBox.currentText() == "单天线功率检波":
                            self.ser.close()
                            self.ser.open()
                            pg.plot(list(receiveData.keys()), list(receiveData.values()))
                            self.testButton.setText("开始测试")
                        elif self.comboBox.currentText() == "双天线功率检波":
                            self.ser.close()
                            self.ser.open()
                            pg.plot(list(receiveData.keys()), list(receiveData.values()))
                            self.testButton.setText("开始测试")
                    else:
                        self.ser.close()
                        self.ser.open()
                

            # hex显示
            if self.hex_receive.checkState():
                print("=== marker 1 ===")
                out_s = ''
                for i in range(0, len(data)):
                    out_s = out_s + '{:02X}'.format(data[i]) + ' '
                self.s2__receive_text.insertPlainText(out_s)
            else:
                # 串口接收到的字符串为b'123',要转化成unicode字符串才能输出到窗口中去
                # print("=== marker 2 ===")
                self.s2__receive_text.insertPlainText(data.decode('iso-8859-1'))

            # 统计接收字符的数量
            self.data_num_received += num
            self.lineEdit.setText(str(self.data_num_received))

            # 获取到text光标
            textCursor = self.s2__receive_text.textCursor()
            # 滚动到底部
            textCursor.movePosition(textCursor.End)
            # 设置光标到text中去
            self.s2__receive_text.setTextCursor(textCursor)
        else:
            pass

    # 定时发送数据
    def data_send_timer(self):
        if self.timer_send_cb.isChecked():
            self.timer_send.start(int(self.lineEdit_3.text()))
            self.lineEdit_3.setEnabled(False)
        else:
            self.timer_send.stop()
            self.lineEdit_3.setEnabled(True)

    # 清除显示
    def send_data_clear(self):
        self.s3__send_text.setText("")

    # 接收数据清除
    def receive_data_clear(self):
        global receiveData, freqList,dicTimeAndTAndF,temperatureList
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

    # def Fun(self, p, x):
    #     a1, a2, a3 = p
    #     return a1 * x ** 2 + a2 * x + a3

    # def error(self, p, x, y):
    #     return self.Fun(p, x) - y

    # 实时的保存数据到文件中去
    # 将串口得到的值RSSI中的突变值删掉
    def deleteMutationValue(self, valueRange):
        global receiveData
        f = list(receiveData.keys())
        rssi = list(receiveData.values())
        for i in range(1, len(rssi) - 1):
            if abs(rssi[i] - rssi[i - 1]) >= valueRange:
                receiveData.pop(f[i])


    def data_process(self):
        global threshold, flag, startFreq, endFreq, receiveData, freq, freqList,currentTemperature,dicTimeAndTAndF
        global minTemperature,maxTemperature
        indexList = set()

        f = list(receiveData.keys())
        rssi = list(receiveData.values())

        maxRssi = max(rssi)
        maxIndex = rssi.index(maxRssi)
        freq = 0

        if maxRssi < threshold:
            self.receiveText_2.setText(str(freq))   # **********************************************************************************
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
                freq = np.mean(list(indexList))
                currentTemperature = (self.lookUpMethod(originData1_x,originData1_y,freq)+self.lookUpMethod(originData2_x,originData2_y,freq))/2
                freq = round(freq, 2)
                currentTemperature = round(currentTemperature,1)
                # 如果跟随温度变化按钮被选中了，那么这个就会工作，设置频率
                if self.checkBox.checkState() == QtCore.Qt.Checked:
                    self.set_freq_1(freq - freqRange, freq + freqRange)
            self.receiveText_2.setText(str(freq))
            self.receiveText.setText(str(currentTemperature))
            # 将工作得到的结果保存在freqlist和dicTimeAndTAndF中
            key = time.strftime("%H:%M:%S")
            dicTimeAndTAndF[key] = [freq,currentTemperature]
            freqList.append(freq)
            temperatureList.append(currentTemperature)
            # 实时保存文件
            if self.save2FileRealTime.checkState()==QtCore.Qt.Checked:
                dataRealTime = str(key)+"\t"+str(dicTimeAndTAndF[key][0])+"\t"+str(dicTimeAndTAndF[key][1])+"\n"
                self.save2FileRealTimeFun(dataRealTime)
            # 画图
            minTemperature = min(temperatureList)-10
            maxTemperature = max(temperatureList)+10
            self.plot.setYRange(minTemperature, maxTemperature)
            self.curve = self.plot.plot()

    # 根据实验得到的结果使用查表法,得到温度
    # originData_x谐振频率，从大到小排列
    # originData_y温度的值
    def lookUpMethod(self,originData_x,originData_y,freq):
        global calibration
        if freq > originData_x[0]:
            return 20 + calibration
            # return -46.175455*freq+20389.4872+calibration
        if freq < originData_x[len(originData_x)-1]:
            return -35.50046 * freq + 15567.2342 + calibration

            # return -13.891*freq*freq+11931.68589*freq-2561673.53198+calibration
        for i in range(len(originData_x)):
            if freq == originData_x[i]:
                return originData_y[i]+calibration
            if freq > originData_x[i]:
                t = (freq-originData_x[i-1])/(originData_x[i]-originData_x[i-1])*(originData_y[i]-originData_y[i-1])+originData_y[i-1]
                return t+calibration

    # ************
    # 计算此刻的温度，用于显示
    # *************
    def lookUp_tem(self,freqq):
        global calibration
        return two_stage_T * freqq * freqq+ one_stage_T * freqq + zero_stage_T

    # ************
    # 计算此刻的应变，用于显示
    # *************
    def lookUp_defom(self,freqq):
        global calibration
        return two_stage_D * freqq * freqq+ one_stage_D * freqq + zero_stage_D

    # ************
    # 计算此刻的压力，用于显示
    # *************
    def lookUp_press(self,freqq):
        global calibration
        return two_stage_P * freqq * freqq+ one_stage_P * freqq + zero_stage_P


if __name__ == '__main__':
    # os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    # sys.argv += ['--style', 'fusion']
    app = QApplication([])
    window = MainWoindow()
    window.show()
    app.exec_() 
