# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Labra.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDial, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionTallenna = QAction(MainWindow)
        self.actionTallenna.setObjectName(u"actionTallenna")
        self.actionLopeta = QAction(MainWindow)
        self.actionLopeta.setObjectName(u"actionLopeta")
        self.actionTulosta_viivakoodi = QAction(MainWindow)
        self.actionTulosta_viivakoodi.setObjectName(u"actionTulosta_viivakoodi")
        self.actionNimilappu = QAction(MainWindow)
        self.actionNimilappu.setObjectName(u"actionNimilappu")
        self.actionTulosta_2 = QAction(MainWindow)
        self.actionTulosta_2.setObjectName(u"actionTulosta_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ssnLineEdit = QLineEdit(self.centralwidget)
        self.ssnLineEdit.setObjectName(u"ssnLineEdit")
        self.ssnLineEdit.setGeometry(QRect(20, 60, 231, 31))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(20)
        self.ssnLineEdit.setFont(font)
        self.ssnLabel = QLabel(self.centralwidget)
        self.ssnLabel.setObjectName(u"ssnLabel")
        self.ssnLabel.setGeometry(QRect(20, 30, 71, 16))
        self.firstNameLineEdit = QLineEdit(self.centralwidget)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")
        self.firstNameLineEdit.setGeometry(QRect(20, 140, 231, 31))
        self.firstNameLineEdit.setFont(font)
        self.lastNameLineEdit = QLineEdit(self.centralwidget)
        self.lastNameLineEdit.setObjectName(u"lastNameLineEdit")
        self.lastNameLineEdit.setGeometry(QRect(270, 140, 231, 31))
        self.lastNameLineEdit.setFont(font)
        self.firstNameLabel = QLabel(self.centralwidget)
        self.firstNameLabel.setObjectName(u"firstNameLabel")
        self.firstNameLabel.setGeometry(QRect(20, 110, 71, 16))
        self.LastNameLabel = QLabel(self.centralwidget)
        self.LastNameLabel.setObjectName(u"LastNameLabel")
        self.LastNameLabel.setGeometry(QRect(280, 110, 71, 16))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 190, 131, 31))
        font1 = QFont()
        font1.setFamilies([u"Libre Barcode 128 Text"])
        font1.setPointSize(25)
        self.label.setFont(font1)
        self.printPushButton = QPushButton(self.centralwidget)
        self.printPushButton.setObjectName(u"printPushButton")
        self.printPushButton.setGeometry(QRect(270, 240, 231, 31))
        font2 = QFont()
        font2.setPointSize(18)
        self.printPushButton.setFont(font2)
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(420, 190, 81, 41))
        font3 = QFont()
        font3.setPointSize(24)
        self.spinBox.setFont(font3)
        self.spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.dial = QDial(self.centralwidget)
        self.dial.setObjectName(u"dial")
        self.dial.setGeometry(QRect(130, 370, 50, 64))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 420, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuTiedosto = QMenu(self.menubar)
        self.menuTiedosto.setObjectName(u"menuTiedosto")
        self.menuTulosta = QMenu(self.menuTiedosto)
        self.menuTulosta.setObjectName(u"menuTulosta")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.ssnLineEdit, self.firstNameLineEdit)
        QWidget.setTabOrder(self.firstNameLineEdit, self.lastNameLineEdit)
        QWidget.setTabOrder(self.lastNameLineEdit, self.spinBox)
        QWidget.setTabOrder(self.spinBox, self.printPushButton)

        self.menubar.addAction(self.menuTiedosto.menuAction())
        self.menuTiedosto.addAction(self.actionTallenna)
        self.menuTiedosto.addAction(self.menuTulosta.menuAction())
        self.menuTiedosto.addSeparator()
        self.menuTiedosto.addAction(self.actionLopeta)
        self.menuTulosta.addAction(self.actionTulosta_viivakoodi)
        self.menuTulosta.addAction(self.actionNimilappu)

        self.retranslateUi(MainWindow)
        self.ssnLineEdit.textChanged.connect(self.label.setText)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionTallenna.setText(QCoreApplication.translate("MainWindow", u"Tallenna...", None))
#if QT_CONFIG(shortcut)
        self.actionTallenna.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionLopeta.setText(QCoreApplication.translate("MainWindow", u"Lopeta", None))
        self.actionTulosta_viivakoodi.setText(QCoreApplication.translate("MainWindow", u"Tulosta viivakoodi", None))
#if QT_CONFIG(shortcut)
        self.actionTulosta_viivakoodi.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionNimilappu.setText(QCoreApplication.translate("MainWindow", u"Nimilappu", None))
        self.actionTulosta_2.setText(QCoreApplication.translate("MainWindow", u"Tulosta", None))
#if QT_CONFIG(tooltip)
        self.actionTulosta_2.setToolTip(QCoreApplication.translate("MainWindow", u"Tulosta viivakoodi", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionTulosta_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+P", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.ssnLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Suomalainen henkil\u00f6tunnus", None))
#endif // QT_CONFIG(tooltip)
        self.ssnLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ppkkvv-999x", None))
        self.ssnLabel.setText(QCoreApplication.translate("MainWindow", u"Henkil\u00f6tunnus", None))
        self.firstNameLabel.setText(QCoreApplication.translate("MainWindow", u"Etunimi", None))
        self.LastNameLabel.setText(QCoreApplication.translate("MainWindow", u"Sukunimi", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ppkkvv-nnnv", None))
        self.printPushButton.setText(QCoreApplication.translate("MainWindow", u"Tulosta", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menuTiedosto.setTitle(QCoreApplication.translate("MainWindow", u"Tiedosto", None))
        self.menuTulosta.setTitle(QCoreApplication.translate("MainWindow", u"Tulosta", None))
    # retranslateUi

