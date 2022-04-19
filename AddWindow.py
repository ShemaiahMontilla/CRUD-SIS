from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import csv

# The class for the Ui_AddWindow, the 2nd window
class Ui_AddWindow(object):
#Function for the setupUI , setting of the UI buttons,Input widgets , and etc
    def setupUi(self, AddWindow):
        AddWindow.setObjectName("AddWindow")
        AddWindow.resize(640, 480)
        AddWindow.setStyleSheet("background-color: rgb(255, 238, 228);\n"
"border-color: rgb(39, 24, 255);")


        self.centralwidget = QtWidgets.QWidget(AddWindow)
        self.centralwidget.setObjectName("centralwidget")




        self.labelName = QtWidgets.QLabel(self.centralwidget)
        self.labelName.setGeometry(QtCore.QRect(10, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelName.setFont(font)
        self.labelName.setObjectName("labelName")

        
        self.labelID_Number = QtWidgets.QLabel(self.centralwidget)
        self.labelID_Number.setGeometry(QtCore.QRect(10, 30, 190, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.labelID_Number.setFont(font)
        self.labelID_Number.setObjectName("labelID_Number")

        self.labelCourse = QtWidgets.QLabel(self.centralwidget)
        self.labelCourse.setGeometry(QtCore.QRect(10, 110, 75, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelCourse.setFont(font)
        self.labelCourse.setObjectName("labelCourse")

        self.labelYearLevel = QtWidgets.QLabel(self.centralwidget)
        self.labelYearLevel.setGeometry(QtCore.QRect(10, 150, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelYearLevel.setFont(font)
        self.labelYearLevel.setObjectName("labelYearLevel")

        self.labelGender = QtWidgets.QLabel(self.centralwidget)
        self.labelGender.setGeometry(QtCore.QRect(10, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelGender.setFont(font)
        self.labelGender.setObjectName("labelGender")

        self.pushButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAdd.setGeometry(QtCore.QRect(180, 300, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAdd.setFont(font)
        self.pushButtonAdd.setStyleSheet("background-color: rgb(170, 170, 255);\n""color:white;\n"
        "border-style:outset;\n"
        "brorder-width:2px;\n"
        "border-radius:10px;\n"
        "border-color:black;\n"
        "padding:6px")
        "border-color: rgb(73, 76, 255);"

        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonAdd.clicked.connect(self.add_student)

        




        
        self.lineEditName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditName.setGeometry(QtCore.QRect(180, 70, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEditName.setFont(font)
        self.lineEditName.setStyleSheet("background-color: rgb(229, 255, 252);\n"
        "border :2px solid ;\n"
        "border-radius:2px;\n"
        "border-color:black;\n")
        self.lineEditName.setObjectName("lineEditName")

        self.lineEditIDNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditIDNumber.setGeometry(QtCore.QRect(180, 30, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEditIDNumber.setFont(font)
        self.lineEditIDNumber.setStyleSheet("background-color: rgb(229, 255, 252);\n"
        "border :2px solid ;\n"
        "border-radius:2px;\n"
        "border-color:black;\n")
        self.lineEditIDNumber.setObjectName("lineEditIDNumber")

        self.lineEditCourse = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCourse.setGeometry(QtCore.QRect(180, 110, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEditCourse.setFont(font)
        self.lineEditCourse.setStyleSheet("background-color: rgb(229, 255, 252);\n"
        "border :2px solid ;\n"
        "border-radius:2px;\n"
        "border-color:black;\n")
        self.lineEditCourse .setObjectName("lineEditCourse")



        self.comboBoxYearLevel = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxYearLevel.setGeometry(QtCore.QRect(180, 150, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.comboBoxYearLevel.setFont(font)
        self.comboBoxYearLevel.setStyleSheet("background-color: rgb(229, 255, 252);\n"
        "border :2px solid ;\n"
        "border-radius:2px;\n"
        "border-color:black;\n")
        self.comboBoxYearLevel.setObjectName("comboBoxYearLevel")
        self.comboBoxYearLevel.addItem("")
        self.comboBoxYearLevel.addItem("")
        self.comboBoxYearLevel.addItem("")
        self.comboBoxYearLevel.addItem("")


        self.comboBoxGender = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxGender.setGeometry(QtCore.QRect(180, 190, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxGender.setFont(font)
        self.comboBoxGender.setStyleSheet("background-color: rgb(229, 255, 252);\n"
        "border :2px solid ;\n"
        "border-radius:2px;\n"
        "border-color:black;\n")
        self.comboBoxGender.setObjectName("comboBoxGender")
        self.comboBoxGender.addItem("")
        self.comboBoxGender.addItem("")

        AddWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AddWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        AddWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AddWindow)
        self.statusbar.setObjectName("statusbar")
        AddWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddWindow)
        QtCore.QMetaObject.connectSlotsByName(AddWindow)


#Function for retanslateUI, it set the text for the button, input widgets and etc
    def retranslateUi(self, AddWindow):
        _translate = QtCore.QCoreApplication.translate
        AddWindow.setWindowTitle(_translate("AddWindow", "Add Window"))
        self.labelName.setText(_translate("AddWindow", "Name:"))
        self.labelID_Number.setText(_translate("AddWindow", "ID Number:"))

        self.labelCourse.setText(_translate("AddWindow", "Course:"))
        self.labelYearLevel.setText(_translate("AddWindow", "Year Level:"))
        self.labelGender.setText(_translate("AddWindow", "Gender:"))
        self.pushButtonAdd.setText(_translate("AddWindow", "Add"))

        self.comboBoxYearLevel.setItemText(0, _translate("AddWindow", "1st Year"))
        self.comboBoxYearLevel.setItemText(1, _translate("AddWindow", "2nd Year"))
        self.comboBoxYearLevel.setItemText(2, _translate("AddWindow", "3rd Year"))
        self.comboBoxYearLevel.setItemText(3, _translate("AddWindow", "4th Year"))

        self.comboBoxGender.setItemText(0, _translate("AddWindow", "Male"))
        self.comboBoxGender.setItemText(1, _translate("AddWindow", "Female"))

        
 
#Function that add a student
    def add_student(self):
        fileName = 'C:/Users/monti/A-CRUD/students.csv'
        name = self.lineEditName.text()
        idnumber = self.lineEditIDNumber.text()
        yearlevel = self.comboBoxYearLevel.currentText()
        gender = self.comboBoxGender.currentText()
        course = self.lineEditCourse.text()

        student_data = [idnumber,name,course,yearlevel,gender]

        with open(fileName, 'a+',
         encoding="utf-8",newline="") as fileInput:
                writer = csv.writer(fileInput)
                writer.writerows([student_data])
        
        msg=QMessageBox()
        msg.setWindowTitle("--- Add a Student ---")
        msg.setText("Data saved successfully")
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
    AddWindow = QtWidgets.QMainWindow()
    ui = Ui_AddWindow()
    ui.setupUi(AddWindow)
    AddWindow.show()
    sys.exit(app.exec_())