# Form implementation generated from reading ui file 'gotify_tray/gui/designs\widget_main.ui'
#
# Created by: PyQt6 UI code generator 6.1.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(809, 572)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listView_applications = QtWidgets.QListView(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView_applications.sizePolicy().hasHeightForWidth())
        self.listView_applications.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.listView_applications.setFont(font)
        self.listView_applications.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_applications.setWordWrap(True)
        self.listView_applications.setObjectName("listView_applications")
        self.gridLayout_2.addWidget(self.listView_applications, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pb_delete_all = QtWidgets.QPushButton(Form)
        self.pb_delete_all.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pb_delete_all.setFont(font)
        self.pb_delete_all.setObjectName("pb_delete_all")
        self.gridLayout.addWidget(self.pb_delete_all, 0, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.label_selected = QtWidgets.QLabel(Form)
        self.label_selected.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_selected.setFont(font)
        self.label_selected.setObjectName("label_selected")
        self.gridLayout.addWidget(self.label_selected, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.pb_refresh = QtWidgets.QPushButton(Form)
        self.pb_refresh.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pb_refresh.setFont(font)
        self.pb_refresh.setObjectName("pb_refresh")
        self.gridLayout.addWidget(self.pb_refresh, 0, 4, 1, 1)
        self.label_status = QtWidgets.QLabel(Form)
        self.label_status.setText("")
        self.label_status.setObjectName("label_status")
        self.gridLayout.addWidget(self.label_status, 0, 0, 1, 1)
        self.listView_messages = QtWidgets.QListView(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView_messages.sizePolicy().hasHeightForWidth())
        self.listView_messages.setSizePolicy(sizePolicy)
        self.listView_messages.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.listView_messages.setObjectName("listView_messages")
        self.gridLayout.addWidget(self.listView_messages, 1, 0, 1, 6)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.pb_refresh, self.pb_delete_all)
        Form.setTabOrder(self.pb_delete_all, self.listView_messages)
        Form.setTabOrder(self.listView_messages, self.listView_applications)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pb_delete_all.setText(_translate("Form", "Delete All"))
        self.label_selected.setText(_translate("Form", "TextLabel"))
        self.pb_refresh.setText(_translate("Form", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())