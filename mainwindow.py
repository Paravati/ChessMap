# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(715, 774)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 891, 731))
        self.tabWidget.setObjectName("tabWidget")
        self.Nauka = QtWidgets.QWidget()
        self.Nauka.setObjectName("Nauka")
        self.lcdNumber = QtWidgets.QLCDNumber(self.Nauka)
        self.lcdNumber.setGeometry(QtCore.QRect(60, 40, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.Nauka)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 90, 621, 604))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_44 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_44.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_44.setText("")
        self.pushButton_44.setObjectName("pushButton_44")
        self.gridLayout_2.addWidget(self.pushButton_44, 2, 5, 1, 1)
        self.pushButton_47 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_47.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_47.setText("")
        self.pushButton_47.setObjectName("pushButton_47")
        self.gridLayout_2.addWidget(self.pushButton_47, 1, 3, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_22.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_2.addWidget(self.pushButton_22, 6, 6, 1, 1)
        self.pushButton_38 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_38.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_38.setText("")
        self.pushButton_38.setObjectName("pushButton_38")
        self.gridLayout_2.addWidget(self.pushButton_38, 7, 4, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_30.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_30.setText("")
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_2.addWidget(self.pushButton_30, 6, 5, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_12.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_12.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 3, 1, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_23.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_23.setText("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_2.addWidget(self.pushButton_23, 7, 6, 1, 1)
        self.pushButton_19 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_19.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_19.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_19.setText("")
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_2.addWidget(self.pushButton_19, 3, 6, 1, 1)
        self.pushButton_52 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_52.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_52.setText("")
        self.pushButton_52.setObjectName("pushButton_52")
        self.gridLayout_2.addWidget(self.pushButton_52, 3, 2, 1, 1)
        self.pushButton_28 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_28.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_28.setText("")
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout_2.addWidget(self.pushButton_28, 7, 7, 1, 1)
        self.pushButton_36 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_36.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_36.setText("")
        self.pushButton_36.setObjectName("pushButton_36")
        self.gridLayout_2.addWidget(self.pushButton_36, 5, 4, 1, 1)
        self.pushButton_54 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_54.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_54.setText("")
        self.pushButton_54.setObjectName("pushButton_54")
        self.gridLayout_2.addWidget(self.pushButton_54, 4, 1, 1, 1)
        self.pushButton_39 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_39.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_39.setText("")
        self.pushButton_39.setObjectName("pushButton_39")
        self.gridLayout_2.addWidget(self.pushButton_39, 7, 3, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_14.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_2.addWidget(self.pushButton_14, 0, 1, 1, 1)
        self.pushButton_50 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_50.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_50.setText("")
        self.pushButton_50.setObjectName("pushButton_50")
        self.gridLayout_2.addWidget(self.pushButton_50, 1, 6, 1, 1)
        self.pushButton_40 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_40.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_40.setText("")
        self.pushButton_40.setObjectName("pushButton_40")
        self.gridLayout_2.addWidget(self.pushButton_40, 6, 3, 1, 1)
        self.pushButton_34 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_34.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_34.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_34.setText("")
        self.pushButton_34.setObjectName("pushButton_34")
        self.gridLayout_2.addWidget(self.pushButton_34, 3, 4, 1, 1)
        self.pushButton_53 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_53.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_53.setText("")
        self.pushButton_53.setObjectName("pushButton_53")
        self.gridLayout_2.addWidget(self.pushButton_53, 4, 2, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_17.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_17.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_17.setText("")
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_2.addWidget(self.pushButton_17, 2, 3, 1, 1)
        self.pushButton_60 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_60.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_60.setText("")
        self.pushButton_60.setObjectName("pushButton_60")
        self.gridLayout_2.addWidget(self.pushButton_60, 6, 1, 1, 1)
        self.pushButton_45 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_45.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_45.setText("")
        self.pushButton_45.setObjectName("pushButton_45")
        self.gridLayout_2.addWidget(self.pushButton_45, 2, 6, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_20.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_20.setText("")
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_2.addWidget(self.pushButton_20, 4, 6, 1, 1)
        self.pushButton_58 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_58.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_58.setText("")
        self.pushButton_58.setObjectName("pushButton_58")
        self.gridLayout_2.addWidget(self.pushButton_58, 6, 2, 1, 1)
        self.pushButton_33 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_33.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_33.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_33.setText("")
        self.pushButton_33.setObjectName("pushButton_33")
        self.gridLayout_2.addWidget(self.pushButton_33, 3, 5, 1, 1)
        self.pushButton_43 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_43.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_43.setText("")
        self.pushButton_43.setObjectName("pushButton_43")
        self.gridLayout_2.addWidget(self.pushButton_43, 3, 3, 1, 1)
        self.pushButton_41 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_41.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_41.setText("")
        self.pushButton_41.setObjectName("pushButton_41")
        self.gridLayout_2.addWidget(self.pushButton_41, 5, 3, 1, 1)
        self.pushButton_42 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_42.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_42.setText("")
        self.pushButton_42.setObjectName("pushButton_42")
        self.gridLayout_2.addWidget(self.pushButton_42, 4, 3, 1, 1)
        self.pushButton_57 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_57.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_57.setText("")
        self.pushButton_57.setObjectName("pushButton_57")
        self.gridLayout_2.addWidget(self.pushButton_57, 5, 1, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_16.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_16.setText("")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_2.addWidget(self.pushButton_16, 0, 0, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_24.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_24.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_24.setText("")
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_2.addWidget(self.pushButton_24, 3, 7, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_29.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_29.setText("")
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout_2.addWidget(self.pushButton_29, 7, 5, 1, 1)
        self.pushButton_55 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_55.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_55.setText("")
        self.pushButton_55.setObjectName("pushButton_55")
        self.gridLayout_2.addWidget(self.pushButton_55, 4, 0, 1, 1)
        self.pushButton_65 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_65.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_65.setText("")
        self.pushButton_65.setObjectName("pushButton_65")
        self.gridLayout_2.addWidget(self.pushButton_65, 0, 2, 1, 1)
        self.pushButton_37 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_37.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_37.setText("")
        self.pushButton_37.setObjectName("pushButton_37")
        self.gridLayout_2.addWidget(self.pushButton_37, 6, 4, 1, 1)
        self.pushButton_35 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_35.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_35.setText("")
        self.pushButton_35.setObjectName("pushButton_35")
        self.gridLayout_2.addWidget(self.pushButton_35, 4, 4, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_15.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_15.setText("")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_2.addWidget(self.pushButton_15, 1, 2, 1, 1)
        self.pushButton_51 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_51.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_51.setText("")
        self.pushButton_51.setObjectName("pushButton_51")
        self.gridLayout_2.addWidget(self.pushButton_51, 1, 7, 1, 1)
        self.pushButton_59 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_59.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_59.setText("")
        self.pushButton_59.setObjectName("pushButton_59")
        self.gridLayout_2.addWidget(self.pushButton_59, 5, 2, 1, 1)
        self.pushButton_61 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_61.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_61.setText("")
        self.pushButton_61.setObjectName("pushButton_61")
        self.gridLayout_2.addWidget(self.pushButton_61, 7, 2, 1, 1)
        self.pushButton_46 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_46.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_46.setText("")
        self.pushButton_46.setObjectName("pushButton_46")
        self.gridLayout_2.addWidget(self.pushButton_46, 2, 7, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_21.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_21.setText("")
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_2.addWidget(self.pushButton_21, 5, 6, 1, 1)
        self.pushButton_64 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_64.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_64.setText("")
        self.pushButton_64.setObjectName("pushButton_64")
        self.gridLayout_2.addWidget(self.pushButton_64, 6, 0, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_25.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_25.setText("")
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_2.addWidget(self.pushButton_25, 4, 7, 1, 1)
        self.pushButton_62 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_62.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_62.setText("")
        self.pushButton_62.setObjectName("pushButton_62")
        self.gridLayout_2.addWidget(self.pushButton_62, 7, 1, 1, 1)
        self.pushButton_48 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_48.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_48.setText("")
        self.pushButton_48.setObjectName("pushButton_48")
        self.gridLayout_2.addWidget(self.pushButton_48, 1, 4, 1, 1)
        self.pushButton_66 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_66.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_66.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_66.setText("")
        self.pushButton_66.setObjectName("pushButton_66")
        self.gridLayout_2.addWidget(self.pushButton_66, 2, 2, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_27.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_27.setText("")
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_2.addWidget(self.pushButton_27, 6, 7, 1, 1)
        self.pushButton_32 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_32.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_32.setText("")
        self.pushButton_32.setObjectName("pushButton_32")
        self.gridLayout_2.addWidget(self.pushButton_32, 4, 5, 1, 1)
        self.pushButton_49 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_49.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_49.setText("")
        self.pushButton_49.setObjectName("pushButton_49")
        self.gridLayout_2.addWidget(self.pushButton_49, 1, 5, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_18.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_18.setText("")
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_2.addWidget(self.pushButton_18, 2, 4, 1, 1)
        self.pushButton_56 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_56.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_56.setText("")
        self.pushButton_56.setObjectName("pushButton_56")
        self.gridLayout_2.addWidget(self.pushButton_56, 5, 0, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_31.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_31.setText("")
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout_2.addWidget(self.pushButton_31, 5, 5, 1, 1)
        self.pushButton_63 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_63.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_63.setText("")
        self.pushButton_63.setObjectName("pushButton_63")
        self.gridLayout_2.addWidget(self.pushButton_63, 7, 0, 1, 1)
        self.pushButton_26 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_26.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_26.setText("")
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_2.addWidget(self.pushButton_26, 5, 7, 1, 1)
        self.pushButton_67 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_67.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_67.setText("")
        self.pushButton_67.setObjectName("pushButton_67")
        self.gridLayout_2.addWidget(self.pushButton_67, 0, 3, 1, 1)
        self.pushButton_68 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_68.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_68.setText("")
        self.pushButton_68.setObjectName("pushButton_68")
        self.gridLayout_2.addWidget(self.pushButton_68, 1, 1, 1, 1)
        self.pushButton_69 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_69.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_69.setText("")
        self.pushButton_69.setObjectName("pushButton_69")
        self.gridLayout_2.addWidget(self.pushButton_69, 2, 1, 1, 1)
        self.pushButton_70 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_70.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_70.setText("")
        self.pushButton_70.setObjectName("pushButton_70")
        self.gridLayout_2.addWidget(self.pushButton_70, 1, 0, 1, 1)
        self.pushButton_71 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_71.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_71.setText("")
        self.pushButton_71.setObjectName("pushButton_71")
        self.gridLayout_2.addWidget(self.pushButton_71, 2, 0, 1, 1)
        self.pushButton_72 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_72.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_72.setMaximumSize(QtCore.QSize(70, 70))
        self.pushButton_72.setText("")
        self.pushButton_72.setObjectName("pushButton_72")
        self.gridLayout_2.addWidget(self.pushButton_72, 3, 0, 1, 1)
        self.pushButton_73 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_73.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_73.setText("")
        self.pushButton_73.setObjectName("pushButton_73")
        self.gridLayout_2.addWidget(self.pushButton_73, 0, 4, 1, 1)
        self.pushButton_74 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_74.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_74.setText("")
        self.pushButton_74.setObjectName("pushButton_74")
        self.gridLayout_2.addWidget(self.pushButton_74, 0, 5, 1, 1)
        self.pushButton_75 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_75.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_75.setText("")
        self.pushButton_75.setObjectName("pushButton_75")
        self.gridLayout_2.addWidget(self.pushButton_75, 0, 6, 1, 1)
        self.pushButton_76 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_76.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton_76.setText("")
        self.pushButton_76.setObjectName("pushButton_76")
        self.gridLayout_2.addWidget(self.pushButton_76, 0, 7, 1, 1)
        self.label = QtWidgets.QLabel(self.Nauka)
        self.label.setGeometry(QtCore.QRect(340, 40, 55, 16))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.Nauka, "")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(390, 20, 71, 81))
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 220, 194, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.widget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(90, 70, 141, 71))
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(160, 410, 241, 111))
        self.label_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.widget, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 715, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nazwa"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Nauka), _translate("MainWindow", "Nauka"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "Praktyka"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
