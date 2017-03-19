# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PMU_PQ_Visual.ui'
#
# Created: Wed Aug 19 10:00:44 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
import svdPortion
import numpy as np
import constants
import csv
import math
from PyQt4 import QtCore, QtGui
import OSU_powersystem_Bus1_rc
import OSU_powersystem_Bus21_rc
import OSU_powersystem_Bus164_rc
import OSU_powersystem_Bus217_rc


#startingRecordFile = '150809,230000000,0,WESRF1,OSU.csv'
#startingRecordFile = '151002,220000000,0,WESRF1,OSU.csv'
#startingRecordFile = '151213,000000000,0,WESRF1,OSU_gilbert.csv'
startingRecordFile = '/Users/benmccamish/PMUData/151215,230000000,0,WESRF1,OSU.csv'

recordFileMatrix = ''
recordCounter = 1
vBarTranspose = 0
r = list()
c = list()
i = list()
estimatedPower = list()
deletedCols = list()
#csvFileTest = open('estimatedPowerCSV.csv', 'a')
#estimatedPowerCSV = csv.writer(csvFileTest)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(QtGui.QWidget):

	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setupUi(self)

	def start(self):
		self.timer.start()

	def stop(self):
		self.timer.stop()

	def setupUi(self, Form):
		Form.setObjectName(_fromUtf8("Form"))
		Form.resize(1319, 1009)

		self.timer  = QtCore.QTimer(self)
		self.timer.setInterval(16.6667)          # Throw event timeout with an interval of 1000 milliseconds
		self.timer.timeout.connect(self.updateBars)

		Form.setObjectName(_fromUtf8("Form"))
		Form.resize(1242, 1333)
		self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
		self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
		self.scrollArea = QtGui.QScrollArea(Form)
		self.scrollArea.setWidgetResizable(True)
		self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
		self.scrollAreaWidgetContents = QtGui.QWidget()
		self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1216, 1656))
		self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
		self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
		self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
		self.gridLayout = QtGui.QGridLayout()
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.gridLayoutPMU3 = QtGui.QGridLayout()
		self.gridLayoutPMU3.setObjectName(_fromUtf8("gridLayoutPMU3"))
		self.line_29 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_29.setFrameShape(QtGui.QFrame.HLine)
		self.line_29.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_29.setObjectName(_fromUtf8("line_29"))
		self.gridLayoutPMU3.addWidget(self.line_29, 8, 1, 1, 1)
		self.progressBarPMU3_I_Active = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.progressBarPMU3_I_Active.sizePolicy().hasHeightForWidth())
		self.progressBarPMU3_I_Active.setSizePolicy(sizePolicy)
		self.progressBarPMU3_I_Active.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.progressBarPMU3_I_Active.setAutoFillBackground(False)
		self.progressBarPMU3_I_Active.setProperty("value", 24)
		self.progressBarPMU3_I_Active.setAlignment(QtCore.Qt.AlignCenter)
		self.progressBarPMU3_I_Active.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU3_I_Active.setInvertedAppearance(False)
		self.progressBarPMU3_I_Active.setObjectName(_fromUtf8("progressBarPMU3_I_Active"))
		self.gridLayoutPMU3.addWidget(self.progressBarPMU3_I_Active, 3, 2, 1, 1)
		self.labelPMU3Value_C_Reactive = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU3Value_C_Reactive.setObjectName(_fromUtf8("labelPMU3Value_C_Reactive"))
		self.gridLayoutPMU3.addWidget(self.labelPMU3Value_C_Reactive, 9, 1, 1, 1)
		self.labelPMU3Title_C = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU3Title_C.setObjectName(_fromUtf8("labelPMU3Title_C"))
		self.gridLayoutPMU3.addWidget(self.labelPMU3Title_C, 0, 1, 1, 1)
		self.label_15 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_15.setAlignment(QtCore.Qt.AlignCenter)
		self.label_15.setObjectName(_fromUtf8("label_15"))
		self.gridLayoutPMU3.addWidget(self.label_15, 2, 0, 1, 1)
		self.progressBarPMU3_I_Reactive = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU3_I_Reactive.setProperty("value", 24)
		self.progressBarPMU3_I_Reactive.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU3_I_Reactive.setObjectName(_fromUtf8("progressBarPMU3_I_Reactive"))
		self.gridLayoutPMU3.addWidget(self.progressBarPMU3_I_Reactive, 7, 2, 1, 1)
		self.line_30 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_30.setFrameShape(QtGui.QFrame.HLine)
		self.line_30.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_30.setObjectName(_fromUtf8("line_30"))
		self.gridLayoutPMU3.addWidget(self.line_30, 1, 1, 1, 1)
		self.line_31 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_31.setFrameShape(QtGui.QFrame.HLine)
		self.line_31.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_31.setObjectName(_fromUtf8("line_31"))
		self.gridLayoutPMU3.addWidget(self.line_31, 1, 0, 1, 1)
		self.line_32 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_32.setFrameShape(QtGui.QFrame.HLine)
		self.line_32.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_32.setObjectName(_fromUtf8("line_32"))
		self.gridLayoutPMU3.addWidget(self.line_32, 5, 0, 1, 1)
		self.labelPMU3Value_R_Reactive = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU3Value_R_Reactive.setObjectName(_fromUtf8("labelPMU3Value_R_Reactive"))
		self.gridLayoutPMU3.addWidget(self.labelPMU3Value_R_Reactive, 9, 0, 1, 1)
		self.labelPMU3Title_R = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU3Title_R.setObjectName(_fromUtf8("labelPMU3Title_R"))
		self.gridLayoutPMU3.addWidget(self.labelPMU3Title_R, 0, 0, 1, 1)
		self.progressBarPMU3_C_Active = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU3_C_Active.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.progressBarPMU3_C_Active.setProperty("value", 24)
		self.progressBarPMU3_C_Active.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU3_C_Active.setObjectName(_fromUtf8("progressBarPMU3_C_Active"))
		self.gridLayoutPMU3.addWidget(self.progressBarPMU3_C_Active, 3, 1, 1, 1)
		self.labelPMU3Title_I = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU3Title_I.setObjectName(_fromUtf8("labelPMU3Title_I"))
		self.gridLayoutPMU3.addWidget(self.labelPMU3Title_I, 0, 2, 1, 1)
		self.labelPMU3Value_I_Reactive = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU3Value_I_Reactive.setObjectName(_fromUtf8("labelPMU3Value_I_Reactive"))
		self.gridLayoutPMU3.addWidget(self.labelPMU3Value_I_Reactive, 9, 2, 1, 1)
		self.progressBarPMU3_R_Active = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU3_R_Active.setProperty("value", 24)
		self.progressBarPMU3_R_Active.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU3_R_Active.setInvertedAppearance(False)
		self.progressBarPMU3_R_Active.setTextDirection(QtGui.QProgressBar.TopToBottom)
		self.progressBarPMU3_R_Active.setObjectName(_fromUtf8("progressBarPMU3_R_Active"))
		self.gridLayoutPMU3.addWidget(self.progressBarPMU3_R_Active, 3, 0, 1, 1)
		self.line_33 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_33.setFrameShape(QtGui.QFrame.HLine)
		self.line_33.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_33.setObjectName(_fromUtf8("line_33"))
		self.gridLayoutPMU3.addWidget(self.line_33, 8, 0, 1, 1)
		self.line_34 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_34.setFrameShape(QtGui.QFrame.HLine)
		self.line_34.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_34.setObjectName(_fromUtf8("line_34"))
		self.gridLayoutPMU3.addWidget(self.line_34, 8, 2, 1, 1)
		self.line_35 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_35.setFrameShape(QtGui.QFrame.HLine)
		self.line_35.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_35.setObjectName(_fromUtf8("line_35"))
		self.gridLayoutPMU3.addWidget(self.line_35, 1, 2, 1, 1)
		self.labelPMU3Range_C_Upper = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU3Range_C_Upper.setAlignment(QtCore.Qt.AlignCenter)
		self.labelPMU3Range_C_Upper.setObjectName(_fromUtf8("labelPMU3Range_C_Upper"))
		self.gridLayoutPMU3.addWidget(self.labelPMU3Range_C_Upper, 2, 1, 1, 1)
		self.labelPMU3Range_I_Upper = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU3Range_I_Upper.setAlignment(QtCore.Qt.AlignCenter)
		self.labelPMU3Range_I_Upper.setObjectName(_fromUtf8("labelPMU3Range_I_Upper"))
		self.gridLayoutPMU3.addWidget(self.labelPMU3Range_I_Upper, 2, 2, 1, 1)
		self.line_36 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_36.setFrameShape(QtGui.QFrame.HLine)
		self.line_36.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_36.setObjectName(_fromUtf8("line_36"))
		self.gridLayoutPMU3.addWidget(self.line_36, 5, 2, 1, 1)
		self.progressBarPMU3_C_Reactive = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU3_C_Reactive.setProperty("value", 24)
		self.progressBarPMU3_C_Reactive.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU3_C_Reactive.setObjectName(_fromUtf8("progressBarPMU3_C_Reactive"))
		self.gridLayoutPMU3.addWidget(self.progressBarPMU3_C_Reactive, 7, 1, 1, 1)
		self.label_16 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_16.setAlignment(QtCore.Qt.AlignCenter)
		self.label_16.setObjectName(_fromUtf8("label_16"))
		self.gridLayoutPMU3.addWidget(self.label_16, 6, 2, 1, 1)
		self.line_37 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_37.setFrameShape(QtGui.QFrame.HLine)
		self.line_37.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_37.setObjectName(_fromUtf8("line_37"))
		self.gridLayoutPMU3.addWidget(self.line_37, 5, 1, 1, 1)
		self.label_17 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_17.setAlignment(QtCore.Qt.AlignCenter)
		self.label_17.setObjectName(_fromUtf8("label_17"))
		self.gridLayoutPMU3.addWidget(self.label_17, 6, 0, 1, 1)
		self.label_18 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_18.setAlignment(QtCore.Qt.AlignCenter)
		self.label_18.setObjectName(_fromUtf8("label_18"))
		self.gridLayoutPMU3.addWidget(self.label_18, 6, 1, 1, 1)
		self.progressBarPMU3_R_Reactive = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU3_R_Reactive.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.progressBarPMU3_R_Reactive.setProperty("value", 24)
		self.progressBarPMU3_R_Reactive.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU3_R_Reactive.setObjectName(_fromUtf8("progressBarPMU3_R_Reactive"))
		self.gridLayoutPMU3.addWidget(self.progressBarPMU3_R_Reactive, 7, 0, 1, 1)
		self.labelPMU3Value_R_Active = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU3Value_R_Active.setObjectName(_fromUtf8("labelPMU3Value_R_Active"))
		self.gridLayoutPMU3.addWidget(self.labelPMU3Value_R_Active, 4, 0, 1, 1)
		self.labelPMU3Value_C_Active = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU3Value_C_Active.setObjectName(_fromUtf8("labelPMU3Value_C_Active"))
		self.gridLayoutPMU3.addWidget(self.labelPMU3Value_C_Active, 4, 1, 1, 1)
		self.label_19 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_19.setObjectName(_fromUtf8("label_19"))
		self.gridLayoutPMU3.addWidget(self.label_19, 4, 2, 1, 1)
		self.gridLayout.addLayout(self.gridLayoutPMU3, 2, 0, 1, 1)
		self.gridLayoutPMU4 = QtGui.QGridLayout()
		self.gridLayoutPMU4.setObjectName(_fromUtf8("gridLayoutPMU4"))
		self.line_21 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_21.setFrameShape(QtGui.QFrame.HLine)
		self.line_21.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_21.setObjectName(_fromUtf8("line_21"))
		self.gridLayoutPMU4.addWidget(self.line_21, 8, 1, 1, 1)
		self.progressBarPMU4_I_Active = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.progressBarPMU4_I_Active.sizePolicy().hasHeightForWidth())
		self.progressBarPMU4_I_Active.setSizePolicy(sizePolicy)
		self.progressBarPMU4_I_Active.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.progressBarPMU4_I_Active.setAutoFillBackground(False)
		self.progressBarPMU4_I_Active.setProperty("value", 24)
		self.progressBarPMU4_I_Active.setAlignment(QtCore.Qt.AlignCenter)
		self.progressBarPMU4_I_Active.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU4_I_Active.setInvertedAppearance(False)
		self.progressBarPMU4_I_Active.setObjectName(_fromUtf8("progressBarPMU4_I_Active"))
		self.gridLayoutPMU4.addWidget(self.progressBarPMU4_I_Active, 3, 2, 1, 1)
		self.labelPMU4Value_C_Reactive = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU4Value_C_Reactive.setObjectName(_fromUtf8("labelPMU4Value_C_Reactive"))
		self.gridLayoutPMU4.addWidget(self.labelPMU4Value_C_Reactive, 9, 1, 1, 1)
		self.labelPMU4Title_C = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU4Title_C.setObjectName(_fromUtf8("labelPMU4Title_C"))
		self.gridLayoutPMU4.addWidget(self.labelPMU4Title_C, 0, 1, 1, 1)
		self.label_10 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_10.setAlignment(QtCore.Qt.AlignCenter)
		self.label_10.setObjectName(_fromUtf8("label_10"))
		self.gridLayoutPMU4.addWidget(self.label_10, 2, 0, 1, 1)
		self.progressBarPMU4_I_Reactive = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU4_I_Reactive.setProperty("value", 24)
		self.progressBarPMU4_I_Reactive.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU4_I_Reactive.setObjectName(_fromUtf8("progressBarPMU4_I_Reactive"))
		self.gridLayoutPMU4.addWidget(self.progressBarPMU4_I_Reactive, 7, 2, 1, 1)
		self.line_4 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_4.setFrameShape(QtGui.QFrame.HLine)
		self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_4.setObjectName(_fromUtf8("line_4"))
		self.gridLayoutPMU4.addWidget(self.line_4, 1, 1, 1, 1)
		self.line_22 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_22.setFrameShape(QtGui.QFrame.HLine)
		self.line_22.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_22.setObjectName(_fromUtf8("line_22"))
		self.gridLayoutPMU4.addWidget(self.line_22, 1, 0, 1, 1)
		self.line_23 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_23.setFrameShape(QtGui.QFrame.HLine)
		self.line_23.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_23.setObjectName(_fromUtf8("line_23"))
		self.gridLayoutPMU4.addWidget(self.line_23, 5, 0, 1, 1)
		self.labelPMU4Value_R_Reactive = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU4Value_R_Reactive.setObjectName(_fromUtf8("labelPMU4Value_R_Reactive"))
		self.gridLayoutPMU4.addWidget(self.labelPMU4Value_R_Reactive, 9, 0, 1, 1)
		self.labelPMU4Title_R = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU4Title_R.setObjectName(_fromUtf8("labelPMU4Title_R"))
		self.gridLayoutPMU4.addWidget(self.labelPMU4Title_R, 0, 0, 1, 1)
		self.progressBarPMU4_C_Active = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU4_C_Active.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.progressBarPMU4_C_Active.setProperty("value", 24)
		self.progressBarPMU4_C_Active.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU4_C_Active.setObjectName(_fromUtf8("progressBarPMU4_C_Active"))
		self.gridLayoutPMU4.addWidget(self.progressBarPMU4_C_Active, 3, 1, 1, 1)
		self.labelPMU4Title_I = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU4Title_I.setObjectName(_fromUtf8("labelPMU4Title_I"))
		self.gridLayoutPMU4.addWidget(self.labelPMU4Title_I, 0, 2, 1, 1)
		self.labelPMU4Value_I_Reactive = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU4Value_I_Reactive.setObjectName(_fromUtf8("labelPMU4Value_I_Reactive"))
		self.gridLayoutPMU4.addWidget(self.labelPMU4Value_I_Reactive, 9, 2, 1, 1)
		self.progressBarPMU4_R_Active = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU4_R_Active.setProperty("value", 24)
		self.progressBarPMU4_R_Active.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU4_R_Active.setInvertedAppearance(False)
		self.progressBarPMU4_R_Active.setTextDirection(QtGui.QProgressBar.TopToBottom)
		self.progressBarPMU4_R_Active.setObjectName(_fromUtf8("progressBarPMU4_R_Active"))
		self.gridLayoutPMU4.addWidget(self.progressBarPMU4_R_Active, 3, 0, 1, 1)
		self.line_24 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_24.setFrameShape(QtGui.QFrame.HLine)
		self.line_24.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_24.setObjectName(_fromUtf8("line_24"))
		self.gridLayoutPMU4.addWidget(self.line_24, 8, 0, 1, 1)
		self.line_25 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_25.setFrameShape(QtGui.QFrame.HLine)
		self.line_25.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_25.setObjectName(_fromUtf8("line_25"))
		self.gridLayoutPMU4.addWidget(self.line_25, 8, 2, 1, 1)
		self.line_26 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_26.setFrameShape(QtGui.QFrame.HLine)
		self.line_26.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_26.setObjectName(_fromUtf8("line_26"))
		self.gridLayoutPMU4.addWidget(self.line_26, 1, 2, 1, 1)
		self.labelPMU4Range_C_Upper = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU4Range_C_Upper.setAlignment(QtCore.Qt.AlignCenter)
		self.labelPMU4Range_C_Upper.setObjectName(_fromUtf8("labelPMU4Range_C_Upper"))
		self.gridLayoutPMU4.addWidget(self.labelPMU4Range_C_Upper, 2, 1, 1, 1)
		self.labelPMU4Range_I_Upper = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU4Range_I_Upper.setAlignment(QtCore.Qt.AlignCenter)
		self.labelPMU4Range_I_Upper.setObjectName(_fromUtf8("labelPMU4Range_I_Upper"))
		self.gridLayoutPMU4.addWidget(self.labelPMU4Range_I_Upper, 2, 2, 1, 1)
		self.line_27 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_27.setFrameShape(QtGui.QFrame.HLine)
		self.line_27.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_27.setObjectName(_fromUtf8("line_27"))
		self.gridLayoutPMU4.addWidget(self.line_27, 5, 2, 1, 1)
		self.progressBarPMU4_C_Reactive = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU4_C_Reactive.setProperty("value", 24)
		self.progressBarPMU4_C_Reactive.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU4_C_Reactive.setObjectName(_fromUtf8("progressBarPMU4_C_Reactive"))
		self.gridLayoutPMU4.addWidget(self.progressBarPMU4_C_Reactive, 7, 1, 1, 1)
		self.label_11 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_11.setAlignment(QtCore.Qt.AlignCenter)
		self.label_11.setObjectName(_fromUtf8("label_11"))
		self.gridLayoutPMU4.addWidget(self.label_11, 6, 2, 1, 1)
		self.line_28 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_28.setFrameShape(QtGui.QFrame.HLine)
		self.line_28.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_28.setObjectName(_fromUtf8("line_28"))
		self.gridLayoutPMU4.addWidget(self.line_28, 5, 1, 1, 1)
		self.label_12 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_12.setAlignment(QtCore.Qt.AlignCenter)
		self.label_12.setObjectName(_fromUtf8("label_12"))
		self.gridLayoutPMU4.addWidget(self.label_12, 6, 0, 1, 1)
		self.label_13 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_13.setAlignment(QtCore.Qt.AlignCenter)
		self.label_13.setObjectName(_fromUtf8("label_13"))
		self.gridLayoutPMU4.addWidget(self.label_13, 6, 1, 1, 1)
		self.progressBarPMU4_R_Reactive = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU4_R_Reactive.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.progressBarPMU4_R_Reactive.setProperty("value", 24)
		self.progressBarPMU4_R_Reactive.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU4_R_Reactive.setObjectName(_fromUtf8("progressBarPMU4_R_Reactive"))
		self.gridLayoutPMU4.addWidget(self.progressBarPMU4_R_Reactive, 7, 0, 1, 1)
		self.labelPMU4Value_R_Active = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU4Value_R_Active.setObjectName(_fromUtf8("labelPMU4Value_R_Active"))
		self.gridLayoutPMU4.addWidget(self.labelPMU4Value_R_Active, 4, 0, 1, 1)
		self.labelPMU4Value_C_Active = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU4Value_C_Active.setObjectName(_fromUtf8("labelPMU4Value_C_Active"))
		self.gridLayoutPMU4.addWidget(self.labelPMU4Value_C_Active, 4, 1, 1, 1)
		self.label_14 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_14.setObjectName(_fromUtf8("label_14"))
		self.gridLayoutPMU4.addWidget(self.label_14, 4, 2, 1, 1)
		self.gridLayout.addLayout(self.gridLayoutPMU4, 3, 0, 1, 1)
		self.gridLayoutPMU2 = QtGui.QGridLayout()
		self.gridLayoutPMU2.setObjectName(_fromUtf8("gridLayoutPMU2"))
		self.line_11 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_11.setFrameShape(QtGui.QFrame.HLine)
		self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_11.setObjectName(_fromUtf8("line_11"))
		self.gridLayoutPMU2.addWidget(self.line_11, 8, 1, 1, 1)
		self.progressBarPMU2_I_Active = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.progressBarPMU2_I_Active.sizePolicy().hasHeightForWidth())
		self.progressBarPMU2_I_Active.setSizePolicy(sizePolicy)
		self.progressBarPMU2_I_Active.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.progressBarPMU2_I_Active.setAutoFillBackground(False)
		self.progressBarPMU2_I_Active.setProperty("value", 24)
		self.progressBarPMU2_I_Active.setAlignment(QtCore.Qt.AlignCenter)
		self.progressBarPMU2_I_Active.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU2_I_Active.setInvertedAppearance(False)
		self.progressBarPMU2_I_Active.setObjectName(_fromUtf8("progressBarPMU2_I_Active"))
		self.gridLayoutPMU2.addWidget(self.progressBarPMU2_I_Active, 3, 2, 1, 1)
		self.labelPMU2Value_C_Reactive = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU2Value_C_Reactive.setObjectName(_fromUtf8("labelPMU2Value_C_Reactive"))
		self.gridLayoutPMU2.addWidget(self.labelPMU2Value_C_Reactive, 9, 1, 1, 1)
		self.labelPMU2Title_C = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU2Title_C.setObjectName(_fromUtf8("labelPMU2Title_C"))
		self.gridLayoutPMU2.addWidget(self.labelPMU2Title_C, 0, 1, 1, 1)
		self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_5.setAlignment(QtCore.Qt.AlignCenter)
		self.label_5.setObjectName(_fromUtf8("label_5"))
		self.gridLayoutPMU2.addWidget(self.label_5, 2, 0, 1, 1)
		self.progressBarPMU2_I_Reactive = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU2_I_Reactive.setProperty("value", 24)
		self.progressBarPMU2_I_Reactive.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU2_I_Reactive.setObjectName(_fromUtf8("progressBarPMU2_I_Reactive"))
		self.gridLayoutPMU2.addWidget(self.progressBarPMU2_I_Reactive, 7, 2, 1, 1)
		self.line_12 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_12.setFrameShape(QtGui.QFrame.HLine)
		self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_12.setObjectName(_fromUtf8("line_12"))
		self.gridLayoutPMU2.addWidget(self.line_12, 1, 1, 1, 1)
		self.line_13 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_13.setFrameShape(QtGui.QFrame.HLine)
		self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_13.setObjectName(_fromUtf8("line_13"))
		self.gridLayoutPMU2.addWidget(self.line_13, 1, 0, 1, 1)
		self.line_15 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_15.setFrameShape(QtGui.QFrame.HLine)
		self.line_15.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_15.setObjectName(_fromUtf8("line_15"))
		self.gridLayoutPMU2.addWidget(self.line_15, 5, 0, 1, 1)
		self.labelPMU2Value_R_Reactive = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU2Value_R_Reactive.setObjectName(_fromUtf8("labelPMU2Value_R_Reactive"))
		self.gridLayoutPMU2.addWidget(self.labelPMU2Value_R_Reactive, 9, 0, 1, 1)
		self.labelPMU2Title_R = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU2Title_R.setObjectName(_fromUtf8("labelPMU2Title_R"))
		self.gridLayoutPMU2.addWidget(self.labelPMU2Title_R, 0, 0, 1, 1)
		self.progressBarPMU2_C_Active = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU2_C_Active.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.progressBarPMU2_C_Active.setProperty("value", 24)
		self.progressBarPMU2_C_Active.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU2_C_Active.setObjectName(_fromUtf8("progressBarPMU2_C_Active"))
		self.gridLayoutPMU2.addWidget(self.progressBarPMU2_C_Active, 3, 1, 1, 1)
		self.labelPMU2Title_I = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU2Title_I.setObjectName(_fromUtf8("labelPMU2Title_I"))
		self.gridLayoutPMU2.addWidget(self.labelPMU2Title_I, 0, 2, 1, 1)
		self.labelPMU2Value_I_Reactive = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU2Value_I_Reactive.setObjectName(_fromUtf8("labelPMU2Value_I_Reactive"))
		self.gridLayoutPMU2.addWidget(self.labelPMU2Value_I_Reactive, 9, 2, 1, 1)
		self.progressBarPMU2_R_Active = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU2_R_Active.setProperty("value", 24)
		self.progressBarPMU2_R_Active.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU2_R_Active.setInvertedAppearance(False)
		self.progressBarPMU2_R_Active.setTextDirection(QtGui.QProgressBar.TopToBottom)
		self.progressBarPMU2_R_Active.setObjectName(_fromUtf8("progressBarPMU2_R_Active"))
		self.gridLayoutPMU2.addWidget(self.progressBarPMU2_R_Active, 3, 0, 1, 1)
		self.line_16 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_16.setFrameShape(QtGui.QFrame.HLine)
		self.line_16.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_16.setObjectName(_fromUtf8("line_16"))
		self.gridLayoutPMU2.addWidget(self.line_16, 8, 0, 1, 1)
		self.line_17 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_17.setFrameShape(QtGui.QFrame.HLine)
		self.line_17.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_17.setObjectName(_fromUtf8("line_17"))
		self.gridLayoutPMU2.addWidget(self.line_17, 8, 2, 1, 1)
		self.line_18 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_18.setFrameShape(QtGui.QFrame.HLine)
		self.line_18.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_18.setObjectName(_fromUtf8("line_18"))
		self.gridLayoutPMU2.addWidget(self.line_18, 1, 2, 1, 1)
		self.labelPMU2Range_C_Upper = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU2Range_C_Upper.setAlignment(QtCore.Qt.AlignCenter)
		self.labelPMU2Range_C_Upper.setObjectName(_fromUtf8("labelPMU2Range_C_Upper"))
		self.gridLayoutPMU2.addWidget(self.labelPMU2Range_C_Upper, 2, 1, 1, 1)
		self.labelPMU2Range_I_Upper = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU2Range_I_Upper.setAlignment(QtCore.Qt.AlignCenter)
		self.labelPMU2Range_I_Upper.setObjectName(_fromUtf8("labelPMU2Range_I_Upper"))
		self.gridLayoutPMU2.addWidget(self.labelPMU2Range_I_Upper, 2, 2, 1, 1)
		self.line_19 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_19.setFrameShape(QtGui.QFrame.HLine)
		self.line_19.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_19.setObjectName(_fromUtf8("line_19"))
		self.gridLayoutPMU2.addWidget(self.line_19, 5, 2, 1, 1)
		self.progressBarPMU2_C_Reactive = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU2_C_Reactive.setProperty("value", 24)
		self.progressBarPMU2_C_Reactive.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU2_C_Reactive.setObjectName(_fromUtf8("progressBarPMU2_C_Reactive"))
		self.gridLayoutPMU2.addWidget(self.progressBarPMU2_C_Reactive, 7, 1, 1, 1)
		self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_6.setAlignment(QtCore.Qt.AlignCenter)
		self.label_6.setObjectName(_fromUtf8("label_6"))
		self.gridLayoutPMU2.addWidget(self.label_6, 6, 2, 1, 1)
		self.line_20 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_20.setFrameShape(QtGui.QFrame.HLine)
		self.line_20.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_20.setObjectName(_fromUtf8("line_20"))
		self.gridLayoutPMU2.addWidget(self.line_20, 5, 1, 1, 1)
		self.label_8 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_8.setAlignment(QtCore.Qt.AlignCenter)
		self.label_8.setObjectName(_fromUtf8("label_8"))
		self.gridLayoutPMU2.addWidget(self.label_8, 6, 0, 1, 1)
		self.label_9 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_9.setAlignment(QtCore.Qt.AlignCenter)
		self.label_9.setObjectName(_fromUtf8("label_9"))
		self.gridLayoutPMU2.addWidget(self.label_9, 6, 1, 1, 1)
		self.progressBarPMU2_R_Reactive = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU2_R_Reactive.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.progressBarPMU2_R_Reactive.setProperty("value", 24)
		self.progressBarPMU2_R_Reactive.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU2_R_Reactive.setObjectName(_fromUtf8("progressBarPMU2_R_Reactive"))
		self.gridLayoutPMU2.addWidget(self.progressBarPMU2_R_Reactive, 7, 0, 1, 1)
		self.labelPMU2Value_R_Active = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU2Value_R_Active.setObjectName(_fromUtf8("labelPMU2Value_R_Active"))
		self.gridLayoutPMU2.addWidget(self.labelPMU2Value_R_Active, 4, 0, 1, 1)
		self.labelPMU2Value_C_Active = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU2Value_C_Active.setObjectName(_fromUtf8("labelPMU2Value_C_Active"))
		self.gridLayoutPMU2.addWidget(self.labelPMU2Value_C_Active, 4, 1, 1, 1)
		self.labelPMU2Value_I_Active = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU2Value_I_Active.setObjectName(_fromUtf8("labelPMU2Value_I_Active"))
		self.gridLayoutPMU2.addWidget(self.labelPMU2Value_I_Active, 4, 2, 1, 1)
		self.gridLayout.addLayout(self.gridLayoutPMU2, 1, 0, 1, 1)
		self.gridLayoutPMU1 = QtGui.QGridLayout()
		self.gridLayoutPMU1.setObjectName(_fromUtf8("gridLayoutPMU1"))
		self.progressBarPMU1_C_Reactive = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU1_C_Reactive.setProperty("value", 24)
		self.progressBarPMU1_C_Reactive.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU1_C_Reactive.setObjectName(_fromUtf8("progressBarPMU1_C_Reactive"))
		self.gridLayoutPMU1.addWidget(self.progressBarPMU1_C_Reactive, 7, 1, 1, 1)
		self.labelPMU1Title_R = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU1Title_R.setObjectName(_fromUtf8("labelPMU1Title_R"))
		self.gridLayoutPMU1.addWidget(self.labelPMU1Title_R, 0, 0, 1, 1)
		self.progressBarPMU1_I_Active = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.progressBarPMU1_I_Active.sizePolicy().hasHeightForWidth())
		self.progressBarPMU1_I_Active.setSizePolicy(sizePolicy)
		self.progressBarPMU1_I_Active.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.progressBarPMU1_I_Active.setAutoFillBackground(False)
		self.progressBarPMU1_I_Active.setProperty("value", 24)
		self.progressBarPMU1_I_Active.setAlignment(QtCore.Qt.AlignCenter)
		self.progressBarPMU1_I_Active.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU1_I_Active.setInvertedAppearance(False)
		self.progressBarPMU1_I_Active.setObjectName(_fromUtf8("progressBarPMU1_I_Active"))
		self.gridLayoutPMU1.addWidget(self.progressBarPMU1_I_Active, 3, 2, 1, 1)
		self.labelPMU1Range_C_Upper = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU1Range_C_Upper.setAlignment(QtCore.Qt.AlignCenter)
		self.labelPMU1Range_C_Upper.setObjectName(_fromUtf8("labelPMU1Range_C_Upper"))
		self.gridLayoutPMU1.addWidget(self.labelPMU1Range_C_Upper, 2, 1, 1, 1)
		self.line = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line.setFrameShape(QtGui.QFrame.HLine)
		self.line.setFrameShadow(QtGui.QFrame.Sunken)
		self.line.setObjectName(_fromUtf8("line"))
		self.gridLayoutPMU1.addWidget(self.line, 1, 0, 1, 1)
		self.labelPMU1Title_I = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU1Title_I.setObjectName(_fromUtf8("labelPMU1Title_I"))
		self.gridLayoutPMU1.addWidget(self.labelPMU1Title_I, 0, 2, 1, 1)
		self.line_2 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_2.setFrameShape(QtGui.QFrame.HLine)
		self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_2.setObjectName(_fromUtf8("line_2"))
		self.gridLayoutPMU1.addWidget(self.line_2, 1, 1, 1, 1)
		self.progressBarPMU1_C_Active = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU1_C_Active.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.progressBarPMU1_C_Active.setProperty("value", 24)
		self.progressBarPMU1_C_Active.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU1_C_Active.setObjectName(_fromUtf8("progressBarPMU1_C_Active"))
		self.gridLayoutPMU1.addWidget(self.progressBarPMU1_C_Active, 3, 1, 1, 1)
		self.labelPMU1Title_C = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU1Title_C.setObjectName(_fromUtf8("labelPMU1Title_C"))
		self.gridLayoutPMU1.addWidget(self.labelPMU1Title_C, 0, 1, 1, 1)
		self.progressBarPMU1_I_Reactive = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU1_I_Reactive.setProperty("value", 24)
		self.progressBarPMU1_I_Reactive.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU1_I_Reactive.setObjectName(_fromUtf8("progressBarPMU1_I_Reactive"))
		self.gridLayoutPMU1.addWidget(self.progressBarPMU1_I_Reactive, 7, 2, 1, 1)
		self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_4.setAlignment(QtCore.Qt.AlignCenter)
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.gridLayoutPMU1.addWidget(self.label_4, 6, 2, 1, 1)
		self.line_6 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_6.setFrameShape(QtGui.QFrame.HLine)
		self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_6.setObjectName(_fromUtf8("line_6"))
		self.gridLayoutPMU1.addWidget(self.line_6, 5, 1, 1, 1)
		self.progressBarPMU1_R_Active = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU1_R_Active.setProperty("value", 24)
		self.progressBarPMU1_R_Active.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU1_R_Active.setInvertedAppearance(False)
		self.progressBarPMU1_R_Active.setTextDirection(QtGui.QProgressBar.TopToBottom)
		self.progressBarPMU1_R_Active.setObjectName(_fromUtf8("progressBarPMU1_R_Active"))
		self.gridLayoutPMU1.addWidget(self.progressBarPMU1_R_Active, 3, 0, 1, 1)
		self.line_14 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_14.setFrameShape(QtGui.QFrame.HLine)
		self.line_14.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_14.setObjectName(_fromUtf8("line_14"))
		self.gridLayoutPMU1.addWidget(self.line_14, 1, 2, 1, 1)
		self.line_9 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_9.setFrameShape(QtGui.QFrame.HLine)
		self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_9.setObjectName(_fromUtf8("line_9"))
		self.gridLayoutPMU1.addWidget(self.line_9, 8, 2, 1, 1)
		self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_7.setObjectName(_fromUtf8("label_7"))
		self.gridLayoutPMU1.addWidget(self.label_7, 4, 2, 1, 1)
		self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_3.setAlignment(QtCore.Qt.AlignCenter)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.gridLayoutPMU1.addWidget(self.label_3, 6, 1, 1, 1)
		self.labelPMU1Value_C_Reactive = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU1Value_C_Reactive.setObjectName(_fromUtf8("labelPMU1Value_C_Reactive"))
		self.gridLayoutPMU1.addWidget(self.labelPMU1Value_C_Reactive, 9, 1, 1, 1)
		self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_2.setAlignment(QtCore.Qt.AlignCenter)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.gridLayoutPMU1.addWidget(self.label_2, 6, 0, 1, 1)
		self.line_5 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_5.setFrameShape(QtGui.QFrame.HLine)
		self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_5.setObjectName(_fromUtf8("line_5"))
		self.gridLayoutPMU1.addWidget(self.line_5, 5, 0, 1, 1)
		self.labelPMU1Value_R_Reactive = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU1Value_R_Reactive.setObjectName(_fromUtf8("labelPMU1Value_R_Reactive"))
		self.gridLayoutPMU1.addWidget(self.labelPMU1Value_R_Reactive, 9, 0, 1, 1)
		self.labelPMU1Range_I_Upper = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU1Range_I_Upper.setAlignment(QtCore.Qt.AlignCenter)
		self.labelPMU1Range_I_Upper.setObjectName(_fromUtf8("labelPMU1Range_I_Upper"))
		self.gridLayoutPMU1.addWidget(self.labelPMU1Range_I_Upper, 2, 2, 1, 1)
		self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName(_fromUtf8("label"))
		self.gridLayoutPMU1.addWidget(self.label, 2, 0, 1, 1)
		self.line_7 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_7.setFrameShape(QtGui.QFrame.HLine)
		self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_7.setObjectName(_fromUtf8("line_7"))
		self.gridLayoutPMU1.addWidget(self.line_7, 8, 0, 1, 1)
		self.line_8 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_8.setFrameShape(QtGui.QFrame.HLine)
		self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_8.setObjectName(_fromUtf8("line_8"))
		self.gridLayoutPMU1.addWidget(self.line_8, 8, 1, 1, 1)
		self.labelPMU1Value_R_Active = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU1Value_R_Active.setObjectName(_fromUtf8("labelPMU1Value_R_Active"))
		self.gridLayoutPMU1.addWidget(self.labelPMU1Value_R_Active, 4, 0, 1, 1)
		self.line_10 = QtGui.QFrame(self.scrollAreaWidgetContents)
		self.line_10.setFrameShape(QtGui.QFrame.HLine)
		self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
		self.line_10.setObjectName(_fromUtf8("line_10"))
		self.gridLayoutPMU1.addWidget(self.line_10, 5, 2, 1, 1)
		self.labelPMU1Value_C_Active = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU1Value_C_Active.setObjectName(_fromUtf8("labelPMU1Value_C_Active"))
		self.gridLayoutPMU1.addWidget(self.labelPMU1Value_C_Active, 4, 1, 1, 1)
		self.progressBarPMU1_R_Reactive = QtGui.QProgressBar(self.scrollAreaWidgetContents)
		self.progressBarPMU1_R_Reactive.setLayoutDirection(QtCore.Qt.LeftToRight)
		self.progressBarPMU1_R_Reactive.setProperty("value", 24)
		self.progressBarPMU1_R_Reactive.setOrientation(QtCore.Qt.Vertical)
		self.progressBarPMU1_R_Reactive.setObjectName(_fromUtf8("progressBarPMU1_R_Reactive"))
		self.gridLayoutPMU1.addWidget(self.progressBarPMU1_R_Reactive, 7, 0, 1, 1)
		self.labelPMU1Value_I_Reactive = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.labelPMU1Value_I_Reactive.setObjectName(_fromUtf8("labelPMU1Value_I_Reactive"))
		self.gridLayoutPMU1.addWidget(self.labelPMU1Value_I_Reactive, 9, 2, 1, 1)
		self.gridLayout.addLayout(self.gridLayoutPMU1, 0, 0, 1, 1)
		self.label_20 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_20.setMaximumSize(QtCore.QSize(800, 400))
		self.label_20.setText(_fromUtf8(""))
		self.label_20.setPixmap(QtGui.QPixmap(_fromUtf8(":/Maps/OSU_powersystem_Bus1.jpg")))
		self.label_20.setScaledContents(True)
		self.label_20.setObjectName(_fromUtf8("label_20"))
		self.gridLayout.addWidget(self.label_20, 0, 2, 1, 1)
		self.label_21 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_21.setMaximumSize(QtCore.QSize(800, 400))
		self.label_21.setText(_fromUtf8(""))
		self.label_21.setPixmap(QtGui.QPixmap(_fromUtf8(":/Maps/OSU_powersystem_Bus21.jpeg")))
		self.label_21.setScaledContents(True)
		self.label_21.setObjectName(_fromUtf8("label_21"))
		self.gridLayout.addWidget(self.label_21, 1, 2, 1, 1)
		self.label_22 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_22.setMaximumSize(QtCore.QSize(800, 400))
		self.label_22.setText(_fromUtf8(""))
		self.label_22.setPixmap(QtGui.QPixmap(_fromUtf8(":/Maps/OSU_powersystem_Bus164.jpg")))
		self.label_22.setScaledContents(True)
		self.label_22.setObjectName(_fromUtf8("label_22"))
		self.gridLayout.addWidget(self.label_22, 2, 2, 1, 1)
		self.label_23 = QtGui.QLabel(self.scrollAreaWidgetContents)
		self.label_23.setMaximumSize(QtCore.QSize(800, 400))
		self.label_23.setText(_fromUtf8(""))
		self.label_23.setPixmap(QtGui.QPixmap(_fromUtf8(":/Maps/OSU_powersystem_Bus217.jpeg")))
		self.label_23.setScaledContents(True)
		self.label_23.setObjectName(_fromUtf8("label_23"))
		self.gridLayout.addWidget(self.label_23, 3, 2, 1, 1)
		self.verticalLayout.addLayout(self.gridLayout)
		self.scrollArea.setWidget(self.scrollAreaWidgetContents)
		self.verticalLayout_2.addWidget(self.scrollArea)

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)
	
	def retranslateUi(self, Form):
		Form.setWindowTitle(_translate("Form", "Status", None))
		self.labelPMU3Value_C_Reactive.setText(_translate("Form", "50 MVAR", None))
		self.labelPMU3Title_C.setText(_translate("Form", "C Bus 3", None))
		self.label_15.setText(_translate("Form", "Active", None))
		self.labelPMU3Value_R_Reactive.setText(_translate("Form", "50 MVAR", None))
		self.labelPMU3Title_R.setText(_translate("Form", "R Bus 3", None))
		self.labelPMU3Title_I.setText(_translate("Form", "I Bus 3", None))
		self.labelPMU3Value_I_Reactive.setText(_translate("Form", "50MVAR", None))
		self.progressBarPMU3_R_Active.setFormat(_translate("Form", "%p%", None))
		self.labelPMU3Range_C_Upper.setText(_translate("Form", "Active", None))
		self.labelPMU3Range_I_Upper.setText(_translate("Form", "Active", None))
		self.label_16.setText(_translate("Form", "Reactive", None))
		self.label_17.setText(_translate("Form", "Reactive", None))
		self.label_18.setText(_translate("Form", "Reactive", None))
		self.labelPMU3Value_R_Active.setText(_translate("Form", "50 MW", None))
		self.labelPMU3Value_C_Active.setText(_translate("Form", "50 MW", None))
		self.label_19.setText(_translate("Form", "50 MW", None))
		self.labelPMU4Value_C_Reactive.setText(_translate("Form", "50 MVAR", None))
		self.labelPMU4Title_C.setText(_translate("Form", "C Bus 4", None))
		self.label_10.setText(_translate("Form", "Active", None))
		self.labelPMU4Value_R_Reactive.setText(_translate("Form", "50 MVAR", None))
		self.labelPMU4Title_R.setText(_translate("Form", "R Bus 4", None))
		self.labelPMU4Title_I.setText(_translate("Form", "I Bus 4", None))
		self.labelPMU4Value_I_Reactive.setText(_translate("Form", "50MVAR", None))
		self.progressBarPMU4_R_Active.setFormat(_translate("Form", "%p%", None))
		self.labelPMU4Range_C_Upper.setText(_translate("Form", "Active", None))
		self.labelPMU4Range_I_Upper.setText(_translate("Form", "Active", None))
		self.label_11.setText(_translate("Form", "Reactive", None))
		self.label_12.setText(_translate("Form", "Reactive", None))
		self.label_13.setText(_translate("Form", "Reactive", None))
		self.labelPMU4Value_R_Active.setText(_translate("Form", "50 MW", None))
		self.labelPMU4Value_C_Active.setText(_translate("Form", "50 MW", None))
		self.label_14.setText(_translate("Form", "50 MW", None))
		self.labelPMU2Value_C_Reactive.setText(_translate("Form", "50 MVAR", None))
		self.labelPMU2Title_C.setText(_translate("Form", "C Bus 2", None))
		self.label_5.setText(_translate("Form", "Active", None))
		self.labelPMU2Value_R_Reactive.setText(_translate("Form", "50 MVAR", None))
		self.labelPMU2Title_R.setText(_translate("Form", "R Bus 2", None))
		self.labelPMU2Title_I.setText(_translate("Form", "I Bus 2", None))
		self.labelPMU2Value_I_Reactive.setText(_translate("Form", "50MVAR", None))
		self.progressBarPMU2_R_Active.setFormat(_translate("Form", "%p%", None))
		self.labelPMU2Range_C_Upper.setText(_translate("Form", "Active", None))
		self.labelPMU2Range_I_Upper.setText(_translate("Form", "Active", None))
		self.label_6.setText(_translate("Form", "Reactive", None))
		self.label_8.setText(_translate("Form", "Reactive", None))
		self.label_9.setText(_translate("Form", "Reactive", None))
		self.labelPMU2Value_R_Active.setText(_translate("Form", "50 MW", None))
		self.labelPMU2Value_C_Active.setText(_translate("Form", "50 MW", None))
		self.labelPMU2Value_I_Active.setText(_translate("Form", "50 MW", None))
		self.labelPMU1Title_R.setText(_translate("Form", "R Bus 1", None))
		self.labelPMU1Range_C_Upper.setText(_translate("Form", "Active", None))
		self.labelPMU1Title_I.setText(_translate("Form", "I Bus 1", None))
		self.labelPMU1Title_C.setText(_translate("Form", "C Bus 1", None))
		self.label_4.setText(_translate("Form", "Reactive", None))
		self.progressBarPMU1_R_Active.setFormat(_translate("Form", "%p%", None))
		self.label_7.setText(_translate("Form", "50 MW", None))
		self.label_3.setText(_translate("Form", "Reactive", None))
		self.labelPMU1Value_C_Reactive.setText(_translate("Form", "50 MVAR", None))
		self.label_2.setText(_translate("Form", "Reactive", None))
		self.labelPMU1Value_R_Reactive.setText(_translate("Form", "50 MVAR", None))
		self.labelPMU1Range_I_Upper.setText(_translate("Form", "Active", None))
		self.label.setText(_translate("Form", "Active", None))
		self.labelPMU1Value_R_Active.setText(_translate("Form", "50 MW", None))
		self.labelPMU1Value_C_Active.setText(_translate("Form", "50 MW", None))
		self.labelPMU1Value_I_Reactive.setText(_translate("Form", "50MVAR", None))

		#self.updateBars()

	def cleanString(self, s):
		#return s.replace('(','').replace(')','').replace('R','').replace('C','').replace('I','').replace('%','')
		return s.replace('(','').replace(')','').replace('%','').strip()
	
	def getRCI(self, busNum):
		breakdown = constants.rci[busNum-1]
		test = breakdown.split(',')
		C = '0'
		R = '0'
		I = '0'
		for x in test:
			x = self.cleanString(x)
			if x[0] == 'C':
				C = x.strip('C')
			elif x[0] == 'R':
				R = x.strip('R')
			elif x[0] == 'I':
				I = x.strip('I')

		return float(R),float(C),float(I)
		
	def testRecord(self, rowNum):
		newRecord = [0] * 1144
		for i, x in enumerate(constants.realValues):
			newRecord[(x-1)*4 + 2] = float(0.1)
		return np.asarray(newRecord)
		

	def openNewFile(self, fileName):
		csvfile = open(fileName, 'rb')
		pdcFile = csv.reader(csvfile, delimiter=',')
		return list(pdcFile)

	def calculatePower(self, vM, vA, iM, iA):
		P = -3 * vM * iM * math.cos(math.pi/180*(vA - iA))
		Q = -3 * vM * iM * math.sin(math.pi/180*(vA - iA))

		P = P / 1e6
		Q = Q / 1e6

		return P, Q

	def reduceNewRecord(self, record):
		global deletedCols
		dColCount = 0
		for i, col in enumerate(record):
			if i in deletedCols:
				record = np.delete(record, i - dColCount)
				dColCount += 1

		return record

	def getNextRow(self,rowNum):
		global recordFileMatrix
		iAngWESRF = 0
		iMagWESRF = 0
		iAngGILBERT = 0
		iMagGILBERT = 0
		iAngSNELL = 0
		iMagSNELL = 0

		vAngWESRF = 0
		vMagWESRF = 0
		vAngGILBERT = 0
		vMagGILBERT = 0
		vAngSNELL = 0
		vMagSNELL = 0

		for i, colName in enumerate(recordFileMatrix[0]):
			#WESRF
			if 'STATION A:IAPM:Magnitude' == colName:
				iMagWESRF = i

			if 'STATION A:IAPM:Angle' == colName:
				iAngWESRF = i

			if 'STATION A:VAPM:Magnitude' == colName:
				vMagWESRF = i

			if 'STATION A:VAPM:Angle' == colName:
				vAngWESRF = i

			#GILBERT
			if 'GILBERT_PMU:IB:Magnitude' == colName:
				iMagGILBERT = i

			if 'GILBERT_PMU:IB:Angle' == colName:
				iAngGILBERT = i

			if 'GILBERT_PMU:VB:Magnitude' == colName:
				vMagGILBERT = i

			if 'GILBERT_PMU:VB:Angle' == colName:
				vAngGILBERT = i

			#SNELL
			if 'SNELL_PMU:IASPM:Magnitude' == colName:
				iMagSNELL = i

			if 'SNELL_PMU:IASPM:Angle' == colName:
				iAngSNELL = i

			if 'SNELL_PMU:VAVPM:Magnitude' == colName:
				vMagSNELL = i

			if 'SNELL_PMU:VAVPM:Angle' == colName:
				vAngSNELL = i


		newRecord = list()
		#WESRF

		#GILBERT
		GILBERT_VM = float(recordFileMatrix[rowNum][vMagGILBERT])/120
		GILBERT_VA = float(recordFileMatrix[rowNum][vAngGILBERT])
		GILBERT_IM = float(recordFileMatrix[rowNum][iMagGILBERT])
		GILBERT_IA = float(recordFileMatrix[rowNum][iAngGILBERT])


		WESRF_VM = float(recordFileMatrix[rowNum][vMagWESRF])/280
		WESRF_VA = float(recordFileMatrix[rowNum][vAngWESRF]) - GILBERT_VA
		WESRF_IM = float(recordFileMatrix[rowNum][iMagWESRF])
		WESRF_IA = float(recordFileMatrix[rowNum][iAngWESRF]) - GILBERT_VA

		print 'Time: ', recordFileMatrix[rowNum][0]

		#print "Record",recordFileMatrix[rowNum][26]
		#SDL_VA = float(recordFileMatrix[rowNum][26])
		#SDL_VM = float(recordFileMatrix[rowNum][25])/277

		#SNELL
		SNELL_VM = float(recordFileMatrix[rowNum][vMagSNELL])/120
		SNELL_VA = float(recordFileMatrix[rowNum][vAngSNELL]) - GILBERT_VA
		SNELL_IM = float(recordFileMatrix[rowNum][iMagSNELL])
		SNELL_IA = float(recordFileMatrix[rowNum][iAngSNELL]) - GILBERT_VA

		GILBERT_IA = GILBERT_IA - GILBERT_VA
		GILBERT_VA = 0
		# 280
		# row 140000
		# 1000000
		#

		#print "WESRF voltage magnitude (pre-normalize):", WESRF_VM
		#print "WESRF voltage angle (pre-normalize):", WESRF_VA
		#print "SDL voltage magnitude (pre-normalize):", SDL_VM
		#print "SDL voltage angle (pre-normalize):", SDL_VA

		#print "GILBERT voltage magnitude (pre-normalize):", GILBERT_VM
		#print "GILBERT voltage angle (pre-normalize):", GILBERT_VA

		#WESRF
		if WESRF_VM == '':
			WESRF_VM = 0

		if WESRF_VA == '':
			WESRF_VA = 0

		if WESRF_IM == '':
			WESRF_IM = 0

		if WESRF_IA == '':
			WESRF_IA = 0

		#GILBERT
		if GILBERT_VA == '':
			GILBERT_VA = 0

		if GILBERT_VM == '':
			GILBERT_VM = 0

		if GILBERT_IA == '':
			GILBERT_IA = 0

		if GILBERT_IM == '':
			GILBERT_IM = 0

		#SNELL
		if SNELL_VM == '':
			SNELL_VM = 0

		if SNELL_VA == '':
			SNELL_VA = 0

		if SNELL_IM == '':
			SNELL_IM = 0

		if SNELL_IA == '':
			SNELL_IA = 0


		#WESRF
		WESRF_P, WESRF_Q = self.calculatePower(WESRF_VM*280, WESRF_VA, WESRF_IM, WESRF_IA)
		
		#GILBERT
		GILBERT_P, GILBERT_Q = self.calculatePower(GILBERT_VM*120, GILBERT_VA, GILBERT_IM, GILBERT_IA)

		#SNELL
		SNELL_P, SNELL_Q = self.calculatePower(SNELL_VM*120, SNELL_VA, SNELL_IM, SNELL_IA)
		
		print  'Raw Data Values (after first normalization):'
		print  '            VM         VA      IM           IA          P          Q'
		print ('Gilbert %10.4f %10.4f %10.4f %10.4f %10.4f %10.4f') % (GILBERT_VM, GILBERT_VA, GILBERT_IM, GILBERT_IA, GILBERT_P, GILBERT_Q)
		print ('WESRF   %10.4f %10.4f %10.4f %10.4f %10.4f %10.4f') % (WESRF_VM, WESRF_VA, WESRF_IM, WESRF_IA, WESRF_P, WESRF_Q)
		print ('SNELL   %10.4f %10.4f %10.4f %10.4f %10.4f %10.4f') % (SNELL_VM, SNELL_VA, SNELL_IM, SNELL_IA, SNELL_P, SNELL_Q)

		valuesFromMeasured = [WESRF_VM, WESRF_VA, WESRF_P, WESRF_Q, GILBERT_VM, GILBERT_VA, GILBERT_P, GILBERT_Q, SNELL_VM, SNELL_VA, SNELL_P, SNELL_Q]
		newRecord = [0] * 1144
		for i, x in enumerate(constants.realValues):
			#V Mag
			newRecord[(x-1)*4] = float(valuesFromMeasured[i*4])
			
			#V Ang
			newRecord[(x-1)*4 + 1] = float(valuesFromMeasured[(i*4) + 1])
			
			#P
			newRecord[(x-1)*4 + 2] = float(valuesFromMeasured[(i*4) + 2])

			#Q
			newRecord[(x-1)*4 + 3] = float(valuesFromMeasured[(i*4) + 3])

		return np.asarray(newRecord)


	def updateBars(self):
		global vBarTranspose
		global recordCounter
		global startingRecordFile
		global recordFileMatrix
		global r
		global c
		global i
		#global estimatedPowerCSV
		#global csvFileTest

		if recordCounter == 1:
			print 'Reading next file'
			recordFileMatrix = self.openNewFile(startingRecordFile)

		#print "****Case****"
		#print recordCounter
		transformedRecord = self.getNextRow(140000)
		reducedRecord = self.reduceNewRecord(transformedRecord)
		actualValues = self.getNextRow(140000)
		#transformedRecord = self.testRecord(45500)
		#estimatedRecord = svdPortion.testEstimateRecord(np.copy(transformedRecord), np.copy(reducedRecord), deletedCols, vBarTranspose)
		estimatedRecord = svdPortion.estimateRecord(np.copy(transformedRecord), np.copy(reducedRecord), deletedCols, vBarTranspose)

		recordCounter += 1
		if recordCounter >= len(recordFileMatrix):
			recordCounter = 1


		normalizedEstimatedRecord = np.copy(estimatedRecord)
		#print normalizedEstimatedRecord
		with open('estimatedPowerCSV.txt', 'a') as csvFileTest:
			csvFileTest.write("Actual V: %f Estimated V: %f\n" % ((actualValues[163*4]), (estimatedRecord[163*4])))
			csvFileTest.write("Actual Phase: %f Estimated Phase: %f\n" % ((actualValues[163*4 + 1]), (estimatedRecord[163*4 + 1])))
		#	estimatedPowerCSV = csv.writer(csvFileTest)
		#	estimatedPowerCSV.writerow('Hello')
		
		#Testing Portion, simple for now
		#csvFileTest.write('Hello')

		#estimatedPowerCSV.writerow('Hello')
		#estimatedPower.append(estimatedRecord[163*4 +2] * 20)
		


		estimatedRecord = svdPortion.Denormalize(estimatedRecord)

		PMU1_P = estimatedRecord[(constants.measuredPMU[0]-1)*4 + 2]
		PMU1_Q = estimatedRecord[(constants.measuredPMU[0]-1)*4 + 3]
		PMU1_P_Bar = normalizedEstimatedRecord[(constants.measuredPMU[0]-1)*4 + 2]
		PMU1_Q_Bar = normalizedEstimatedRecord[(constants.measuredPMU[0]-1)*4 + 3]

		PMU2_P = estimatedRecord[(constants.measuredPMU[1]-1)*4 + 2]
		PMU2_Q = estimatedRecord[(constants.measuredPMU[1]-1)*4 + 3]
		PMU2_P_Bar = normalizedEstimatedRecord[(constants.measuredPMU[1]-1)*4 + 2]
		PMU2_Q_Bar = normalizedEstimatedRecord[(constants.measuredPMU[1]-1)*4 + 3]

		PMU3_P = estimatedRecord[(constants.measuredPMU[2]-1)*4 + 2]
		PMU3_Q = estimatedRecord[(constants.measuredPMU[2]-1)*4 + 3]
		PMU3_P_Bar = normalizedEstimatedRecord[(constants.measuredPMU[2]-1)*4 + 2]
		PMU3_Q_Bar = normalizedEstimatedRecord[(constants.measuredPMU[2]-1)*4 + 3]
		
		PMU4_P = estimatedRecord[(constants.measuredPMU[3]-1)*4 + 2]
		PMU4_Q = estimatedRecord[(constants.measuredPMU[3]-1)*4 + 3]
		PMU4_P_Bar = normalizedEstimatedRecord[(constants.measuredPMU[2]-1)*4 + 2]
		PMU4_Q_Bar = normalizedEstimatedRecord[(constants.measuredPMU[2]-1)*4 + 3]
		#print 
		#print estimatedRecord[866]
		#print "Bus 217 active power (normalized):", PMU3_P_Bar
		#print "Bus 217 active power (un-normalized):", PMU3_P
		self.labelPMU1Value_C_Reactive.setText(_translate("Form", "%.2f MVAR" % PMU1_Q, None))
		self.labelPMU1Value_R_Reactive.setText(_translate("Form", "0 MVAR", None))
		self.labelPMU1Value_I_Reactive.setText(_translate("Form", "0 MVAR", None))
		self.labelPMU1Value_R_Active.setText(_translate("Form", "0 MW", None))
		self.labelPMU1Value_C_Active.setText(_translate("Form", "%.2f MW" % PMU1_P, None))
		#I_Active
		self.label_7.setText(_translate("Form", "0 MW", None))

		self.labelPMU2Value_C_Reactive.setText(_translate("Form", "%.2f MVAR" % PMU2_Q, None))
		self.labelPMU2Value_R_Reactive.setText(_translate("Form", "0 MVAR", None))
		self.labelPMU2Value_I_Reactive.setText(_translate("Form", "0 MVAR", None))
		self.labelPMU2Value_R_Active.setText(_translate("Form", "0 MW", None))
		self.labelPMU2Value_C_Active.setText(_translate("Form", "%.2f MW" % PMU2_P, None))
		self.labelPMU2Value_I_Active.setText(_translate("Form", "0 MW", None))

		self.labelPMU3Value_C_Reactive.setText(_translate("Form", "%.2f MVAR" % PMU3_Q, None))
		self.labelPMU3Value_R_Reactive.setText(_translate("Form", "0 MVAR", None))
		self.labelPMU3Value_I_Reactive.setText(_translate("Form", "0 MVAR", None))
		self.labelPMU3Value_R_Active.setText(_translate("Form", "0 MW", None))
		self.labelPMU3Value_C_Active.setText(_translate("Form", "%.2f MW" % PMU3_P, None))
		#I_Active
		self.label_19.setText(_translate("Form", "0 MW", None))

		#print "**********R = ", r[3]
		self.labelPMU4Value_C_Reactive.setText(_translate("Form", "%.2f MVAR" % (PMU4_Q*c[3]), None))
		self.labelPMU4Value_R_Reactive.setText(_translate("Form", "%.2f MVAR" % (PMU4_Q*r[3]), None))
		self.labelPMU4Value_I_Reactive.setText(_translate("Form", "%.2f MVAR" % (PMU4_Q*i[3]), None))
		self.labelPMU4Value_R_Active.setText(_translate("Form", "%.2f MW" % (PMU4_P*r[3]), None))
		self.labelPMU4Value_C_Active.setText(_translate("Form", "%.2f MW" % (PMU4_P*c[3]), None))
		#I_Active
		self.label_14.setText(_translate("Form", "%.2f MW" % (PMU4_P*i[3]), None))

		self.progressBarPMU1_I_Active.setValue(0)
		self.progressBarPMU1_I_Reactive.setValue(0)
		self.progressBarPMU1_C_Active.setValue(abs(PMU1_P))
		self.progressBarPMU1_R_Active.setValue(0)
		self.progressBarPMU1_C_Reactive.setValue(abs(PMU1_Q))
		self.progressBarPMU1_R_Reactive.setValue(0)

		self.progressBarPMU2_I_Active.setValue(0)
		self.progressBarPMU2_I_Reactive.setValue(0)
		self.progressBarPMU2_C_Active.setValue(abs(PMU2_P))
		self.progressBarPMU2_R_Active.setValue(0)
		self.progressBarPMU2_C_Reactive.setValue(abs(PMU2_Q))
		self.progressBarPMU2_R_Reactive.setValue(0)

		self.progressBarPMU3_I_Active.setValue(0)
		self.progressBarPMU3_I_Reactive.setValue(0)
		self.progressBarPMU3_C_Active.setValue(abs(PMU3_P))
		self.progressBarPMU3_R_Active.setValue(0)
		self.progressBarPMU3_C_Reactive.setValue(abs(PMU3_Q))
		self.progressBarPMU3_R_Reactive.setValue(0)

		self.progressBarPMU4_I_Active.setValue(abs(PMU4_P*i[3]))
		self.progressBarPMU4_I_Reactive.setValue(abs(PMU4_Q*i[3]))
		self.progressBarPMU4_C_Active.setValue(abs(PMU4_P*c[3]))
		self.progressBarPMU4_R_Active.setValue(abs(PMU4_P*r[3]))
		self.progressBarPMU4_C_Reactive.setValue(abs(PMU4_Q*c[3]))
		self.progressBarPMU4_R_Reactive.setValue(abs(PMU4_Q*r[3]))


