# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1089, 659)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #f5f5f5;")
        self.topPanel = QFrame(self.centralwidget)
        self.topPanel.setObjectName(u"topPanel")
        self.topPanel.setGeometry(QRect(10, 10, 1069, 64))
        self.topPanel.setStyleSheet(u"background-color: white;\n"
"border: none;\n"
"border-radius: 14px;")
        self.topPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.topPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.topPanel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.titleLayout = QVBoxLayout()
        self.titleLayout.setSpacing(2)
        self.titleLayout.setObjectName(u"titleLayout")
        self.titleLabel = QLabel(self.topPanel)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setMinimumSize(QSize(175, 19))
        self.titleLabel.setStyleSheet(u"color: #118983;\n"
"font-size: 18px;\n"
"font-weight: bold;\n"
"font-family: \"Helvetica\"")
        self.titleLabel.setMidLineWidth(1)

        self.titleLayout.addWidget(self.titleLabel)

        self.subtitleLabel = QLabel(self.topPanel)
        self.subtitleLabel.setObjectName(u"subtitleLabel")
        self.subtitleLabel.setMinimumSize(QSize(175, 0))
        self.subtitleLabel.setStyleSheet(u"color: #333333;\n"
"font-size: 17px;\n"
"font-family: \"Helvetica\"\n"
"")

        self.titleLayout.addWidget(self.subtitleLabel)


        self.horizontalLayout.addLayout(self.titleLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.startButton = QPushButton(self.topPanel)
        self.startButton.setObjectName(u"startButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setStyleSheet(u"background-color: #118983;\n"
"color: white;\n"
"border: none;\n"
"border-radius: 10px;\n"
"padding: 6px 20px;\n"
"font-weight: bold;")

        self.horizontalLayout.addWidget(self.startButton)

        self.leftPanel = QFrame(self.centralwidget)
        self.leftPanel.setObjectName(u"leftPanel")
        self.leftPanel.setGeometry(QRect(12, 89, 283, 490))
        self.leftPanel.setStyleSheet(u"background-color: white;\n"
"border: none;\n"
"border-radius: 14px;")
        self.leftPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.toothLabel = QLabel(self.leftPanel)
        self.toothLabel.setObjectName(u"toothLabel")
        self.toothLabel.setGeometry(QRect(10, 10, 251, 21))
        self.toothLabel.setAutoFillBackground(False)
        self.toothLabel.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")
        self.toothIconLabel = QLabel(self.leftPanel)
        self.toothIconLabel.setObjectName(u"toothIconLabel")
        self.toothIconLabel.setGeometry(QRect(10, 50, 63, 63))
        self.toothIconLabel.setPixmap(QPixmap(u"../tooth_circle.svg"))
        self.toothIconLabel.setScaledContents(True)
        self.selectATooth = QLabel(self.leftPanel)
        self.selectATooth.setObjectName(u"selectATooth")
        self.selectATooth.setGeometry(QRect(82, 83, 181, 16))
        self.selectATooth.setStyleSheet(u"color: #768599;\n"
"font-family: \"Helvetica\";")
        self.noToothSelected = QLabel(self.leftPanel)
        self.noToothSelected.setObjectName(u"noToothSelected")
        self.noToothSelected.setGeometry(QRect(83, 62, 147, 21))
        self.noToothSelected.setStyleSheet(u"font-size: 17px;\n"
"font-weight: 450;\n"
"color: #333333;\n"
"")
        self.joints = QLabel(self.leftPanel)
        self.joints.setObjectName(u"joints")
        self.joints.setGeometry(QRect(10, 291, 58, 16))
        self.joints.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")
        self.toothTargetFrame = QFrame(self.leftPanel)
        self.toothTargetFrame.setObjectName(u"toothTargetFrame")
        self.toothTargetFrame.setGeometry(QRect(0, 151, 281, 91))
        self.toothTargetFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.toothTargetFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.toothTargetFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.toothTarget = QLabel(self.toothTargetFrame)
        self.toothTarget.setObjectName(u"toothTarget")
        self.toothTarget.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")

        self.verticalLayout.addWidget(self.toothTarget)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(20, -1, 10, -1)
        self.Y = QLabel(self.toothTargetFrame)
        self.Y.setObjectName(u"Y")
        self.Y.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")

        self.gridLayout_2.addWidget(self.Y, 0, 1, 1, 1)

        self.X = QLabel(self.toothTargetFrame)
        self.X.setObjectName(u"X")
        self.X.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")

        self.gridLayout_2.addWidget(self.X, 0, 0, 1, 1)

        self.Z = QLabel(self.toothTargetFrame)
        self.Z.setObjectName(u"Z")
        self.Z.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")

        self.gridLayout_2.addWidget(self.Z, 0, 2, 1, 1)

        self.label = QLabel(self.toothTargetFrame)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_13 = QLabel(self.toothTargetFrame)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 1, 1, 1, 1)

        self.label_14 = QLabel(self.toothTargetFrame)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_2.addWidget(self.label_14, 1, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.jointsFrame = QFrame(self.leftPanel)
        self.jointsFrame.setObjectName(u"jointsFrame")
        self.jointsFrame.setGeometry(QRect(0, 310, 281, 121))
        self.jointsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.jointsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.jointsFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_9 = QLabel(self.jointsFrame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")

        self.gridLayout.addWidget(self.label_9, 2, 2, 1, 1)

        self.label_7 = QLabel(self.jointsFrame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_6 = QLabel(self.jointsFrame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)

        self.label_5 = QLabel(self.jointsFrame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.label_3 = QLabel(self.jointsFrame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.jointsFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.J1 = QLabel(self.jointsFrame)
        self.J1.setObjectName(u"J1")
        self.J1.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")

        self.gridLayout.addWidget(self.J1, 0, 0, 1, 1)

        self.label_8 = QLabel(self.jointsFrame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")

        self.gridLayout.addWidget(self.label_8, 2, 1, 1, 1)

        self.label_2 = QLabel(self.jointsFrame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)

        self.label_10 = QLabel(self.jointsFrame)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)

        self.label_11 = QLabel(self.jointsFrame)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 3, 1, 1, 1)

        self.label_12 = QLabel(self.jointsFrame)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 3, 2, 1, 1)

        self.centerPanel = QFrame(self.centralwidget)
        self.centerPanel.setObjectName(u"centerPanel")
        self.centerPanel.setGeometry(QRect(310, 89, 458, 490))
        self.centerPanel.setStyleSheet(u"background-color: white;\n"
"border: none;\n"
"border-radius: 14px;")
        self.centerPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.centerPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.label_17 = QLabel(self.centerPanel)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(192, 10, 61, 16))
        self.label_17.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")
        self.label_18 = QLabel(self.centerPanel)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(182, 458, 81, 16))
        self.label_18.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")
        self.rightTopPanel = QFrame(self.centralwidget)
        self.rightTopPanel.setObjectName(u"rightTopPanel")
        self.rightTopPanel.setGeometry(QRect(783, 89, 285, 279))
        self.rightTopPanel.setStyleSheet(u"background-color: white;\n"
"border: none;\n"
"border-radius: 14px;")
        self.rightTopPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.rightTopPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.label_16 = QLabel(self.rightTopPanel)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 10, 111, 16))
        self.label_16.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")
        self.leftBottomPanel = QFrame(self.centralwidget)
        self.leftBottomPanel.setObjectName(u"leftBottomPanel")
        self.leftBottomPanel.setGeometry(QRect(783, 410, 285, 166))
        self.leftBottomPanel.setStyleSheet(u"background-color: white;\n"
"border: none;\n"
"border-radius: 14px;\n"
"font-size:17px;\n"
"")
        self.leftBottomPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftBottomPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.label_15 = QLabel(self.leftBottomPanel)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 10, 91, 16))
        self.label_15.setStyleSheet(u"color: #768599;\n"
"font-weight: 450;\n"
"font-family: \"Helvetica\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1089, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DentaVision Control Panel", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>DentaVision<br/></p></body></html>", None))
        self.subtitleLabel.setText(QCoreApplication.translate("MainWindow", u"Control Panel", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.toothLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">SELECTED TOOTH</span></p></body></html>", None))
        self.toothIconLabel.setText("")
        self.selectATooth.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Select a tooth from the chart</span></p></body></html>", None))
        self.noToothSelected.setText(QCoreApplication.translate("MainWindow", u"No tooth selected", None))
        self.joints.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">JOINTS</span></p></body></html>", None))
        self.toothTarget.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">TOOTH TARGET</span></p></body></html>", None))
        self.Y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.X.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.Z.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"J6", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"J4", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"J3", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"J2", None))
        self.J1.setText(QCoreApplication.translate("MainWindow", u"J1", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"J5", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>MAXILLA</p><p><br/></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>MANDIBULA</p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">HEAD POSITION</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-style:italic;\">STATUS</span></p></body></html>", None))
    # retranslateUi

