# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableView
from PyQt5.QtCore import Qt, QSortFilterProxyModel
import pandas as pd
from EditWindow import  Ui_EditWindow
from AddWindow import  Ui_AddWindow

import csv



# The class for the Ui_MainWindow
class Ui_MainWindow(object):
    #A function that will open the second window for the edit operation and it check if the inputted student's is in the data set or not
    def openEditWindow(self):
        
        fileName = 'C:/Users/monti/A-CRUD/students.csv'
        idnumber = self.lineEditEdit.text()
        index_student = None
        updated_data = []

        with open(fileName, "r", encoding="utf-8") as fileInput:
            reader = csv.reader(fileInput)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if idnumber == row[0]:
                        index_student = counter
                        #A Message Box that will pop up if the ID-Number is found in the data set
                        msg=QMessageBox()
                        msg.setWindowTitle("--- Edit Student ---")
                        msg.setText("ID-Number found in our dataset..")
                        msg.setInformativeText("Student Found: at index "+str(index_student))
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                        msg.exec()   
                        self.window =QtWidgets.QMainWindow()
                        self.ui = Ui_EditWindow()
                        self.ui.setupUi(self.window)
                        self.window.show()
                    else:
                     updated_data.append(row)
                    counter += 1
         #A Message Box that will pop up if the ID-Number is not found in the data set
        if index_student is None:
            msg=QMessageBox()
            msg.setWindowTitle("--- ---")
            msg.setText("ID-Number not found in our dataset..")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            msg.exec()  

    
    def openAddWindow(self):
        self.window =QtWidgets.QMainWindow()
        self.ui = Ui_AddWindow()
        self.ui.setupUi(self.window)
        self.window.show()


        

        

                    
                        
