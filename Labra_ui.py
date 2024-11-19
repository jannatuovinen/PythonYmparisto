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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(589, 351)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ssnLineEdit = QLineEdit(self.centralwidget)
        self.ssnLineEdit.setObjectName(u"ssnLineEdit")
        self.ssnLineEdit.setGeometry(QRect(20, 50, 231, 31))
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(20)
        self.ssnLineEdit.setFont(font)
        self.ssnLineEdit.setStyleSheet(u"")
        self.ssnLineEdit.setClearButtonEnabled(True)
        self.ssnLabel = QLabel(self.centralwidget)
        self.ssnLabel.setObjectName(u"ssnLabel")
        self.ssnLabel.setGeometry(QRect(20, 30, 71, 16))
        self.firstNameLineEdit = QLineEdit(self.centralwidget)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")
        self.firstNameLineEdit.setGeometry(QRect(20, 130, 231, 31))
        self.firstNameLineEdit.setFont(font)
        self.lastNameLineEdit = QLineEdit(self.centralwidget)
        self.lastNameLineEdit.setObjectName(u"lastNameLineEdit")
        self.lastNameLineEdit.setGeometry(QRect(280, 130, 231, 31))
        self.lastNameLineEdit.setFont(font)
        self.firstNameLabel = QLabel(self.centralwidget)
        self.firstNameLabel.setObjectName(u"firstNameLabel")
        self.firstNameLabel.setGeometry(QRect(20, 110, 71, 16))
        self.LastNameLabel = QLabel(self.centralwidget)
        self.LastNameLabel.setObjectName(u"LastNameLabel")
        self.LastNameLabel.setGeometry(QRect(280, 110, 71, 16))
        self.barcodeLabel = QLabel(self.centralwidget)
        self.barcodeLabel.setObjectName(u"barcodeLabel")
        self.barcodeLabel.setGeometry(QRect(30, 200, 171, 61))
        font1 = QFont()
        font1.setFamilies([u"Libre Barcode 128 Text"])
        font1.setPointSize(30)
        self.barcodeLabel.setFont(font1)
        self.printPushButton = QPushButton(self.centralwidget)
        self.printPushButton.setObjectName(u"printPushButton")
        self.printPushButton.setGeometry(QRect(390, 210, 131, 41))
        font2 = QFont()
        font2.setPointSize(18)
        self.printPushButton.setFont(font2)
        self.printPushButton.setStyleSheet(u"")
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(220, 210, 131, 41))
        font3 = QFont()
        font3.setPointSize(24)
        self.spinBox.setFont(font3)
        self.spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.amountLabel = QLabel(self.centralwidget)
        self.amountLabel.setObjectName(u"amountLabel")
        self.amountLabel.setGeometry(QRect(220, 190, 81, 16))
        self.esampleStickerLabel = QLabel(self.centralwidget)
        self.esampleStickerLabel.setObjectName(u"esampleStickerLabel")
        self.esampleStickerLabel.setGeometry(QRect(30, 190, 61, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 589, 21))
        MainWindow.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.ssnLineEdit, self.firstNameLineEdit)
        QWidget.setTabOrder(self.firstNameLineEdit, self.lastNameLineEdit)
        QWidget.setTabOrder(self.lastNameLineEdit, self.spinBox)
        QWidget.setTabOrder(self.spinBox, self.printPushButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.ssnLineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"Suomalainen henkil\u00f6tunnus", None))
#endif // QT_CONFIG(tooltip)
        self.ssnLineEdit.setText(QCoreApplication.translate("MainWindow", u"311259-123X", None))
        self.ssnLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ppkkvv-999x", None))
        self.ssnLabel.setText(QCoreApplication.translate("MainWindow", u"Henkil\u00f6tunnus", None))
        self.firstNameLabel.setText(QCoreApplication.translate("MainWindow", u"Etunimi", None))
        self.LastNameLabel.setText(QCoreApplication.translate("MainWindow", u"Sukunimi", None))
        self.barcodeLabel.setText(QCoreApplication.translate("MainWindow", u"ppkkvv-nnnv", None))
        self.printPushButton.setText(QCoreApplication.translate("MainWindow", u"Tulosta", None))
        self.amountLabel.setText(QCoreApplication.translate("MainWindow", u"Etikettien m\u00e4\u00e4r\u00e4", None))
        self.esampleStickerLabel.setText(QCoreApplication.translate("MainWindow", u"Mallietiketti", None))
    # retranslateUi

