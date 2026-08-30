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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

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
        self.centerPanel = QFrame(self.centralwidget)
        self.centerPanel.setObjectName(u"centerPanel")
        self.centerPanel.setGeometry(QRect(310, 89, 458, 490))
        self.centerPanel.setStyleSheet(u"background-color: white;\n"
"border: none;\n"
"border-radius: 14px;")
        self.centerPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.centerPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.rightTopPanel = QFrame(self.centralwidget)
        self.rightTopPanel.setObjectName(u"rightTopPanel")
        self.rightTopPanel.setGeometry(QRect(783, 89, 285, 279))
        self.rightTopPanel.setStyleSheet(u"background-color: white;\n"
"border: none;\n"
"border-radius: 14px;")
        self.rightTopPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.rightTopPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.leftBottomPanel = QFrame(self.centralwidget)
        self.leftBottomPanel.setObjectName(u"leftBottomPanel")
        self.leftBottomPanel.setGeometry(QRect(783, 410, 285, 166))
        self.leftBottomPanel.setStyleSheet(u"background-color: white;\n"
"border: none;\n"
"border-radius: 14px;")
        self.leftBottomPanel.setFrameShape(QFrame.Shape.StyledPanel)
        self.leftBottomPanel.setFrameShadow(QFrame.Shadow.Raised)
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
        self.toothLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:17pt; font-style:italic;\">SELECTED TOOTH</span></p></body></html>", None))
    # retranslateUi

