# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multi_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(843, 544)
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setGeometry(QtCore.QRect(30, 100, 201, 311))
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.s1__lb_1 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_1.setObjectName("s1__lb_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.s1__lb_1)
        self.s1__box_1 = QtWidgets.QPushButton(self.formGroupBox)
        self.s1__box_1.setAutoRepeatInterval(100)
        self.s1__box_1.setDefault(True)
        self.s1__box_1.setObjectName("s1__box_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.s1__box_1)
        self.s1__lb_2 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_2.setObjectName("s1__lb_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.s1__lb_2)
        self.s1__box_2 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_2.setObjectName("s1__box_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.s1__box_2)
        self.state_label = QtWidgets.QLabel(self.formGroupBox)
        self.state_label.setText("")
        self.state_label.setTextFormat(QtCore.Qt.AutoText)
        self.state_label.setScaledContents(True)
        self.state_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.state_label.setObjectName("state_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.state_label)
        self.s1__lb_3 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_3.setObjectName("s1__lb_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.s1__lb_3)
        self.s1__box_3 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_3.setObjectName("s1__box_3")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.s1__box_3)
        self.s1__lb_4 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_4.setObjectName("s1__lb_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.s1__lb_4)
        self.s1__box_4 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_4.setObjectName("s1__box_4")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.s1__box_4)
        self.s1__lb_5 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_5.setObjectName("s1__lb_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.s1__lb_5)
        self.s1__box_5 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_5.setObjectName("s1__box_5")
        self.s1__box_5.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.s1__box_5)
        self.s1__lb_6 = QtWidgets.QLabel(self.formGroupBox)
        self.s1__lb_6.setObjectName("s1__lb_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.s1__lb_6)
        self.s1__box_6 = QtWidgets.QComboBox(self.formGroupBox)
        self.s1__box_6.setObjectName("s1__box_6")
        self.s1__box_6.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.s1__box_6)
        self.open_button = QtWidgets.QPushButton(self.formGroupBox)
        self.open_button.setObjectName("open_button")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.open_button)
        self.close_button = QtWidgets.QPushButton(self.formGroupBox)
        self.close_button.setObjectName("close_button")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.close_button)
        self.verticalGroupBox = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox.setGeometry(QtCore.QRect(270, 100, 401, 71))
        self.verticalGroupBox.setObjectName("verticalGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.s2__receive_text = QtWidgets.QTextBrowser(self.verticalGroupBox)
        self.s2__receive_text.setObjectName("s2__receive_text")
        self.verticalLayout.addWidget(self.s2__receive_text)
        self.verticalGroupBox_2 = QtWidgets.QGroupBox(Form)
        self.verticalGroupBox_2.setGeometry(QtCore.QRect(260, 410, 401, 81))
        self.verticalGroupBox_2.setObjectName("verticalGroupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalGroupBox_2)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.s3__send_text = QtWidgets.QTextEdit(self.verticalGroupBox_2)
        self.s3__send_text.setObjectName("s3__send_text")
        self.verticalLayout_2.addWidget(self.s3__send_text)
        self.s3__send_button = QtWidgets.QPushButton(Form)
        self.s3__send_button.setGeometry(QtCore.QRect(670, 450, 61, 31))
        self.s3__send_button.setObjectName("s3__send_button")
        self.s3__clear_button = QtWidgets.QPushButton(Form)
        self.s3__clear_button.setGeometry(QtCore.QRect(670, 490, 61, 31))
        self.s3__clear_button.setObjectName("s3__clear_button")
        self.formGroupBox1 = QtWidgets.QGroupBox(Form)
        self.formGroupBox1.setGeometry(QtCore.QRect(30, 420, 201, 111))
        self.formGroupBox1.setObjectName("formGroupBox1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formGroupBox1)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.formGroupBox1)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formGroupBox1)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formGroupBox1)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formGroupBox1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.hex_send = QtWidgets.QCheckBox(Form)
        self.hex_send.setGeometry(QtCore.QRect(670, 420, 81, 16))
        self.hex_send.setObjectName("hex_send")
        self.hex_receive = QtWidgets.QCheckBox(Form)
        self.hex_receive.setGeometry(QtCore.QRect(680, 110, 81, 16))
        self.hex_receive.setObjectName("hex_receive")
        self.s2__clear_button = QtWidgets.QPushButton(Form)
        self.s2__clear_button.setGeometry(QtCore.QRect(680, 130, 61, 31))
        self.s2__clear_button.setObjectName("s2__clear_button")
        self.timer_send_cb = QtWidgets.QCheckBox(Form)
        self.timer_send_cb.setGeometry(QtCore.QRect(300, 500, 91, 16))
        self.timer_send_cb.setObjectName("timer_send_cb")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(400, 500, 61, 20))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.dw = QtWidgets.QLabel(Form)
        self.dw.setGeometry(QtCore.QRect(470, 500, 54, 20))
        self.dw.setObjectName("dw")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(270, 170, 101, 71))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(80, 30, 21, 21))
        self.label_3.setObjectName("label_3")
        self.receiveText = QtWidgets.QTextBrowser(self.groupBox)
        self.receiveText.setGeometry(QtCore.QRect(0, 30, 71, 31))
        self.receiveText.setObjectName("receiveText")
        self.logo = QtWidgets.QLabel(Form)
        self.logo.setGeometry(QtCore.QRect(30, 10, 60, 60))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo_60.png"))
        self.logo.setObjectName("logo")
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(100, 10, 481, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.title.setFont(font)
        self.title.setTextFormat(QtCore.Qt.RichText)
        self.title.setObjectName("title")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(380, 170, 101, 71))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(80, 30, 21, 21))
        self.label_4.setObjectName("label_4")
        self.receiveText_2 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.receiveText_2.setGeometry(QtCore.QRect(0, 30, 71, 31))
        self.receiveText_2.setObjectName("receiveText_2")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(490, 170, 101, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(80, 30, 21, 21))
        self.label_5.setObjectName("label_5")
        self.receiveText_3 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.receiveText_3.setGeometry(QtCore.QRect(0, 30, 71, 31))
        self.receiveText_3.setObjectName("receiveText_3")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(600, 170, 101, 71))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(80, 30, 21, 21))
        self.label_6.setObjectName("label_6")
        self.receiveText_4 = QtWidgets.QTextBrowser(self.groupBox_4)
        self.receiveText_4.setGeometry(QtCore.QRect(0, 30, 71, 31))
        self.receiveText_4.setObjectName("receiveText_4")
        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setGeometry(QtCore.QRect(710, 170, 101, 71))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(80, 30, 21, 21))
        self.label_7.setObjectName("label_7")
        self.receiveText_5 = QtWidgets.QTextBrowser(self.groupBox_5)
        self.receiveText_5.setGeometry(QtCore.QRect(0, 30, 71, 31))
        self.receiveText_5.setObjectName("receiveText_5")
        self.groupBox_6 = QtWidgets.QGroupBox(Form)
        self.groupBox_6.setGeometry(QtCore.QRect(270, 250, 101, 71))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_8 = QtWidgets.QLabel(self.groupBox_6)
        self.label_8.setGeometry(QtCore.QRect(80, 30, 21, 21))
        self.label_8.setObjectName("label_8")
        self.receiveText_6 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.receiveText_6.setGeometry(QtCore.QRect(0, 30, 71, 31))
        self.receiveText_6.setObjectName("receiveText_6")
        self.groupBox_7 = QtWidgets.QGroupBox(Form)
        self.groupBox_7.setGeometry(QtCore.QRect(380, 250, 101, 71))
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox_7)
        self.label_9.setGeometry(QtCore.QRect(80, 30, 21, 21))
        self.label_9.setObjectName("label_9")
        self.receiveText_7 = QtWidgets.QTextBrowser(self.groupBox_7)
        self.receiveText_7.setGeometry(QtCore.QRect(0, 30, 71, 31))
        self.receiveText_7.setObjectName("receiveText_7")
        self.groupBox_8 = QtWidgets.QGroupBox(Form)
        self.groupBox_8.setGeometry(QtCore.QRect(490, 250, 101, 71))
        self.groupBox_8.setObjectName("groupBox_8")
        self.label_10 = QtWidgets.QLabel(self.groupBox_8)
        self.label_10.setGeometry(QtCore.QRect(80, 30, 21, 21))
        self.label_10.setObjectName("label_10")
        self.receiveText_8 = QtWidgets.QTextBrowser(self.groupBox_8)
        self.receiveText_8.setGeometry(QtCore.QRect(0, 30, 71, 31))
        self.receiveText_8.setObjectName("receiveText_8")
        self.groupBox_9 = QtWidgets.QGroupBox(Form)
        self.groupBox_9.setGeometry(QtCore.QRect(600, 250, 101, 71))
        self.groupBox_9.setObjectName("groupBox_9")
        self.label_11 = QtWidgets.QLabel(self.groupBox_9)
        self.label_11.setGeometry(QtCore.QRect(80, 30, 21, 21))
        self.label_11.setObjectName("label_11")
        self.receiveText_9 = QtWidgets.QTextBrowser(self.groupBox_9)
        self.receiveText_9.setGeometry(QtCore.QRect(0, 30, 71, 31))
        self.receiveText_9.setObjectName("receiveText_9")
        self.groupBox_10 = QtWidgets.QGroupBox(Form)
        self.groupBox_10.setGeometry(QtCore.QRect(710, 250, 101, 71))
        self.groupBox_10.setObjectName("groupBox_10")
        self.label_12 = QtWidgets.QLabel(self.groupBox_10)
        self.label_12.setGeometry(QtCore.QRect(80, 30, 21, 21))
        self.label_12.setObjectName("label_12")
        self.receiveText_10 = QtWidgets.QTextBrowser(self.groupBox_10)
        self.receiveText_10.setGeometry(QtCore.QRect(0, 30, 71, 31))
        self.receiveText_10.setObjectName("receiveText_10")
        self.groupBox_11 = QtWidgets.QGroupBox(Form)
        self.groupBox_11.setGeometry(QtCore.QRect(270, 330, 101, 71))
        self.groupBox_11.setObjectName("groupBox_11")
        self.label_13 = QtWidgets.QLabel(self.groupBox_11)
        self.label_13.setGeometry(QtCore.QRect(80, 30, 21, 21))
        self.label_13.setObjectName("label_13")
        self.receiveText_11 = QtWidgets.QTextBrowser(self.groupBox_11)
        self.receiveText_11.setGeometry(QtCore.QRect(0, 30, 71, 31))
        self.receiveText_11.setObjectName("receiveText_11")
        self.groupBox_12 = QtWidgets.QGroupBox(Form)
        self.groupBox_12.setGeometry(QtCore.QRect(380, 330, 101, 71))
        self.groupBox_12.setObjectName("groupBox_12")
        self.label_14 = QtWidgets.QLabel(self.groupBox_12)
        self.label_14.setGeometry(QtCore.QRect(80, 30, 21, 21))
        self.label_14.setObjectName("label_14")
        self.receiveText_12 = QtWidgets.QTextBrowser(self.groupBox_12)
        self.receiveText_12.setGeometry(QtCore.QRect(0, 30, 71, 31))
        self.receiveText_12.setObjectName("receiveText_12")
        self.groupBox_13 = QtWidgets.QGroupBox(Form)
        self.groupBox_13.setGeometry(QtCore.QRect(490, 330, 101, 71))
        self.groupBox_13.setObjectName("groupBox_13")
        self.label_15 = QtWidgets.QLabel(self.groupBox_13)
        self.label_15.setGeometry(QtCore.QRect(80, 30, 21, 21))
        self.label_15.setObjectName("label_15")
        self.receiveText_13 = QtWidgets.QTextBrowser(self.groupBox_13)
        self.receiveText_13.setGeometry(QtCore.QRect(0, 30, 71, 31))
        self.receiveText_13.setObjectName("receiveText_13")
        self.groupBox_14 = QtWidgets.QGroupBox(Form)
        self.groupBox_14.setGeometry(QtCore.QRect(600, 330, 101, 71))
        self.groupBox_14.setObjectName("groupBox_14")
        self.label_16 = QtWidgets.QLabel(self.groupBox_14)
        self.label_16.setGeometry(QtCore.QRect(80, 30, 21, 21))
        self.label_16.setObjectName("label_16")
        self.receiveText_14 = QtWidgets.QTextBrowser(self.groupBox_14)
        self.receiveText_14.setGeometry(QtCore.QRect(0, 30, 71, 31))
        self.receiveText_14.setObjectName("receiveText_14")
        self.groupBox_15 = QtWidgets.QGroupBox(Form)
        self.groupBox_15.setGeometry(QtCore.QRect(710, 330, 101, 71))
        self.groupBox_15.setObjectName("groupBox_15")
        self.label_17 = QtWidgets.QLabel(self.groupBox_15)
        self.label_17.setGeometry(QtCore.QRect(80, 30, 21, 21))
        self.label_17.setObjectName("label_17")
        self.receiveText_15 = QtWidgets.QTextBrowser(self.groupBox_15)
        self.receiveText_15.setGeometry(QtCore.QRect(0, 30, 71, 31))
        self.receiveText_15.setObjectName("receiveText_15")
        self.verticalGroupBox.raise_()
        self.verticalGroupBox_2.raise_()
        self.formGroupBox.raise_()
        self.s3__send_button.raise_()
        self.s3__clear_button.raise_()
        self.formGroupBox.raise_()
        self.hex_send.raise_()
        self.hex_receive.raise_()
        self.s2__clear_button.raise_()
        self.timer_send_cb.raise_()
        self.lineEdit_3.raise_()
        self.dw.raise_()
        self.groupBox.raise_()
        self.logo.raise_()
        self.title.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox_4.raise_()
        self.groupBox_5.raise_()
        self.groupBox_6.raise_()
        self.groupBox_7.raise_()
        self.groupBox_8.raise_()
        self.groupBox_9.raise_()
        self.groupBox_10.raise_()
        self.groupBox_11.raise_()
        self.groupBox_12.raise_()
        self.groupBox_13.raise_()
        self.groupBox_14.raise_()
        self.groupBox_15.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.formGroupBox.setTitle(_translate("Form", "串口设置"))
        self.s1__lb_1.setText(_translate("Form", "串口检测："))
        self.s1__box_1.setText(_translate("Form", "检测串口"))
        self.s1__lb_2.setText(_translate("Form", "串口选择："))
        self.s1__lb_3.setText(_translate("Form", "波特率："))
        self.s1__box_3.setItemText(0, _translate("Form", "115200"))
        self.s1__box_3.setItemText(1, _translate("Form", "2400"))
        self.s1__box_3.setItemText(2, _translate("Form", "4800"))
        self.s1__box_3.setItemText(3, _translate("Form", "9600"))
        self.s1__box_3.setItemText(4, _translate("Form", "14400"))
        self.s1__box_3.setItemText(5, _translate("Form", "19200"))
        self.s1__box_3.setItemText(6, _translate("Form", "38400"))
        self.s1__box_3.setItemText(7, _translate("Form", "57600"))
        self.s1__box_3.setItemText(8, _translate("Form", "76800"))
        self.s1__box_3.setItemText(9, _translate("Form", "12800"))
        self.s1__box_3.setItemText(10, _translate("Form", "230400"))
        self.s1__box_3.setItemText(11, _translate("Form", "460800"))
        self.s1__lb_4.setText(_translate("Form", "数据位："))
        self.s1__box_4.setItemText(0, _translate("Form", "8"))
        self.s1__box_4.setItemText(1, _translate("Form", "7"))
        self.s1__box_4.setItemText(2, _translate("Form", "6"))
        self.s1__box_4.setItemText(3, _translate("Form", "5"))
        self.s1__lb_5.setText(_translate("Form", "校验位："))
        self.s1__box_5.setItemText(0, _translate("Form", "N"))
        self.s1__lb_6.setText(_translate("Form", "停止位："))
        self.s1__box_6.setItemText(0, _translate("Form", "1"))
        self.open_button.setText(_translate("Form", "打开串口"))
        self.close_button.setText(_translate("Form", "关闭串口"))
        self.verticalGroupBox.setTitle(_translate("Form", "接收区"))
        self.verticalGroupBox_2.setTitle(_translate("Form", "发送区"))
        self.s3__send_text.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:9pt;\">123456</span></p></body></html>"))
        self.s3__send_button.setText(_translate("Form", "发送"))
        self.s3__clear_button.setText(_translate("Form", "清除"))
        self.formGroupBox1.setTitle(_translate("Form", "串口状态"))
        self.label.setText(_translate("Form", "已接收："))
        self.label_2.setText(_translate("Form", "已发送："))
        self.hex_send.setText(_translate("Form", "Hex发送"))
        self.hex_receive.setText(_translate("Form", "Hex接收"))
        self.s2__clear_button.setText(_translate("Form", "清除"))
        self.timer_send_cb.setText(_translate("Form", "定时发送"))
        self.lineEdit_3.setText(_translate("Form", "1000"))
        self.dw.setText(_translate("Form", "ms/次"))
        self.groupBox.setTitle(_translate("Form", "温度1"))
        self.label_3.setText(_translate("Form", "℃"))
        self.title.setText(_translate("Form", "无源无线温度传感系统 - multiple"))
        self.groupBox_2.setTitle(_translate("Form", "温度2"))
        self.label_4.setText(_translate("Form", "℃"))
        self.groupBox_3.setTitle(_translate("Form", "温度3"))
        self.label_5.setText(_translate("Form", "℃"))
        self.groupBox_4.setTitle(_translate("Form", "温度4"))
        self.label_6.setText(_translate("Form", "℃"))
        self.groupBox_5.setTitle(_translate("Form", "温度5"))
        self.label_7.setText(_translate("Form", "℃"))
        self.groupBox_6.setTitle(_translate("Form", "温度6"))
        self.label_8.setText(_translate("Form", "℃"))
        self.groupBox_7.setTitle(_translate("Form", "温度7"))
        self.label_9.setText(_translate("Form", "℃"))
        self.groupBox_8.setTitle(_translate("Form", "温度8"))
        self.label_10.setText(_translate("Form", "℃"))
        self.groupBox_9.setTitle(_translate("Form", "温度9"))
        self.label_11.setText(_translate("Form", "℃"))
        self.groupBox_10.setTitle(_translate("Form", "温度10"))
        self.label_12.setText(_translate("Form", "℃"))
        self.groupBox_11.setTitle(_translate("Form", "温度11"))
        self.label_13.setText(_translate("Form", "℃"))
        self.groupBox_12.setTitle(_translate("Form", "温度12"))
        self.label_14.setText(_translate("Form", "℃"))
        self.groupBox_13.setTitle(_translate("Form", "温度13"))
        self.label_15.setText(_translate("Form", "℃"))
        self.groupBox_14.setTitle(_translate("Form", "温度14"))
        self.label_16.setText(_translate("Form", "℃"))
        self.groupBox_15.setTitle(_translate("Form", "温度15"))
        self.label_17.setText(_translate("Form", "℃"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())