def basePhase(trainingData, pmu):
	for i,row in enumerate(trainingData):
		if i != 0 or i != 1:
			for x,element in enumerate(row):
				if (x%4) is 1:
					row[x] = row[x] - row[(pmu*4) + 1]
	return trainingData

def cleanString(s):
	#return s.replace('(','').replace(')','').replace('R','').replace('C','').replace('I','').replace('%','')
	return s.replace('(','').replace(')','').replace('%','').strip()

def getRCI(busNum):
	breakdown = constants.rci[busNum-1]
	test = breakdown.split(',')
	C = '0'
	R = '0'
	I = '0'
	for x in test:
		x = cleanString(x)
		if len(x) == 0:
			pass
		elif x[0] == 'C':
			C = x.strip('C')
		elif x[0] == 'R':
			R = x.strip('R')
		elif x[0] == 'I':
			I = x.strip('I')


	return float(R)/100,float(C)/100,float(I)/100

if __name__ == '__main__':
	'''Main, just for testing right now'''
	#global vBarTranspose
	#global r, c, i
	#global estimatedPower
	global deletedCols
	
	for x in constants.measuredPMU:
		localR, localC, localI = getRCI(int(x))
		r.append(localR)
		c.append(localC)
		i.append(localI)

	#trainingData = svdPortion.CreateMatrix('286busLibTransposed_Paper.csv')
	#trainingData = svdPortion.CreateMatrix('286busLibrary_0924_Transposed.csv')
	#trainingData = svdPortion.CreateMatrix('NewRecords.csv')
	#trainingData = svdPortion.CreateMatrix('286busLibraryUpdated.csv')
	trainingData = svdPortion.CreateMatrix('WESRF_Snell_Gilbert_Library.csv')
	trainingData = basePhase(trainingData, 165 - 1)

	normalizedData = svdPortion.normalizeFile(trainingData)

	reducedData, deletedCols = svdPortion.reduceCol(normalizedData, 0.1)

	print deletedCols
	print "Normalized"
	u, s, vTranspose = svdPortion.SVD(reducedData)

	# Numpy SVD returns 1d matrix for s, this creates a 2d matrix 
	# with proper dimensions and fills the rest in with 0's
	sDiag = np.zeros((u.shape[1], vTranspose.shape[0]))
	sDiag[:s.shape[0], :s.shape[0]] = np.diag(s)

	uBar, sBar, vBarTranspose = svdPortion.Reduce(u, sDiag, vTranspose, s)

	print vBarTranspose.shape
	# Setup GUI and begin livestream
	app = QtGui.QApplication(sys.argv)
	ex = Ui_Form()
	ex.show()
	ex.start()
	sys.exit(app.exec_())
	#csvFileTest.close()
