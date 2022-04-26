# Form implementation generated from reading ui file 'saw_single_ui.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo_343x60.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Heiti SC")
        font.setPointSize(18)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.South)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 241, 201))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 58, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 58, 16))
        self.label_4.setObjectName("label_4")
        self.s1__box_1 = QtWidgets.QPushButton(self.groupBox)
        self.s1__box_1.setGeometry(QtCore.QRect(90, 30, 141, 41))
        self.s1__box_1.setObjectName("s1__box_1")
        self.s1__box_2 = QtWidgets.QComboBox(self.groupBox)
        self.s1__box_2.setGeometry(QtCore.QRect(90, 80, 141, 31))
        self.s1__box_2.setObjectName("s1__box_2")
        self.state_label = QtWidgets.QLabel(self.groupBox)
        self.state_label.setGeometry(QtCore.QRect(20, 120, 211, 21))
        self.state_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.state_label.setObjectName("state_label")
        self.open_button = QtWidgets.QPushButton(self.groupBox)
        self.open_button.setGeometry(QtCore.QRect(10, 150, 100, 41))
        self.open_button.setObjectName("open_button")
        self.close_button = QtWidgets.QPushButton(self.groupBox)
        self.close_button.setGeometry(QtCore.QRect(130, 150, 100, 41))
        self.close_button.setObjectName("close_button")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_6.setGeometry(QtCore.QRect(280, 10, 201, 71))
        self.groupBox_6.setObjectName("groupBox_6")
        self.receiveText_2 = QtWidgets.QTextBrowser(self.groupBox_6)
        self.receiveText_2.setGeometry(QtCore.QRect(10, 30, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.receiveText_2.setFont(font)
        self.receiveText_2.setObjectName("receiveText_2")
        self.label_12 = QtWidgets.QLabel(self.groupBox_6)
        self.label_12.setGeometry(QtCore.QRect(180, 30, 31, 20))
        self.label_12.setObjectName("label_12")
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_7.setGeometry(QtCore.QRect(640, 10, 201, 71))
        self.groupBox_7.setObjectName("groupBox_7")
        self.receiveText = QtWidgets.QTextBrowser(self.groupBox_7)
        self.receiveText.setGeometry(QtCore.QRect(10, 30, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        self.receiveText.setFont(font)
        self.receiveText.setObjectName("receiveText")
        self.label_13 = QtWidgets.QLabel(self.groupBox_7)
        self.label_13.setGeometry(QtCore.QRect(180, 30, 21, 16))
        self.label_13.setObjectName("label_13")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 220, 241, 111))
        self.groupBox_8.setObjectName("groupBox_8")
        self.testButton = QtWidgets.QPushButton(self.groupBox_8)
        self.testButton.setGeometry(QtCore.QRect(70, 30, 100, 41))
        self.testButton.setObjectName("testButton")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_8)
        self.progressBar.setGeometry(QtCore.QRect(7, 80, 221, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.groupBox_15 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_15.setGeometry(QtCore.QRect(10, 340, 241, 80))
        self.groupBox_15.setObjectName("groupBox_15")
        self.monitorButton = QtWidgets.QPushButton(self.groupBox_15)
        self.monitorButton.setGeometry(QtCore.QRect(10, 30, 100, 41))
        self.monitorButton.setObjectName("monitorButton")
        self.stopMonitorButton = QtWidgets.QPushButton(self.groupBox_15)
        self.stopMonitorButton.setGeometry(QtCore.QRect(130, 30, 100, 41))
        self.stopMonitorButton.setObjectName("stopMonitorButton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 90, 701, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.plotDataViewVerticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.plotDataViewVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.plotDataViewVerticalLayout.setObjectName("plotDataViewVerticalLayout")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 10, 231, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(70, 190, 100, 32))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 181, 136))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.s1__box_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.s1__box_3.setObjectName("s1__box_3")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.s1__box_3.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.s1__box_3)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.s1__box_4 = QtWidgets.QComboBox(self.layoutWidget)
        self.s1__box_4.setObjectName("s1__box_4")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.s1__box_4.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.s1__box_4)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.s1__box_5 = QtWidgets.QComboBox(self.layoutWidget)
        self.s1__box_5.setObjectName("s1__box_5")
        self.s1__box_5.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.s1__box_5)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.s1__box_6 = QtWidgets.QComboBox(self.layoutWidget)
        self.s1__box_6.setObjectName("s1__box_6")
        self.s1__box_6.addItem("")
        self.s1__box_6.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.s1__box_6)
        self.formGroupBox = QtWidgets.QGroupBox(self.tab_2)
        self.formGroupBox.setGeometry(QtCore.QRect(9, 250, 231, 121))
        self.formGroupBox.setObjectName("formGroupBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.formGroupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 40, 211, 54))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(9, 380, 231, 231))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 30, 211, 80))
        self.groupBox_4.setObjectName("groupBox_4")
        self.s3__send_text = QtWidgets.QTextEdit(self.groupBox_4)
        self.s3__send_text.setGeometry(QtCore.QRect(10, 30, 181, 31))
        self.s3__send_text.setObjectName("s3__send_text")
        self.timer_send_cb = QtWidgets.QCheckBox(self.groupBox_3)
        self.timer_send_cb.setGeometry(QtCore.QRect(10, 130, 85, 20))
        self.timer_send_cb.setObjectName("timer_send_cb")
        self.hex_send = QtWidgets.QCheckBox(self.groupBox_3)
        self.hex_send.setGeometry(QtCore.QRect(140, 130, 85, 20))
        self.hex_send.setObjectName("hex_send")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 160, 71, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(110, 160, 58, 16))
        self.label_11.setObjectName("label_11")
        self.s3__send_button = QtWidgets.QPushButton(self.groupBox_3)
        self.s3__send_button.setGeometry(QtCore.QRect(10, 190, 100, 32))
        self.s3__send_button.setObjectName("s3__send_button")
        self.s3__clear_button = QtWidgets.QPushButton(self.groupBox_3)
        self.s3__clear_button.setGeometry(QtCore.QRect(120, 190, 100, 32))
        self.s3__clear_button.setObjectName("s3__clear_button")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(250, 10, 240, 141))
        self.groupBox_5.setObjectName("groupBox_5")
        self.s2__receive_text = QtWidgets.QTextBrowser(self.groupBox_5)
        self.s2__receive_text.setGeometry(QtCore.QRect(20, 30, 201, 41))
        self.s2__receive_text.setObjectName("s2__receive_text")
        self.hex_receive = QtWidgets.QCheckBox(self.groupBox_5)
        self.hex_receive.setGeometry(QtCore.QRect(20, 80, 85, 20))
        self.hex_receive.setChecked(False)
        self.hex_receive.setObjectName("hex_receive")
        self.s2__clear_button = QtWidgets.QPushButton(self.groupBox_5)
        self.s2__clear_button.setGeometry(QtCore.QRect(70, 100, 100, 32))
        self.s2__clear_button.setObjectName("s2__clear_button")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_9.setGeometry(QtCore.QRect(510, 10, 241, 80))
        self.groupBox_9.setObjectName("groupBox_9")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_9)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 221, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_10.setGeometry(QtCore.QRect(510, 100, 241, 211))
        self.groupBox_10.setObjectName("groupBox_10")
        self.sendFreqButton = QtWidgets.QPushButton(self.groupBox_10)
        self.sendFreqButton.setGeometry(QtCore.QRect(70, 160, 100, 32))
        self.sendFreqButton.setObjectName("sendFreqButton")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_10)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 30, 221, 116))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.layoutWidget2)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setItalic(False)
        font.setUnderline(False)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_14)
        self.textEditStartFreq = QtWidgets.QLineEdit(self.layoutWidget2)
        self.textEditStartFreq.setObjectName("textEditStartFreq")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEditStartFreq)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_15.setObjectName("label_15")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_15)
        self.textEditEndFreq = QtWidgets.QLineEdit(self.layoutWidget2)
        self.textEditEndFreq.setObjectName("textEditEndFreq")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEditEndFreq)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_16.setObjectName("label_16")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_16)
        self.textEditEndFreq_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.textEditEndFreq_2.setObjectName("textEditEndFreq_2")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEditEndFreq_2)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_17)
        self.rssiThreshold_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.rssiThreshold_2.setObjectName("rssiThreshold_2")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.rssiThreshold_2)
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_11.setGeometry(QtCore.QRect(510, 320, 241, 141))
        self.groupBox_11.setObjectName("groupBox_11")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_11)
        self.checkBox.setGeometry(QtCore.QRect(20, 30, 201, 20))
        self.checkBox.setObjectName("checkBox")
        self.label_18 = QtWidgets.QLabel(self.groupBox_11)
        self.label_18.setGeometry(QtCore.QRect(20, 60, 58, 16))
        self.label_18.setObjectName("label_18")
        self.freqChange = QtWidgets.QLineEdit(self.groupBox_11)
        self.freqChange.setGeometry(QtCore.QRect(60, 60, 131, 21))
        self.freqChange.setObjectName("freqChange")
        self.label_19 = QtWidgets.QLabel(self.groupBox_11)
        self.label_19.setGeometry(QtCore.QRect(200, 60, 31, 16))
        self.label_19.setObjectName("label_19")
        self.sendFreqRangeButton = QtWidgets.QPushButton(self.groupBox_11)
        self.sendFreqRangeButton.setGeometry(QtCore.QRect(70, 100, 100, 32))
        self.sendFreqRangeButton.setObjectName("sendFreqRangeButton")
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_12.setGeometry(QtCore.QRect(760, 10, 231, 421))
        self.groupBox_12.setObjectName("groupBox_12")
        self.evalModelButton = QtWidgets.QPushButton(self.groupBox_12)
        self.evalModelButton.setGeometry(QtCore.QRect(29, 340, 171, 32))
        self.evalModelButton.setObjectName("evalModelButton")
        self.label_33 = QtWidgets.QLabel(self.groupBox_12)
        self.label_33.setGeometry(QtCore.QRect(20, 380, 61, 16))
        self.label_33.setObjectName("label_33")
        self.R2Text = QtWidgets.QTextBrowser(self.groupBox_12)
        self.R2Text.setGeometry(QtCore.QRect(90, 380, 121, 31))
        self.R2Text.setObjectName("R2Text")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_12)
        self.layoutWidget3.setGeometry(QtCore.QRect(22, 34, 191, 302))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.layoutWidget3)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_20 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_20.setObjectName("label_20")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_20)
        self.firstFreq = QtWidgets.QLineEdit(self.layoutWidget3)
        self.firstFreq.setPlaceholderText("")
        self.firstFreq.setObjectName("firstFreq")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.firstFreq)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_21.setObjectName("label_21")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_21)
        self.firstTemp = QtWidgets.QLineEdit(self.layoutWidget3)
        self.firstTemp.setPlaceholderText("")
        self.firstTemp.setObjectName("firstTemp")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.firstTemp)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_22.setObjectName("label_22")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_22)
        self.secondFreq = QtWidgets.QLineEdit(self.layoutWidget3)
        self.secondFreq.setPlaceholderText("")
        self.secondFreq.setObjectName("secondFreq")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.secondFreq)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_23.setObjectName("label_23")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_23)
        self.secondTemp = QtWidgets.QLineEdit(self.layoutWidget3)
        self.secondTemp.setPlaceholderText("")
        self.secondTemp.setObjectName("secondTemp")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.secondTemp)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_24.setObjectName("label_24")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_24)
        self.thirdFreq = QtWidgets.QLineEdit(self.layoutWidget3)
        self.thirdFreq.setPlaceholderText("")
        self.thirdFreq.setObjectName("thirdFreq")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.thirdFreq)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_25.setObjectName("label_25")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_25)
        self.thirdTemp = QtWidgets.QLineEdit(self.layoutWidget3)
        self.thirdTemp.setPlaceholderText("")
        self.thirdTemp.setObjectName("thirdTemp")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.thirdTemp)
        self.label_30 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_30.setObjectName("label_30")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_30)
        self.fourthFreq = QtWidgets.QLineEdit(self.layoutWidget3)
        self.fourthFreq.setPlaceholderText("")
        self.fourthFreq.setObjectName("fourthFreq")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fourthFreq)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_26.setObjectName("label_26")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_26)
        self.fourthTemp = QtWidgets.QLineEdit(self.layoutWidget3)
        self.fourthTemp.setPlaceholderText("")
        self.fourthTemp.setObjectName("fourthTemp")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fourthTemp)
        self.label_32 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_32.setObjectName("label_32")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_32)
        self.fifthFreq = QtWidgets.QLineEdit(self.layoutWidget3)
        self.fifthFreq.setPlaceholderText("")
        self.fifthFreq.setObjectName("fifthFreq")
        self.formLayout_4.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fifthFreq)
        self.label_31 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_31.setObjectName("label_31")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_31)
        self.fifthTemp = QtWidgets.QLineEdit(self.layoutWidget3)
        self.fifthTemp.setPlaceholderText("")
        self.fifthTemp.setObjectName("fifthTemp")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fifthTemp)
        self.groupBox_13 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_13.setGeometry(QtCore.QRect(250, 170, 241, 61))
        self.groupBox_13.setObjectName("groupBox_13")
        self.save2FileRealTime = QtWidgets.QCheckBox(self.groupBox_13)
        self.save2FileRealTime.setGeometry(QtCore.QRect(10, 30, 211, 20))
        self.save2FileRealTime.setObjectName("save2FileRealTime")
        self.groupBox_14 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_14.setGeometry(QtCore.QRect(510, 540, 241, 80))
        self.groupBox_14.setObjectName("groupBox_14")
        self.saveTempAndFreq = QtWidgets.QPushButton(self.groupBox_14)
        self.saveTempAndFreq.setGeometry(QtCore.QRect(30, 30, 181, 32))
        self.saveTempAndFreq.setObjectName("saveTempAndFreq")
        self.debugButton = QtWidgets.QPushButton(self.tab_2)
        self.debugButton.setGeometry(QtCore.QRect(540, 480, 171, 51))
        self.debugButton.setObjectName("debugButton")
        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(493, 0, 16, 631))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.groupBox_16 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_16.setGeometry(QtCore.QRect(760, 440, 231, 181))
        self.groupBox_16.setObjectName("groupBox_16")
        self.groupBox_17 = QtWidgets.QGroupBox(self.groupBox_16)
        self.groupBox_17.setGeometry(QtCore.QRect(-1, 20, 111, 111))
        self.groupBox_17.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_17.setObjectName("groupBox_17")
        self.intercept_a = QtWidgets.QLineEdit(self.groupBox_17)
        self.intercept_a.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.intercept_a.setObjectName("intercept_a")
        self.slope_2_a = QtWidgets.QLineEdit(self.groupBox_17)
        self.slope_2_a.setGeometry(QtCore.QRect(10, 80, 91, 21))
        self.slope_2_a.setObjectName("slope_2_a")
        self.slope_1_a = QtWidgets.QLineEdit(self.groupBox_17)
        self.slope_1_a.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.slope_1_a.setObjectName("slope_1_a")
        self.groupBox_18 = QtWidgets.QGroupBox(self.groupBox_16)
        self.groupBox_18.setGeometry(QtCore.QRect(120, 20, 111, 111))
        self.groupBox_18.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_18.setObjectName("groupBox_18")
        self.intercept_b = QtWidgets.QLineEdit(self.groupBox_18)
        self.intercept_b.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.intercept_b.setObjectName("intercept_b")
        self.slope_1_b = QtWidgets.QLineEdit(self.groupBox_18)
        self.slope_1_b.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.slope_1_b.setObjectName("slope_1_b")
        self.slope_2_b = QtWidgets.QLineEdit(self.groupBox_18)
        self.slope_2_b.setGeometry(QtCore.QRect(10, 80, 91, 21))
        self.slope_2_b.setObjectName("slope_2_b")
        self.pushButton_a = QtWidgets.QPushButton(self.groupBox_16)
        self.pushButton_a.setGeometry(QtCore.QRect(10, 140, 91, 32))
        self.pushButton_a.setObjectName("pushButton_a")
        self.pushButton_b = QtWidgets.QPushButton(self.groupBox_16)
        self.pushButton_b.setGeometry(QtCore.QRect(130, 140, 91, 32))
        self.pushButton_b.setObjectName("pushButton_b")
        self.line_2 = QtWidgets.QFrame(self.groupBox_16)
        self.line_2.setGeometry(QtCore.QRect(107, 20, 16, 161))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.groupBox_19 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_19.setEnabled(True)
        self.groupBox_19.setGeometry(QtCore.QRect(250, 250, 241, 71))
        self.groupBox_19.setObjectName("groupBox_19")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_19)
        self.spinBox.setGeometry(QtCore.QRect(20, 30, 201, 22))
        self.spinBox.setMinimum(10)
        self.spinBox.setMaximum(600)
        self.spinBox.setSingleStep(10)
        self.spinBox.setProperty("value", 300)
        self.spinBox.setObjectName("spinBox")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionQuick_Start = QtGui.QAction(MainWindow)
        self.actionQuick_Start.setObjectName("actionQuick_Start")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "无源无线温度传感系统"))
        self.groupBox.setTitle(_translate("MainWindow", "Step 1: 串口连接"))
        self.label_3.setText(_translate("MainWindow", "串口检测："))
        self.label_4.setText(_translate("MainWindow", "串口选择："))
        self.s1__box_1.setText(_translate("MainWindow", "检测串口"))
        self.state_label.setText(_translate("MainWindow", "串口未选择"))
        self.open_button.setText(_translate("MainWindow", "打开串口"))
        self.close_button.setText(_translate("MainWindow", "关闭串口"))
        self.groupBox_6.setTitle(_translate("MainWindow", "实时频率"))
        self.label_12.setText(_translate("MainWindow", "Hz"))
        self.groupBox_7.setTitle(_translate("MainWindow", "实时温度"))
        self.label_13.setText(_translate("MainWindow", "℃"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Step 2: 初始化扫描"))
        self.testButton.setText(_translate("MainWindow", "开始测试"))
        self.groupBox_15.setTitle(_translate("MainWindow", "Step 3: 连续监测"))
        self.monitorButton.setText(_translate("MainWindow", "开始测试"))
        self.stopMonitorButton.setText(_translate("MainWindow", "停止测试"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "主窗口"))
        self.groupBox_2.setTitle(_translate("MainWindow", "串口设置"))
        self.pushButton.setText(_translate("MainWindow", "写入参数"))
        self.label_5.setText(_translate("MainWindow", "波特率："))
        self.s1__box_3.setItemText(0, _translate("MainWindow", "115200"))
        self.s1__box_3.setItemText(1, _translate("MainWindow", "57600"))
        self.s1__box_3.setItemText(2, _translate("MainWindow", "38400"))
        self.s1__box_3.setItemText(3, _translate("MainWindow", "19200"))
        self.s1__box_3.setItemText(4, _translate("MainWindow", "9600"))
        self.label_6.setText(_translate("MainWindow", "数据位："))
        self.s1__box_4.setItemText(0, _translate("MainWindow", "8"))
        self.s1__box_4.setItemText(1, _translate("MainWindow", "7"))
        self.s1__box_4.setItemText(2, _translate("MainWindow", "6"))
        self.s1__box_4.setItemText(3, _translate("MainWindow", "5"))
        self.label_7.setText(_translate("MainWindow", "校检位："))
        self.s1__box_5.setItemText(0, _translate("MainWindow", "N"))
        self.label_8.setText(_translate("MainWindow", "停止位："))
        self.s1__box_6.setCurrentText(_translate("MainWindow", "1"))
        self.s1__box_6.setItemText(0, _translate("MainWindow", "1"))
        self.s1__box_6.setItemText(1, _translate("MainWindow", "2"))
        self.formGroupBox.setTitle(_translate("MainWindow", "串口状态"))
        self.label_9.setText(_translate("MainWindow", "已接收："))
        self.label_10.setText(_translate("MainWindow", "已发送："))
        self.groupBox_3.setTitle(_translate("MainWindow", "发送区"))
        self.groupBox_4.setTitle(_translate("MainWindow", "发送内容"))
        self.timer_send_cb.setText(_translate("MainWindow", "定时发送"))
        self.hex_send.setText(_translate("MainWindow", "Hex发送"))
        self.lineEdit_3.setText(_translate("MainWindow", "1000"))
        self.label_11.setText(_translate("MainWindow", "ms/次"))
        self.s3__send_button.setText(_translate("MainWindow", "发送"))
        self.s3__clear_button.setText(_translate("MainWindow", "清除"))
        self.groupBox_5.setTitle(_translate("MainWindow", "接收区"))
        self.hex_receive.setText(_translate("MainWindow", "Hex接收"))
        self.s2__clear_button.setText(_translate("MainWindow", "清除"))
        self.groupBox_9.setTitle(_translate("MainWindow", "工作模式"))
        self.comboBox.setItemText(0, _translate("MainWindow", "单天线功率检波"))
        self.comboBox.setItemText(1, _translate("MainWindow", "双天线功率检波"))
        self.groupBox_10.setTitle(_translate("MainWindow", "频率（MHz）和 RSSI 阈值设置"))
        self.sendFreqButton.setText(_translate("MainWindow", "写入参数"))
        self.label_14.setText(_translate("MainWindow", "开始频率："))
        self.label_15.setText(_translate("MainWindow", "结束频率："))
        self.label_16.setText(_translate("MainWindow", "RSSI阈值："))
        self.label_17.setText(_translate("MainWindow", "阈值范围："))
        self.groupBox_11.setTitle(_translate("MainWindow", "扫频跟随"))
        self.checkBox.setText(_translate("MainWindow", "跟随谐振频率变化（实时生效）"))
        self.label_18.setText(_translate("MainWindow", "Span:"))
        self.label_19.setText(_translate("MainWindow", "MHz"))
        self.sendFreqRangeButton.setText(_translate("MainWindow", "写入span参数"))
        self.groupBox_12.setTitle(_translate("MainWindow", "校准（Hz; ℃）"))
        self.evalModelButton.setText(_translate("MainWindow", "计算简易模型参数"))
        self.label_33.setText(_translate("MainWindow", "模型R2:"))
        self.R2Text.setPlaceholderText(_translate("MainWindow", "模型未计算"))
        self.label_20.setText(_translate("MainWindow", "频率1："))
        self.label_21.setText(_translate("MainWindow", "温度1："))
        self.label_22.setText(_translate("MainWindow", "频率2："))
        self.label_23.setText(_translate("MainWindow", "温度2："))
        self.label_24.setText(_translate("MainWindow", "频率3："))
        self.label_25.setText(_translate("MainWindow", "温度3："))
        self.label_30.setText(_translate("MainWindow", "频率4："))
        self.label_26.setText(_translate("MainWindow", "温度4："))
        self.label_32.setText(_translate("MainWindow", "频率5："))
        self.label_31.setText(_translate("MainWindow", "温度5："))
        self.groupBox_13.setTitle(_translate("MainWindow", "实时保存"))
        self.save2FileRealTime.setText(_translate("MainWindow", "实时保存数据"))
        self.groupBox_14.setTitle(_translate("MainWindow", "手动保存数据"))
        self.saveTempAndFreq.setText(_translate("MainWindow", "保存该单次测试数据"))
        self.debugButton.setText(_translate("MainWindow", "单次测试"))
        self.groupBox_16.setTitle(_translate("MainWindow", "模型参数"))
        self.groupBox_17.setTitle(_translate("MainWindow", "初始模型参数"))
        self.intercept_a.setPlaceholderText(_translate("MainWindow", "intercept"))
        self.slope_2_a.setPlaceholderText(_translate("MainWindow", "slope 2"))
        self.slope_1_a.setPlaceholderText(_translate("MainWindow", "slope 1"))
        self.groupBox_18.setTitle(_translate("MainWindow", "简易模型参数"))
        self.intercept_b.setPlaceholderText(_translate("MainWindow", "intercept"))
        self.slope_1_b.setPlaceholderText(_translate("MainWindow", "slope 1"))
        self.slope_2_b.setPlaceholderText(_translate("MainWindow", "slope 2"))
        self.pushButton_a.setText(_translate("MainWindow", "写入参数"))
        self.pushButton_b.setText(_translate("MainWindow", "写入参数"))
        self.groupBox_19.setTitle(_translate("MainWindow", "实时温度曲线数据点上限"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "设置"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionQuick_Start.setText(_translate("MainWindow", "Quick_Start"))