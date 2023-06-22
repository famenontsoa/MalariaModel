# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 504)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(480, 0))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBoxInputParam = QtWidgets.QGroupBox(self.page_1)
        font = QtGui.QFont()
        font.setBold(True)
        self.groupBoxInputParam.setFont(font)
        self.groupBoxInputParam.setObjectName("groupBoxInputParam")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxInputParam)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_rainFileName = QtWidgets.QLabel(self.groupBoxInputParam)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_rainFileName.setFont(font)
        self.label_rainFileName.setObjectName("label_rainFileName")
        self.gridLayout_2.addWidget(self.label_rainFileName, 3, 1, 1, 1)
        self.parcelFileName = QtWidgets.QLineEdit(self.groupBoxInputParam)
        self.parcelFileName.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        self.parcelFileName.setFont(font)
        self.parcelFileName.setObjectName("parcelFileName")
        self.gridLayout_2.addWidget(self.parcelFileName, 1, 2, 1, 1)
        self.btn_parcelFileName = QtWidgets.QToolButton(self.groupBoxInputParam)
        self.btn_parcelFileName.setObjectName("btn_parcelFileName")
        self.gridLayout_2.addWidget(self.btn_parcelFileName, 1, 4, 1, 1)
        self.tempFileName = QtWidgets.QLineEdit(self.groupBoxInputParam)
        self.tempFileName.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        self.tempFileName.setFont(font)
        self.tempFileName.setObjectName("tempFileName")
        self.gridLayout_2.addWidget(self.tempFileName, 4, 2, 1, 1)
        self.label_parcelFileName = QtWidgets.QLabel(self.groupBoxInputParam)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_parcelFileName.setFont(font)
        self.label_parcelFileName.setObjectName("label_parcelFileName")
        self.gridLayout_2.addWidget(self.label_parcelFileName, 1, 1, 1, 1)
        self.label_tempFileName = QtWidgets.QLabel(self.groupBoxInputParam)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_tempFileName.setFont(font)
        self.label_tempFileName.setObjectName("label_tempFileName")
        self.gridLayout_2.addWidget(self.label_tempFileName, 4, 1, 1, 1)
        self.btn_tempFileName = QtWidgets.QToolButton(self.groupBoxInputParam)
        self.btn_tempFileName.setObjectName("btn_tempFileName")
        self.gridLayout_2.addWidget(self.btn_tempFileName, 4, 4, 1, 1)
        self.rainFileName = QtWidgets.QLineEdit(self.groupBoxInputParam)
        self.rainFileName.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        self.rainFileName.setFont(font)
        self.rainFileName.setObjectName("rainFileName")
        self.gridLayout_2.addWidget(self.rainFileName, 3, 2, 1, 1)
        self.btn_rainFileName = QtWidgets.QToolButton(self.groupBoxInputParam)
        self.btn_rainFileName.setObjectName("btn_rainFileName")
        self.gridLayout_2.addWidget(self.btn_rainFileName, 3, 4, 1, 1)
        self.gridLayout_3.addWidget(self.groupBoxInputParam, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_1)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QtCore.QSize(310, 120))
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.gridLayout_6.addWidget(self.tableWidget, 8, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_add_gite = QtWidgets.QToolButton(self.groupBox_2)
        self.btn_add_gite.setObjectName("btn_add_gite")
        self.verticalLayout.addWidget(self.btn_add_gite)
        self.btn_delete_gite = QtWidgets.QToolButton(self.groupBox_2)
        self.btn_delete_gite.setObjectName("btn_delete_gite")
        self.verticalLayout.addWidget(self.btn_delete_gite)
        self.gridLayout_6.addLayout(self.verticalLayout, 7, 2, 1, 1)
        self.table_gites = QtWidgets.QTableWidget(self.groupBox_2)
        self.table_gites.setEnabled(True)
        self.table_gites.setMaximumSize(QtCore.QSize(310, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        self.table_gites.setFont(font)
        self.table_gites.setObjectName("table_gites")
        self.table_gites.setColumnCount(0)
        self.table_gites.setRowCount(0)
        self.gridLayout_6.addWidget(self.table_gites, 7, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.page_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.edate = QtWidgets.QDateEdit(self.groupBox)
        self.edate.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        self.edate.setFont(font)
        self.edate.setCalendarPopup(True)
        self.edate.setObjectName("edate")
        self.gridLayout.addWidget(self.edate, 5, 3, 1, 1)
        self.label_frequence_display = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_frequence_display.setFont(font)
        self.label_frequence_display.setObjectName("label_frequence_display")
        self.gridLayout.addWidget(self.label_frequence_display, 4, 0, 1, 1)
        self.frequence = QtWidgets.QComboBox(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        self.frequence.setFont(font)
        self.frequence.setObjectName("frequence")
        self.gridLayout.addWidget(self.frequence, 4, 2, 1, 2)
        self.label_edate = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_edate.setFont(font)
        self.label_edate.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_edate.setObjectName("label_edate")
        self.gridLayout.addWidget(self.label_edate, 5, 2, 1, 1)
        self.lastdate = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        self.lastdate.setFont(font)
        self.lastdate.setObjectName("lastdate")
        self.gridLayout.addWidget(self.lastdate, 2, 1, 1, 1)
        self.btn_pathOutput = QtWidgets.QToolButton(self.groupBox)
        self.btn_pathOutput.setObjectName("btn_pathOutput")
        self.gridLayout.addWidget(self.btn_pathOutput, 1, 4, 1, 1)
        self.label_result_type = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_result_type.setFont(font)
        self.label_result_type.setObjectName("label_result_type")
        self.gridLayout.addWidget(self.label_result_type, 2, 0, 1, 1)
        self.outputKML = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        self.outputKML.setFont(font)
        self.outputKML.setObjectName("outputKML")
        self.gridLayout.addWidget(self.outputKML, 8, 3, 1, 1)
        self.label_bdate_output = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_bdate_output.setFont(font)
        self.label_bdate_output.setObjectName("label_bdate_output")
        self.gridLayout.addWidget(self.label_bdate_output, 5, 0, 1, 1)
        self.label_output_format = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_output_format.setFont(font)
        self.label_output_format.setObjectName("label_output_format")
        self.gridLayout.addWidget(self.label_output_format, 8, 0, 1, 1)
        self.label_pathOutput = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_pathOutput.setFont(font)
        self.label_pathOutput.setObjectName("label_pathOutput")
        self.gridLayout.addWidget(self.label_pathOutput, 1, 0, 1, 1)
        self.outputSHP = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        self.outputSHP.setFont(font)
        self.outputSHP.setObjectName("outputSHP")
        self.gridLayout.addWidget(self.outputSHP, 8, 1, 1, 1)
        self.multidate = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        self.multidate.setFont(font)
        self.multidate.setObjectName("multidate")
        self.gridLayout.addWidget(self.multidate, 2, 2, 1, 1)
        self.outputCSV = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        self.outputCSV.setFont(font)
        self.outputCSV.setObjectName("outputCSV")
        self.gridLayout.addWidget(self.outputCSV, 8, 2, 1, 1)
        self.pathOutput = QtWidgets.QLineEdit(self.groupBox)
        self.pathOutput.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        self.pathOutput.setFont(font)
        self.pathOutput.setObjectName("pathOutput")
        self.gridLayout.addWidget(self.pathOutput, 1, 1, 1, 3)
        self.frequence_display = QtWidgets.QSpinBox(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        self.frequence_display.setFont(font)
        self.frequence_display.setMinimum(1)
        self.frequence_display.setObjectName("frequence_display")
        self.gridLayout.addWidget(self.frequence_display, 4, 1, 1, 1)
        self.bdate_output = QtWidgets.QDateEdit(self.groupBox)
        self.bdate_output.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        self.bdate_output.setFont(font)
        self.bdate_output.setCalendarPopup(True)
        self.bdate_output.setObjectName("bdate_output")
        self.gridLayout.addWidget(self.bdate_output, 5, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 1, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_date_intro = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_date_intro.setFont(font)
        self.label_date_intro.setObjectName("label_date_intro")
        self.gridLayout_10.addWidget(self.label_date_intro, 1, 0, 1, 1)
        self.date_intro = QtWidgets.QDateEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        self.date_intro.setFont(font)
        self.date_intro.setObjectName("date_intro")
        self.gridLayout_10.addWidget(self.date_intro, 1, 1, 1, 1)
        self.label_pers_infectes = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_pers_infectes.setFont(font)
        self.label_pers_infectes.setObjectName("label_pers_infectes")
        self.gridLayout_10.addWidget(self.label_pers_infectes, 0, 0, 1, 1)
        self.nb_pers_infectes = QtWidgets.QSpinBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setBold(False)
        self.nb_pers_infectes.setFont(font)
        self.nb_pers_infectes.setMinimum(1)
        self.nb_pers_infectes.setObjectName("nb_pers_infectes")
        self.gridLayout_10.addWidget(self.nb_pers_infectes, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_4, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_parcelFileName_2 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_parcelFileName_2.setFont(font)
        self.label_parcelFileName_2.setObjectName("label_parcelFileName_2")
        self.gridLayout_7.addWidget(self.label_parcelFileName_2, 0, 1, 1, 1)
        self.label_rainFileName_2 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_rainFileName_2.setFont(font)
        self.label_rainFileName_2.setObjectName("label_rainFileName_2")
        self.gridLayout_7.addWidget(self.label_rainFileName_2, 1, 1, 1, 1)
        self.btn_cancel = QtWidgets.QPushButton(self.page)
        self.btn_cancel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout_7.addWidget(self.btn_cancel, 29, 3, 1, 1)
        self.edate_2 = QtWidgets.QDateEdit(self.page)
        self.edate_2.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        self.edate_2.setFont(font)
        self.edate_2.setCalendarPopup(True)
        self.edate_2.setObjectName("edate_2")
        self.gridLayout_7.addWidget(self.edate_2, 11, 3, 1, 1)
        self.label_pathOutput_2 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_pathOutput_2.setFont(font)
        self.label_pathOutput_2.setObjectName("label_pathOutput_2")
        self.gridLayout_7.addWidget(self.label_pathOutput_2, 7, 1, 1, 1)
        self.btn_execute = QtWidgets.QPushButton(self.page)
        self.btn_execute.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_execute.setObjectName("btn_execute")
        self.gridLayout_7.addWidget(self.btn_execute, 29, 1, 1, 1)
        self.label_output_format_2 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_output_format_2.setFont(font)
        self.label_output_format_2.setObjectName("label_output_format_2")
        self.gridLayout_7.addWidget(self.label_output_format_2, 28, 1, 1, 1)
        self.output_format_2 = QtWidgets.QLineEdit(self.page)
        self.output_format_2.setEnabled(False)
        self.output_format_2.setObjectName("output_format_2")
        self.gridLayout_7.addWidget(self.output_format_2, 28, 3, 1, 1)
        self.label_frequence_display_2 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_frequence_display_2.setFont(font)
        self.label_frequence_display_2.setObjectName("label_frequence_display_2")
        self.gridLayout_7.addWidget(self.label_frequence_display_2, 8, 1, 1, 1)
        self.label_tempFileName_2 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_tempFileName_2.setFont(font)
        self.label_tempFileName_2.setObjectName("label_tempFileName_2")
        self.gridLayout_7.addWidget(self.label_tempFileName_2, 2, 1, 1, 1)
        self.bdate_output_2 = QtWidgets.QDateEdit(self.page)
        self.bdate_output_2.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        self.bdate_output_2.setFont(font)
        self.bdate_output_2.setCalendarPopup(True)
        self.bdate_output_2.setObjectName("bdate_output_2")
        self.gridLayout_7.addWidget(self.bdate_output_2, 10, 3, 1, 1)
        self.label_edate_2 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_edate_2.setFont(font)
        self.label_edate_2.setObjectName("label_edate_2")
        self.gridLayout_7.addWidget(self.label_edate_2, 11, 1, 1, 1)
        self.label_bdate_output_2 = QtWidgets.QLabel(self.page)
        font = QtGui.QFont()
        font.setBold(False)
        self.label_bdate_output_2.setFont(font)
        self.label_bdate_output_2.setObjectName("label_bdate_output_2")
        self.gridLayout_7.addWidget(self.label_bdate_output_2, 10, 1, 1, 1)
        self.frequence_2 = QtWidgets.QLineEdit(self.page)
        self.frequence_2.setEnabled(False)
        self.frequence_2.setObjectName("frequence_2")
        self.gridLayout_7.addWidget(self.frequence_2, 8, 4, 1, 1)
        self.parcelFileName_2 = QtWidgets.QLineEdit(self.page)
        self.parcelFileName_2.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        self.parcelFileName_2.setFont(font)
        self.parcelFileName_2.setObjectName("parcelFileName_2")
        self.gridLayout_7.addWidget(self.parcelFileName_2, 0, 3, 1, 2)
        self.rainFileName_2 = QtWidgets.QLineEdit(self.page)
        self.rainFileName_2.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        self.rainFileName_2.setFont(font)
        self.rainFileName_2.setObjectName("rainFileName_2")
        self.gridLayout_7.addWidget(self.rainFileName_2, 1, 3, 1, 2)
        self.tempFileName_2 = QtWidgets.QLineEdit(self.page)
        self.tempFileName_2.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        self.tempFileName_2.setFont(font)
        self.tempFileName_2.setObjectName("tempFileName_2")
        self.gridLayout_7.addWidget(self.tempFileName_2, 2, 3, 1, 2)
        self.pathOutput_2 = QtWidgets.QLineEdit(self.page)
        self.pathOutput_2.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        self.pathOutput_2.setFont(font)
        self.pathOutput_2.setObjectName("pathOutput_2")
        self.gridLayout_7.addWidget(self.pathOutput_2, 7, 3, 1, 2)
        self.frequence_display_2 = QtWidgets.QSpinBox(self.page)
        self.frequence_display_2.setEnabled(False)
        self.frequence_display_2.setObjectName("frequence_display_2")
        self.gridLayout_7.addWidget(self.frequence_display_2, 8, 3, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.gridLayout_4.addWidget(self.stackedWidget, 0, 2, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(200, 0))
        self.textEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_4.addWidget(self.textEdit, 0, 3, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_4.addWidget(self.listWidget, 0, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 959, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuApropos = QtWidgets.QMenu(self.menubar)
        self.menuApropos.setObjectName("menuApropos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBonjourjhhd = QtGui.QAction(MainWindow)
        self.actionBonjourjhhd.setObjectName("actionBonjourjhhd")
        self.actionOuvrir = QtGui.QAction(MainWindow)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.actionSauvegarder = QtGui.QAction(MainWindow)
        self.actionSauvegarder.setObjectName("actionSauvegarder")
        self.actionQuitter = QtGui.QAction(MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionAide = QtGui.QAction(MainWindow)
        self.actionAide.setObjectName("actionAide")
        self.menuFile.addAction(self.actionOuvrir)
        self.menuFile.addAction(self.actionSauvegarder)
        self.menuFile.addAction(self.actionQuitter)
        self.menuApropos.addAction(self.actionAide)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuApropos.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBoxInputParam.setTitle(_translate("MainWindow", "Nom des fichiers d\'entrée"))
        self.label_rainFileName.setText(_translate("MainWindow", "Précipitations:"))
        self.btn_parcelFileName.setText(_translate("MainWindow", "..."))
        self.label_parcelFileName.setText(_translate("MainWindow", "Fichier environnemental:"))
        self.label_tempFileName.setText(_translate("MainWindow", "Températures:"))
        self.btn_tempFileName.setText(_translate("MainWindow", "..."))
        self.btn_rainFileName.setText(_translate("MainWindow", "..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "Paramètres KL"))
        self.btn_add_gite.setText(_translate("MainWindow", "+"))
        self.btn_delete_gite.setText(_translate("MainWindow", "-"))
        self.groupBox.setTitle(_translate("MainWindow", "Paramètres de sortie"))
        self.label_frequence_display.setText(_translate("MainWindow", "Tous les "))
        self.label_edate.setText(_translate("MainWindow", "Date de fin:"))
        self.lastdate.setText(_translate("MainWindow", "Pour une date"))
        self.btn_pathOutput.setText(_translate("MainWindow", "..."))
        self.label_result_type.setText(_translate("MainWindow", "Résultats:"))
        self.outputKML.setText(_translate("MainWindow", "KML"))
        self.label_bdate_output.setText(_translate("MainWindow", "Date de début :"))
        self.label_output_format.setText(_translate("MainWindow", "Format:"))
        self.label_pathOutput.setText(_translate("MainWindow", "Répertoire de sortie:"))
        self.outputSHP.setText(_translate("MainWindow", "Shapefile"))
        self.multidate.setText(_translate("MainWindow", "Pour une période"))
        self.outputCSV.setText(_translate("MainWindow", "CSV"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Cas infectés"))
        self.label_date_intro.setText(_translate("MainWindow", "Date d\'introduction des permiers cas infectés"))
        self.label_pers_infectes.setText(_translate("MainWindow", "Nombre de personnes initalement infectées"))
        self.label_parcelFileName_2.setText(_translate("MainWindow", "Fichier environnemental:"))
        self.label_rainFileName_2.setText(_translate("MainWindow", "Précipitations:"))
        self.btn_cancel.setText(_translate("MainWindow", "Annuler"))
        self.label_pathOutput_2.setText(_translate("MainWindow", "Répertoire de sortie:"))
        self.btn_execute.setText(_translate("MainWindow", "Executer"))
        self.label_output_format_2.setText(_translate("MainWindow", "Format:"))
        self.label_frequence_display_2.setText(_translate("MainWindow", "Tous les"))
        self.label_tempFileName_2.setText(_translate("MainWindow", "Températures:"))
        self.label_edate_2.setText(_translate("MainWindow", "Date de fin de simulation:"))
        self.label_bdate_output_2.setText(_translate("MainWindow", "Date de début des sorties:"))
        self.menuFile.setTitle(_translate("MainWindow", "Fichier"))
        self.menuApropos.setTitle(_translate("MainWindow", "A propos"))
        self.actionBonjourjhhd.setText(_translate("MainWindow", "Bonjour jhhd feef fffffffffffffffxxxwdd"))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir"))
        self.actionSauvegarder.setText(_translate("MainWindow", "Sauvegarder"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionAide.setText(_translate("MainWindow", "Aide"))
