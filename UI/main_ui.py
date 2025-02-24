from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_qwidget(object):
    def setupUi(self, qwidget):
        qwidget.setObjectName("qwidget")
        qwidget.resize(837, 460)
        self.label_3 = QtWidgets.QLabel(parent=qwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 0, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(parent=qwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 31, 821, 381))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.addButton = QtWidgets.QPushButton(parent=qwidget)
        self.addButton.setGeometry(QtCore.QRect(20, 420, 241, 23))
        self.addButton.setObjectName("addButton")

        self.retranslateUi(qwidget)
        QtCore.QMetaObject.connectSlotsByName(qwidget)

    def retranslateUi(self, qwidget):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("qwidget", "Каталог кофейного магазина"))
        self.addButton.setText(_translate("qwidget", "Добавить/редактировать"))
