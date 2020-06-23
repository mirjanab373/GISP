# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GISP_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GISPDialogBase(object):
    def setupUi(self, GISPDialogBase):
        GISPDialogBase.setObjectName("GISPDialogBase")
        GISPDialogBase.resize(390, 300)
        self.button_box = QtWidgets.QDialogButtonBox(GISPDialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.label = QtWidgets.QLabel(GISPDialogBase)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.label.setObjectName("label")
        self.output = QtWidgets.QLineEdit(GISPDialogBase)
        self.output.setGeometry(QtCore.QRect(130, 20, 191, 21))
        self.output.setObjectName("output")
        self.dugme = QtWidgets.QPushButton(GISPDialogBase)
        self.dugme.setGeometry(QtCore.QRect(330, 20, 31, 21))
        self.dugme.setObjectName("dugme")

        self.retranslateUi(GISPDialogBase)
        self.button_box.accepted.connect(GISPDialogBase.accept)
        self.button_box.rejected.connect(GISPDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(GISPDialogBase)

    def retranslateUi(self, GISPDialogBase):
        _translate = QtCore.QCoreApplication.translate
        GISPDialogBase.setWindowTitle(_translate("GISPDialogBase", "GISP"))
        self.label.setText(_translate("GISPDialogBase", "Select input raster"))
        self.dugme.setText(_translate("GISPDialogBase", "..."))
