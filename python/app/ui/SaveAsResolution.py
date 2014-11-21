# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\RTS\People\Mclaeys\GIT\wtd-multi-saveas\resources\SaveAsResolution.ui'
#
# Created: Fri Nov 21 15:24:43 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SaveAsResolution(object):
    def setupUi(self, SaveAsResolution):
        SaveAsResolution.setObjectName("SaveAsResolution")
        SaveAsResolution.resize(400, 130)
        SaveAsResolution.setMinimumSize(QtCore.QSize(400, 130))
        SaveAsResolution.setMaximumSize(QtCore.QSize(400, 130))
        self.horizontalLayoutWidget = QtGui.QWidget(SaveAsResolution)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 381, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Save = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.horizontalLayout.addWidget(self.pushButton_Save)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_changeArea = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_changeArea.setObjectName("pushButton_changeArea")
        self.horizontalLayout.addWidget(self.pushButton_changeArea)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_cancel = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.groupBox_SaveAs = QtGui.QGroupBox(SaveAsResolution)
        self.groupBox_SaveAs.setGeometry(QtCore.QRect(10, 10, 381, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_SaveAs.setFont(font)
        self.groupBox_SaveAs.setObjectName("groupBox_SaveAs")
        self.label_fileName = QtGui.QLabel(self.groupBox_SaveAs)
        self.label_fileName.setGeometry(QtCore.QRect(10, 30, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_fileName.setFont(font)
        self.label_fileName.setObjectName("label_fileName")
        self.label_workArea = QtGui.QLabel(self.groupBox_SaveAs)
        self.label_workArea.setGeometry(QtCore.QRect(10, 50, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(False)
        self.label_workArea.setFont(font)
        self.label_workArea.setObjectName("label_workArea")

        self.retranslateUi(SaveAsResolution)
        QtCore.QMetaObject.connectSlotsByName(SaveAsResolution)

    def retranslateUi(self, SaveAsResolution):
        SaveAsResolution.setWindowTitle(QtGui.QApplication.translate("SaveAsResolution", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Save.setToolTip(QtGui.QApplication.translate("SaveAsResolution", "<html><head/><body><p>Click to save the file.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Save.setText(QtGui.QApplication.translate("SaveAsResolution", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_changeArea.setToolTip(QtGui.QApplication.translate("SaveAsResolution", "<html><head/><body><p>Click to set another work area.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_changeArea.setText(QtGui.QApplication.translate("SaveAsResolution", "Change WorkArea", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_cancel.setText(QtGui.QApplication.translate("SaveAsResolution", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_SaveAs.setTitle(QtGui.QApplication.translate("SaveAsResolution", "Save as...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fileName.setToolTip(QtGui.QApplication.translate("SaveAsResolution", "<html><head/><body><p><span style=\" font-size:9pt;\">Example of what the filename will be.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fileName.setText(QtGui.QApplication.translate("SaveAsResolution", "filename", None, QtGui.QApplication.UnicodeUTF8))
        self.label_workArea.setToolTip(QtGui.QApplication.translate("SaveAsResolution", "<html><head/><body><p>This is your current workarea. <span style=\" color:#ff0000;\">Change it if it is not correct!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_workArea.setText(QtGui.QApplication.translate("SaveAsResolution", "workarea", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\RTS\People\Mclaeys\GIT\wtd-multi-saveas\resources\SaveAsResolution.ui'
#
# Created: Fri Nov 21 15:34:04 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SaveAsResolution(object):
    def setupUi(self, SaveAsResolution):
        SaveAsResolution.setObjectName("SaveAsResolution")
        SaveAsResolution.resize(400, 130)
        SaveAsResolution.setMinimumSize(QtCore.QSize(400, 130))
        SaveAsResolution.setMaximumSize(QtCore.QSize(400, 130))
        self.horizontalLayoutWidget = QtGui.QWidget(SaveAsResolution)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 381, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Save = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.horizontalLayout.addWidget(self.pushButton_Save)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_changeArea = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_changeArea.setObjectName("pushButton_changeArea")
        self.horizontalLayout.addWidget(self.pushButton_changeArea)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_cancel = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.groupBox_SaveAs = QtGui.QGroupBox(SaveAsResolution)
        self.groupBox_SaveAs.setGeometry(QtCore.QRect(10, 10, 381, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_SaveAs.setFont(font)
        self.groupBox_SaveAs.setObjectName("groupBox_SaveAs")
        self.label_fileName = QtGui.QLabel(self.groupBox_SaveAs)
        self.label_fileName.setGeometry(QtCore.QRect(10, 30, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_fileName.setFont(font)
        self.label_fileName.setObjectName("label_fileName")
        self.label_workArea = QtGui.QLabel(self.groupBox_SaveAs)
        self.label_workArea.setGeometry(QtCore.QRect(10, 50, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(False)
        self.label_workArea.setFont(font)
        self.label_workArea.setObjectName("label_workArea")

        self.retranslateUi(SaveAsResolution)
        QtCore.QMetaObject.connectSlotsByName(SaveAsResolution)

    def retranslateUi(self, SaveAsResolution):
        SaveAsResolution.setWindowTitle(QtGui.QApplication.translate("SaveAsResolution", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Save.setToolTip(QtGui.QApplication.translate("SaveAsResolution", "<html><head/><body><p>Click to save the file.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Save.setText(QtGui.QApplication.translate("SaveAsResolution", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_changeArea.setToolTip(QtGui.QApplication.translate("SaveAsResolution", "<html><head/><body><p>Click to set another work area.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_changeArea.setText(QtGui.QApplication.translate("SaveAsResolution", "Change WorkArea", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_cancel.setText(QtGui.QApplication.translate("SaveAsResolution", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_SaveAs.setTitle(QtGui.QApplication.translate("SaveAsResolution", "Save as...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fileName.setToolTip(QtGui.QApplication.translate("SaveAsResolution", "<html><head/><body><p><span style=\" font-size:9pt;\">Example of what the filename will be.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fileName.setText(QtGui.QApplication.translate("SaveAsResolution", "filename", None, QtGui.QApplication.UnicodeUTF8))
        self.label_workArea.setToolTip(QtGui.QApplication.translate("SaveAsResolution", "<html><head/><body><p>This is your current workarea. <span style=\" color:#ff0000;\">Change it if it is not correct!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_workArea.setText(QtGui.QApplication.translate("SaveAsResolution", "workarea", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'W:\RTS\People\Mclaeys\GIT\wtd-multi-saveas\resources\SaveAsResolution.ui'
#
# Created: Fri Nov 21 15:35:43 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SaveAsResolution(object):
    def setupUi(self, SaveAsResolution):
        SaveAsResolution.setObjectName("SaveAsResolution")
        SaveAsResolution.resize(500, 130)
        SaveAsResolution.setMinimumSize(QtCore.QSize(500, 130))
        SaveAsResolution.setMaximumSize(QtCore.QSize(500, 130))
        self.horizontalLayoutWidget = QtGui.QWidget(SaveAsResolution)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 481, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Save = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Save.setObjectName("pushButton_Save")
        self.horizontalLayout.addWidget(self.pushButton_Save)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_changeArea = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_changeArea.setObjectName("pushButton_changeArea")
        self.horizontalLayout.addWidget(self.pushButton_changeArea)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_cancel = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.groupBox_SaveAs = QtGui.QGroupBox(SaveAsResolution)
        self.groupBox_SaveAs.setGeometry(QtCore.QRect(10, 10, 481, 81))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_SaveAs.sizePolicy().hasHeightForWidth())
        self.groupBox_SaveAs.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.groupBox_SaveAs.setFont(font)
        self.groupBox_SaveAs.setObjectName("groupBox_SaveAs")
        self.label_fileName = QtGui.QLabel(self.groupBox_SaveAs)
        self.label_fileName.setGeometry(QtCore.QRect(10, 30, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.label_fileName.setFont(font)
        self.label_fileName.setObjectName("label_fileName")
        self.label_workArea = QtGui.QLabel(self.groupBox_SaveAs)
        self.label_workArea.setGeometry(QtCore.QRect(10, 50, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setItalic(True)
        font.setBold(False)
        self.label_workArea.setFont(font)
        self.label_workArea.setObjectName("label_workArea")

        self.retranslateUi(SaveAsResolution)
        QtCore.QMetaObject.connectSlotsByName(SaveAsResolution)

    def retranslateUi(self, SaveAsResolution):
        SaveAsResolution.setWindowTitle(QtGui.QApplication.translate("SaveAsResolution", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Save.setToolTip(QtGui.QApplication.translate("SaveAsResolution", "<html><head/><body><p>Click to save the file.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_Save.setText(QtGui.QApplication.translate("SaveAsResolution", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_changeArea.setToolTip(QtGui.QApplication.translate("SaveAsResolution", "<html><head/><body><p>Click to set another work area.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_changeArea.setText(QtGui.QApplication.translate("SaveAsResolution", "Change WorkArea", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_cancel.setText(QtGui.QApplication.translate("SaveAsResolution", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_SaveAs.setTitle(QtGui.QApplication.translate("SaveAsResolution", "Save as...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fileName.setToolTip(QtGui.QApplication.translate("SaveAsResolution", "<html><head/><body><p><span style=\" font-size:9pt;\">Example of what the filename will be.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_fileName.setText(QtGui.QApplication.translate("SaveAsResolution", "filename", None, QtGui.QApplication.UnicodeUTF8))
        self.label_workArea.setToolTip(QtGui.QApplication.translate("SaveAsResolution", "<html><head/><body><p>This is your current workarea. <span style=\" color:#ff0000;\">Change it if it is not correct!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_workArea.setText(QtGui.QApplication.translate("SaveAsResolution", "workarea", None, QtGui.QApplication.UnicodeUTF8))

