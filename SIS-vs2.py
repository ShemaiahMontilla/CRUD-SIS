# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\monti\A-CRUD\NewCode\Test-crud.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
from datetime import date
from DB_Connection import con,mycursor
from datetime import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 1400, 700))
        self.tabWidget.setStyleSheet(u"font: 75 12pt \"MS Shell Dlg 2\";")
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(210, 30, 251, 51))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.coursecodelineEdit = QtWidgets.QLineEdit(self.tab)
        self.coursecodelineEdit.setGeometry(QtCore.QRect(800, 30, 251, 51))
        self.coursecodelineEdit.setText("")
        self.coursecodelineEdit.setObjectName("courselineEdit")

        self.courselineEdit = QtWidgets.QLineEdit(self.tab)
        self.courselineEdit.setGeometry(QtCore.QRect(800, 130, 251, 51))
        self.courselineEdit.setText("")
        self.courselineEdit.setObjectName("courselineEdit")



        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 100, 251, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.comboBoxGender = QtWidgets.QComboBox(self.tab)
        self.comboBoxGender.setGeometry(QtCore.QRect(210, 170, 100, 31))
        self.comboBoxGender.setEditable(True)
        self.comboBoxGender.setObjectName("comboBoxGender")
        self.comboBoxGender.addItem("")
        self.comboBoxGender.addItem("")

        self.comboBoxYearLevel = QtWidgets.QComboBox(self.tab)
        self.comboBoxYearLevel.setGeometry(QtCore.QRect(210, 220, 100, 31))
        self.comboBoxYearLevel.setEditable(True)
        self.comboBoxYearLevel.setObjectName("comboBoxYearLevel")
        self.comboBoxYearLevel.addItem("")
        self.comboBoxYearLevel.addItem("")
        self.comboBoxYearLevel.addItem("")
        self.comboBoxYearLevel.addItem("")

        self.comboBoxCoursecode = QtWidgets.QComboBox(self.tab)
        self.comboBoxCoursecode.setGeometry(QtCore.QRect(210, 270, 100, 31))
        self.comboBoxCoursecode.setEditable(True)
        self.comboBoxCoursecode.setObjectName("comboBoxCoursecode")
        self.comboBoxCoursecode.addItem("")
        self.comboBoxCoursecode.addItem("")
        self.comboBoxCoursecode.addItem("")
        self.comboBoxCoursecode.addItem("")
        self.comboBoxCoursecode.addItem("")
        self.comboBoxCoursecode.addItem("")
        self.comboBoxCoursecode.addItem("")
        self.comboBoxCoursecode.addItem("")

  



        self.coursecodelabel = QtWidgets.QLabel(self.tab)
        self.coursecodelabel.setGeometry(QtCore.QRect(670, 35, 111, 31))
        self.coursecodelabel.setAutoFillBackground(False)
        self.coursecodelabel.setObjectName("coursecodelabel")

        self.courselabel = QtWidgets.QLabel(self.tab)
        self.courselabel.setGeometry(QtCore.QRect(670, 151, 111, 31))
        self.courselabel.setAutoFillBackground(False)
        self.courselabel.setObjectName("courselabel")

        self.AddCourseCodeButton = QtWidgets.QPushButton(self.tab)
        self.AddCourseCodeButton.setGeometry(QtCore.QRect(700, 201, 200, 31))
        self.AddCourseCodeButton.setObjectName("AddCourseButton")
        self.AddCourseCodeButton.clicked.connect(self.InsertCourse)

        self.IDlabel = QtWidgets.QLabel(self.tab)
        self.IDlabel.setGeometry(QtCore.QRect(50, 40, 111, 31))
        self.IDlabel.setAutoFillBackground(False)
        self.IDlabel.setObjectName("IDlabel")

        self.Namelabel_2 = QtWidgets.QLabel(self.tab)
        self.Namelabel_2.setGeometry(QtCore.QRect(50, 110, 111, 31))
        self.Namelabel_2.setAutoFillBackground(False)
        self.Namelabel_2.setObjectName("Namelabel_2")

        self.Genderlabel_3 = QtWidgets.QLabel(self.tab)
        self.Genderlabel_3.setGeometry(QtCore.QRect(50, 180, 111, 31))
        self.Genderlabel_3.setAutoFillBackground(False)
        self.Genderlabel_3.setObjectName("Genderlabel_3")

        self.yearlevellabel_4 = QtWidgets.QLabel(self.tab)
        self.yearlevellabel_4.setGeometry(QtCore.QRect(50, 220, 111, 31))
        self.yearlevellabel_4.setAutoFillBackground(False)
        self.yearlevellabel_4.setObjectName("yearlevellabel_4")

        self.coursecodelabel_5 = QtWidgets.QLabel(self.tab)
        self.coursecodelabel_5.setGeometry(QtCore.QRect(50, 270, 111, 31))
        self.coursecodelabel_5.setAutoFillBackground(False)
        self.coursecodelabel_5.setObjectName("coursecodelabel_5")

        self.InsertButton = QtWidgets.QPushButton(self.tab)
        self.InsertButton.setGeometry(QtCore.QRect(210, 380, 200, 31))
        self.InsertButton.setObjectName("InsertButton")
        self.InsertButton.clicked.connect(self.InsertPeople)


        self.tabWidget.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

  
        self.edit =QtWidgets.QLineEdit(self.tab_2)
        self.edit.setGeometry(QtCore.QRect(300, 25, 900, 41))
        self.edit.textChanged.connect(self.filter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.edit.setFont(font)          
        self.edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border :2px solid ;\n"
        "border-radius:2px;\n"
        "border-color:black;\n")
       

        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(300, 60, 900, 531))
        self.tableWidget.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        
        
        

        self.DisplayButton = QtWidgets.QPushButton(self.tab_2)
        self.DisplayButton.setGeometry(QtCore.QRect(1030, 599, 160, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DisplayButton.setFont(font)
        self.DisplayButton.setStyleSheet("background-color: skyblue;\n""color:white;\n"
        "border :5px solid ;\n"
        "border-radius:10px;\n"
        "border-color:skyblue;\n"
        "padding:6px")
        "border-color: rgb(0, 255, 255);"
        self.DisplayButton.setObjectName("DisplayButton")
        self.DisplayButton.clicked.connect(self.Tablefill)

        self.tabWidget.addTab(self.tab_2, "")
    
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 20, 200, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.lineEditCourseCode = QtWidgets.QLineEdit(self.tab_3)
        self.lineEditCourseCode.setGeometry(QtCore.QRect(900, 20, 200, 31))
        self.lineEditCourseCode.setObjectName("lineEditCourseCode")

        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(40, 10, 91, 51))
        self.label_6.setObjectName("label_6")

        self.labelSearchCcode = QtWidgets.QLabel(self.tab_3)
        self.labelSearchCcode.setGeometry(QtCore.QRect(700, 10, 200, 51))
        self.labelSearchCcode.setObjectName("labelSearchCcode")

        self.DeleteCourseButton = QtWidgets.QPushButton(self.tab_3)
        self.DeleteCourseButton.setGeometry(QtCore.QRect(1120, 20, 175, 31))
        self.DeleteCourseButton.setObjectName("DeleteCourseButton")
        self.DeleteCourseButton.clicked.connect(self.delete_crs)


        self.DeletepushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.DeletepushButton_2.setGeometry(QtCore.QRect(420, 20, 175, 31))
        self.DeletepushButton_2.setObjectName("SearchpushButton_2")
        self.DeletepushButton_2.clicked.connect(self.delete_ppl)

        self.label_7 = QtWidgets.QLabel(self.tab_3)
        self.label_7.setGeometry(QtCore.QRect(40, 290, 111, 31))
        self.label_7.setAutoFillBackground(False)
        self.label_7.setObjectName("label_7")


        self.yearlevellabel_8 = QtWidgets.QLabel(self.tab_3)
        self.yearlevellabel_8.setGeometry(QtCore.QRect(40, 300, 111, 31))
        self.yearlevellabel_8.setAutoFillBackground(False)
        self.yearlevellabel_8.setObjectName("yearlevellabel_8")

        self.comboBoxYearLevel1 = QtWidgets.QComboBox(self.tab_3)
        self.comboBoxYearLevel1.setGeometry(QtCore.QRect(200, 300, 100, 31))
        self.comboBoxYearLevel1.setEditable(True)
        self.comboBoxYearLevel1.setObjectName("comboBoxYearLevel")
        self.comboBoxYearLevel1.addItem("")
        self.comboBoxYearLevel1.addItem("")
        self.comboBoxYearLevel1.addItem("")
        self.comboBoxYearLevel1.addItem("")

        self.coursecodelabel_8 = QtWidgets.QLabel(self.tab_3)
        self.coursecodelabel_8.setGeometry(QtCore.QRect(40, 380, 111, 31))
        self.coursecodelabel_8.setAutoFillBackground(False)
        self.coursecodelabel_8.setObjectName("label_8")

        self.comboBoxCoursecode1 = QtWidgets.QComboBox(self.tab_3)
        self.comboBoxCoursecode1.setGeometry(QtCore.QRect(200, 380, 100, 31))
        self.comboBoxCoursecode1.setEditable(True)
        self.comboBoxCoursecode1.setObjectName("comboBoxCoursecode")
        self.comboBoxCoursecode1.addItem("")
        self.comboBoxCoursecode1.addItem("")
        self.comboBoxCoursecode1.addItem("")
        self.comboBoxCoursecode1.addItem("")
        self.comboBoxCoursecode1.addItem("")
        self.comboBoxCoursecode1.addItem("")
        self.comboBoxCoursecode1.addItem("")
        self.comboBoxCoursecode1.addItem("")

        self.StudentsIDlabel_9 = QtWidgets.QLabel(self.tab_3)
        self.StudentsIDlabel_9.setGeometry(QtCore.QRect(40, 80, 111, 31))
        self.StudentsIDlabel_9.setAutoFillBackground(False)
        self.StudentsIDlabel_9.setObjectName("StudentsIDlabel_9")

        self.genderlabel_10 = QtWidgets.QLabel(self.tab_3)
        self.genderlabel_10.setGeometry(QtCore.QRect(40, 220, 111, 31))
        self.genderlabel_10.setAutoFillBackground(False)
        self.genderlabel_10.setObjectName("label_10")

        self.comboBoxGender1 = QtWidgets.QComboBox(self.tab_3)
        self.comboBoxGender1.setGeometry(QtCore.QRect(200, 220, 100, 31))
        self.comboBoxGender1.setEditable(True)
        self.comboBoxGender1.setObjectName("comboBoxGender")
        self.comboBoxGender1.addItem("")
        self.comboBoxGender1.addItem("")



        

        self.StudentsIDlineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.StudentsIDlineEdit_5.setGeometry(QtCore.QRect(200, 70, 251, 51))
        self.StudentsIDlineEdit_5.setInputMask("")
        self.StudentsIDlineEdit_5.setText("")
        self.StudentsIDlineEdit_5.setPlaceholderText("")
        self.StudentsIDlineEdit_5.setObjectName("StudentsIDlineEdit_5")

        self.EditCourseCodelabel = QtWidgets.QLabel(self.tab_3)
        self.EditCourseCodelabel.setGeometry(QtCore.QRect(700, 70, 111, 31))
        self.EditCourseCodelabel.setAutoFillBackground(False)
        self.EditCourseCodelabel.setObjectName("EditCourseCodelabel")

        self.EditCourselabel = QtWidgets.QLabel(self.tab_3)
        self.EditCourselabel.setGeometry(QtCore.QRect(700, 170, 111, 31))
        self.EditCourselabel.setAutoFillBackground(False)
        self.EditCourselabel.setObjectName("EditCourselabel")


        self.CoursCodelineEdit_5 = QtWidgets.QLineEdit(self.tab_3)
        self.CoursCodelineEdit_5.setGeometry(QtCore.QRect(900, 70, 251, 51))
        self.CoursCodelineEdit_5.setInputMask("")
        self.CoursCodelineEdit_5.setText("")
        self.CoursCodelineEdit_5.setPlaceholderText("")
        self.CoursCodelineEdit_5.setObjectName("CoursCodelineEdit_5")

        self.EditCourselineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.EditCourselineEdit.setGeometry(QtCore.QRect(900, 150, 251, 51))
        self.EditCourselineEdit.setInputMask("")
        self.EditCourselineEdit.setText("")
        self.EditCourselineEdit.setPlaceholderText("")
        self.EditCourselineEdit.setObjectName("EditCourselineEdit")

        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(40, 150, 111, 31))
        self.label_11.setAutoFillBackground(False)
        self.label_11.setObjectName("label_11")





        self.UpdateButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.UpdateButton_3.setGeometry(QtCore.QRect(200, 420, 200, 31))
        self.UpdateButton_3.setObjectName("pushButton_3")
        self.UpdateButton_3.clicked.connect(self.Update_ppl)

        self.UpdateCourseButton = QtWidgets.QPushButton(self.tab_3)
        self.UpdateCourseButton.setGeometry(QtCore.QRect(900, 270, 200, 31))
        self.UpdateCourseButton.setObjectName("UpdateCourseButton")
        self.UpdateCourseButton.clicked.connect(self.Update_crs)
      

        self.NamelineEdit_7 = QtWidgets.QLineEdit(self.tab_3)
        self.NamelineEdit_7.setGeometry(QtCore.QRect(200, 140, 251, 51))
        self.NamelineEdit_7.setPlaceholderText("")
        self.NamelineEdit_7.setObjectName("NamelineEdit_7")



        self.tabWidget.addTab(self.tab_3, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")

  
        self.edit1 =QtWidgets.QLineEdit(self.tab_4)
        self.edit1.setGeometry(QtCore.QRect(300, 25, 900, 41))
        self.edit1.textChanged.connect(self.filter1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.edit.setFont(font)          
        self.edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border :2px solid ;\n"
        "border-radius:2px;\n"
        "border-color:black;\n")
       

        self.tableWidget1 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget1.setGeometry(QtCore.QRect(300, 60, 900, 531))
        self.tableWidget1.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.tableWidget1.setTabKeyNavigation(False)
        self.tableWidget1.setProperty("showDropIndicator", False)
        self.tableWidget1.setObjectName("tableWidget1")
        self.tableWidget1.setColumnCount(0)
        self.tableWidget1.setRowCount(0)
        
        
        

        self.DisplayButton1 = QtWidgets.QPushButton(self.tab_4)
        self.DisplayButton1.setGeometry(QtCore.QRect(1030, 599, 160, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.DisplayButton1.setFont(font)
        self.DisplayButton1.setStyleSheet("background-color: skyblue;\n""color:white;\n"
        "border :5px solid ;\n"
        "border-radius:10px;\n"
        "border-color:skyblue;\n"
        "padding:6px")
        "border-color: rgb(0, 255, 255);"
        self.DisplayButton1.setObjectName("DisplayButton1")
        self.DisplayButton1.clicked.connect(self.Tablefill1)

        self.tabWidget.addTab(self.tab_4, "")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Add The Student ID"))
        self.coursecodelineEdit.setPlaceholderText(_translate("MainWindow", "Add Course Code"))
        self.courselineEdit.setPlaceholderText(_translate("MainWindow", "Add Course"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Add the Full name"))
        self.edit.setPlaceholderText(_translate("MainWindow", "Search by ID Number"))
        self.edit1.setPlaceholderText(_translate("MainWindow", "Search by Course Code"))
        self.comboBoxGender.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBoxGender.setItemText(1, _translate("MainWindow", "Female"))
        self.comboBoxYearLevel.setItemText(0, _translate("MainWindow", "1st Year"))
        self.comboBoxYearLevel.setItemText(1, _translate("MainWindow", "2nd Year"))
        self.comboBoxYearLevel.setItemText(2, _translate("MainWindow", "3rd Year"))
        self.comboBoxYearLevel.setItemText(3, _translate("MainWindow", "4th Year"))

        self.comboBoxCoursecode.setItemText(0, _translate("MainWindow", "BSA"))
        self.comboBoxCoursecode.setItemText(1, _translate("MainWindow", "BSCA"))
        self.comboBoxCoursecode.setItemText(2, _translate("MainWindow", "BSCE"))
        self.comboBoxCoursecode.setItemText(3, _translate("MainWindow", "BSCS"))
        self.comboBoxCoursecode.setItemText(4, _translate("MainWindow", "BSEE"))
        self.comboBoxCoursecode.setItemText(5, _translate("MainWindow", "BSIS"))
        self.comboBoxCoursecode.setItemText(6, _translate("MainWindow", "BSIT"))
        self.comboBoxCoursecode.setItemText(7, _translate("MainWindow", "BSStat"))

   
        


   
        self.IDlabel.setText(_translate("MainWindow", "Student ID:"))
        self.coursecodelabel.setText(_translate("MainWindow", "Course Code:"))
        self.Namelabel_2.setText(_translate("MainWindow", "Name:"))
        self.Genderlabel_3.setText(_translate("MainWindow", "Gender:"))
        self.yearlevellabel_4.setText(_translate("MainWindow", "Year Level:"))
        self.coursecodelabel_5.setText(_translate("MainWindow", "Course Code:"))

        self.InsertButton.setText(_translate("MainWindow", "Add a student:"))
        self.AddCourseCodeButton.setText(_translate("MainWindow", "Add the Course:"))
        self.DisplayButton.setText(_translate("MainWindow", "Display Table:"))
        self.DisplayButton1.setText(_translate("MainWindow", "Display Table:"))


        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "ADD STUDENT/COURSE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Student Table"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Enter the student Id"))
        self.label_6.setText(_translate("MainWindow", "Search Id"))
        self.labelSearchCcode.setText(_translate("MainWindow", "Search Course Code:"))
        self.EditCourseCodelabel.setText(_translate("MainWindow", "Course Code:"))
        self.EditCourselabel.setText(_translate("MainWindow", "Course:"))

        self.DeletepushButton_2.setText(_translate("MainWindow", "Delete the Student"))
        self.DeleteCourseButton.setText(_translate("MainWindow", "Delete the Course"))
        self.UpdateCourseButton.setText(_translate("MainWindow", "Update the Course"))
       
        self.coursecodelabel_8.setText(_translate("MainWindow", "Course Code"))
        self.courselabel.setText(_translate("MainWindow", "Course"))
        self.comboBoxCoursecode1.setItemText(0, _translate("MainWindow", "BSA"))
        self.comboBoxCoursecode1.setItemText(1, _translate("MainWindow", "BSCA"))
        self.comboBoxCoursecode1.setItemText(2, _translate("MainWindow", "BSCE"))
        self.comboBoxCoursecode1.setItemText(3, _translate("MainWindow", "BSCS"))
        self.comboBoxCoursecode1.setItemText(4, _translate("MainWindow", "BSEE"))
        self.comboBoxCoursecode1.setItemText(5, _translate("MainWindow", "BSIS"))
        self.comboBoxCoursecode1.setItemText(6, _translate("MainWindow", "BSIT"))
        self.comboBoxCoursecode1.setItemText(7, _translate("MainWindow", "BSStat"))

        self.StudentsIDlabel_9.setText(_translate("MainWindow", "Student ID"))

        self.genderlabel_10.setText(_translate("MainWindow", "Gender"))
        self.comboBoxGender1.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBoxGender1.setItemText(1, _translate("MainWindow", "Female"))

        self.label_11.setText(_translate("MainWindow", "Name"))
        self.UpdateButton_3.setText(_translate("MainWindow", "Update the Student"))

        self.yearlevellabel_8.setText(_translate("MainWindow", "Year level"))
        self.comboBoxYearLevel1.setItemText(0, _translate("MainWindow", "1st Year"))
        self.comboBoxYearLevel1.setItemText(1, _translate("MainWindow", "2nd Year"))
        self.comboBoxYearLevel1.setItemText(2, _translate("MainWindow", "3rd Year"))
        self.comboBoxYearLevel1.setItemText(3, _translate("MainWindow", "4th Year"))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "SEARCH, DELETE AND UPDATE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "COURSE TABLE"))



    
    def Tablefill(self):
        self.tableWidget.setColumnCount(0)
        sql = ("SELECT * FROM students_info")
        mycursor.execute(sql)
        all_data = mycursor.fetchall()
        self.tableWidget.setRowCount(len(all_data[1]))
        self.tableWidget.setColumnCount(len(all_data[0]))
        self.tableWidget.setColumnWidth(0,150)
        self.tableWidget.setColumnWidth(1,200)
        self.tableWidget.setColumnWidth(2,150)
        self.tableWidget.setColumnWidth(3,150)
        self.tableWidget.setColumnWidth(4,150)
        self.tableWidget.setHorizontalHeaderLabels(['Student ID', 'Name', 'Gender', 'Year Level', 'Course Code'])
        for row in range(1):
            for column in range(0):
                item = QTableWidgetItem(all_data[row][column])
                self.tableWidget.setItem(row, column, item)


        
        for Row,allval in enumerate(all_data):
            for Column,value in enumerate(allval):
                self.tableWidget.setItem(Row,Column, QTableWidgetItem(str(value)))
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

    def Tablefill1(self):
        self.tableWidget1.setColumnCount(0)
        sql = ("SELECT * FROM course")
        mycursor.execute(sql)
        all_data1 = mycursor.fetchall()
        self.tableWidget1.setRowCount(len(all_data1[1]))
        self.tableWidget1.setColumnCount(len(all_data1[0]))
        self.tableWidget1.setColumnWidth(0,250)
        self.tableWidget1.setColumnWidth(1,500)

        self.tableWidget1.setHorizontalHeaderLabels([ 'Course Code', 'Course'])
        for row in range(1):
            for column in range(0):
                item1 = QTableWidgetItem(all_data1[row][column])
                self.tableWidget1.setItem(row, column, item1)


        
        for Row,allval1 in enumerate(all_data1):
            for Column,value in enumerate(allval1):
                self.tableWidget1.setItem(Row,Column, QTableWidgetItem(str(value)))
            row_position = self.tableWidget1.rowCount()
            self.tableWidget1.insertRow(row_position)

    def InsertPeople(self):
        #print("date")
        stID = self.lineEdit.text()
        stName = self.lineEdit_2.text()
        stgender =  self.comboBoxGender.currentText()
        styearlevel =  self.comboBoxYearLevel.currentText()
        stcoursecode =  self.comboBoxCoursecode.Text()


        sql = ("INSERT INTO students_info (studentsID,studentsName,gender,yearlevel,coursecode)"
 					"VALUES (%s,%s,%s,%s,%s)")

        value = [stID, stName, stgender, styearlevel, stcoursecode]
        mycursor.execute(sql, value)
        con.commit()

        self.Tablefill()
    
    def InsertCourse(self):
        #print("date")
        coursecode = self.coursecodelineEdit.text()
        course = self.courselineEdit.text()


        sql = ("INSERT INTO course(coursecode, course)"
 					"VALUES (%s,%s)")

        value = [coursecode, course]
        mycursor.execute(sql, value)
        con.commit()

        self.Tablefill1()



    def filter(self, filter_text):
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(i, j)
                if item is not None:
                    match = filter_text.lower() not in item.text().lower()
                    self.tableWidget.setRowHidden(i, match)
                    if not match:
                        break

    def filter1(self, filter_text):
        for i in range(self.tableWidget1.rowCount()):
            for j in range(self.tableWidget1.columnCount()):
                item = self.tableWidget1.item(i, j)
                if item is not None:
                    match = filter_text.lower() not in item.text().lower()
                    self.tableWidget1.setRowHidden(i, match)
                    if not match:
                        break
    def delete_ppl(self):
        idSearch = self.lineEdit_4.text()
        sql = (f"DELETE FROM students_info WHERE studentsID = '{idSearch}'")
        mycursor.execute(sql)
        con.commit()
        self.Tablefill()
        msg=QMessageBox()
        msg.setWindowTitle("--- Delete a Student ---")
        msg.setText("ID-Number found in our dataset..")
        msg.setInformativeText("Student with an ID-Number: "+idSearch+" was deleted successfully")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        font=QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        msg.setFont(font)
        msg.exec()

    def delete_crs(self):
        coursecode2 =  self.lineEditCourseCode.text()
        sql = (f"DELETE FROM course WHERE coursecode = '{coursecode2}'")
        mycursor.execute(sql)
        con.commit()
        self.Tablefill1()
        msg=QMessageBox()
        msg.setWindowTitle("--- Delete a Course---")
        msg.setText("Course Code found in our dataset..")
        msg.setInformativeText("Course with a Course Code: "+coursecode2+" was deleted successfully")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        font=QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        msg.setFont(font)
        msg.exec()

    def Update_ppl(self):
        idSearch = self.lineEdit_4.text()
        studentID1 = self.StudentsIDlineEdit_5.text()
        Name1 = self.NamelineEdit_7.text()
        gender1 = self.comboBoxGender1.currentText()
        yearlevel1 = self.comboBoxYearLevel1.currentText()
        coursecode1 = self.comboBoxCoursecode1.currentText()
        sql = (f"UPDATE students_info SET studentsID= '{studentID1}', studentsName= '{Name1}' , gender = '{gender1}' , yearlevel = '{yearlevel1}', coursecode '{coursecode1}'WHERE studentsID = '{idSearch}'")
        mycursor.execute(sql)
        con.commit()
        self.Tablefill()
        msg=QMessageBox()
        msg.setWindowTitle("--- Edit a Student ---")
        msg.setText("Succesfully updated student "+idSearch+"")
        msg.setInformativeText("Updated to student with an ID Number: "+idSearch+"")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        font=QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        msg.setFont(font)
        msg.exec()

    def Update_crs(self):
        coursecode2 =  self.lineEditCourseCode.text()
        coursecodeEdited =  self.CoursCodelineEdit_5.text()
        courseEdited = self.EditCourselineEdit.text()
       

        sql = (f"UPDATE course SET coursecode= '{coursecodeEdited}', course = '{courseEdited}'WHERE coursecode = '{coursecode2}'")
        mycursor.execute(sql)
        con.commit()
        self.Tablefill()
        msg=QMessageBox()
        msg.setWindowTitle("--- Edit a Course ---")
        msg.setText("Succesfully updated Course with a course code :"+coursecode2+"")
        msg.setInformativeText("Updated to student with an course code: "+coursecode2+"")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        font=QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        msg.setFont(font)
        msg.exec()
        





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())