#Function for the setupUI , setting of the UI buttons,Input widgets , table view and etc
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 1000)
        MainWindow.setStyleSheet("background-color: rgb(251, 233, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")





        self.labelSIS = QtWidgets.QLabel(self.centralwidget)
        self.labelSIS.setGeometry(QtCore.QRect(550, 30, 821, 70))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(22)
        self.labelSIS.setFont(font)
        self.labelSIS.setStyleSheet("background-color: rgb(108, 255, 255);\n"
        "border :5px solid ;\n"
        "border-radius:5px;\n"
        "border-color:blue;\n"
        "padding:6px")
        self.labelSIS.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSIS.setObjectName("labelSIS")


        self.labelSearch = QtWidgets.QLabel(self.centralwidget)
        self.labelSearch.setGeometry(QtCore.QRect(350, 400, 120, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelSearch.setFont(font)
        self.labelSearch.setStyleSheet("background-color: rgb(108, 255, 255);\n"
        "border :5px solid ;\n"
        "border-radius:5px;\n"
        "border-color:blue;\n"
        "padding:6px")
        self.labelSearch.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSearch.setObjectName("labelSearch")



        self.ButtonDisplay = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDisplay.setGeometry(QtCore.QRect(350, 340, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonDisplay.setFont(font)
        self.ButtonDisplay.setStyleSheet("background-color: skyblue;\n""color:white;\n"
        "border :5px solid ;\n"
        "border-radius:10px;\n"
        "border-color:skyblue;\n"
        "padding:6px")
        "border-color: rgb(0, 255, 255);"
        self.ButtonDisplay.setObjectName("ButtonDisplay")
        self.ButtonDisplay.clicked.connect(self.loadCsv)



        self.ButtonEdit = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.openEditWindow())
        self.ButtonEdit.setGeometry(QtCore.QRect(370, 240, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonEdit.setFont(font)
        self.ButtonEdit.setStyleSheet("background-color: rgb(255, 170, 255);\n"
        "border :5px solid ;\n"
        "border-radius:10px;\n"
        "border-color:black;\n"
        "padding:6px")
        "border-color: rgb(73, 76, 255);"
        self.ButtonEdit.setObjectName("pushButton_2")
        

        self.lineEditEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEdit.setGeometry(QtCore.QRect(533, 250, 281, 41 ))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditEdit.setFont(font)
        self.lineEditEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border :2px solid ;\n"
        "border-radius:2px;\n"
        "border-color:black;\n")
        self.lineEditEdit.setText("")
        self.lineEditEdit.setObjectName("lineEditEdit")

        self.ButtonAdd= QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.openAddWindow())
        self.ButtonAdd.setGeometry(QtCore.QRect(1350, 240, 175, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonAdd.setFont(font)
        self.ButtonAdd.setStyleSheet("background-color: rgb(170, 170, 255);\n"
        "border :5px solid ;\n"
        "border-radius:10px;\n"
        "border-color:blue;\n"
        "padding:6px")
        "border-color: rgb(73, 76, 255);"
       
        self.ButtonAdd.setObjectName("pushButton_3")
       # self.ButtonAdd.clicked.connect(self.add_student)

        self.ButtonDelete= QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDelete.setGeometry(QtCore.QRect(850, 240, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ButtonDelete.setFont(font)
        self.ButtonDelete.setStyleSheet("background-color: rgb(255, 170, 255);\n"
        "border :5px solid ;\n"
        "border-radius:10px;\n"
        "border-color:black;\n"
        "padding:6px")
        "border-color: rgb(73, 76, 255);"
        self.ButtonDelete.setObjectName("pushButton_4")
        self.ButtonDelete.clicked.connect(self.delete_student)

        self.lineEditDelete = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDelete.setGeometry(QtCore.QRect(1043, 250, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDelete.setFont(font)
        self.lineEditDelete.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border :2px solid ;\n"
        "border-radius:2px;\n"
        "border-color:black;\n")
        self.lineEditDelete.setText("")
        self.lineEditDelete.setObjectName("lineEditDelete")

        self.BtnClear = QtWidgets.QPushButton(self.centralwidget)
        self.BtnClear.setGeometry(QtCore.QRect(500, 340, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BtnClear.setFont(font)
        self.BtnClear.setStyleSheet("background-color: skyblue;\n""color:white;\n"
        "border :5px solid ;\n"
        "border-radius:10px;\n"
        "border-color:skyblue;\n"
        "padding:6px")
        self.BtnClear.setObjectName("BtnClear")
        self.BtnClear.clicked.connect(self.clear)










        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.model = QtGui.QStandardItemModel(MainWindow)
        self.model.setHorizontalHeaderLabels(['ID Number', 'Name', 'Course', 'Year', 'Gender'])


        self.filter_proxy_model =QtCore.QSortFilterProxyModel(self.centralwidget)
        self.filter_proxy_model.setSourceModel(self.model)
        self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.filter_proxy_model.setFilterKeyColumn(0)

        self.search_field = QtWidgets.QLineEdit(self.centralwidget)
        self.search_field.setGeometry(QtCore.QRect(471, 400, 1181, 41 ))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.search_field.setFont(font)          
        self.search_field.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border :2px solid ;\n"
        "border-radius:2px;\n"
        "border-color:black;\n")
        self.search_field.textChanged.connect(self.filter_proxy_model.setFilterRegExp)
        self.search_field.setPlaceholderText("Search by ID -Number")
       

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(350, 450, 1300, 461))
        self.tableView.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.tableView.setObjectName("tableView")
        self.tableView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableView.setModel(self.filter_proxy_model)
        #self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)

#Function for retanslateUI, it set the text for the button, input widgets and etc
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelSIS.setText(_translate("MainWindow", "Simple Student Information System"))

        self.labelSearch.setText(_translate("MainWindow",  "Search"))
        


        self.ButtonDisplay.setText(_translate("MainWindow", "Display All"))
        self.ButtonEdit.setText(_translate("MainWindow", "Edit Student"))
        self.lineEditEdit.setPlaceholderText(_translate("MainWindow", "Enter student's id-number to update:"))
        self.ButtonAdd.setText(_translate("MainWindow", "Add new student"))
        self.ButtonDelete.setText(_translate("MainWindow", "Delete a student"))
        self.BtnClear.setText(_translate("MainWindow", "Clear Table"))
        
        self.lineEditDelete.setPlaceholderText(_translate("MainWindow", "Enter student's id-number to delete:"))
        
  #Fucntion that will display the dataset from the text file or csv file. It will load the data  
    def loadCsv(self):
        fileName = 'C:/Users/monti/A-CRUD/students.csv'
        
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):    
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)



    #Function that will clear the display on the table
    def clear(self):
        self.model.clear()
                
  #Function that searches the student using a key value which is the id number, it pop ups the data of the said student 
    def search_student(self):

        fileName = 'C:/Users/monti/A-CRUD/students.csv'
        
        id_number = self.lineEditSearch.text()
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput): 
                if len(row) > 0:
                        if id_number == row[0]:
                            # Message box that will pop up when the student is found and it shows the data of the said student
                                msg=QMessageBox()
                                msg.setWindowTitle("--- Search a tudent ---")
                                msg.setText("ID-Number found in our dataset..")
                                msg.setInformativeText("ID-Number:  "+row[0]+"\n" "Name:  " +row[1]+ "\n""Course:  "+row[2]+"\n""Year-Level:  "+row[3]+"\n""Gender:  "+row[4])
                                msg.setIcon(QMessageBox.Information)
                                msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                                font=QtGui.QFont()
                                font.setPointSize(12)
                                font.setBold(True)
                                font.setWeight(75)
                                msg.setFont(font)
                                msg.exec()
                                break
            else:
                #A Message box if the student's id number does not have a match in the dataset
                msg=QMessageBox()
                msg.setWindowTitle("---Search a Student")
                msg.setText("ID-Number not found in our dataset..")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                font=QtGui.QFont()
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                msg.setFont(font)
                msg.exec()

        
        

   #A function that will add the student in the data set
   # def add_student(self):
        #fileName = 'C:/Users/monti/A-CRUD/students.csv'
        #name = self.lineEditName.text()
        #idnumber = self.lineEditIdnumber.text()
        #yearlevel = self.YearLevelcomboBox.currentText()
        #gender = self.comboBox.currentText()
        #course = self.lineEditCourse.text()

        #student_data = [idnumber,name,course,yearlevel,gender]

        #with open(fileName, 'a+',
         #encoding="utf-8",newline="") as fileInput:
                #writer = csv.writer(fileInput)
                #writer.writerows([student_data])
# A message box that will show that the student was added to the set successfully
        #msg=QMessageBox()
        #msg.setWindowTitle("--- Add a Student ---")
        #msg.setText("Data saved successfully")
        #msg.setIcon(QMessageBox.Information)
        #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        #font=QtGui.QFont()
        #font.setPointSize(12)
        #font.setBold(True)
        #font.setWeight(75)
        #msg.setFont(font)
        #msg.exec()
        

                
        
 
#A function that will delete a student from the data set
    def delete_student(self):
        fileName = 'C:/Users/monti/A-CRUD/students.csv'
        ID_number = self.lineEditDelete.text()
        student_found = False
        updated_data = []
        with open(fileName, "r", encoding="utf-8") as fileInput:
            reader = csv.reader(fileInput)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if ID_number != row[0]:
                        updated_data.append(row)
                        counter += 1
                    else:
                        student_found = True
        

        if student_found is True:
            with open(fileName, "w", encoding="utf-8", newline="") as fileInput:
                writer = csv.writer(fileInput)
                writer.writerows(updated_data)
            # Message box that shows if the student was deleted succesfully
            msg=QMessageBox()
            msg.setWindowTitle("--- Delete a Student ---")
            msg.setText("ID-Number found in our dataset..")
            msg.setInformativeText("Student with an ID-Number: "+ID_number+" was deleted successfully")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            font=QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            msg.setFont(font)
            msg.exec()
            # Message box that shows if the student was not deleted succesfully                        
        else:
            msg=QMessageBox()
            msg.setWindowTitle("--- Delete a Student ---")
            msg.setText("ID-Number not found in our dataset..")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            font=QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            msg.setFont(font)
            msg.exec()
        
        self.model.clear()

        fileName = 'C:/Users/monti/A-CRUD/students.csv'
        
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):    
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)


########################  The Edit/Update operation is in the 2nd python file for the 2nd or EDIT window   ##############################
           
           
        

 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# The class for the Ui_EditWindow, the 2nd window
