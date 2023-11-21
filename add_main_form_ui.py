from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Ui_AddWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
          
        MainWindow.resize(408, 336)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.sort = QLineEdit(self.centralwidget)
        self.sort.setObjectName(u"sort")
        self.sort.setGeometry(QRect(20, 19, 371, 31))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.sort.setFont(font)
        self.roasting = QLineEdit(self.centralwidget)
        self.roasting.setObjectName(u"roasting")
        self.roasting.setGeometry(QRect(20, 60, 141, 31))
        self.roasting.setFont(font)
        self.coffee = QLineEdit(self.centralwidget)
        self.coffee.setObjectName(u"coffee")
        self.coffee.setGeometry(QRect(180, 60, 211, 31))
        self.coffee.setFont(font)
        self.taste = QLineEdit(self.centralwidget)
        self.taste.setObjectName(u"taste")
        self.taste.setGeometry(QRect(20, 110, 371, 31))
        self.taste.setFont(font)
        self.price = QLineEdit(self.centralwidget)
        self.price.setObjectName(u"price")
        self.price.setGeometry(QRect(20, 160, 371, 31))
        self.price.setFont(font)
        self.capacity = QLineEdit(self.centralwidget)
        self.capacity.setObjectName(u"capacity")
        self.capacity.setGeometry(QRect(20, 210, 371, 31))
        self.capacity.setFont(font)
        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(230, 260, 161, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u043a\u043e\u0444\u0435", None))
        self.sort.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0441\u043e\u0440\u0442\u0430 \u043d\u043e\u0432\u043e\u0433\u043e \u043a\u043e\u0444\u0435.", None))
        self.roasting.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0435\u043f\u0435\u043d\u044c \u043e\u0431\u0436\u0430\u0440\u043a\u0438.", None))
        self.coffee.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043a\u043e\u0444\u0435.", None))
        self.taste.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0432\u043a\u0443\u0441\u0430 \u043d\u043e\u0432\u043e\u0433\u043e \u043a\u043e\u0444\u0435.", None))
        self.price.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0446\u0435\u043d\u0443 \u043d\u043e\u0432\u043e\u0433\u043e \u043a\u043e\u0444\u0435 \u0437\u0430 1 \u043a\u0438\u043b\u043e\u0433\u0440\u0430\u043c\u043c.", None))
        self.capacity.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043e\u0431\u044a\u0435\u043c \u0443\u043f\u0430\u043a\u043e\u0432\u043a\u0438 \u043d\u043e\u0432\u043e\u0433\u043e \u043a\u043e\u0444\u0435.", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u043e\u0435 \u043a\u043e\u0444\u0435", None))
