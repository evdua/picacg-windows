# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'readimg.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReadImg(object):
    def setupUi(self, ReadImg):
        ReadImg.setObjectName("ReadImg")
        ReadImg.resize(223, 786)
        self.gridLayout_2 = QtWidgets.QGridLayout(ReadImg)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(ReadImg)
        self.label_5.setStyleSheet("color: #ee2a24")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(ReadImg)
        self.label_6.setStyleSheet("color: #ee2a24")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.radioButton = QtWidgets.QRadioButton(ReadImg)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.buttonGroup = QtWidgets.QButtonGroup(ReadImg)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton)
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(ReadImg)
        self.radioButton_2.setObjectName("radioButton_2")
        self.buttonGroup.addButton(self.radioButton_2)
        self.verticalLayout.addWidget(self.radioButton_2)
        self.label_4 = QtWidgets.QLabel(ReadImg)
        self.label_4.setStyleSheet("color: #ee2a24")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.resolutionLabel = QtWidgets.QLabel(ReadImg)
        self.resolutionLabel.setObjectName("resolutionLabel")
        self.verticalLayout.addWidget(self.resolutionLabel)
        self.sizeLabel = QtWidgets.QLabel(ReadImg)
        self.sizeLabel.setObjectName("sizeLabel")
        self.verticalLayout.addWidget(self.sizeLabel)
        self.stateLable = QtWidgets.QLabel(ReadImg)
        self.stateLable.setObjectName("stateLable")
        self.verticalLayout.addWidget(self.stateLable)
        self.epsLabel = QtWidgets.QLabel(ReadImg)
        self.epsLabel.setMinimumSize(QtCore.QSize(0, 20))
        self.epsLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.epsLabel.setObjectName("epsLabel")
        self.verticalLayout.addWidget(self.epsLabel)
        self.label = QtWidgets.QLabel(ReadImg)
        self.label.setStyleSheet("color: #ee2a24")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.checkBox = QtWidgets.QCheckBox(ReadImg)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.label_2 = QtWidgets.QLabel(ReadImg)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(ReadImg)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_9 = QtWidgets.QLabel(ReadImg)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.resolutionWaifu = QtWidgets.QLabel(ReadImg)
        self.resolutionWaifu.setObjectName("resolutionWaifu")
        self.verticalLayout.addWidget(self.resolutionWaifu)
        self.sizeWaifu = QtWidgets.QLabel(ReadImg)
        self.sizeWaifu.setObjectName("sizeWaifu")
        self.verticalLayout.addWidget(self.sizeWaifu)
        self.tickLabel = QtWidgets.QLabel(ReadImg)
        self.tickLabel.setObjectName("tickLabel")
        self.verticalLayout.addWidget(self.tickLabel)
        self.stateWaifu = QtWidgets.QLabel(ReadImg)
        self.stateWaifu.setObjectName("stateWaifu")
        self.verticalLayout.addWidget(self.stateWaifu)
        self.lastPage = QtWidgets.QPushButton(ReadImg)
        self.lastPage.setMinimumSize(QtCore.QSize(0, 0))
        self.lastPage.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lastPage.setObjectName("lastPage")
        self.verticalLayout.addWidget(self.lastPage)
        self.nextPage = QtWidgets.QPushButton(ReadImg)
        self.nextPage.setMinimumSize(QtCore.QSize(0, 0))
        self.nextPage.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.nextPage.setObjectName("nextPage")
        self.verticalLayout.addWidget(self.nextPage)
        self.copyButton = QtWidgets.QPushButton(ReadImg)
        self.copyButton.setObjectName("copyButton")
        self.verticalLayout.addWidget(self.copyButton)
        self.returePage = QtWidgets.QPushButton(ReadImg)
        self.returePage.setMinimumSize(QtCore.QSize(0, 0))
        self.returePage.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.returePage.setObjectName("returePage")
        self.verticalLayout.addWidget(self.returePage)
        self.pushButton_2 = QtWidgets.QPushButton(ReadImg)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(ReadImg)
        self.lastPage.clicked.connect(ReadImg.LastPage)
        self.nextPage.clicked.connect(ReadImg.NextPage)
        self.returePage.clicked.connect(ReadImg.ReturnPage)
        self.radioButton_2.clicked.connect(ReadImg.SwitchPicture)
        self.radioButton.clicked.connect(ReadImg.SwitchPicture)
        self.pushButton_2.clicked.connect(ReadImg.hide)
        self.checkBox.clicked.connect(ReadImg.OpenWaifu)
        self.copyButton.clicked.connect(ReadImg.CopyPicture)
        QtCore.QMetaObject.connectSlotsByName(ReadImg)
        ReadImg.setTabOrder(self.radioButton, self.radioButton_2)

    def retranslateUi(self, ReadImg):
        _translate = QtCore.QCoreApplication.translate
        ReadImg.setWindowTitle(_translate("ReadImg", "Form"))
        self.label_5.setText(_translate("ReadImg", "点击右键打开关闭"))
        self.label_6.setText(_translate("ReadImg", "按住左Alt+滚轮放大"))
        self.radioButton.setText(_translate("ReadImg", "铺满高度（还原图片）"))
        self.radioButton_2.setText(_translate("ReadImg", "铺满宽度（还原图片）"))
        self.label_4.setText(_translate("ReadImg", "图片信息"))
        self.resolutionLabel.setText(_translate("ReadImg", "分辨率："))
        self.sizeLabel.setText(_translate("ReadImg", "大小："))
        self.stateLable.setText(_translate("ReadImg", "状态："))
        self.epsLabel.setText(_translate("ReadImg", "位置："))
        self.label.setText(_translate("ReadImg", "Waifu2x参数"))
        self.checkBox.setText(_translate("ReadImg", "打开Waifu2x"))
        self.label_2.setText(_translate("ReadImg", "噪点等级：3"))
        self.label_3.setText(_translate("ReadImg", "放大倍数：2"))
        self.label_9.setText(_translate("ReadImg", "转码模式：GPU"))
        self.resolutionWaifu.setText(_translate("ReadImg", "分辨率："))
        self.sizeWaifu.setText(_translate("ReadImg", "大小："))
        self.tickLabel.setText(_translate("ReadImg", "耗时："))
        self.stateWaifu.setText(_translate("ReadImg", "状态："))
        self.lastPage.setText(_translate("ReadImg", "上一页"))
        self.nextPage.setText(_translate("ReadImg", "下一页"))
        self.copyButton.setText(_translate("ReadImg", "复制图片"))
        self.returePage.setText(_translate("ReadImg", "返回"))
        self.pushButton_2.setText(_translate("ReadImg", "隐藏"))
