#!/usr/bin/python
# -*- coding: utf-8 -*-

from functions import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


# Global Variables
Users = list()
liste=list()
shareUser = list()
permissionsList1 = list()
lineEditValue=list()
isfile=False

if sys.argv[1][0] != "/":
    fullpath=os.getcwd()+"/"+sys.argv[1]
else:
    fullpath=sys.argv[1]

# Main Window Interface Code
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        # Components

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 460)
        MainWindow.setStyleSheet("background-image: url('./img/arkaplan.png');")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("background-color: #ffba00;")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(240, 210, 101, 25))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 240, 331, 141))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(110, 40, 204, 23))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.readCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.readCheckBox.setObjectName("readCheckBox")
        self.horizontalLayout_4.addWidget(self.readCheckBox)
        self.writeCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.writeCheckBox.setObjectName("writeCheckBox")
        self.horizontalLayout_4.addWidget(self.writeCheckBox)
        self.executeCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget_3)
        self.executeCheckBox.setObjectName("executeCheckBox")
        self.horizontalLayout_4.addWidget(self.executeCheckBox)
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(110, 10, 201, 23))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(210, 70, 101, 25))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_8.addWidget(self.pushButton_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(110, 40, 204, 23))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.readCheckBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.readCheckBox_2.setObjectName("readCheckBox_2")
        self.horizontalLayout_3.addWidget(self.readCheckBox_2)
        self.writeCheckBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.writeCheckBox_2.setObjectName("writeCheckBox_2")
        self.horizontalLayout_3.addWidget(self.writeCheckBox_2)
        self.executeCheckBox_2 = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.executeCheckBox_2.setObjectName("executeCheckBox_2")
        self.horizontalLayout_3.addWidget(self.executeCheckBox_2)
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 10, 201, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(210, 70, 101, 25))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_1 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout_7.addWidget(self.pushButton_1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 10, 201, 23))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 80, 99, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_share = QtWidgets.QLabel(self.tab_3)
        self.label_share.setGeometry(QtCore.QRect(110, 41, 201, 31))
        self.label_share.setText("")
        self.label_share.setObjectName("label_share")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 351, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Adding Action to Components

        self.pushButton_1.clicked.connect(self.addGroupButtonAction)
        self.pushButton_2.clicked.connect(self.addUserButtonAction)
        self.pushButton_3.clicked.connect(self.removeButtonAction)
        self.pushButton_4.clicked.connect(self.shareButtonAction)
        self.pushButton_1.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.lineEdit.textChanged.connect(self.line_edit_text_changed_1)
        self.lineEdit_2.textChanged.connect(self.line_edit_text_changed_2)
        self.lineEdit_3.textChanged.connect(self.line_edit_text_changed_3)
        self.listWidget.itemDoubleClicked.connect(self.listWidgetAction)
        self.firstOpen()



    """
    def active (self):
       if( self.tab.isActiveWindow()==True):
           self.lineEdit_2.clear()
           self.lineEdit_3.clear()

       elif(self.tab_2.isActiveWindow()==True):
            self.lineEdit.clear()
            self.lineEdit_3.clear()

       elif (self.tab_3.isActiveWindow() == True):
           self.lineEdit.clear()
           self.lineEdit_2.clear()
           
    """

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Paylaşım - "+fullpath))
        self.label.setText(_translate("MainWindow", "Users and Groups"))
        self.pushButton_3.setText(_translate("MainWindow", "Remove"))
        self.readCheckBox.setText(_translate("MainWindow", "Read"))
        self.writeCheckBox.setText(_translate("MainWindow", "Write"))
        self.executeCheckBox.setText(_translate("MainWindow", "Execute"))
        self.label_4.setText(_translate("MainWindow", "User Name:"))
        self.pushButton_2.setText(_translate("MainWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Add User"))
        self.readCheckBox_2.setText(_translate("MainWindow", "Read"))
        self.writeCheckBox_2.setText(_translate("MainWindow", "Write"))
        self.executeCheckBox_2.setText(_translate("MainWindow", "Execute"))
        self.label_3.setText(_translate("MainWindow", "Group Name:"))
        self.pushButton_1.setText(_translate("MainWindow", "Add"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Add Group"))
        self.label_5.setText(_translate("MainWindow", "Share Name:"))
        self.pushButton_4.setText(_translate("MainWindow", "Share"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Share"))

    # Action and Event Functions

    def showmessage(self):

        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText("Error")
        self.msg.setInformativeText('invalid insertion')
        self.msg.setWindowTitle("Error")
        self.msg.exec_()

    def firstOpen(self):


        labelcomment = controlSharePath(fullpath)
        labelsplit = list()


        ismount=mountsearch(fullpath)

        self.lineEdit_3.setText(str(getShareName(fullpath)))


        if (ismount == False):
            self.label_share.clear()
            permissions = UserAndGroupPermissions(fullpath)
            permissionsList = list()

            for i in range(1, len(permissions)):
                permissionsList.append(permissions[i][0].replace(":", " "))

                if (str(permissionsList[i - 1][0:4]) == "user"):
                    self.itm = QListWidgetItem(permissionsList[i - 1])
                    self.itm.setIcon(QIcon(r"./img/user.png"))
                    self.listWidget.setIconSize(QtCore.QSize(15, 15))
                    self.listWidget.addItem(self.itm)

                elif (str(permissionsList[i - 1][0:5]) == "group"):
                    self.itm = QListWidgetItem(permissionsList[i - 1])
                    self.itm.setIcon(QIcon(r"./img/group.png"))
                    self.listWidget.setIconSize(QtCore.QSize(15, 15))
                    self.listWidget.addItem(self.itm)

        else:
            if len(labelsplit) != 0:
                labelsplit.append(labelcomment.split("="))
                self.label_share.setText("share name:" + labelsplit[0][1])


                labelsplit[0][1] = labelsplit[0][1].strip(" ")
                #self.lineEdit_3.setText(labelsplit[0][1])

                isfile = searchOnFile(labelsplit[0][1])

            else:

                permissions1 = UserAndGroupPermissions(fullpath)

                self.listWidget.clear()
                for i in range(0, len(permissions1)):
                    permissionsList1.append(permissions1[i][0].replace(":", " "))

                    self.itm = QListWidgetItem(permissionsList1[i])
                    self.listWidget.addItem(self.itm)

    def line_edit_text_changed_1(self, text):

        if (text):
            self.pushButton_2.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)

    def line_edit_text_changed_2(self, text):

        if (text):
            self.pushButton_1.setEnabled(True)
        else:
            self.pushButton_1.setEnabled(False)


    def line_edit_text_changed_3(self, text):

        if (text):
            self.pushButton_4.setEnabled(True)
        else:
            self.pushButton_4.setEnabled(False)
            self.lineEdit_3.clear()

    def shareButtonAction(self):

        lineEditValue.append(self.lineEdit_3.text())
        isfile = searchOnFile(lineEditValue[0])

        if(isfile==True):
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setText("Info")
            self.msg.setInformativeText('Previously Added')
            self.msg.setWindowTitle("Info")
            self.msg.exec_()
        else:

            Dialog = QDialog()
            ui = Ui_UserLogin()
            ui.setupUi2(Dialog)
            Dialog.show()
            Dialog.exec_()

            lineEditValue.clear()
            self.lineEdit_3.clear()
            self.pushButton_4.setEnabled(False)

    def listWidgetAction(self):

        self.pushButton_3.setEnabled(True)

    def removeButtonAction(self):

        listItems = self.listWidget.selectedItems()
        removelist = list()
        if not listItems:
            return
        for a in listItems:
            self.listWidget.takeItem(self.listWidget.row(a))
            x = a.text()
            removelist = x.split()

            if (removelist[0] == "group"):
                removeGroup(removelist[1],fullpath)

            elif (removelist[0] == "user"):
                removeUser(removelist[1],fullpath)

        self.pushButton_3.setEnabled(False)

    def addUserButtonAction(self):
        '''
        Users.append(self.lineEdit.text())

        Dialog = QDialog()
        ui = Ui_UserLogin()
        ui.setupUi2(Dialog)
        Dialog.show()
        Dialog.exec_()
        '''

        usersSplit = list()
        elementNumbers = self.listWidget.count()

        if (elementNumbers == 0):
            self.addUserWithPermission()

        else:
            user_word = self.lineEdit.text()

            for index in range(0, elementNumbers):
                usersSplit.append(self.listWidget.item(index).text().split())

            for i in range(0, elementNumbers):
                if (str(user_word) == usersSplit[i][1] and "user" == usersSplit[i][0]):
                    liste = self.listWidget.item(i)
                    self.listWidget.takeItem(self.listWidget.row(liste))
                    self.addUserWithPermission()


        self.addUserWithPermission()


    def addUserWithPermission(self):

                if (
                    self.readCheckBox.isChecked() == True and self.writeCheckBox.isChecked() == False and self.executeCheckBox.isChecked() == False):
                   if( userAllow(self.lineEdit.text(), "r", fullpath)==True):
                        self.itm=QListWidgetItem("user " + self.lineEdit.text() + " " + "r--")
                        self.itm.setIcon(QIcon(r"./img/user.png"))
                        self.listWidget.setIconSize(QtCore.QSize(15,15))
                        self.listWidget.addItem(self.itm)
                        self.lineEdit.clear()
                        self.pushButton_2.setEnabled(False)
                        self.readCheckBox.setChecked(False)
                   else:
                    print("eklenemedi")
                    self.showmessage()
                    self.lineEdit.clear()
                    self.pushButton_2.setEnabled(False)
                    self.readCheckBox.setChecked(False)

                elif (
                    self.readCheckBox.isChecked() == False and self.writeCheckBox.isChecked() == True and self.executeCheckBox.isChecked() == False):
                    if(userAllow(self.lineEdit.text(), "w", fullpath)==True):
                        self.itm = QListWidgetItem("user " +self.lineEdit.text() + " " + "-w-")
                        self.itm.setIcon(QIcon(r"./img/user.png"))
                        self.listWidget.setIconSize(QtCore.QSize(15, 15))
                        self.listWidget.addItem(self.itm)
                        self.lineEdit.clear()
                        self.pushButton_2.setEnabled(False)
                        self.writeCheckBox.setChecked(False)
                    else:
                       print("eklenemedi")
                       self.showmessage()
                       self.lineEdit.clear()
                       self.pushButton_2.setEnabled(False)
                       self.writeCheckBox.setChecked(False)

                elif (
                    self.readCheckBox.isChecked() == False and self.writeCheckBox.isChecked() == False and self.executeCheckBox.isChecked() == True):
                    if(userAllow(self.lineEdit.text(), "x", fullpath)==True):
                        self.itm = QListWidgetItem("user " + self.lineEdit.text() + " " + "--x")
                        self.itm.setIcon(QIcon(r"./img/user.png"))
                        self.listWidget.setIconSize(QtCore.QSize(15, 15))
                        self.listWidget.addItem(self.itm)
                        self.lineEdit.clear()
                        self.pushButton_2.setEnabled(False)
                        self.executeCheckBox.setChecked(False)
                    else:
                        print("eklenemedi")
                        self.showmessage()
                        self.lineEdit.clear()
                        self.pushButton_2.setEnabled(False)
                        self.executeCheckBox.setChecked(False)
                elif (
                    self.readCheckBox.isChecked() == True and self.writeCheckBox.isChecked() == True and self.executeCheckBox.isChecked() == False):
                    if(userAllow(self.lineEdit.text(), "rw", fullpath)==True):
                        self.itm = QListWidgetItem("user " + self.lineEdit.text() + " " + "rw-")
                        self.itm.setIcon(QIcon(r"./img/user.png"))
                        self.listWidget.setIconSize(QtCore.QSize(15, 15))
                        self.listWidget.addItem(self.itm)
                        self.lineEdit.clear()
                        self.pushButton_2.setEnabled(False)
                        self.readCheckBox.setChecked(False)
                        self.writeCheckBox.setChecked(False)
                    else:
                        print("eklenemedi")
                        self.showmessage()
                        self.lineEdit.clear()
                        self.pushButton_2.setEnabled(False)
                        self.readCheckBox.setChecked(False)
                        self.writeCheckBox.setChecked(False)


                elif (
                    self.readCheckBox.isChecked() == True and self.writeCheckBox.isChecked() == False and self.executeCheckBox.isChecked() == True):
                    if(userAllow(self.lineEdit.text(), "rx", fullpath)==True):
                        self.itm = QListWidgetItem("user " + self.lineEdit.text() + " " + "r-x")
                        self.itm.setIcon(QIcon(r"./img/user.png"))
                        self.listWidget.setIconSize(QtCore.QSize(15, 15))
                        self.listWidget.addItem(self.itm)
                        self.lineEdit.clear()
                        self.pushButton_2.setEnabled(False)
                        self.readCheckBox.setChecked(False)
                        self.executeCheckBox.setChecked(False)

                    else:
                        print("eklenemedi")
                        self.showmessage()
                        self.lineEdit.clear()
                        self.pushButton_2.setEnabled(False)
                        self.readCheckBox.setChecked(False)
                        self.executeCheckBox.setChecked(False)

                elif (
                    self.readCheckBox.isChecked() == False and self.writeCheckBox.isChecked() == True and self.executeCheckBox.isChecked() == True):
                    if(userAllow(self.lineEdit.text(), "wx", fullpath)==True):
                        self.itm=QListWidgetItem("user " + self.lineEdit.text() + " " + "-wx")
                        self.itm.setIcon(QIcon(r"./img/user.png"))
                        self.listWidget.setIconSize(QtCore.QSize(15,15))
                        self.listWidget.addItem(self.itm)
                        self.lineEdit.clear()
                        self.pushButton_2.setEnabled(False)
                        self.writeCheckBox.setChecked(False)
                        self.executeCheckBox.setChecked(False)
                    else:
                        print("eklenemedi")
                        self.showmessage()
                        self.lineEdit.clear()
                        self.pushButton_2.setEnabled(False)
                        self.writeCheckBox.setChecked(False)
                        self.executeCheckBox.setChecked(False)

                elif (
                    self.readCheckBox.isChecked() == True and self.writeCheckBox.isChecked() == False and self.executeCheckBox.isChecked() == True):
                    if(userAllow(self.lineEdit.text(), "rx", fullpath) ==True):
                        self.itm = QListWidgetItem("user " + self.lineEdit.text() + " " + "r-x")
                        self.itm.setIcon(QIcon(r"./img/user.png"))
                        self.listWidget.setIconSize(QtCore.QSize(15, 15))
                        self.listWidget.addItem(self.itm)
                        self.lineEdit.clear()
                        self.pushButton_2.setEnabled(False)
                        self.readCheckBox.setChecked(False)
                        self.executeCheckBox.setChecked(False)
                    else:
                        print("eklenemedi")
                        self.showmessage()
                        self.lineEdit.clear()
                        self.pushButton_2.setEnabled(False)
                        self.readCheckBox.setChecked(False)
                        self.executeCheckBox.setChecked(False)
                elif (
                    self.readCheckBox.isChecked() == True and self.writeCheckBox.isChecked() == True and self.executeCheckBox.isChecked() == True):
                    if(userAllow(self.lineEdit.text(), "rwx", fullpath)==True):
                        self.itm = QListWidgetItem("user " + self.lineEdit.text() + " " + "rwx")
                        self.itm.setIcon(QIcon(r"./img/user.png"))
                        self.listWidget.setIconSize(QtCore.QSize(15, 15))
                        self.listWidget.addItem(self.itm)
                        self.lineEdit.clear()
                        self.pushButton_2.setEnabled(False)
                        self.readCheckBox.setChecked(False)
                        self.writeCheckBox.setChecked(False)
                        self.executeCheckBox.setChecked(False)
                    else:
                        print("eklenemedi")
                        self.showmessage()
                        self.lineEdit.clear()
                        self.pushButton_2.setEnabled(False)
                        self.readCheckBox.setChecked(False)
                        self.writeCheckBox.setChecked(False)
                        self.executeCheckBox.setChecked(False)


    def addGroupButtonAction(self):

        groupSplit = list()
        elementNumbers = self.listWidget.count()

        if (elementNumbers == 0):
            self.addGroupWithPermission()

        else:
            group_word = self.lineEdit_2.text()

            for index in range(0, elementNumbers):
                groupSplit.append(self.listWidget.item(index).text().split())

            for i in range(0, elementNumbers):
                if (str(group_word) == groupSplit[i][1] and "group" == groupSplit[i][0]):
                    liste = self.listWidget.item(i)
                    self.listWidget.takeItem(self.listWidget.row(liste))
                    self.addGroupWithPermission()

            self.addGroupWithPermission()

    def addGroupWithPermission(self):


            if (
                    self.readCheckBox_2.isChecked() == True and self.writeCheckBox_2.isChecked() == False and self.executeCheckBox_2.isChecked() == False):
                if(groupAllow(self.lineEdit_2.text(), "r", fullpath)==True):
                    self.itm = QListWidgetItem("group "+self.lineEdit_2.text() + " " + "r--")
                    self.itm.setIcon(QIcon(r"./img/group.png"))
                    self.listWidget.setIconSize(QtCore.QSize(15, 15))
                    self.listWidget.addItem(self.itm)
                    self.lineEdit_2.clear()
                    self.pushButton_1.setEnabled(False)
                    self.readCheckBox_2.setChecked(False)
                else:
                    print("eklenemedi")
                    self.showmessage()
                    self.lineEdit_2.clear()
                    self.pushButton_1.setEnabled(False)
                    self.readCheckBox_2.setChecked(False)

            elif (
                    self.readCheckBox_2.isChecked() == False and self.writeCheckBox_2.isChecked() == True and self.executeCheckBox_2.isChecked() == False):
                if(groupAllow(self.lineEdit_2.text(), "w", fullpath)==True):
                    self.itm = QListWidgetItem("group " + self.lineEdit_2.text() + " " + "-w-")
                    self.itm.setIcon(QIcon(r"./img/group.png"))
                    self.listWidget.setIconSize(QtCore.QSize(15, 15))
                    self.listWidget.addItem(self.itm)
                    self.lineEdit_2.clear()
                    self.pushButton_1.setEnabled(False)
                    self.writeCheckBox_2.setChecked(False)

                else:
                    print("eklenemedi")
                    self.showmessage()
                    self.lineEdit_2.clear()
                    self.pushButton_1.setEnabled(False)
                    self.writeCheckBox_2.setChecked(False)

            elif (
                    self.readCheckBox_2.isChecked() == False and self.writeCheckBox_2.isChecked() == False and self.executeCheckBox_2.isChecked() == True):
                if(groupAllow(self.lineEdit_2.text(), "x", fullpath)==True):
                    self.itm = QListWidgetItem("group "+ self.lineEdit_2.text() + " " + "--x")
                    self.itm.setIcon(QIcon(r"./img/group.png"))
                    self.listWidget.setIconSize(QtCore.QSize(15, 15))
                    self.listWidget.addItem(self.itm)
                    self.lineEdit_2.clear()
                    self.pushButton_1.setEnabled(False)
                    self.executeCheckBox_2.setChecked(False)

                else:
                    print("eklenemedi")
                    self.showmessage()
                    self.lineEdit_2.clear()
                    self.pushButton_1.setEnabled(False)
                    self.executeCheckBox_2.setChecked(False)

            elif (
                    self.readCheckBox_2.isChecked() == True and self.writeCheckBox_2.isChecked() == True and self.executeCheckBox_2.isChecked() == False):
                if(groupAllow(self.lineEdit_2.text(), "rw", fullpath)==True):
                    self.itm = QListWidgetItem("group "+self.lineEdit_2.text() + " " + "rw-")
                    self.itm.setIcon(QIcon(r"./img/group.png"))
                    self.listWidget.setIconSize(QtCore.QSize(15, 15))
                    self.listWidget.addItem(self.itm)
                    self.lineEdit_2.clear()
                    self.pushButton_1.setEnabled(False)
                    self.readCheckBox_2.setChecked(False)
                    self.writeCheckBox_2.setChecked(False)
                else:
                    print("eklenemedi")
                    self.showmessage()
                    self.lineEdit_2.clear()
                    self.pushButton_1.setEnabled(False)
                    self.readCheckBox_2.setChecked(False)
                    self.writeCheckBox_2.setChecked(False)
            elif (
                    self.readCheckBox_2.isChecked() == True and self.writeCheckBox_2.isChecked() == False and self.executeCheckBox_2.isChecked() == True):
                if(groupAllow(self.lineEdit_2.text(), "rx", fullpath)==True):
                    self.itm = QListWidgetItem("group "+ self.lineEdit_2.text() + " " + "r-x")
                    self.itm.setIcon(QIcon(r"./img/group.png"))
                    self.listWidget.setIconSize(QtCore.QSize(15, 15))
                    self.listWidget.addItem(self.itm)
                    self.lineEdit_2.clear()
                    self.pushButton_1.setEnabled(False)
                    self.readCheckBox_2.setChecked(False)
                    self.executeCheckBox_2.setChecked(False)
                else:
                    print("eklenemedi")
                    self.showmessage()
                    self.lineEdit_2.clear()
                    self.pushButton_1.setEnabled(False)
                    self.readCheckBox_2.setChecked(False)
                    self.executeCheckBox_2.setChecked(False)

            elif (
                    self.readCheckBox_2.isChecked() == False and self.writeCheckBox_2.isChecked() == True and self.executeCheckBox_2.isChecked() == True):
                if(groupAllow(self.lineEdit_2.text(), "wx", fullpath)==True):
                    self.itm = QListWidgetItem("group "+ self.lineEdit_2.text() + " " + "-wx")
                    self.itm.setIcon(QIcon(r"./img/group.png"))
                    self.listWidget.setIconSize(QtCore.QSize(15, 15))
                    self.listWidget.addItem(self.itm)
                    self.lineEdit_2.clear()
                    self.pushButton_1.setEnabled(False)
                    self.writeCheckBox_2.setChecked(False)
                    self.executeCheckBox_2.setChecked(False)
                else:
                    print("eklenemedi")
                    self.showmessage()
                    self.lineEdit_2.clear()
                    self.pushButton_1.setEnabled(False)
                    self.writeCheckBox_2.setChecked(False)
                    self.executeCheckBox_2.setChecked(False)

            elif (
                    self.readCheckBox_2.isChecked() == True and self.writeCheckBox_2.isChecked() == False and self.executeCheckBox_2.isChecked() == True):
                if(groupAllow(self.lineEdit_2.text(), "rx", fullpath)==True):
                    self.itm = QListWidgetItem("group "+ self.lineEdit_2.text() + " " + "r-x")
                    self.itm.setIcon(QIcon(r"./img/group.png"))
                    self.listWidget.setIconSize(QtCore.QSize(15, 15))
                    self.listWidget.addItem(self.itm)
                    self.lineEdit_2.clear()
                    self.pushButton_1.setEnabled(False)
                    self.readCheckBox_2.setChecked(False)
                    self.executeCheckBox_2.setChecked(False)
                else:
                    print("eklenemedi")
                    self.showmessage()
                    self.lineEdit_2.clear()
                    self.pushButton_1.setEnabled(False)
                    self.readCheckBox_2.setChecked(False)
                    self.executeCheckBox_2.setChecked(False)

            elif (
                    self.readCheckBox_2.isChecked() == True and self.writeCheckBox_2.isChecked() == True and self.executeCheckBox_2.isChecked() == True):
                if(groupAllow(self.lineEdit_2.text(), "rwx", fullpath)==True):
                    self.itm = QListWidgetItem("group "+ self.lineEdit_2.text() + " " + "rwx")
                    self.itm.setIcon(QIcon(r"./img/group.png"))
                    self.listWidget.setIconSize(QtCore.QSize(15, 15))
                    self.listWidget.addItem(self.itm)
                    self.lineEdit_2.clear()
                    self.pushButton_1.setEnabled(False)
                    self.readCheckBox_2.setChecked(False)
                    self.writeCheckBox_2.setChecked(False)
                    self.executeCheckBox_2.setChecked(False)
                else:
                    print("eklenemedi")
                    self.showmessage()
                    self.lineEdit_2.clear()
                    self.pushButton_1.setEnabled(False)
                    self.readCheckBox_2.setChecked(False)
                    self.writeCheckBox_2.setChecked(False)
                    self.executeCheckBox_2.setChecked(False)


# User Login Screen Interface Code

class Ui_UserLogin(object):

    def setupUi2(self, UserLogin):

        # Components

        UserLogin.setObjectName("UserLogin")
        UserLogin.resize(360, 345)
        UserLogin.setStyleSheet("QDialog { background-image: url('./img/user-background.png'); }")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(UserLogin)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 230, 91, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.HL2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.HL2.setContentsMargins(0, 0, 0, 0)
        self.HL2.setObjectName("HL2")
        self.usernameLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.usernameLabel.setObjectName("usernameLabel")
        self.HL2.addWidget(self.usernameLabel)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(UserLogin)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(130, 230, 181, 25))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.HL2_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.HL2_2.setContentsMargins(0, 0, 0, 0)
        self.HL2_2.setObjectName("HL2_2")
        self.username = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.username.setObjectName("username")
        computer_name = str(getWhoAmI())
        #cn1 = computer_name.replace("b'", "")
        #cn2 = cn1[:-3]
        self.username.setText(str(computer_name))
        self.HL2_2.addWidget(self.username)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(UserLogin)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 260, 91, 21))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.HL2_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.HL2_3.setContentsMargins(0, 0, 0, 0)
        self.HL2_3.setObjectName("HL2_3")
        self.passwordLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.passwordLabel.setObjectName("passwordLabel")
        self.HL2_3.addWidget(self.passwordLabel)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(UserLogin)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(130, 260, 181, 25))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.HL2_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.HL2_4.setContentsMargins(0, 0, 0, 0)
        self.HL2_4.setObjectName("HL2_4")
        self.password = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.HL2_4.addWidget(self.password)
        self.horizontalLayoutWidget = QtWidgets.QWidget(UserLogin)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 20, 152, 152))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(UserLogin)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 170, 311, 44))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pleaseLabel = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.pleaseLabel.setObjectName("pleaseLabel")
        self.horizontalLayout_2.addWidget(self.pleaseLabel)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(UserLogin)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(130, 290, 181, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.loginButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.loginButton.setObjectName("loginButton")
        self.horizontalLayout_3.addWidget(self.loginButton)
        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_6.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.horizontalLayoutWidget_7.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_4.raise_()
        self.horizontalLayoutWidget_5.raise_()
        self.pleaseLabel.raise_()

        # Adding Action to Components

        self.loginButton.clicked.connect(self.loginButtonAction)

        self.retranslateUi(UserLogin)
        QtCore.QMetaObject.connectSlotsByName(UserLogin)

    def retranslateUi(self, UserLogin):
        _translate = QtCore.QCoreApplication.translate
        UserLogin.setWindowTitle(_translate("UserLogin", "Samba Share"))
        self.usernameLabel.setText(_translate("UserLogin",
                                              "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Username:</span></p></body></html>"))
        self.passwordLabel.setText(_translate("UserLogin",
                                              "<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Password:</span></p></body></html>"))
        self.pleaseLabel.setText(_translate("UserLogin",
                                            "<html><head/><body><p align=\"center\">Please login password</p><p align=\"center\">for user authentication.</p></body></html>"))
        self.loginButton.setText(_translate("UserLogin", "Login"))

    # Action and Event Functions
    def loginButtonAction(self):
        if (isfile == False):
            isShare=shareFile(self.password.text(), lineEditValue[0], fullpath)

            if(isShare == True):
                startSamba()
            else:
                self.msg = QMessageBox()
                self.msg.setIcon(QMessageBox.Critical)
                self.msg.setText("Info")
                self.msg.setInformativeText('Wrong Password')
                self.msg.setWindowTitle("Info")
                self.msg.exec_()
                self.password.clear()

            self.password.clear()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
