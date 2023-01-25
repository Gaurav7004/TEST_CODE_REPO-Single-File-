import os, sys
from itertools import count
import numpy as np
import pandas as pd

### PYQT IMPORTS
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp

''' 
S_IREAD is a bit mask that is used to check the read permission of a 
file in a POSIX-compliant operating system. The constant is used in 
conjunction with other bit masks to check for specific file permissions.
'''
from stat import S_IREAD

# Imports from other packages
from New_Dialog import *
from Calc_Multiplier import *
from Validation_Checks import *
from progress import *
from Message_Box_UI import *
from valChecksCase1 import *
from valChecksCase2 import *

## Importing deque to implement stack 
from collections import deque
import xlrd


# global lst_Design_Template, lst_Data_Template, createList

# class ThreadClass(QtCore.QThread):
#     try:
#         actualProgress = QtCore.pyqtSignal(object)

#         def __init__(self, parent=None):
#             super(ThreadClass, self).__init__(parent)

#         def run(self):
#             t = tqdm(range(101))

#             for e in t:
#                 self.actualProgress.emit(e)
#                 time.sleep(0.1)

#     except:
#         pass


###! **************************** Main UI Class *******************************
###! **************************************************************************
class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(0, 0, 998, 783)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Create = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Create.sizePolicy().hasHeightForWidth())
        self.Create.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Create.setFont(font)
        self.Create.setStyleSheet("background-color: rgb(192, 200, 205);\n"
"color: rgb(107, 136, 152);")
        self.Create.setElideMode(QtCore.Qt.ElideMiddle)
        self.Create.setObjectName("Create")
        self.Create_2 = QtWidgets.QWidget()
        self.Create_2.setStyleSheet("background-color: rgb(191, 200, 198);")
        self.Create_2.setObjectName("Create_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Create_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem, 1, 2, 1, 2)
        self.Edit = QtWidgets.QPushButton(self.Create_2)

        # *** Connection of Load_MULT_DEF_FILE function ***
        self.Edit.clicked.connect(self.Load_MULT_DEF_FILE)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Edit.sizePolicy().hasHeightForWidth())
        self.Edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Edit.setFont(font)
        self.Edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Edit.setObjectName("Edit")
        self.gridLayout_9.addWidget(self.Edit, 4, 2, 1, 2)
        self.pushButton_2 = QtWidgets.QPushButton(self.Create_2)

        # *** Connection of onClickNextTab0 function ***
        self.pushButton_2.clicked.connect(self.onClickNextTab0)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_9.addWidget(self.pushButton_2, 7, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem1, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem2, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem3, 7, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem4, 3, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem5, 7, 2, 1, 1)
        self.create = QtWidgets.QPushButton(self.Create_2)

        # *** Connection of Create_MULT_DEF_FILE function ***
        self.create.clicked.connect(self.Create_MULT_DEF_FILE)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create.sizePolicy().hasHeightForWidth())
        self.create.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.create.setFont(font)
        self.create.setStyleSheet("background-color: rgb(236, 250, 244);")
        self.create.setObjectName("create")
        self.gridLayout_9.addWidget(self.create, 3, 2, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem6, 3, 6, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem7, 3, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem8, 6, 2, 1, 2)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem9, 5, 2, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_9)
        self.Create.addTab(self.Create_2, "")

        index = self.Create.addTab(self.Create_2, "MULT-DEF File")
        self.Create.setTabToolTip(index, "MULT-DEF File")

        self.FSU = QtWidgets.QWidget()
        self.FSU.setStyleSheet("background-color: rgb(191, 200, 198);")
        self.FSU.setObjectName("FSU")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.FSU)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.FSU)

        # *** Connection of onClickPreviousTab1 function ***
        self.pushButton_5.clicked.connect(self.onClickPreviousTab1)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_5.addWidget(self.pushButton_5, 1, 2, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.FSU)

        # *** Connection of onClickNextTab1 function ***
        self.pushButton_6.clicked.connect(self.onClickNextTab1)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_5.addWidget(self.pushButton_6, 1, 3, 1, 1)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem10, 1, 2, 1, 1)
        self.No_2 = QtWidgets.QRadioButton(self.FSU)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.No_2.sizePolicy().hasHeightForWidth())
        self.No_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.No_2.setFont(font)
        self.No_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.No_2.setObjectName("No_2")
        self.gridLayout_12.addWidget(self.No_2, 4, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem11, 7, 1, 1, 1)
        self.Yes_2 = QtWidgets.QRadioButton(self.FSU)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Yes_2.sizePolicy().hasHeightForWidth())
        self.Yes_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Yes_2.setFont(font)
        self.Yes_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Yes_2.setObjectName("Yes_2")
        self.gridLayout_12.addWidget(self.Yes_2, 2, 1, 1, 1)
        self.SSU_2 = QtWidgets.QLabel(self.FSU)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SSU_2.sizePolicy().hasHeightForWidth())
        self.SSU_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SSU_2.setFont(font)
        self.SSU_2.setStyleSheet("background-color: rgb(87, 122, 131);\n"
"color: rgb(255, 255, 255);")
        self.SSU_2.setAlignment(QtCore.Qt.AlignCenter)
        self.SSU_2.setObjectName("SSU_2")
        self.gridLayout_12.addWidget(self.SSU_2, 1, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem12, 4, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_12.addItem(spacerItem13, 0, 1, 1, 1)
        self.SSN_2 = QtWidgets.QLabel(self.FSU)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SSN_2.sizePolicy().hasHeightForWidth())
        self.SSN_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SSN_2.setFont(font)
        self.SSN_2.setStyleSheet("background-color: rgb(87, 122, 131);\n"
"color: rgb(255, 255, 255);")
        self.SSN_2.setAlignment(QtCore.Qt.AlignCenter)
        self.SSN_2.setObjectName("SSN_2")
        self.gridLayout_12.addWidget(self.SSN_2, 5, 1, 1, 1)
        self.SubSample_num = QtWidgets.QSpinBox(self.FSU)

        ###  number of Sub-Sample used default value
        self.SubSample_num.setValue(1)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubSample_num.sizePolicy().hasHeightForWidth())
        self.SubSample_num.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SubSample_num.setFont(font)
        self.SubSample_num.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SubSample_num.setAlignment(QtCore.Qt.AlignCenter)
        self.SubSample_num.setObjectName("SubSample_num")
        self.gridLayout_12.addWidget(self.SubSample_num, 6, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_12, 0, 1, 1, 3)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem14, 7, 1, 1, 1)
        self.SRSWOR_3 = QtWidgets.QRadioButton(self.FSU)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SRSWOR_3.sizePolicy().hasHeightForWidth())
        self.SRSWOR_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SRSWOR_3.setFont(font)
        self.SRSWOR_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SRSWOR_3.setObjectName("SRSWOR_3")
        self.gridLayout_11.addWidget(self.SRSWOR_3, 2, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem15, 0, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem16, 4, 2, 1, 1)
        self.SRSWR_3 = QtWidgets.QRadioButton(self.FSU)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SRSWR_3.sizePolicy().hasHeightForWidth())
        self.SRSWR_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SRSWR_3.setFont(font)
        self.SRSWR_3.setStyleSheet("background-color: rgb(236, 250, 244);")
        self.SRSWR_3.setObjectName("SRSWR_3")
        self.gridLayout_11.addWidget(self.SRSWR_3, 1, 1, 1, 1)
        self.PPSWOR_3 = QtWidgets.QRadioButton(self.FSU)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PPSWOR_3.sizePolicy().hasHeightForWidth())
        self.PPSWOR_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PPSWOR_3.setFont(font)
        self.PPSWOR_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.PPSWOR_3.setObjectName("PPSWOR_3")
        self.gridLayout_11.addWidget(self.PPSWOR_3, 4, 1, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.FSU)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_5.sizePolicy().hasHeightForWidth())
        self.radioButton_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_11.addWidget(self.radioButton_5, 6, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem17, 3, 0, 1, 1)
        self.PPSWR_3 = QtWidgets.QRadioButton(self.FSU)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PPSWR_3.sizePolicy().hasHeightForWidth())
        self.PPSWR_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PPSWR_3.setFont(font)
        self.PPSWR_3.setStyleSheet("background-color: rgb(236, 250, 244);")
        self.PPSWR_3.setObjectName("PPSWR_3")
        self.gridLayout_11.addWidget(self.PPSWR_3, 3, 1, 1, 1)
        self.SystematicSRS_3 = QtWidgets.QRadioButton(self.FSU)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SystematicSRS_3.sizePolicy().hasHeightForWidth())
        self.SystematicSRS_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SystematicSRS_3.setFont(font)
        self.SystematicSRS_3.setStyleSheet("background-color: rgb(236, 250, 244);")
        self.SystematicSRS_3.setObjectName("SystematicSRS_3")
        self.gridLayout_11.addWidget(self.SystematicSRS_3, 5, 1, 1, 1)
        self.gridLayout_11.setColumnStretch(0, 1)
        self.gridLayout_11.setColumnStretch(1, 5)
        self.gridLayout_5.addLayout(self.gridLayout_11, 0, 0, 1, 1)
        self.Create.addTab(self.FSU, "")

        index = self.Create.addTab(self.FSU, "FSU Sampling Method")
        self.Create.setTabToolTip(index, "FSU Sampling Method")

        self.HGFormation = QtWidgets.QWidget()
        self.HGFormation.setStyleSheet("background-color: rgb(191, 200, 198);")
        self.HGFormation.setObjectName("HGFormation")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.HGFormation)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem18, 2, 0, 1, 3)
        self.pushButton_3 = QtWidgets.QPushButton(self.HGFormation)

        # *** Connection of onClickPreviousTab2 function ***
        self.pushButton_3.clicked.connect(self.onClickPreviousTab2)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 2, 4, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.PurPPS = QtWidgets.QRadioButton(self.HGFormation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PurPPS.sizePolicy().hasHeightForWidth())
        self.PurPPS.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PurPPS.setFont(font)
        self.PurPPS.setStyleSheet("background-color: rgb(236, 250, 244);")
        self.PurPPS.setObjectName("PurPPS")
        self.gridLayout_10.addWidget(self.PurPPS, 5, 1, 1, 1)
        self.SRS = QtWidgets.QRadioButton(self.HGFormation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SRS.sizePolicy().hasHeightForWidth())
        self.SRS.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SRS.setFont(font)
        self.SRS.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SRS.setObjectName("SRS")
        self.gridLayout_10.addWidget(self.SRS, 6, 1, 1, 1)
        self.EntireFSU = QtWidgets.QRadioButton(self.HGFormation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EntireFSU.sizePolicy().hasHeightForWidth())
        self.EntireFSU.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.EntireFSU.setFont(font)
        self.EntireFSU.setStyleSheet("background-color: rgb(236, 250, 244);")
        self.EntireFSU.setObjectName("EntireFSU")
        self.gridLayout_10.addWidget(self.EntireFSU, 1, 1, 1, 1)
        self.PPS = QtWidgets.QRadioButton(self.HGFormation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PPS.sizePolicy().hasHeightForWidth())
        self.PPS.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PPS.setFont(font)
        self.PPS.setStyleSheet("background-color: rgb(236, 250, 244);")
        self.PPS.setObjectName("PPS")
        self.gridLayout_10.addWidget(self.PPS, 7, 1, 1, 1)
        self.SRSWORSYS = QtWidgets.QRadioButton(self.HGFormation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SRSWORSYS.sizePolicy().hasHeightForWidth())
        self.SRSWORSYS.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SRSWORSYS.setFont(font)
        self.SRSWORSYS.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.SRSWORSYS.setObjectName("SRSWORSYS")
        self.gridLayout_10.addWidget(self.SRSWORSYS, 4, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem19, 4, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem20, 8, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem21, 0, 1, 1, 1)
        self.PPSSRS = QtWidgets.QRadioButton(self.HGFormation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PPSSRS.sizePolicy().hasHeightForWidth())
        self.PPSSRS.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PPSSRS.setFont(font)
        self.PPSSRS.setStyleSheet("background-color: rgb(236, 250, 244);")
        self.PPSSRS.setObjectName("PPSSRS")
        self.gridLayout_10.addWidget(self.PPSSRS, 3, 1, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem22, 4, 2, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.HGFormation)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_10.addWidget(self.radioButton, 2, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_10, 1, 1, 1, 5)

        # ## Creating ButtonGroup for tab 1
        self.btnGrouptab2 = QtWidgets.QButtonGroup(self.gridLayout_10)
        self.btnGrouptab2.addButton(self.EntireFSU)
        self.btnGrouptab2.addButton(self.radioButton)
        self.btnGrouptab2.addButton(self.PPSSRS)
        self.btnGrouptab2.addButton(self.SRSWORSYS)
        self.btnGrouptab2.addButton(self.PurPPS)
        self.btnGrouptab2.addButton(self.SRS)
        self.btnGrouptab2.addButton(self.PPS)

        self.pushButton_4 = QtWidgets.QPushButton(self.HGFormation)

        # *** Connection of onClickNextTab2 function ***
        self.pushButton_4.clicked.connect(self.onClickNextTab2)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.pushButton_4, 2, 5, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem23, 2, 3, 1, 1)
        self.Create.addTab(self.HGFormation, "")

        index = self.Create.addTab(self.HGFormation, "HG/SB or Sub-Division Formation")
        self.Create.setTabToolTip(index, "HG/SB or Sub-Division Formation")

        self.SSS = QtWidgets.QWidget()
        self.SSS.setStyleSheet("background-color: rgb(191, 200, 198);")
        self.SSS.setObjectName("SSS")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.SSS)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.SSS)

        # *** Connection of onClickPreviousTab3 function ***
        self.pushButton_7.clicked.connect(self.onClickPreviousTab3)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_6.addWidget(self.pushButton_7, 1, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.SSS)

        # *** Connection of onClickNextTab3 function ***
        self.pushButton_8.clicked.connect(self.onClickNextTab3)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_6.addWidget(self.pushButton_8, 1, 2, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem24, 1, 0, 1, 1)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem25, 1, 1, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_13.addItem(spacerItem26, 0, 1, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem27, 5, 1, 1, 1)
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem28, 2, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.SSS)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(87, 122, 131);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_13.addWidget(self.label_2, 2, 1, 1, 1)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem29, 2, 0, 1, 1)
        self.No_SSS = QtWidgets.QSpinBox(self.SSS)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.No_SSS.sizePolicy().hasHeightForWidth())
        self.No_SSS.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.No_SSS.setFont(font)
        self.No_SSS.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.No_SSS.setAlignment(QtCore.Qt.AlignCenter)
        self.No_SSS.setObjectName("No_SSS")
        self.gridLayout_13.addWidget(self.No_SSS, 3, 1, 1, 1)
        self.gridLayout_13.setRowStretch(0, 4)
        self.gridLayout_6.addLayout(self.gridLayout_13, 0, 0, 1, 3)
        self.Create.addTab(self.SSS, "")

        index = self.Create.addTab(self.SSS, "SSS Formation")
        self.Create.setTabToolTip(index, "SSS Formation")

        self.SC = QtWidgets.QWidget()
        self.SC.setObjectName("SC")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.SC)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.gridLayout_16 = QtWidgets.QGridLayout()
        self.gridLayout_16.setObjectName("gridLayout_16")
        
        self.pushButton_17 = QtWidgets.QPushButton(self.SC)

        # *** Connection of onClickNextTab4 function ***
        self.pushButton_17.clicked.connect(self.onClickNextTab4)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_16.addWidget(self.pushButton_17, 7, 6, 1, 1)
        
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem30, 2, 0, 1, 1)

        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem31, 8, 3, 1, 1)
        self.SurveyCodes = QtWidgets.QLabel(self.SC)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SurveyCodes.sizePolicy().hasHeightForWidth())
        self.SurveyCodes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SurveyCodes.setFont(font)
        self.SurveyCodes.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SurveyCodes.setStyleSheet("background-color: rgb(87, 122, 131);\n"
"color: rgb(255, 255, 255);")
        self.SurveyCodes.setAlignment(QtCore.Qt.AlignCenter)
        self.SurveyCodes.setObjectName("SurveyCodes")
        self.gridLayout_16.addWidget(self.SurveyCodes, 0, 1, 1, 5)

        
        
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem32, 2, 6, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.SC)

        # *** Connection of onClickPreviousTab4 function ***
        self.pushButton_16.clicked.connect(self.onClickPreviousTab4)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_16.addWidget(self.pushButton_16, 7, 5, 1, 1)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem33, 2, 6, 1, 1)
        self.Default_msg = QtWidgets.QLabel(self.SC)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Default_msg.sizePolicy().hasHeightForWidth())
        self.Default_msg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Default_msg.setFont(font)
        self.Default_msg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Default_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.Default_msg.setObjectName("Default_msg")
        self.gridLayout_16.addWidget(self.Default_msg, 1, 1, 1, 5)

        ###! RSE Method radio buttons {Button 1}
        ###! ***********************************
        self.radioButton_3 = QtWidgets.QRadioButton(self.SC)
        self.radioButton_3.setStyleSheet("background-color: rgb(236, 250, 244);\n"
        "font: 15pt \"MS Shell Dlg 2\";")
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_16.addWidget(self.radioButton_3, 3, 2, 1, 1)

        self.radioButton_2 = QtWidgets.QRadioButton(self.SC)
        self.radioButton_2.setStyleSheet("background-color: rgb(236, 250, 244);font: 15pt \"MS Shell Dlg 2\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_16.addWidget(self.radioButton_2, 4, 2, 1, 1)

        self.radioButton_4 = QtWidgets.QRadioButton(self.SC)
        self.radioButton_4.setStyleSheet("background-color: rgb(236, 250, 244);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_16.addWidget(self.radioButton_4, 5, 2, 1, 1)

        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem34, 8, 4, 1, 1)
        
        spacerItem35 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem35, 6, 1, 1, 6)
        spacerItem36 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem36, 7, 4, 1, 1)
        self.gridLayout_16.setColumnStretch(1, 2)
        self.gridLayout_16.setColumnStretch(2, 3)
        self.gridLayout_16.setColumnStretch(4, 1)
        self.gridLayout_17.addLayout(self.gridLayout_16, 1, 0, 1, 1)
        self.Create.addTab(self.SC, "")

        index = self.Create.addTab(self.SC, "RSE Methods")
        self.Create.setTabToolTip(index, "RSE Methods")

        self.Templates = QtWidgets.QWidget()
        self.Templates.setObjectName("Templates")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.Templates)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pushButton_12 = QtWidgets.QPushButton(self.Templates)

        # *** Connection of onClickPreviousTab5 function ***
        self.pushButton_12.clicked.connect(self.onClickPreviousTab5)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_8.addWidget(self.pushButton_12, 9, 5, 1, 1)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem37, 3, 6, 2, 1)
        self.Data_2 = QtWidgets.QPushButton(self.Templates)

        # *** Connection of onClickDownloadDataTemp function ***
        self.Data_2.clicked.connect(self.onClickDownloadDataTemp)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Data_2.sizePolicy().hasHeightForWidth())
        self.Data_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Data_2.setFont(font)
        self.Data_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Data_2.setObjectName("Data_2")
        self.gridLayout_8.addWidget(self.Data_2, 4, 4, 1, 2)
        self.pushButton_13 = QtWidgets.QPushButton(self.Templates)

        # *** Connection of onClickNextTab5 function ***
        self.pushButton_13.clicked.connect(self.onClickNextTab5)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_8.addWidget(self.pushButton_13, 9, 6, 1, 1)
        spacerItem38 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem38, 0, 3, 2, 3)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem39, 9, 4, 1, 1)
        self.listView = QtWidgets.QListWidget(self.Templates)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listView.setFont(font)
        self.listView.setStyleSheet("\n"
"background-color: rgb(245, 253, 245);")
        self.listView.setObjectName("listView")
        self.gridLayout_8.addWidget(self.listView, 1, 1, 7, 2)
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem40, 1, 0, 1, 1)
        self.Design = QtWidgets.QPushButton(self.Templates)

        # *** Connection of onClickDownloadDesTemp function ***
        self.Design.clicked.connect(self.onClickDownloadDesTemp)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Design.sizePolicy().hasHeightForWidth())
        self.Design.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Design.setFont(font)
        self.Design.setStyleSheet("background-color: rgb(236, 250, 244);")
        self.Design.setObjectName("Design")
        self.gridLayout_8.addWidget(self.Design, 3, 4, 1, 2)
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem41, 9, 3, 1, 1)
        spacerItem42 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem42, 2, 4, 1, 1)
        spacerItem43 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem43, 5, 3, 2, 3)
        spacerItem44 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem44, 7, 3, 2, 3)
        spacerItem45 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem45, 8, 1, 2, 1)
        spacerItem46 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem46, 0, 1, 1, 2)
        self.gridLayout_8.setColumnStretch(0, 1)
        self.gridLayout_8.setColumnStretch(1, 5)
        self.gridLayout_8.setColumnStretch(4, 1)
        self.gridLayout_8.setRowStretch(0, 1)
        self.gridLayout_8.setRowStretch(2, 2)
        self.gridLayout_8.setRowStretch(3, 2)
        self.gridLayout_8.setRowStretch(4, 2)
        self.gridLayout_8.setRowStretch(6, 1)
        self.gridLayout_8.setRowStretch(8, 1)
        self.gridLayout_8.setRowStretch(9, 1)
        self.gridLayout_19.addLayout(self.gridLayout_8, 0, 0, 1, 2)
        self.Create.addTab(self.Templates, "")

        index = self.Create.addTab(self.Templates, "Templates")
        self.Create.setTabToolTip(index, "Templates")

        self.Data = QtWidgets.QWidget()
        self.Data.setStyleSheet("background-color: rgb(191, 200, 198);")
        self.Data.setObjectName("Data")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.Data)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.Data)

        # *** Connection of onClickPreviousTab6 function ***
        self.pushButton_9.clicked.connect(self.onClickPreviousTab6)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_7.addWidget(self.pushButton_9, 1, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.Data)

        # *** Connection of onClickNextTab6 function ***
        self.pushButton_10.clicked.connect(self.onClickNextTab6)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_7.addWidget(self.pushButton_10, 1, 2, 1, 1)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        spacerItem47 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem47, 4, 0, 1, 2)
        self.pushButton_15 = QtWidgets.QPushButton(self.Data)

        # *** Connection of onValidateUploadedData function ***
        self.pushButton_15.clicked.connect(self.onValidateUploadedData)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: rgb(236, 250, 244);")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_14.addWidget(self.pushButton_15, 4, 2, 1, 2)
        spacerItem48 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem48, 0, 3, 1, 1)
        spacerItem49 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem49, 10, 3, 1, 1)
        self.EstimationFile = QtWidgets.QPushButton(self.Data)

        # *** Connection of onValidateUploadedData function ***
        self.EstimationFile.clicked.connect(self.onUploadDataTemplate)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EstimationFile.sizePolicy().hasHeightForWidth())
        self.EstimationFile.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.EstimationFile.setFont(font)
        self.EstimationFile.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EstimationFile.setObjectName("EstimationFile")
        self.gridLayout_14.addWidget(self.EstimationFile, 2, 1, 1, 2)
        self.SampleList1 = QtWidgets.QLineEdit(self.Data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SampleList1.sizePolicy().hasHeightForWidth())
        self.SampleList1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SampleList1.setFont(font)
        self.SampleList1.setStyleSheet("background-color: rgb(236, 250, 244);")
        self.SampleList1.setAlignment(QtCore.Qt.AlignCenter)
        self.SampleList1.setObjectName("SampleList1")
        self.gridLayout_14.addWidget(self.SampleList1, 1, 3, 1, 8)
        spacerItem50 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem50, 4, 7, 1, 1)
        spacerItem51 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem51, 4, 5, 1, 1)
        spacerItem52 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_14.addItem(spacerItem52, 3, 3, 1, 1)
        spacerItem53 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem53, 1, 0, 1, 1)
        self.Estimation1 = QtWidgets.QLineEdit(self.Data)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Estimation1.sizePolicy().hasHeightForWidth())
        self.Estimation1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Estimation1.setFont(font)
        self.Estimation1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Estimation1.setAlignment(QtCore.Qt.AlignCenter)
        self.Estimation1.setObjectName("Estimation1")
        self.gridLayout_14.addWidget(self.Estimation1, 2, 3, 1, 8)
        self.ListFile = QtWidgets.QPushButton(self.Data)

        # *** Connection of onUploadDesignTemplate function ***
        self.ListFile.clicked.connect(self.onUploadDesignTemplate)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ListFile.sizePolicy().hasHeightForWidth())
        self.ListFile.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ListFile.setFont(font)
        self.ListFile.setStyleSheet("background-color: rgb(236, 250, 244);")
        self.ListFile.setObjectName("ListFile")
        self.gridLayout_14.addWidget(self.ListFile, 1, 1, 1, 2)
        spacerItem54 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem54, 4, 6, 1, 1)
        spacerItem55 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem55, 4, 8, 1, 1)
        spacerItem56 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem56, 1, 11, 1, 1)
        spacerItem57 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem57, 4, 9, 1, 3)
        spacerItem58 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem58, 4, 4, 1, 1)
        self.gridLayout_14.setColumnStretch(1, 5)
        self.gridLayout_14.setColumnStretch(3, 8)
        self.gridLayout_7.addLayout(self.gridLayout_14, 0, 0, 1, 3)
        spacerItem59 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem59, 1, 0, 1, 1)
        self.Create.addTab(self.Data, "")

        index = self.Create.addTab(self.Data, "Data Files")
        self.Create.setTabToolTip(index, "Data Files")

        self.Multiplier = QtWidgets.QWidget()

        self.Multiplier.setStyleSheet("background-color: rgb(191, 200, 198);")
        self.Multiplier.setObjectName("Multiplier")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Multiplier)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem60 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem60, 0, 1, 1, 2)
        spacerItem61 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem61, 2, 4, 1, 2)

        self.Multiplier1 = QtWidgets.QPushButton(self.Multiplier)

        # *** Connection of onClickCalcMultilpier function ***
        self.Multiplier1.clicked.connect(self.onClickCalcMultilpier)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Multiplier1.sizePolicy().hasHeightForWidth())
        self.Multiplier1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Multiplier1.setFont(font)
        self.Multiplier1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.Multiplier1.setObjectName("Multiplier1")
        self.gridLayout_2.addWidget(self.Multiplier1, 2, 1, 1, 3)

        ###! Progress Bar
        # self.progressBarMultplierCalc = QtWidgets.QProgressBar(self.Multiplier)
        # self.progressBarMultplierCalc.setProperty("value", 0)
        # self.progressBarMultplierCalc.setObjectName("progressBar")
        # self.gridLayout_2.addWidget(self.progressBarMultplierCalc, 3, 1, 1, 3)

        ###! Progress Bar
        # self.thread = ThreadClass(self.Multiplier)
        # self.thread.actualProgress.connect(self.toShowProgress)

        spacerItem62 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem62, 2, 0, 1, 1)
        spacerItem63 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem63, 4, 1, 1, 2)
        spacerItem64 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem64, 1, 1, 1, 1)
        spacerItem65 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem65, 6, 5, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.Multiplier)

        # *** Connection of onClickPreviousTab7 function ***
        self.pushButton_11.clicked.connect(self.onClickPreviousTab7)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 7, 5, 1, 1)
        self.Export = QtWidgets.QPushButton(self.Multiplier)

        # *** Connection of onClickExport function ***
        self.Export.clicked.connect(self.onClickExport)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Export.sizePolicy().hasHeightForWidth())
        self.Export.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Export.setFont(font)
        self.Export.setStyleSheet("background-color: rgb(87, 122, 131);\n"
"color: rgb(255, 255, 255);")
        self.Export.setObjectName("Export")
        self.gridLayout_2.addWidget(self.Export, 4, 1, 1, 3)
        spacerItem66 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem66, 7, 0, 1, 5)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(5, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.Create.addTab(self.Multiplier, "")

        index = self.Create.addTab(self.Multiplier, "RSE Calculation")
        self.Create.setTabToolTip(index, "RSE Calculation")

        self.gridLayout.addWidget(self.Create, 3, 1, 1, 2)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        spacerItem67 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem67, 0, 1, 1, 1)
        spacerItem68 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem68, 0, 0, 1, 1)
        spacerItem69 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem69, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        # *** Connection of onClickExit function ***
        self.pushButton.clicked.connect(self.onClickExit)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_15.addWidget(self.pushButton, 0, 3, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_15, 5, 2, 1, 1)
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_18.addWidget(self.label_3, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")

        # self.label.setPixmap(QtGui.QPixmap(self.resource_path('C://Users//gaurav//Desktop//MOSPI TOOL SEPTEMBER 2022//MOSPI_TOOL_UPDATES_JULY_2022-master//MOSPI_TOOL_UPDATES_JULY_2022-master//Success.png')))
        self.label.setPixmap(QtGui.QPixmap(self.resource_path('MoSPI_1.png')))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_18.addWidget(self.label, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_18.addWidget(self.label_4, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_18, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        ###! User Manual Button
        ###! ------------------
        self.pushButton_UserManual = QtWidgets.QPushButton(self.centralwidget)
        self.gridLayout_18.addWidget(self.pushButton_UserManual, 2, 1, 1, 1)
        self.pushButton_UserManual.setText("User Manual")
        self.pushButton_UserManual.setFont(font)
        self.pushButton_UserManual.setStyleSheet("background-color: rgb(0, 0, 127);\n"
            "color: rgb(255, 255, 255);\n"
            "")

        # *** Connection of User_Manual function ***
        self.pushButton_UserManual.clicked.connect(self.User_Manual)

        ###
        self.btnGrouptab1 = QtWidgets.QButtonGroup(self.gridLayout_11)
        self.btnGrouptab1.addButton(self.SRSWR_3)
        self.btnGrouptab1.addButton(self.SRSWOR_3)
        self.btnGrouptab1.addButton(self.PPSWR_3)
        self.btnGrouptab1.addButton(self.PPSWOR_3)
        self.btnGrouptab1.addButton(self.SystematicSRS_3)
        self.btnGrouptab1.addButton(self.radioButton_5)

        ###
        self.btnGroupYesNotab1 = QtWidgets.QButtonGroup(self.gridLayout_12)
        self.btnGroupYesNotab1.addButton(self.Yes_2)
        self.btnGroupYesNotab1.addButton(self.No_2)

        #### Disabling widgets of tab 1 (FSU Sampling Method)
        ### ---------------------------
        self.Create.setTabEnabled(1, False)
        self.Create.setTabEnabled(2, False)
        self.Create.setTabEnabled(3, False)
        self.Create.setTabEnabled(4, False)
        self.Create.setTabEnabled(5, False)
        self.Create.setTabEnabled(6, False)
        self.Create.setTabEnabled(7, False)

        #### Disabling previous button of tab7 (Calculate Multiplier)
        self.pushButton_11.setDisabled(True)

        self.retranslateUi(MainWindow)
        self.Create.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    ##! ********************************************************************************************
    ##! Use this function To attach files to the exe file (eg - png, txt, jpg etc) using pyinstaller
    ##! ********************************************************************************************
    def resource_path(self, relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    ### set text of the UI elements
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MOSPI MULTIPLIER TOOL"))
        self.SurveyCodes.setText(_translate("MainWindow", "RSE Methods :"))
        self.Edit.setText(_translate("MainWindow", "Load MULT-DEF File"))
        self.pushButton_2.setText(_translate("MainWindow", "Next"))
        self.create.setText(_translate("MainWindow", "Create MULT-DEF File"))
        self.Create.setTabText(
            self.Create.indexOf(self.Create_2),
            _translate("MainWindow", "MULT-DEF File"),
        )
        self.radioButton_3.setText(_translate("MainWindow", "Systematic Sampling"))
        self.radioButton_4.setText(_translate("MainWindow", "JackKnife Method"))
        self.radioButton_2.setText(_translate("MainWindow", "Bootstrap Method"))
        self.pushButton_5.setText(_translate("MainWindow", "Previous"))
        self.pushButton_6.setText(_translate("MainWindow", "Next"))
        self.No_2.setText(_translate("MainWindow", "                            No"))
        self.Yes_2.setText(_translate("MainWindow", "                           Yes"))
        self.SSU_2.setText(_translate("MainWindow", "Sub-Sampling used"))
        self.SSN_2.setText(
            _translate(
                "MainWindow", "         If Yes, number of Sub-Sample used          "
            )
        )
        self.SRSWOR_3.setText(
            _translate("MainWindow", "                               SRSWOR")
        )
        self.SRSWR_3.setText(
            _translate("MainWindow", "                               SRSWR")
        )
        self.PPSWOR_3.setText(
            _translate("MainWindow", "                               PPSWOR")
        )
        self.radioButton_5.setText(
            _translate("MainWindow", "                              Systematic PPS")
        )
        self.PPSWR_3.setText(
            _translate("MainWindow", "                               PPSWR")
        )
        self.SystematicSRS_3.setText(
            _translate("MainWindow", "                               Systematic SRS")
        )
        self.Create.setTabText(
            self.Create.indexOf(self.FSU),
            _translate("MainWindow", "FSU Sampling Method"),
        )
        self.pushButton_3.setText(_translate("MainWindow", "Previous"))
        self.PurPPS.setText(
            _translate(
                "MainWindow", "        Two selected, one purposefully, another by PPS"
            )
        )
        self.SRS.setText(_translate("MainWindow", "        Only one selected by SRS"))
        self.EntireFSU.setText(
            _translate("MainWindow", "         Entire FSU is surveyed")
        )
        self.PPS.setText(_translate("MainWindow", "        Only one selected by PPS"))
        self.SRSWORSYS.setText(
            _translate("MainWindow", "        Two selected by SRSWOR/SYSTEMATIC")
        )
        self.PPSSRS.setText(
            _translate(
                "MainWindow", "        Two selected, one purposefully, another by SRS"
            )
        )
        self.radioButton.setText(
            _translate(
                "MainWindow",
                "        Three selected, one purposefully, two merged into one group by SRS  ",
            )
        )
        self.pushButton_4.setText(_translate("MainWindow", "Next"))
        self.Create.setTabText(
            self.Create.indexOf(self.HGFormation),
            _translate("MainWindow", "HG/SB or Sub-Division Formation"),
        )
        self.pushButton_7.setText(_translate("MainWindow", "Previous"))
        self.pushButton_8.setText(_translate("MainWindow", "Next"))
        self.label_2.setText(
            _translate(
                "MainWindow", "    Enter number of Second Stage Stratum used    "
            )
        )
        self.Create.setTabText(
            self.Create.indexOf(self.SSS), _translate("MainWindow", "SSS Formation")
        )
        self.pushButton_17.setText(_translate("MainWindow", "Next"))
        self.Default_msg.setText(
            _translate(
                "MainWindow",
                "Select the appropriate RSE Method",
            )
        )
        self.pushButton_16.setText(_translate("MainWindow", "Previous"))
        self.Create.setTabText(
            self.Create.indexOf(self.SC), _translate("MainWindow", "RSE Methods")
        )
        self.pushButton_12.setText(
            _translate("MainWindow", "Go back to select options again")
        )
        self.Data_2.setText(_translate("MainWindow", "Download the Data Template"))
        self.Design.setText(_translate("MainWindow", "Download the Design Template"))
        self.pushButton_13.setText(_translate("MainWindow", "Next"))
        self.Create.setTabText(
            self.Create.indexOf(self.Templates), _translate("MainWindow", "Templates")
        )
        self.pushButton_9.setText(_translate("MainWindow", "Previous"))
        self.pushButton_10.setText(_translate("MainWindow", "Next"))
        self.Estimation1.setPlaceholderText(
            _translate("MainWindow", "  Your uploaded file name will display here ...")
        )
        self.pushButton_15.setText(_translate("MainWindow", "Validate Uploaded Data"))
        self.EstimationFile.setText(
            _translate("MainWindow", "Upload the Data of Data Template")
        )
        self.ListFile.setText(
            _translate("MainWindow", "Upload the Data of Design Template")
        )
        self.SampleList1.setPlaceholderText(
            _translate("MainWindow", "  Your uploaded file name will display here ...")
        )
        self.Create.setTabText(
            self.Create.indexOf(self.Data), _translate("MainWindow", "Data Files")
        )
        self.Multiplier1.setText(_translate("MainWindow", "CALCULATE MULTIPLIER"))
        self.pushButton_11.setText(_translate("MainWindow", "Previous"))
        self.Export.setText(_translate("MainWindow", "EXPORT"))
        self.Create.setTabText(
            self.Create.indexOf(self.Multiplier),
            _translate("MainWindow", "RSE Calculation"),
        )
        self.pushButton.setText(_translate("MainWindow", "EXIT"))
        self.label_3.setText(
            _translate(
                "MainWindow",
                "Relative Standard Error Calculator for NSS Two- Stage Samples",
            )
        )

    ### Function to create a blank mult file
    ### ************************************
    def Create_MULT_DEF_FILE(self):
        global fname, flag, stack_create
        fname = QtWidgets.QFileDialog.getSaveFileName(
            None, "Save file", (QtCore.QDir.currentPath()), "MULT-DEF files (*.mlt)"
        )[0]

        ### Initializing deque as blank stack
        stack_create = deque()

        self.label_4.setText(fname.split('/')[-1])

        ### creating a blank mult_def file
        try:
            with open(fname, "w+") as fp:
                msg_ = msgBox_UI()
                msg_.label_2.setText("File created successfully")
                msg_.pushButton.clicked.connect(msg_.success)
                returnValue = msg_.exec_()

                if returnValue == 1:
                    pass
        except:
            pass

        try:
            if flag == "upload_flag":
                ### Enabling Tab1
                self.Create.setTabEnabled(1, True)

                ###! Enabling all the widgets of Tab0 ###
                self.SRSWR_3.setDisabled(False)
                self.SRSWOR_3.setDisabled(False)
                self.PPSWR_3.setDisabled(False)
                self.PPSWOR_3.setDisabled(False)
                self.SystematicSRS_3.setDisabled(False)
                self.radioButton_5.setDisabled(False)

                ###! Enabling all the widgets of Tab0 ###
                self.No_2.setDisabled(False)
                self.Yes_2.setDisabled(False)
                self.SubSample_num.setDisabled(False)

                ###! Enabling all radio buttons after filling automatically from the stack_load
                self.EntireFSU.setDisabled(False)
                self.radioButton.setDisabled(False)
                self.PPSSRS.setDisabled(False)
                self.SRSWORSYS.setDisabled(False)
                self.PurPPS.setDisabled(False)
                self.SRS.setDisabled(False)
                self.PPS.setDisabled(False)
                self.No_SSS.setDisabled(False)
                self.Inhabited_SC.setDisabled(False)
                self.Uninhabited_SC.setDisabled(False)
                self.casualty_codes.setDisabled(False)

        except:
            pass

        ### ************************************
        ### ********** create flag *************
        flag = "create_flag"

        return stack_create


    ### To open file dialog to browse the files and select the required file extension
    ### ******************************************************************************
    def Load_MULT_DEF_FILE(self):
        global fname, flag, stack_load, uploaded_data

        ### Initializing deque as blank stack for uploading mult file
        stack_load = deque()

        ### Calling UI_DIALOG class from NEW_DIALOG.py file
        ui = Ui_Dialog()

        ### To handle the code of file uploading the MULT File in tab 0
        try:
            ### On Accept of the dialog button
            if ui.exec_() == QtWidgets.QDialog.Accepted:
                fname = ui.fname[0]
                self.label_4.setText(fname.split('/')[-1])
                ui.close()

            ### Reading uploaded file
            with open(fname, "r") as f:
                uploaded_data = f.readlines()

            ### Message Box
            msg_ = msgBox_UI()
            msg_.label_2.setText("File uploaded successfully")
            msg_.pushButton.clicked.connect(msg_.success)
            returnValue = msg_.exec_()

            if returnValue == 1:
                print("OK clicked - File Uploaded")
                pass

            ### ************************************
            ### ********** create upload flag *************
            flag = "upload_flag"

        ### If try case fails then just assign the None to fname
        except:
            fname = None
            pass

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("No file has been uploaded!")
            msgBox.setWindowTitle("Alert!")
            msgBox.setStyleSheet(
                "QMessageBox { width:800px; height:800px; } QPushButton{ width:140px; font-size: 20px; }"
            )
            msgBox.setStyleSheet("background-color: #EF9A9A;")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()

            if returnValue == QMessageBox.Ok:
                pass

        finally:
            pass

    ### Regferencing the uploaded data variable to further function
    def reference_uploaded_data(self):
        return uploaded_data

    def reference_flag(self):
        return flag

    ### Tab 0 on click functionality
    ### ----------------------------
    def onClickNextTab0(self):
        ### To validate the mandatory steps in loading the file

        ### Calling UI_Main Class
        ui = Ui_Dialog()

        # try:
        ### if user has not selected any file
        if fname == None:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText(
                "Please Create or Load a Mult File before proceeding further."
            )
            msgBox.setWindowTitle("Critical")
            msgBox.setStyleSheet(
                "QMessageBox { width:800px; height:800px; } QPushButton{ width:140px; font-size: 20px; }"
            )
            msgBox.setStyleSheet("background-color: #B2DFDB;")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()

            if returnValue == QMessageBox.Ok:
                pass

        ### if file is uploaded
        elif fname != None:
            try:
                ### Upload Flag is called
                if flag == "upload_flag":
                    ### Getting the reference of the uploaded data mult file
                    uploaded_data = self.reference_uploaded_data()

                    if len(uploaded_data) == 0:
                        msgBox = QMessageBox()
                        msgBox.setIcon(QMessageBox.Critical)
                        # msgBox.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowTitleHint)
                        msgBox.setText(
                            "Please upload valid MULT-DEF file"
                        )
                        msgBox.setWindowTitle("Critical")
                        msgBox.setStyleSheet(
                            "QMessageBox { width:800px; height:800px; } QPushButton{ width:140px; font-size: 20px; }"
                        )
                        msgBox.setStyleSheet("background-color: #ffebee;")
                        msgBox.setStandardButtons(QMessageBox.Ok)
                        returnValue = msgBox.exec()

                        if returnValue == QMessageBox.Ok:
                            pass

                    elif len(uploaded_data) > 0:
                        self.Create.setTabEnabled(1, True)
                        self.Create.setTabEnabled(0, False)
                        
                        ### Removing new lines
                        uploaded_data = [
                            uploaded_data[i].strip() for i in range(len(uploaded_data))
                        ]

                        ### Removing Blank elements from the uploaded_dat
                        while "" in uploaded_data:
                            uploaded_data.remove("")

                        ###  Removing header from the mult file
                        uploaded_data = uploaded_data[2:]

                        ### Appending the split data into the stack
                        for i in uploaded_data:
                            stack_load.append(i.split(" - ")[1:])

                        ### Variable to store spinBox data from the mult file directly
                        num = int(list(stack_load[0])[2])

                        ### If uploaded data matches our requirement then further reqd. actions undertaken
                        if (
                            list(stack_load[0])[0]
                            == (str(self.SRSWR_3.text().ljust(0, " "))).strip()
                        ):
                            self.SRSWR_3.setChecked(True)
                        elif (
                            list(stack_load[0])[0]
                            == (str(self.SRSWOR_3.text().ljust(0, " "))).strip()
                        ):
                            self.SRSWOR_3.setChecked(True)
                        elif (
                            list(stack_load[0])[0]
                            == (str(self.PPSWR_3.text().ljust(0, " "))).strip()
                        ):
                            self.PPSWR_3.setChecked(True)
                        elif (
                            list(stack_load[0])[0]
                            == (str(self.PPSWOR_3.text().ljust(0, " "))).strip()
                        ):
                            self.PPSWOR_3.setChecked(True)
                        elif (
                            list(stack_load[0])[0]
                            == (str(self.SystematicSRS_3.text().ljust(0, " "))).strip()
                        ):
                            self.SystematicSRS_3.setChecked(True)
                        elif (
                            list(stack_load[0])[0]
                            == (str(self.radioButton_5.text().ljust(0, " "))).strip()
                        ):
                            self.radioButton_5.setChecked(True)

                        ### Disabling radio buttons in tab1 (FSU Sampling Method)
                        self.SRSWR_3.setDisabled(True)
                        self.SRSWOR_3.setDisabled(True)
                        self.PPSWR_3.setDisabled(True)
                        self.PPSWOR_3.setDisabled(True)
                        self.SystematicSRS_3.setDisabled(True)
                        self.radioButton_5.setDisabled(True)

                        if (
                            list(stack_load[0])[1]
                            == (str(self.No_2.text().ljust(0, " "))).strip()
                        ):
                            self.No_2.setChecked(True)
                            self.SubSample_num.setValue(num)
                        elif (
                            list(stack_load[0])[1]
                            == (str(self.Yes_2.text().ljust(0, " "))).strip()
                        ):
                            self.Yes_2.setChecked(True)
                            self.SubSample_num.setValue(num)

                        ###! Disabling all the widgets of Tab0 (MULT-DEF File) ###
                        ###  *****************************************************
                        self.No_2.setDisabled(True)
                        self.Yes_2.setDisabled(True)
                        self.SubSample_num.setDisabled(True)

                        self.Create.setCurrentIndex(1)

                ### Create Flag is called
                elif flag == "create_flag":
                    self.Create.setTabEnabled(1, True)
                    self.Create.setTabEnabled(0, False)
                    self.Create.setCurrentIndex(1)

            except:
                ### Message Box
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Critical)
                msgBox.setText(
                    "Please Create or Load a Mult File before proceeding further."
                )
                msgBox.setWindowTitle("Critical")
                msgBox.setStyleSheet(
                    "QMessageBox { width:800px; height:800px; } QPushButton{ width:140px; font-size: 20px; }"
                )
                msgBox.setStyleSheet("background-color: #ffebee;")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()

                if returnValue == QMessageBox.Ok:
                    pass

    ### Tab1(FSU Sampling Method) click functionality for next and previous buttons
    ### ***************************************************************************
    def onClickNextTab1(self):

        ### Verifying the flag 
        if flag == "create_flag":

            ### Handling button group tab1
            def test(self):
                checked_btn = [
                    button.text().ljust(0, " ").strip()
                    for i, button in enumerate(self.btnGrouptab1.buttons())
                    if button.isChecked()
                ]
                return checked_btn[0]

            ### Handling button group tab2
            def test_2(self):
                checked_btn = [
                    button.text().ljust(0, " ").strip()
                    for i, button in enumerate(self.btnGroupYesNotab1.buttons())
                    if button.isChecked()
                ]
                return checked_btn[0]

            if len(stack_create) == 3:
                ## if yes is selected in tab1
                if (
                    test(self)
                    and (test_2(self) == "Yes")
                    and (int(self.SubSample_num.value()) > 1) == True
                ):
                    self.Create.setCurrentIndex(2)

                    ## Disabling tab1 and enabling tab2
                    self.Create.setTabEnabled(2, True)
                    self.Create.setTabEnabled(1, False)

                    ### popping the top of stack three times as empty stack is required to fill it again with the updated values
                    stack_create.pop()
                    stack_create.pop()
                    stack_create.pop()

                    ##* Pushing the selected elements of tab1 in stack
                    ##* pushing the first radio button (statistical method) from tab2 in stack
                    stack_create.append(
                        (
                            str(self.btnGrouptab1.checkedButton().text().ljust(0, " "))
                        ).strip()
                    )
                    print(stack_create)

                    ## pushing the second radio button (yes/no) from tab2 in stack
                    stack_create.append(
                        (
                            str(
                                self.btnGroupYesNotab1.checkedButton()
                                .text()
                                .ljust(0, " ")
                            )
                        ).strip()
                    )

                    ## pushing the third spinBox (subsample) from tab2 in stack
                    stack_create.append(
                        (str(self.SubSample_num.text().ljust(0, " "))).strip()
                    )
    

                ## if No is selected in tab2
                elif (
                    test(self)
                    and (test_2(self) == "No")
                    and (int(self.SubSample_num.value()) == 1) == True
                ):
                    self.Create.setCurrentIndex(2)

                    ### popping the top of stack three times as empty stack is required to fill it again with the updated values
                    stack_create.pop()
                    stack_create.pop()
                    stack_create.pop()

                    ## pushing the first radio button (statistical method) from tab2 in stack
                    stack_create.append(
                        (
                            str(self.btnGrouptab1.checkedButton().text().ljust(0, " "))
                        ).strip()
                    )
                    print(stack_create)

                    ## pushing the second radio button (yes/no) from tab2 in stack
                    stack_create.append(
                        (
                            str(
                                self.btnGroupYesNotab1.checkedButton()
                                .text()
                                .ljust(0, " ")
                            )
                        ).strip()
                    )
                    print(stack_create)

                    ## pushing the third spinBox (subsample) from tab2 in stack
                    stack_create.append("1")
                    print(stack_create)

                    self.onToggledSubSample_num()

                    self.SubSample_num.setValue(1)

                    ## Disabling tab1 and enabling tab2
                    self.Create.setTabEnabled(2, True)
                    self.Create.setTabEnabled(1, False)
            else:
                try:
                    ## if yes is selected in tab1
                    if (
                        test(self)
                        and (test_2(self) == "Yes")
                        and (int(self.SubSample_num.value()) > 1) == True
                    ):
                        self.Create.setCurrentIndex(2)
                        ## Pushing the selected elements of tab1 in stack
                        ## pushing the first radio button (statistical method) from tab2 in stack
                        stack_create.append(
                            (
                                str(
                                    self.btnGrouptab1.checkedButton()
                                    .text()
                                    .ljust(0, " ")
                                )
                            ).strip()
                        )

                        ## pushing the second radio button (yes/no) from tab2 in stack
                        stack_create.append(
                            (
                                str(
                                    self.btnGroupYesNotab1.checkedButton()
                                    .text()
                                    .ljust(0, " ")
                                )
                            ).strip()
                        )

                        ## pushing the third spinBox (subsample) from tab2 in stack
                        stack_create.append(
                            (str(self.SubSample_num.text().ljust(0, " "))).strip()
                        )

                        ## Disabling tab1 and enabling tab2
                        self.Create.setTabEnabled(2, True)
                        self.Create.setTabEnabled(1, False)

                    ## if No is selected in tab2
                    elif (
                        test(self)
                        and (test_2(self) == "No")
                        and (int(self.SubSample_num.value()) == 1) == True
                    ):
                        self.Create.setCurrentIndex(2)

                        ## Disabling tab1 and enabling tab2
                        self.Create.setTabEnabled(2, True)
                        self.Create.setTabEnabled(1, False)

                        ## pushing the first radio button (statistical method) from tab2 in stack
                        stack_create.append(
                            (
                                str(
                                    self.btnGrouptab1.checkedButton()
                                    .text()
                                    .ljust(0, " ")
                                )
                            ).strip()
                        )
         

                        ## pushing the second radio button (yes/no) from tab2 in stack
                        stack_create.append(
                            (
                                str(
                                    self.btnGroupYesNotab1.checkedButton()
                                    .text()
                                    .ljust(0, " ")
                                )
                            ).strip()
                        )
                        print(stack_create)

                        ## pushing the third spinBox (subsample) from tab2 in stack
                        stack_create.append("1")
                        print(stack_create)

                        self.onToggledSubSample_num()

                        self.SubSample_num.setValue(1)

                    else:
                        if (
                            self.No_2.isChecked()
                            and (int(self.SubSample_num.value()) > 1) == True
                        ):
                            msgBox = QMessageBox()
                            msgBox.setIcon(QMessageBox.Critical)
                            msgBox.setText(
                                "Please change the above option if number of sub samples is greater than 1, otherwise it should be 1."
                            )
                            msgBox.setWindowTitle("Critical")
                            msgBox.setStyleSheet(
                                "QMessageBox { width:800px; height:800px; } QPushButton{ width:140px; font-size: 20px; }"
                            )
                            msgBox.setStyleSheet("background-color: #FFCDD2;")
                            msgBox.setStandardButtons(QMessageBox.Ok)
                            returnValue = msgBox.exec()

                            if returnValue == QMessageBox.Ok:
                                print("OK clicked")

                        elif (
                            self.Yes_2.isChecked()
                            and (int(self.SubSample_num.value()) < 2) == True
                        ):
                            msgBox = QMessageBox()
                            msgBox.setIcon(QMessageBox.Critical)
                            msgBox.setText(
                                "Please select the number of sub samples used, which should be greater than 1."
                            )
                            msgBox.setWindowTitle("Critical")
                            msgBox.setStyleSheet(
                                "QMessageBox { width:800px; height:800px; } QPushButton{ width:140px; font-size: 20px; }"
                            )
                            msgBox.setStyleSheet("background-color: #FFCDD2;")
                            msgBox.setStandardButtons(QMessageBox.Ok)
                            returnValue = msgBox.exec()

                            if returnValue == QMessageBox.Ok:
                                print("OK clicked")

                        else:
                            msgBox = QMessageBox()
                            msgBox.setIcon(QMessageBox.Critical)
                            msgBox.setText("Please select all the options.")
                            msgBox.setWindowTitle("Critical")
                            msgBox.setStyleSheet(
                                "QMessageBox { width:800px; height:800px; } QPushButton{ width:140px; font-size: 20px; }"
                            )
                            msgBox.setStyleSheet("background-color: #FFCDD2;")
                            msgBox.setStandardButtons(QMessageBox.Ok)
                            returnValue = msgBox.exec()

                            if returnValue == QMessageBox.Ok:
                                print("OK clicked")

                except:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Critical)
                    msgBox.setText("Please select all the options.")
                    msgBox.setWindowTitle("Critical")
                    msgBox.setStyleSheet(
                        "QMessageBox { width:800px; height:800px; } QPushButton{ width:140px; font-size: 20px; }"
                    )
                    msgBox.setStyleSheet("background-color: #FFCDD2;")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    returnValue = msgBox.exec()

                    if returnValue == QMessageBox.Ok:
                        print("OK clicked")

        elif flag == "upload_flag":
            print(stack_load)

            ### If uploaded data matches our requirement
            if (
                list(stack_load[1])[0]
                == (str(self.EntireFSU.text().ljust(0, " "))).strip()
            ):
                self.EntireFSU.setChecked(True)
            elif (
                list(stack_load[1])[0]
                == (str(self.radioButton.text().ljust(0, " "))).strip()
            ):
                self.radioButton.setChecked(True)
            elif (
                list(stack_load[1])[0]
                == (str(self.PPSSRS.text().ljust(0, " "))).strip()
            ):
                self.PPSSRS.setChecked(True)
            elif (
                list(stack_load[1])[0]
                == (str(self.SRSWORSYS.text().ljust(0, " "))).strip()
            ):
                self.SRSWORSYS.setChecked(True)
            elif (
                list(stack_load[1])[0]
                == (str(self.PurPPS.text().ljust(0, " "))).strip()
            ):
                self.PurPPS.setChecked(True)
            elif (
                list(stack_load[1])[0] == (str(self.SRS.text().ljust(0, " "))).strip()
            ):
                self.SRS.setChecked(True)
            elif (
                list(stack_load[1])[0] == (str(self.PPS.text().ljust(0, " "))).strip()
            ):
                self.PPS.setChecked(True)

            ### Disabling all radio buttons after filling automatically from the stack_load
            self.EntireFSU.setDisabled(True)
            self.radioButton.setDisabled(True)
            self.PPSSRS.setDisabled(True)
            self.SRSWORSYS.setDisabled(True)
            self.PurPPS.setDisabled(True)
            self.SRS.setDisabled(True)
            self.PPS.setDisabled(True)

            self.Create.setCurrentIndex(2)

            ## Disabling tab1 and enabling tab2
            self.Create.setTabEnabled(2, True)
            self.Create.setTabEnabled(1, False)

    ###! On click Previous of Tab1 (FSU Sampling Method)
    def onClickPreviousTab1(self):

        ###! For create flag
        if flag == "create_flag":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(
                "Are you sure you want to go back? This will reset your current selection."
            )
            msgBox.setWindowTitle("Warning!")
            msgBox.setStyleSheet(
                "QMessageBox { width:800px; height:800px; } QPushButton{ width:140px; font-size: 20px; }"
            )
            msgBox.setStyleSheet("background-color: #B2DFDB;")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            returnValue = msgBox.exec()

            ### To verify the return value (yes/no)
            if returnValue == QMessageBox.Yes:

                ### To verify if top of the stack is empty or Not
                if len(stack_create) > 2:
                    ## Disabling tab1 and enabling tab0
                    self.Create.setTabEnabled(0, True)
                    self.Create.setTabEnabled(1, False)

                    ### Automatically unchecking BUTTON GROUPS
                    ### ------------------------------------------

                    self.btnGrouptab1.setExclusive(False)
                    for button in self.btnGrouptab1.buttons():
                        button.setChecked(False)
                    self.btnGrouptab1.setExclusive(True)

                    self.btnGroupYesNotab1.setExclusive(False)
                    for button in self.btnGroupYesNotab1.buttons():
                        button.setChecked(False)
                    self.btnGroupYesNotab1.setExclusive(True)

                    ### Setting default value in Sub Sample Text
                    self.SubSample_num.setValue(1)

                    ## If stack ids filled with
                    if stack_create:
                        stack_create.pop()
                        stack_create.pop()
                        stack_create.pop()
                        print(stack_create)
                    else:
                        pass

                    ### Setting current index of tab - 0
                    self.Create.setCurrentIndex(0)

                elif len(stack_create) == 0:
                    ### Automatically unchecking of BUTTON GROUPS
                    ### ------------------------------------------

                    ## Disabling tab1 and enabling tab0
                    self.Create.setTabEnabled(0, True)
                    self.Create.setTabEnabled(1, False)

                    self.btnGrouptab1.setExclusive(False)
                    for button in self.btnGrouptab1.buttons():
                        button.setChecked(False)
                    self.btnGrouptab1.setExclusive(True)

                    self.btnGroupYesNotab1.setExclusive(False)
                    for button in self.btnGroupYesNotab1.buttons():
                        button.setChecked(False)
                    self.btnGroupYesNotab1.setExclusive(True)

                    self.SubSample_num.setValue(1)

                    self.Create.setCurrentIndex(0)

            elif returnValue == QMessageBox.No:
                pass

        ###! For upload flag
        elif flag == "upload_flag":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(
                "A file has already been uploaded."
            )
            msgBox.setWindowTitle("Warning!")
            msgBox.setStyleSheet(
            "QMessageBox { width:800px; height:800px; } QPushButton{ width:140px; font-size: 20px; }"
            )
            msgBox.setStyleSheet("background-color: #B2DFDB;")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()

            ### To verify the return value (yes/no)
            if returnValue == QMessageBox.Ok:
                ## Disabling tab1 and enabling tab0
                self.Create.setTabEnabled(0, True)
                self.Create.setTabEnabled(1, False)

                self.Create.setCurrentIndex(0)

    ###! Handling toggle button in Sub Sample
    def onToggledSubSample_num(self):
        ### Opening mult file for first time on toggle of SubSampleNum_2

        ###! For create flag
        if flag == "create_flag":
            if self.Yes_2.isChecked() == True:
                pass
            else:
                self.SubSample_num.setValue(1)
                self.SubSample_num.setEnabled(True)

        ###! For upload flag
        elif flag == "upload_flag":
            pass

    ###! *******************  Tab 2 click functionality **********************
    def onClickNextTab2(self):
        ###! For create flag
        if flag == "create_flag":

            def btnGrpTab2(self):
                checked_btn = [
                    button.text().ljust(0, " ").strip()
                    for i, button in enumerate(self.btnGrouptab2.buttons())
                    if button.isChecked()
                ]
                return checked_btn[0]

            try:
                if btnGrpTab2(self):
                    if len(stack_create) == 4:
                        self.Create.setCurrentIndex(3)

                        ## Disabling tab2 and enabling tab3
                        self.Create.setTabEnabled(3, True)
                        self.Create.setTabEnabled(2, False)

                        stack_create.pop()
                        ## pushing the second radio button (yes/no) from tab2 in stack
                        stack_create.append(
                            (
                                str(
                                    self.btnGrouptab2.checkedButton()
                                    .text()
                                    .ljust(0, " ")
                                )
                            ).strip()
                        )
                        print(stack_create)

                    elif len(stack_create) == 3:
                        self.Create.setCurrentIndex(3)

                        ## Disabling tab2 and enabling tab3
                        self.Create.setTabEnabled(3, True)
                        self.Create.setTabEnabled(2, False)

                        ## pushing the second radio button (yes/no) from tab2 in stack
                        stack_create.append(
                            (
                                str(
                                    self.btnGrouptab2.checkedButton()
                                    .text()
                                    .ljust(0, " ")
                                )
                            ).strip()
                        )

            except:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Please select an option to proceed further.")
                msgBox.setWindowTitle("Warning!")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()

                ### To verify the return value (yes/no)
                if returnValue == QMessageBox.Ok:
                    pass

        ###! For Upload Flag
        elif flag == "upload_flag":
            ## Disabling tab2 and enabling tab3
            self.Create.setTabEnabled(3, True)
            self.Create.setTabEnabled(2, False)

            num = int(list(stack_load[2])[0])
            self.No_SSS.setValue(num)
            self.No_SSS.setDisabled(True)
            self.Create.setCurrentIndex(3)

        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Critical)
            msgBox.setText("Please select an option before proceeding.")
            msgBox.setWindowTitle("Critical")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()

            if returnValue == QMessageBox.Ok:
                pass

    def onClickPreviousTab2(self):
        if flag == "create_flag":
            print("Previous Button Tab 1")
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(
                "Are you sure you want to go back? This will reset your current selection."
            )
            msgBox.setWindowTitle("Warning!")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            returnValue = msgBox.exec()

            ### To verify the return value (yes/no)
            if returnValue == QMessageBox.Yes:
                ## Disabling tab2 and enabling tab1

                ### To verify if top of the stack is empty or Not
                if len(stack_create) > 3:
                    ## Disabling tab2 and enabling tab1
                    self.Create.setTabEnabled(1, True)
                    self.Create.setTabEnabled(2, False)

                    ### Automatically unchecking of BUTTON GROUPS
                    ### ------------------------------------------

                    self.btnGrouptab2.setExclusive(False)
                    for button in self.btnGrouptab2.buttons():
                        button.setChecked(False)
                    self.btnGrouptab2.setExclusive(True)

                    ## If stack ids filled with
                    if stack_create:
                        stack_create.pop()
                        print(stack_create)
                    else:
                        pass

                    ### Setting current index of tab2 to tab1
                    self.Create.setCurrentIndex(1)

                elif len(stack_create) == 3:
                    ### Automatically unchecking of BUTTON GROUPS
                    ### ------------------------------------------

                    ## Disabling tab2 and enabling tab1
                    self.Create.setTabEnabled(1, True)
                    self.Create.setTabEnabled(2, False)

                    self.btnGrouptab2.setExclusive(False)
                    for button in self.btnGrouptab2.buttons():
                        button.setChecked(False)
                    self.btnGrouptab2.setExclusive(True)

                    self.Create.setCurrentIndex(1)

            elif returnValue == QMessageBox.No:
                pass

            ##Disabling tab1 and enabling tab0
            # self.Create.setTabEnabled(0,True)
            # self.Create.setTabEnabled(1,False)

        elif flag == "upload_flag":
            ## Disabling tab2 and enabling tab1
            self.Create.setTabEnabled(1, True)
            self.Create.setTabEnabled(2, False)

            self.Create.setCurrentIndex(1)

    ###! onToggle Tab 3 click functionality
    ###! *********************************
    def onToggled_No_SSS(self):
        ### Opening mult file for first time on toggle of SubSampleNum_2
        if flag == "create_flag":
            pass
        elif flag == "upload_flag":
            pass
        else:
            pass

    ###! Next of Tab 3 click functionality
    ###! *********************************
    def onClickNextTab3(self):
        global inh, unih, csc

        if flag == "create_flag":
            ## Disabling tab2 and enabling tab1
            self.Create.setTabEnabled(4, True)
            self.Create.setTabEnabled(3, False)

            stack_create.append((str(self.No_SSS.text().ljust(0, " "))).strip())
            ### Change current index
            self.Create.setCurrentIndex(4)

        elif flag == "upload_flag":
            ## Disabling tab2 and enabling tab1
            self.Create.setTabEnabled(4, True)
            self.Create.setTabEnabled(3, False)

            ### Removing sq brackets from the text
            inh = str(list(stack_load[3])[0]).strip("[]")
            unih = str(list(stack_load[3])[1]).strip("[]")
            csc = str(list(stack_load[3])[2]).strip("[]")

            ### Change current index of tab
            self.Create.setCurrentIndex(4)

        else:
            pass

    ###! Previous of Tab 3 click functionality
    ###! *************************************
    def onClickPreviousTab3(self):
        if flag == "create_flag":
            print("Previous Button Tab 1")
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(
                "Are you sure you want to go back? This will reset your current selection."
            )
            msgBox.setWindowTitle("Warning!")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            returnValue = msgBox.exec()

            ### To verify the return value (yes/no)
            if returnValue == QMessageBox.Yes:

                ### To verify if top of the stack is empty or Not
                if len(stack_create) > 4:
                    ## Disabling tab3 and enabling tab2
                    self.Create.setTabEnabled(2, True)
                    self.Create.setTabEnabled(3, False)
                    self.No_SSS.setValue(1)

                    ## If stack ids filled with
                    if stack_create:
                        stack_create.pop()
                        print(stack_create)
                    else:
                        pass

                    ### Setting current index of tab - 0
                    self.Create.setCurrentIndex(2)

                elif len(stack_create) > 3:
                    ### Automatically unchecking of BUTTON GROUPS
                    ### ------------------------------------------

                    ## Disabling tab3 and enabling tab2
                    self.Create.setTabEnabled(2, True)
                    self.Create.setTabEnabled(3, False)
                    self.No_SSS.setValue(1)
                    self.Create.setCurrentIndex(2)

            elif returnValue == QMessageBox.No:
                pass

        elif flag == "upload_flag":
            ## Disabling tab3 and enabling tab2
            self.Create.setTabEnabled(2, True)
            self.Create.setTabEnabled(3, False)
            self.Create.setCurrentIndex(2)

    ###! ************************ HANDLING FUNCTIONS OF TAB 4 ************************
    ###! *****************************************************************************

    ## Inhabited
    def onFillingInhabited_SC(self):
        pass

    ## Uninhabited
    def onFillingUninhabited_SC(self):
        pass

    ## Casualty
    def onFillingCasualty(self):
        pass

    ###! Next of Tab 4 click functionality
    ###! *********************************
    def onClickNextTab4(self):
        global inh, unih, csc

        if flag == "create_flag":
            ### Message Box to ask for the creation of mult file as well as data and design templates
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(
                "Click 'Yes' to confirm your selections and to update your mult file."
            )
            msgBox.setWindowTitle("Warning!")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            returnValue = msgBox.exec()

            ### To verify the return value (yes/no)
            if returnValue == QMessageBox.Yes:
                global lst_Design_Template, lst_Data_Template, createList

                ## Disabling tab4 and enabling tab5
                self.Create.setTabEnabled(5, True)
                self.Create.setTabEnabled(4, False)
                self.Create.setCurrentIndex(5)

                ### ************************ REQD TEMPLATES ***************************
                ### *******************************************************************
                ### Design Template
                if stack_create[0] == ('SRSWR' or 'SRSWOR' or 'Systematic SRS'):
                    lst_Design_Template = ["strm_id", "fsu", "capzs"]
                else:
                    lst_Design_Template = ["strm_id", "fsu", "capzs", "smallzs"]

                ### If sub sample number selected by user is greater than 1
                if int(stack_create[2]) > 1:
                    lst_Design_Template.append('ss_no') 
                else:
                    pass

                ###! *** TAB 3 *** Data Template
                ###* CASE1
                if stack_create[3] == 'Entire FSU is surveyed':
                    # lst_Data_Template = ["strm_id", "fsu", "svc"]
                    lst_Data_Template = ["fsu", "svc"]
                    for j in range(1, 2):
                        for i in range(1, int(stack_create[4]) + 1):
                            lst_Data_Template.append('caph' + str(i) + str(j))
                            lst_Data_Template.append('smlh' + str(i) + str(j))
                        break

                if stack_create[3] == 'Only one selected by SRS':
                    lst_Data_Template = ["fsu", "svc", "capdsi"]
                    for j in range(1, 2):
                        for i in range(1, int(stack_create[4]) + 1):
                            lst_Data_Template.append('caph' + str(i) + str(j))
                            lst_Data_Template.append('smlh' + str(i) + str(j))
                        break

                lst_1 = ['Three selected, one purposefully, two merged into one group by SRS', 'Two selected, one purposefully, another by SRS', 'Two selected by SRSWOR/SYSTEMATIC']
                
                ###* CASE2
                for i in lst_1:
                    if stack_create[3] == i:
                        lst_Data_Template = ["fsu", "svc", "capdsi"]

                        for k in range(1, int(stack_create[4]) + 1):
                            for j in range(1, 3):
                                lst_Data_Template.append('caph' + str(k) + str(j))
                                lst_Data_Template.append('smlh' + str(k) + str(j))

                if stack_create[3] == 'Only one selected by SRS':
                    lst_Data_Template = ["fsu", "svc", "capdsi"]
                    for j in range(1, 2):
                        for i in range(1, int(stack_create[4]) + 1):
                            lst_Data_Template.append('caph' + str(i) + str(j))
                            lst_Data_Template.append('smlh' + str(i) + str(j))


                if stack_create[3] == 'Two selected, one purposefully, another by PPS':
                    lst_Data_Template = ["fsu", "svc", "capdsi", "dsizs", "hg1zs", "hg2zs"]
                    for j in range(1, 3):
                        for i in range(1, int(stack_create[4]) + 1):
                            lst_Data_Template.append('caph' + str(i) + str(j))
                            lst_Data_Template.append('smlh' + str(i) + str(j))
                            

                if stack_create[3] == 'Only one selected by PPS':
                    lst_Data_Template = ["fsu", "svc", "capdsi", "dsizs", "hgzs"]
                    for j in range(1, 2):
                        for i in range(1, int(stack_create[4]) + 1):
                            lst_Data_Template.append('caph' + str(i) + str(j))
                            lst_Data_Template.append('smlh' + str(i) + str(j))

                inh, unih, csc = stack_create[5], stack_create[6], stack_create[7]

                ### Blank list to pop items from deque
                createList = []

                ###! Stack is getting empty here (I MEAN FULLY EMPTY AND IT CAN'T BE USED FURTHER)
                ###! *****************************************************************************
                for i in range(len(stack_create)):
                    createList.append(stack_create.pop())

                ### Reversing the current list filled from popping the stack value
                createList = createList[::-1]

                ### Selected options will be displayed
                display_createList_createFlag = ['Your Selected Options - \r\n', 'Tab-1 :: {}, {}, {}'.format(createList[0], createList[1], createList[2]), 'Tab-2 :: {}'.format(createList[3]), 'Tab-3 :: {}'.format(createList[4]),  'Tab-4 :: {} : {} : {}'.format(createList[5], createList[6], createList[7])]

                ### Adding selected items to the list view
                self.listView.addItems(display_createList_createFlag)


                ###? Opening the mult file again and saving the stack data into the mult file
                ###? ************************************************************************

                with open(fname, 'w+') as f:
                    f.write('Selected Options from Tool : ' + '\r\n')
                    f.write('============================' + '\r\n')
                    f.write('\r\n')
                    f.write('Select FSU Sampling Method' + ' - ' + createList[0] + ' - ' + createList[1] + ' - ' + createList[2] + '\r\n')
                    f.write('Select HG/SB or Sub-Division Formation' + ' - ' + createList[3] + '\r\n')
                    f.write('Select SSS Formation Information' + ' - ' + createList[4] + '\r\n')
                    f.write('Select RSE method' + ' - ' + '[' + createList[5] + ']' +' - ' + '[' + createList[6] + ']' + ' - ' + '[' + createList[7] + ']' + '\r\n')

                
                ###! Making the file read Only type
                os.chmod(fname, S_IREAD)

                return createList

        elif flag == "upload_flag":
            ### Message Box to ask for the creation of mult file as well as data and design templates
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(
                "Click 'Yes' to proceed further."
            )
            msgBox.setWindowTitle("Warning!")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            returnValue = msgBox.exec()

            ### To verify the return value (yes/no)
            if returnValue == QMessageBox.Yes:
                ## Disabling tab4 and enabling tab5
                self.Create.setTabEnabled(5, True)
                self.Create.setTabEnabled(4, False)

                self.Create.setCurrentIndex(5)

                ### *************************** REQD TEMPLATES ****************************************
                ###* ----------------------------------------------------------------------------------
                ### Design Template
                if stack_load[0][0] == ("SRSWR" or "SRSWOR" or "Systematic SRS"):
                    lst_Design_Template = ["strm_id", "fsu", "capzs"]
                else:
                    lst_Design_Template = ["strm_id", "fsu", "capzs", "smallzs"]

                ### If sub sample number selected by user is greater than 1
                if int(stack_load[0][2]) > 1:
                    lst_Design_Template.append("ss_no")
                else:
                    pass

                ###!-- TAB 3 --###
                ###! Data Template
                if stack_load[1][0] == "Entire FSU is surveyed":
                    lst_Data_Template = ["fsu", "svc"]
                    for j in range(1, 2):
                        for i in range(1, int(stack_load[2][0]) + 1):
                            lst_Data_Template.append('caph' + str(i) + str(j))
                            lst_Data_Template.append('smlh' + str(i) + str(j))
                        

                if stack_load[1][0] == "Only one selected by SRS":
                    lst_Data_Template = ["fsu", "svc", "capdsi"]
                    for j in range(1, 2):
                        for i in range(1, int(stack_load[2][0]) + 1):
                            lst_Data_Template.append('caph' + str(i) + str(j))
                            lst_Data_Template.append('smlh' + str(i) + str(j))
                        

                lst_1 = ['Three selected, one purposefully, two merged into one group by SRS', 'Two selected, one purposefully, another by SRS', 'Two selected by SRSWOR/SYSTEMATIC']
                
                for i in lst_1:
                    if stack_load[1][0] == i:
                        lst_Data_Template = ["fsu", "svc", "capdsi"]
                        for j in range(1, 3):
                            for i in range(1, int(stack_load[2][0]) + 1):
                                lst_Data_Template.append('caph' + str(i) + str(j))
                                lst_Data_Template.append('smlh' + str(i) + str(j))

                
                if stack_load[1][0] == 'Only one selected by SRS':
                    lst_Data_Template = ["fsu", "svc", "capdsi"]
                    for j in range(1, 2):
                        for i in range(1, int(stack_create[4]) + 1):
                            lst_Data_Template.append('caph' + str(i) + str(j))
                            lst_Data_Template.append('smlh' + str(i) + str(j))
        

                if stack_load[1][0] == 'Two selected, one purposefully, another by PPS':
                    lst_Data_Template = ["fsu", "svc", "capdsi", "dsizs", "hg1zs", "hg2zs"]
                    for j in range(1, 3):
                        for i in range(1, int(stack_load[2][0]) + 1):
                            lst_Data_Template.append('caph' + str(i) + str(j))
                            lst_Data_Template.append('smlh' + str(i) + str(j))
                        

                if stack_load[1][0] == 'Only one selected by PPS':
                    lst_Data_Template = ["fsu", "svc", "capdsi", "dsizs", "hgzs"]
                    for j in range(1, 2):
                        for i in range(1, int(stack_load[2][0]) + 1):
                            lst_Data_Template.append('caph' + str(i) + str(j))
                            lst_Data_Template.append('smlh' + str(i) + str(j))
                        

                ### Blank list to pop items from deque
                uploadList = []

                ###! Stack is getting empty here (I MEAN FULLY EMPTY AND IT CAN'T BE USED FURTHER)
                ###! *****************************************************************************
                for i in range(len(stack_load)):
                    uploadList.append(str(stack_load.pop()))

                ### Reversing the current list filled from popping the stack value
                uploadList = uploadList[::-1]

                ### ! Formattig the list in the upload flow
                ### ! *************************************
                import ast

                lst_before_formatting = [
                    ast.literal_eval(uploadList[i]) for i in range(4)
                ]

                createList = []

                for sub_list in lst_before_formatting:
                    for element in sub_list:
                        createList.append(element.strip("[]"))

                display_createList_uploadFlag = [
                    "Your Selected Options - \r\n",
                    "FSU Sampling Method    ::   {}, {}, {}".format(
                        createList[0], createList[1], createList[2]
                    ),
                    "HG/SB or Sub-Division Formation   ::   {}".format(createList[3]),
                    "SSS Formation   ::   {}".format(createList[4]),
                    "Survey Codes   ::   {} : {} : {}".format(
                        createList[5], createList[6], createList[7]
                    ),
                ]

                self.listView.addItems(display_createList_uploadFlag)

            pass
        else:
            pass

    ### *Handling previous Button(pushBUtton_16) of Tab 4
    ### *------------------------------------------------
    def onClickPreviousTab4(self):
        if flag == "create_flag":

            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(
                "Are you sure you want to go back? This will reset your current selection."
            )
            msgBox.setWindowTitle("Warning!")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            returnValue = msgBox.exec()

            ### To verify the return value (yes/no)
            if returnValue == QMessageBox.Yes:

                ### To verify if top of the stack is empty or Not
                if len(stack_create) > 7:
                    ## Disabling tab4 and enabling tab3
                    self.Create.setTabEnabled(3, True)
                    self.Create.setTabEnabled(4, False)

                    ## If stack ids filled with
                    if stack_create:
                        stack_create.pop()
                        stack_create.pop()
                        stack_create.pop()
                        print(stack_create)
                    else:
                        pass

                    ### Setting current index of tab - 0
                    self.Create.setCurrentIndex(3)

                elif len(stack_create) == 5:
                    ## Disabling tab4 and enabling tab3
                    self.Create.setTabEnabled(3, True)
                    self.Create.setTabEnabled(4, False)

                    ## If stack ids filled with
                    if stack_create:
                        stack_create.pop()
                        print(stack_create)
                    else:
                        pass

                    self.Create.setCurrentIndex(3)

            elif returnValue == QMessageBox.No:
                pass

        elif flag == "upload_flag":
            self.Create.setTabEnabled(3, True)
            self.Create.setTabEnabled(4, False)
            self.Create.setCurrentIndex(3)


    ### ******************** HANDLING FUNCTIONS OF TAB 5 **************************
    ### ***************************************************************************
    def onClickDownloadDesTemp(self):
        try:
            df_designTemplate = pd.DataFrame(columns=lst_Design_Template)

            settings = QtCore.QSettings()
            path = settings.value("Paths/csvfile")
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(None, path, 'Design_Template', filter='*.xls;;*.xlsx;;*.csv')

            if filename:
                finfo = QtCore.QFileInfo(filename)
                settings.setValue("Paths/csvfile", finfo.absoluteDir().absolutePath())

                ###! File selection of xls, xlsx or csv  
                if filename.endswith(".csv"):
                    df_designTemplate.to_csv(filename, index=False)

                if filename.endswith(".xls"):
                    df_designTemplate.to_excel(filename, index=False)

                if filename.endswith(".xlsx"):
                    df_designTemplate.to_excel(filename, index=False)

                msg_ = msgBox_UI()
                msg_.label_2.setText("File downloaded successfully")
                msg_.pushButton.clicked.connect(msg_.success)
                returnValue = msg_.exec_()

                if returnValue == 1:
                    pass

        except:
            pass


    ###! **************** Clicking the Download Data Template ********************
    ###! *************************************************************************
    def onClickDownloadDataTemp(self):
        try:
            df_dataTemplate = pd.DataFrame(columns=lst_Data_Template)

            settings = QtCore.QSettings()
            path = settings.value("Paths/csvfile")
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(None, path, 'Data_Template', filter='*.xls;;*.xlsx;;*.csv')

            if filename:
                finfo = QtCore.QFileInfo(filename)
                settings.setValue("Paths/csvfile", finfo.absoluteDir().absolutePath())

                ###! File selection of xls, xlsx or csv  
                if filename.endswith(".csv"):
                    df_dataTemplate.to_csv(filename, index=False)

                if filename.endswith(".xls"):
                    df_dataTemplate.to_excel(filename, index=False)

                if filename.endswith(".xlsx"):
                    df_dataTemplate.to_excel(filename, index=False)

                msg_ = msgBox_UI()
                msg_.label_2.setText("File downloaded successfully")
                msg_.pushButton.clicked.connect(msg_.success)
                returnValue = msg_.exec_()

            if returnValue == 1:
                pass
            
        except:
            pass

    ### **************** Clicking the previous of tab5 ********************
    ### *******************************************************************
    def onClickPreviousTab5(self):
        if flag == "create_flag":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(
                "Are you sure you want to go back? The templates have already been generated."
            )
            msgBox.setWindowTitle("Warning!")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            returnValue = msgBox.exec()

            ### To verify the return value (yes/no) and close the tool on clicking 'Yes'
            if returnValue == QMessageBox.Yes:
                ### Clrearing the ListWidget in onClickNextTab5
                self.listView.clear()

                ## Disabling tab5 and enabling tab0
                self.Create.setTabEnabled(0, True)
                self.Create.setTabEnabled(5, False)

                ## If stack ids filled with
                if stack_create:
                    stack_create.pop()
                    stack_create.pop()
                    stack_create.pop()
                    print(stack_create)
                else:
                    pass

                print(stack_create)

                self.Create.setCurrentIndex(0)

        elif flag == "upload_flag":
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText(
                "Are you sure you want to go back? The templates have already been generated."
            )
            msgBox.setWindowTitle("Warning!")
            msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            returnValue = msgBox.exec()

            ### To verify the return value (yes/no) and close the tool on clicking 'Yes'
            if returnValue == QMessageBox.Yes:
                ### Clrearing the ListWidget in onClickNextTab5
                self.listView.clear()

                ## Disabling tab5 and enabling tab0
                self.Create.setTabEnabled(0, True)
                self.Create.setTabEnabled(5, False)
                self.Create.setCurrentIndex(0)


    ### **************** Clicking the next of tab5 ********************
    ### ***************************************************************
    def onClickNextTab5(self):
        if flag == "create_flag":
            ## Disabling tab5 and enabling tab6
            self.Create.setTabEnabled(6, True)
            self.Create.setTabEnabled(5, False)
            self.Create.setCurrentIndex(6)

        elif flag == "upload_flag":
            ## Disabling tab5 and enabling tab6
            self.Create.setTabEnabled(6, True)
            self.Create.setTabEnabled(5, False)
            self.Create.setCurrentIndex(6)


    ###! *********************  HANDLING FUNCTIONS OF TAB 6  ***************************
    ###! *******************************************************************************
    ### On upload Design Template
    def onUploadDesignTemplate(self):
        global design_df

        try:
            ### setting the path 
            settings = QtCore.QSettings()
            path = settings.value("Paths/csvfile")

            ### opening the select file template
            design_temp = QtWidgets.QFileDialog.getOpenFileName(
                None, "Upload file", path, "Select csv or xlsx or xls file (*.csv *.xlsx *.xls)"
            )[0]

            if design_temp:
                finfo = QtCore.QFileInfo(design_temp)
                settings.setValue("Paths/csvfile", finfo.absoluteDir().absolutePath())

            ### Read excel, csv files 
            if design_temp:
                ###! File selection of xls, xlsx or csv  
                if design_temp.endswith(".csv"):
                    design_df = pd.read_csv(design_temp)

                if design_temp.endswith(".xls"):
                    design_df = pd.read_excel(design_temp, engine='xlrd')

                if design_temp.endswith(".xlsx"):
                    design_df = pd.read_excel(design_temp)

                if set(lst_Design_Template) == set(design_df.columns.to_list()):
                    self.SampleList1.setText(design_temp)
                    return design_df
                else:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setText("Your uploaded data is not matching with the design template. Please verify your uploaded data again.")
                    msgBox.setWindowTitle("Warning!")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    returnValue = msgBox.exec()

                    ### To verify the return value (yes/no) and close the tool on clicking 'Yes'
                    if returnValue == QMessageBox.Ok:
                        pass
            
            ### if nothing is selected to upload
            elif design_df.empty:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Dataframe is empty. Please upload again!")
                msgBox.setWindowTitle("Warning!")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()

                ### To verify the return value (yes/no) and close the tool on clicking 'Yes'
                if returnValue == QMessageBox.Ok:
                    pass

        except:
            pass

    ### On upload Data Template
    def onUploadDataTemplate(self):
        global data_df

        try:
            settings = QtCore.QSettings()
            path = settings.value("Paths/csvfile")
            data_temp = QtWidgets.QFileDialog.getOpenFileName(
                                None, "Open file", path, "Select csv or xlsx or xls file (*.csv *.xlsx *.xls)"
                            )[0]

            ### Setting path to samre directory_name
            if data_temp:
                finfo = QtCore.QFileInfo(data_temp)
                settings.setValue("Paths/csvfile", finfo.absoluteDir().absolutePath())

                ###! File selection of xls, xlsx or csv  
                if data_temp.endswith(".csv"):
                    data_df = pd.read_csv(data_temp)

                if data_temp.endswith(".xls"):
                    data_df = pd.read_excel(data_temp, engine='xlrd')

                if data_temp.endswith(".xlsx"):
                    data_df = pd.read_excel(data_temp)

                if set(lst_Data_Template) == set(data_df.columns.to_list()):
                    self.Estimation1.setText(data_temp)
                    return data_df
                else:
                    msgBox = QMessageBox()
                    msgBox.setIcon(QMessageBox.Warning)
                    msgBox.setText("Your uploaded data is not matching with the data template. Please verify your uploaded data again.")
                    msgBox.setWindowTitle("Warning!")
                    msgBox.setStandardButtons(QMessageBox.Ok)
                    returnValue = msgBox.exec()

                    ### To verify the return value (yes/no) and close the tool on clicking 'Yes'
                    if returnValue == QMessageBox.Ok:
                        pass

            elif data_df.empty:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Dataframe is empty. Please upload again!")
                msgBox.setWindowTitle("Warning!")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()

                ### To verify the return value (yes/no) and close the tool on clicking 'Yes'
                if returnValue == QMessageBox.Ok:
                    pass

        except:
            pass

    ###! **** To validate uploaded data and design template from the GUI *****
    ###! *********************************************************************
    def onValidateUploadedData(self):
        global success_flag, ui_validate_data

        try:
            if data_df.empty and design_df.empty:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Please upload the design and data files for validation.")
                msgBox.setWindowTitle("Warning!")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()

                ### To verify the return value (yes/no) and close the tool on clicking 'Yes'
                if returnValue == QMessageBox.Ok:
                    pass

            elif set(lst_Data_Template) == set(data_df.columns.to_list()) and set(lst_Design_Template) == set(design_df.columns.to_list()):
                import time

                try:
                    ## Calling validation module
                    ui_validate_data = Validation_Dialog()
                except:
                    pass

                Validation_Summary_List = []

                ###* ------------ 1st case ---------------
                ###* capzs can never be 0

                count_capzs = (design_df["capzs"] == 0).sum()

                if count_capzs > 0:
                    Validation_Summary_List.append(
                        "FSU Sampling Method :  Please check your data, capzs cannot have value 0"       ##! Can't proceed
                    )
                    ui_validate_data.listwidget.addItem(
                        "FSU Sampling Method :  Please check your data, capzs cannot have value 0"
                    )

                else:
                    Validation_Summary_List.append(
                        "FSU Sampling Method :  Validation check on capzs - successful"
                    )
                    ui_validate_data.listwidget.addItem("FSU Sampling Method :  Validation check on capzs - successful")

                ###* ---------------- 2nd case ----------------
                ###* Match the FSU's of the two datasets

                df_fsu = design_df[~(design_df["fsu"].isin(data_df["fsu"]))].reset_index(
                    drop=True
                )

                if df_fsu.empty:
                    Validation_Summary_List.append(
                        "HG/SB or Sub-Division Formation :  The fsu in the two datasets match and are good to go!\n"
                    )
                    ui_validate_data.listwidget.addItem(
                        "HG/SB or Sub-Division Formation :  The fsu in the two datasets match and are good to go!"
                    )
                    
                else:
                    Validation_Summary_List.append(
                        "HG/SB or Sub-Division Formation :  Please check the files uploaded, the fsu of the two datasets should match.\n"           ##! Can't proceed
                    )
                    ui_validate_data.listwidget.addItem(
                        "HG/SB or Sub-Division Formation :  Please check the files uploaded, the fsu of the two datasets should match."
                    )
                    

                ##* --------- 3rd case -----------
                ##* Check for caph and smlh
                no_sss_input = int(createList[4])

                if createList[3] == 'Entire FSU is surveyed':
                    val_type1(self, data_df, no_sss_input, Validation_Summary_List, ui_validate_data)
                    
                elif createList[3] == 'Three selected, one purposefully, two merged into one group by SRS':
                    val_type2(self, data_df, no_sss_input, Validation_Summary_List, ui_validate_data)

                elif createList[3] == 'Two selected, one purposefully, another by SRS':
                    val_type2(self, data_df, no_sss_input, Validation_Summary_List, ui_validate_data)

                elif createList[3] == 'Two selected by SRSWOR/SYSTEMATIC':
                    val_type2(self, data_df, no_sss_input, Validation_Summary_List, ui_validate_data)

                elif createList[3] == 'Two selected, one purposefully, another by PPS':
                    val_type2(self, data_df, no_sss_input, Validation_Summary_List, ui_validate_data)

                elif createList[3] == 'Only one selected by SRS':
                    val_type1(self, data_df, no_sss_input, Validation_Summary_List, ui_validate_data)

                elif createList[3] == 'Only one selected by PPS':
                    val_type1(self, data_df, no_sss_input, Validation_Summary_List, ui_validate_data)

                

                ##* ----- 4th case ------
                ##* Check the svc
                casualty_codes = createList[7]
                inhabited_codes = createList[5]
                uninhabited_codes = createList[6]

                ###! ----- Casualty -----
                ### Splitting values on the basis of ', '
                casualty_codes = casualty_codes.split(",")

                ### Filling the modified elements with svc == in list inhabited_codes
                casualty_codes = [("svc == " + i) for i in casualty_codes]

                ### Joining the list of casualty codes into a single string
                casualty_codes = " or ".join(casualty_codes)
                casualty_codes = "(" + casualty_codes + ") "

                ###! ---------- Inhabited ------------
                ### Splitting values on the basis of ', '
                inhabited_codes = inhabited_codes.split(",")

                ### Filling the modified elements with svc == in list inhabited_codes
                inhabited_codes = [("svc == " + i) for i in inhabited_codes]

                ### Joining the list of casualty codes into a single string
                inhabited_codes = " or ".join(inhabited_codes)

                inhabited_codes = "(" + inhabited_codes + ") "

                ###! ---------- Uninhabited ------------
                ### Splitting values on the basis of ', '
                uninhabited_codes = uninhabited_codes.split(",")

                ### Filling the modified elements with svc == in list inhabited_codes
                uninhabited_codes = [("svc == " + i) for i in uninhabited_codes]

                ### Joining the list of casualty codes into a single string
                uninhabited_codes = " or ".join(uninhabited_codes)

                uninhabited_codes = "(" + uninhabited_codes + ") "

                count_na = data_df["svc"].isnull().sum()

                lst1 = list(set(data_df["svc"].to_list()))
                lst2 = list(set(map(int, set((inh + "," + unih + "," + csc).split(",")))))
                lst_verify_data_df = [item for item in lst2 if item in lst1]

                if count_na > 0:
                    Validation_Summary_List.append(
                        "Survey Codes :  Please check your data, svc cannot have a null value\n"                             ##! Can't proceed
                    )
                    ui_validate_data.listwidget.addItem(
                        "Survey Codes :  Please check your data, svc cannot have a null value"
                    )

                elif len(lst_verify_data_df) == 0 :
                    Validation_Summary_List.append(
                        "Survey Codes :  Please check your data, svc should only have values declared as inhabited, uninhabited and casualty\n"  ##! Can't proceed
                    )
                    ui_validate_data.listwidget.addItem(
                        "Survey Codes :  Please check your data, svc should only have values declared as inhabited, uninhabited and casualty"
                    )

                else:
                    Validation_Summary_List.append(
                        "Survey Codes :  Validation check on svc - successful\n"
                    )
                    ui_validate_data.listwidget.addItem("Survey Codes :  Validation check on svc - successful")

                    ###! Success flag to handle the cycle between create and upload flow
                    success_flag = "***dataValidated***"

                try:
                    ## Executing UI
                    ui_validate_data.exec_()
                except:
                    pass

            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Please upload the design and data files for validation.")
                msgBox.setWindowTitle("Warning!")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()

                ### To verify the return value (yes/no) and close the tool on clicking 'Yes'
                if returnValue == QMessageBox.Ok:
                    pass

        except:
            pass

    ###! ************** To handle next button of Tab 6 ********************
    ###! ******************************************************************
    def onClickNextTab6(self):
        try:
            if success_flag:
                ## Disabling tab5 and enabling tab6
                self.Create.setTabEnabled(7, True)
                self.Create.setTabEnabled(6, False)
                self.Create.setCurrentIndex(7)
            else:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Warning)
                msgBox.setText("Please verify the uploaded data before proceeding further.")
                msgBox.setWindowTitle("Warning!")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()

                ### To verify the return value (yes/no) and close the tool on clicking 'Yes'
                if returnValue == QMessageBox.Ok:
                    pass

        except:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Please verify the uploaded data before proceeding further.")
            msgBox.setWindowTitle("Warning!")
            msgBox.setStandardButtons(QMessageBox.Ok)
            returnValue = msgBox.exec()

            ### To verify the return value (yes/no) and close the tool on clicking 'Yes'
            if returnValue == QMessageBox.Ok:
                pass

    ###! ************** To handle previous button of Tab 6 ********************
    ###! **********************************************************************
    def onClickPreviousTab6(self):
        ## Disabling tab6 and enabling tab5
        self.Create.setTabEnabled(5, True)
        self.Create.setTabEnabled(6, False)
        self.Create.setCurrentIndex(5)


    ###! ****************** Handling Click Multiplier Button functionality ************************
    ###! ******************************************************************************************
    def onClickCalcMultilpier(self):
        global df_

        df_ = calculateMultiplier(self, data_df, design_df, createList)

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(
            "The Multiplier has been calculated and is ready to be exported."
        )
        msgBox.setWindowTitle("Success")
        msgBox.setStyleSheet(
            "QMessageBox { width:800px; height:800px; } QPushButton{ width:140px; font-size: 20px; }"
        )
        msgBox.setStyleSheet("background-color: #A5D6A7;")
        msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec()

        ### To verify the return value (yes/no) and close the tool on clicking 'Yes'
        if returnValue == QMessageBox.Ok:
            self.pushButton_11.setDisabled(False)
        else:
            pass


    ###! ****************** Handling on Click Previous Tab 7 functionality ************************
    ###! ******************************************************************************************
    def onClickPreviousTab7(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(
            "Are you sure you want to go back?"
        )
        msgBox.setWindowTitle("Warning")
        msgBox.setStyleSheet(
            "QMessageBox { width:800px; height:800px; } QPushButton{ width:140px; font-size: 20px; }"
        )
        msgBox.setStyleSheet("background-color: #F5F5DC;")
        msgBox.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        returnValue = msgBox.exec()

        ### To verify the return value (yes/no) and close the tool on clicking 'Yes'
        if returnValue == QMessageBox.Yes:
            ## Disabling tab7 and enabling tab6
            self.Create.setTabEnabled(6, True)
            self.Create.setTabEnabled(7, False)
            self.Create.setCurrentIndex(6)
            self.SampleList1.setText(" ")
            self.Estimation1.setText(" ")
        elif returnValue == QMessageBox.No:
            pass
        else:
            pass

    ###! ****************** Handling on Click Export functionality ************************
    ###! **********************************************************************************
    def onClickExport(self):
        try:
            settings = QtCore.QSettings()
            path = settings.value("Paths/csvfile")
            
            ### Opening file dialog to export multiplier file
            filename_design_template, _  = QtWidgets.QFileDialog.getSaveFileName(None, path, 'Multiplier', filter='*.xls;;*.xlsx;;*.csv')

            if filename_design_template:
                finfo = QtCore.QFileInfo(filename_design_template)
                settings.setValue("Paths/csvfile", finfo.absoluteDir().absolutePath())

                ###! File selection of xls, xlsx or csv  
                if filename_design_template.endswith(".csv"):
                    df_.to_csv(filename_design_template)

                if filename_design_template.endswith(".xls"):
                    df_.to_excel(filename_design_template)

                if filename_design_template.endswith(".xlsx"):
                    df_.to_excel(filename_design_template)

                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Multiplier file successfully exported.")
                msgBox.setWindowTitle("Success")
                msgBox.setStyleSheet(
                    "QMessageBox { width:800px; height:800px; } QPushButton{ width:140px; font-size: 20px; }"
                )
                msgBox.setStyleSheet("background-color: #A5D6A7;")
                msgBox.setStandardButtons(QMessageBox.Ok)
                returnValue = msgBox.exec()

                ### To verify the return value (yes/no) and close the tool on clicking 'Yes'
                if returnValue == QMessageBox.Ok:
                    pass

        except:
            pass


    ###! ***************** Handling user namual button *************************
    ###! ***********************************************************************
    def User_Manual(self):
        os.system('start User_Manual_MOSPI_TOOL.pdf')
        

    ###! ***************** HANDLING EXIT BUTTON (Close the tool!) *************************
    ###! **********************************************************************************
    def onClickExit(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Are you sure you want to exit?")
        msgBox.setWindowTitle("Warning")
        msgBox.setStyleSheet(
            "QMessageBox { width:800px; height:800px; } QPushButton{ width:140px; font-size: 20px; }"
        )
        msgBox.setStyleSheet("background-color: #A5D6A7;")
        msgBox.setStandardButtons(QMessageBox.Yes| QMessageBox.No)
        returnValue = msgBox.exec()

        ### To verify the return value (yes/no) and close the tool on clicking 'Yes'
        if returnValue == QMessageBox.Yes:
            sys.exit(app.exec_())
        elif returnValue == QMessageBox.No:
            pass

###! ***************** Main Function *************************
###! *********************************************************
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_main_window = Ui_MainWindow()
    ui_main_window.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
