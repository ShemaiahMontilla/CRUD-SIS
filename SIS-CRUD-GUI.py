# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableView
from EditWindow import  Ui_EditWindow
import csv


class Ui_MainWindow(object):
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
                        msg=QMessageBox()
                        msg.setWindowTitle("--- Edit Student ---")
                        msg.setText("ID-Number found in our database..")
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
        if index_student is None:
            msg=QMessageBox()
            msg.setWindowTitle("--- ---")
            msg.setText("ID-Number not found in our database..")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            msg.exec()  

                    
                        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 1000)
        MainWindow.setStyleSheet("background-color: rgb(251, 233, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(100, 400, 761, 361))
        self.tableView.setObjectName("tableView")
        #self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.labelSIS = QtWidgets.QLabel(self.centralwidget)
        self.labelSIS.setGeometry(QtCore.QRect(100, 30, 821, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(22)
        self.labelSIS.setFont(font)
        self.labelSIS.setStyleSheet("background-color: rgb(108, 255, 255);")
        self.labelSIS.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSIS.setObjectName("labelSIS")
        self.pushButtonSearch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearch.setGeometry(QtCore.QRect(30, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSearch.setFont(font)
        self.pushButtonSearch.setStyleSheet("background-color: rgb(192, 255, 213);")
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.pushButtonSearch.clicked.connect(self.search_student)
        
        self.lineEditSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSearch.setGeometry(QtCore.QRect(150, 120, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditSearch.setFont(font)
        self.lineEditSearch.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(48, 255, 249);")
        self.lineEditSearch.setText("")
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.labelName = QtWidgets.QLabel(self.centralwidget)
        self.labelName.setGeometry(QtCore.QRect(20, 180, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(16)
        self.labelName.setFont(font)
        self.labelName.setObjectName("labelName")
        self.labelidnumber = QtWidgets.QLabel(self.centralwidget)
        self.labelidnumber.setGeometry(QtCore.QRect(20, 240, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(16)
        self.labelidnumber.setFont(font)
        self.labelidnumber.setObjectName("labelidnumber")
        self.labelYearlevel = QtWidgets.QLabel(self.centralwidget)
        self.labelYearlevel.setGeometry(QtCore.QRect(20, 300, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(16)
        self.labelYearlevel.setFont(font)
        self.labelYearlevel.setObjectName("labelYearlevel")
        self.labelGender = QtWidgets.QLabel(self.centralwidget)
        self.labelGender.setGeometry(QtCore.QRect(620, 180, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(16)
        self.labelGender.setFont(font)
        self.labelGender.setObjectName("labelGender")
        self.labelCourse = QtWidgets.QLabel(self.centralwidget)
        self.labelCourse.setGeometry(QtCore.QRect(620, 250, 91, 41))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        font.setPointSize(16)
        self.labelCourse.setFont(font)
        self.labelCourse.setObjectName("labelCourse")
        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(160, 190, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEditName.setFont(font)
        self.lineEditName.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(170, 255, 255);")
        self.lineEditName.setText("")
        self.lineEditName.setObjectName("lineEditName")
        self.lineEditIdnumber = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditIdnumber.setGeometry(QtCore.QRect(160, 250, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEditIdnumber.setFont(font)
        self.lineEditIdnumber.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(170, 255, 255);")
        self.lineEditIdnumber.setText("")
        self.lineEditIdnumber.setObjectName("lineEditIdnumber")
        self.lineEditYearlevel = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditYearlevel.setGeometry(QtCore.QRect(160, 310, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEditYearlevel.setFont(font)
        self.lineEditYearlevel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(170, 255, 255);")
        self.lineEditYearlevel.setText("")
        self.lineEditYearlevel.setObjectName("lineEditYearlevel")
        self.lineEditCourse = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCourse.setGeometry(QtCore.QRect(710, 260, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEditCourse.setFont(font)
        self.lineEditCourse.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(170, 255, 255);")
        self.lineEditCourse.setText("")
        self.lineEditCourse.setObjectName("lineEditCourse")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(740, 190, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 340, 120, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(175, 255, 166);\n"
"border-color: rgb(0, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loadCsv)



        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.openEditWindow())
        self.pushButton_2.setGeometry(QtCore.QRect(20, 840, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(175, 255, 166);\n"
"border-color: rgb(0, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        

        self.lineEditEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditEdit.setGeometry(QtCore.QRect(192, 850, 281, 41 ))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditEdit.setFont(font)
        self.lineEditEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(48, 255, 249);")
        self.lineEditEdit.setText("")
        self.lineEditEdit.setObjectName("lineEditEdit")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(800, 320, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(175, 255, 166);\n"
"border-color: rgb(0, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.add_student)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(520, 840, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color: rgb(175, 255, 166);\n"
"border-color: rgb(0, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.delete_student)


        self.lineEditDelete = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDelete.setGeometry(QtCore.QRect(730, 850, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditDelete.setFont(font)
        self.lineEditDelete.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(48, 255, 249);")
        self.lineEditDelete.setText("")
        self.lineEditDelete.setObjectName("lineEditDelete")






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
        self.tableView.setModel(self.model)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelSIS.setText(_translate("MainWindow", "Simple Student Information System"))
        self.pushButtonSearch.setText(_translate("MainWindow", "Search"))
        self.lineEditSearch.setPlaceholderText(_translate("MainWindow", "Search by ID -Number"))
        self.labelName.setText(_translate("MainWindow", "Name:"))
        self.labelidnumber.setText(_translate("MainWindow", "ID Number:"))
        self.labelYearlevel.setText(_translate("MainWindow", "Year Level:"))
        self.labelGender.setText(_translate("MainWindow", "Gender:"))
        self.labelCourse.setText(_translate("MainWindow", "Course:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Female"))
        self.pushButton.setText(_translate("MainWindow", "Display All"))
        self.pushButton_2.setText(_translate("MainWindow", "Edit Student"))
        self.lineEditEdit.setPlaceholderText(_translate("MainWindow", "Enter student's id-number to update:"))
        self.pushButton_3.setText(_translate("MainWindow", "Add new student"))
        self.pushButton_4.setText(_translate("MainWindow", "Delete a student"))
        self.lineEditDelete.setPlaceholderText(_translate("MainWindow", "Enter student's id-number to delete:"))
        
    
    def loadCsv(self):
        fileName = 'C:/Users/monti/A-CRUD/students.csv'
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):    
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)
                
   
    def search_student(self):

        fileName = 'C:/Users/monti/A-CRUD/students.csv'
        
        id_number = self.lineEditSearch.text()
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput): 
                if len(row) > 0:
                        if id_number == row[0]:
                                msg=QMessageBox()
                                msg.setWindowTitle("--- Search Student ---")
                                msg.setText("ID-Number found in our database..")
                                msg.setInformativeText("ID-Number:  "+row[0]+"\n" "Name:  " +row[1]+ "\n""Course:  "+row[2]+"\n""Year-Leve:  "+row[3]+"\n""Gender:  "+row[4])
                                msg.setIcon(QMessageBox.Information)
                                msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                                msg.exec()
                                break
            else:
                msg=QMessageBox()
                msg.setWindowTitle("Confirm ation Message")
                msg.setText("ID-Number not found in our database..")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                msg.exec()
   
    def add_student(self):
        fileName = 'C:/Users/monti/A-CRUD/students.csv'
        name = self.lineEditName.text()
        idnumber = self.lineEditIdnumber.text()
        yearlevel = self.lineEditYearlevel.text()
        gender = self.comboBox.currentText()
        course = self.lineEditCourse.text()

        student_data = [idnumber,name,course,yearlevel,gender]

        with open(fileName, 'a+',
         encoding="utf-8") as fileInput:
                writer = csv.writer(fileInput)
                writer.writerows([student_data])

        msg=QMessageBox()
        msg.setWindowTitle("--- Add a Student ---")
        msg.setText("Data saved successfully")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        msg.exec()
        
        with open(fileName, "r") as fileInput:
            for row in csv.reader(fileInput):    
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                ]
                self.model.appendRow(items)
                
        return
 

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
            with open(fileName, "w", encoding="utf-8") as fileInput:
                writer = csv.writer(fileInput)
                writer.writerows(updated_data)
            msg=QMessageBox()
            msg.setWindowTitle("--- Delete a Student ---")
            msg.setText("ID-Number found in our database..")
            msg.setInformativeText("Stdent with an ID-Number: ", ID_number, "was deleted successfully")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            msg.exec()
                                
        else:
            msg=QMessageBox()
            msg.setWindowTitle("--- Delete a Student ---")
            msg.setText("ID-Number found in our database..")
            msg.setInformativeText("ID-Number not found in our database")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            msg.exec()
           
           
        

 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
