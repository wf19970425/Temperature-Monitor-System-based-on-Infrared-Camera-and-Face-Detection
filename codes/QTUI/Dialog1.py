# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 491)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(70, 50, 511, 221))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 60, 191, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 241, 41))
        self.label_2.setObjectName("label_2")
        self.Conf_Text = QtWidgets.QLineEdit(self.frame)
        self.Conf_Text.setGeometry(QtCore.QRect(280, 40, 41, 21))
        self.Conf_Text.setObjectName("Conf_Text")
        self.IOU_Text = QtWidgets.QLineEdit(self.frame)
        self.IOU_Text.setGeometry(QtCore.QRect(280, 70, 41, 21))
        self.IOU_Text.setObjectName("IOU_Text")
        self.FacialPoseCorrection_RBT = QtWidgets.QRadioButton(self.frame)
        self.FacialPoseCorrection_RBT.setGeometry(QtCore.QRect(20, 130, 181, 16))
        self.FacialPoseCorrection_RBT.setObjectName("FacialPoseCorrection_RBT")
        self.DistanceCorrection_RBT = QtWidgets.QRadioButton(self.frame)
        self.DistanceCorrection_RBT.setGeometry(QtCore.QRect(20, 100, 161, 16))
        self.DistanceCorrection_RBT.setObjectName("DistanceCorrection_RBT")
        self.AlarmTem_Text = QtWidgets.QLineEdit(self.frame)
        self.AlarmTem_Text.setGeometry(QtCore.QRect(280, 10, 41, 21))
        self.AlarmTem_Text.setObjectName("AlarmTem_Text")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 241, 41))
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(330, 0, 71, 41))
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(20, 150, 241, 41))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(20, 180, 241, 41))
        self.label_13.setObjectName("label_13")
        self.DCID_Text = QtWidgets.QLineEdit(self.frame)
        self.DCID_Text.setGeometry(QtCore.QRect(210, 160, 271, 21))
        self.DCID_Text.setObjectName("DCID_Text")
        self.ICID_Text = QtWidgets.QLineEdit(self.frame)
        self.ICID_Text.setGeometry(QtCore.QRect(210, 190, 271, 21))
        self.ICID_Text.setObjectName("ICID_Text")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(70, 305, 511, 121))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(20, 0, 81, 41))
        self.label_4.setObjectName("label_4")
        self.FilePath_Text = QtWidgets.QLineEdit(self.frame_2)
        self.FilePath_Text.setGeometry(QtCore.QRect(90, 10, 231, 21))
        self.FilePath_Text.setObjectName("FilePath_Text")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 251, 41))
        self.label_5.setObjectName("label_5")
        self.AutosaveFrameFrequency_Text = QtWidgets.QLineEdit(self.frame_2)
        self.AutosaveFrameFrequency_Text.setGeometry(QtCore.QRect(280, 50, 41, 21))
        self.AutosaveFrameFrequency_Text.setObjectName("AutosaveFrameFrequency_Text")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(330, 40, 71, 41))
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(330, 80, 71, 41))
        self.label_8.setObjectName("label_8")
        self.VideoCalculateFrequency_Text = QtWidgets.QLineEdit(self.frame_2)
        self.VideoCalculateFrequency_Text.setGeometry(QtCore.QRect(280, 90, 41, 21))
        self.VideoCalculateFrequency_Text.setObjectName("VideoCalculateFrequency_Text")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(20, 80, 171, 41))
        self.label_9.setObjectName("label_9")
        self.Browser_BT = QtWidgets.QToolButton(self.frame_2)
        self.Browser_BT.setGeometry(QtCore.QRect(330, 10, 37, 18))
        self.Browser_BT.setObjectName("Browser_BT")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(70, 26, 251, 20))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(70, 280, 241, 21))
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "IOU Tolarance Of Face Detection:"))
        self.label_2.setText(_translate("Dialog", "Confidence Tolarance of Face Detection:"))
        self.Conf_Text.setText(_translate("Dialog", "0.5"))
        self.IOU_Text.setText(_translate("Dialog", "0.3"))
        self.FacialPoseCorrection_RBT.setText(_translate("Dialog", "Facial Pose Correction"))
        self.DistanceCorrection_RBT.setText(_translate("Dialog", "Distance Correction"))
        self.AlarmTem_Text.setText(_translate("Dialog", "37.2"))
        self.label_3.setText(_translate("Dialog", "Alarm Temperature:"))
        self.label_7.setText(_translate("Dialog", "℃"))
        self.label_12.setText(_translate("Dialog", "Digital Camera ID:"))
        self.label_13.setText(_translate("Dialog", "Infrared Camera ID:"))
        self.DCID_Text.setText(_translate("Dialog", "0"))
        self.ICID_Text.setText(_translate("Dialog", "\"http://admin:admin@192.168.1.100:8081/\""))
        self.label_4.setText(_translate("Dialog", "SavePath:"))
        self.FilePath_Text.setText(_translate("Dialog", "./File/"))
        self.label_5.setText(_translate("Dialog", "Frequency of Autosaving Frames:"))
        self.AutosaveFrameFrequency_Text.setText(_translate("Dialog", "5"))
        self.label_6.setText(_translate("Dialog", "f/min"))
        self.label_8.setText(_translate("Dialog", "times/s"))
        self.VideoCalculateFrequency_Text.setText(_translate("Dialog", "10"))
        self.label_9.setText(_translate("Dialog", "Video Calculate Frequency:"))
        self.Browser_BT.setText(_translate("Dialog", "..."))
        self.label_10.setText(_translate("Dialog", "Calculation Parameters Settings:"))
        self.label_11.setText(_translate("Dialog", "Running Parameters Settings:"))

