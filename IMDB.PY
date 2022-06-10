from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
from datetime import date
from db_connection2 import con,mycursor

from datetime import datetime

class Ui_MainWindow(object):
    #Function for the setupUI , setting of the UI buttons,Input widgets , table widgets and etc
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2000, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 1870, 1000))
        self.tabWidget.setStyleSheet(u"background-color: rgb(255, 252, 208);""font: 75 12pt \"MS Shell Dlg 2\";")

        

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")

        self.MovieIDlabel = QtWidgets.QLabel(self.tab)
        self.MovieIDlabel.setGeometry(QtCore.QRect(50, 40, 111, 31))
        self.MovieIDlabel.setAutoFillBackground(False)
        self.MovieIDlabel.setObjectName("MovieIDLabel")

        self.MovieIDlineEdit = QtWidgets.QLineEdit(self.tab)
        self.MovieIDlineEdit.setGeometry(QtCore.QRect(210, 30, 251, 51))
        self.MovieIDlineEdit.setInputMask("")
        self.MovieIDlineEdit.setText("")
        self.MovieIDlineEdit.setObjectName("MovieIDlineEdit")
        self.MovieIDlineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.MovieTitlelabel = QtWidgets.QLabel(self.tab)
        self.MovieTitlelabel.setGeometry(QtCore.QRect(50, 110, 111, 31))
        self.MovieTitlelabel.setAutoFillBackground(False)
        self.MovieTitlelabel.setObjectName("MovieTitleLabel")

        self.MovieTitlelineEdit = QtWidgets.QLineEdit(self.tab)
        self.MovieTitlelineEdit.setGeometry(QtCore.QRect(210, 100, 300, 51))
        self.MovieTitlelineEdit.setInputMask("")
        self.MovieTitlelineEdit.setText("")
        self.MovieTitlelineEdit.setObjectName("MovieTitlelineEdit")
        self.MovieTitlelineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.MovieDescriptionLabel = QtWidgets.QLabel(self.tab)
        self.MovieDescriptionLabel.setGeometry(QtCore.QRect(50, 180, 170, 31))
        self.MovieDescriptionLabel.setAutoFillBackground(False)
        self.MovieDescriptionLabel.setObjectName("MovieDescriptionLabel")

        self.MovieDescriptionlineEdit = QtWidgets.QTextEdit(self.tab)
        self.MovieDescriptionlineEdit.setGeometry(QtCore.QRect(240, 170, 500, 200))
        self.MovieDescriptionlineEdit.setText("")
        self.MovieDescriptionlineEdit.setObjectName("MovieDescriptionlineEdit")
        self.MovieDescriptionlineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.MovieYearLabel = QtWidgets.QLabel(self.tab)
        self.MovieYearLabel.setGeometry(QtCore.QRect(50, 400, 170, 31))
        self.MovieYearLabel.setAutoFillBackground(False)
        self.MovieYearLabel.setObjectName("MovieYearLabel")

        self.MovieYearLineEdit = QtWidgets.QLineEdit(self.tab)
        self.MovieYearLineEdit.setGeometry(QtCore.QRect(210, 400, 251, 51))
        self.MovieYearLineEdit.setText("")
        self.MovieYearLineEdit.setObjectName("MovieYearLineEdit")
        self.MovieYearLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.MovieRatingLabel = QtWidgets.QLabel(self.tab)
        self.MovieRatingLabel.setGeometry(QtCore.QRect(50, 470, 170, 31))
        self.MovieRatingLabel.setAutoFillBackground(False)
        self.MovieRatingLabel.setObjectName("MovieRatingLabel")

        self.MovieRatingComboBox = QtWidgets.QComboBox(self.tab)
        self.MovieRatingComboBox.setGeometry(QtCore.QRect(210, 470, 251, 51))
        self.MovieRatingComboBox.setEditable(True)
        self.MovieRatingComboBox.setObjectName("MovieRatingComboBox")
        self.MovieRatingComboBox.addItem("")
        self.MovieRatingComboBox.addItem("")
        self.MovieRatingComboBox.addItem("")
        self.MovieRatingComboBox.addItem("")
        self.MovieRatingComboBox.addItem("")
        self.MovieRatingComboBox.addItem("")
        self.MovieRatingComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.MovieimdbRatingLabel = QtWidgets.QLabel(self.tab)
        self.MovieimdbRatingLabel.setGeometry(QtCore.QRect(50, 540, 170, 31))
        self.MovieimdbRatingLabel.setAutoFillBackground(False)
        self.MovieimdbRatingLabel.setObjectName("MovieimdbRatingLabel")

        self.MovieimdbRatingLineEdit = QtWidgets.QLineEdit(self.tab)
        self.MovieimdbRatingLineEdit.setGeometry(QtCore.QRect(210, 540, 251, 51))
        self.MovieimdbRatingLineEdit.setText("")
        self.MovieimdbRatingLineEdit.setObjectName("MovieimdbRatingLineEdit")
        self.MovieimdbRatingLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.MovieRunTimeLabel = QtWidgets.QLabel(self.tab)
        self.MovieRunTimeLabel.setGeometry(QtCore.QRect(50, 610, 170, 31))
        self.MovieRunTimeLabel.setAutoFillBackground(False)
        self.MovieRunTimeLabel.setObjectName("MovieRunTimeLabel")
        

        self.MovieRunTimeLineEdit = QtWidgets.QLineEdit(self.tab)
        self.MovieRunTimeLineEdit.setGeometry(QtCore.QRect(210, 610, 251, 51))
        self.MovieRunTimeLineEdit.setText("")
        self.MovieRunTimeLineEdit.setObjectName("MovieRunTimeLineEdit")
        self.MovieRunTimeLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.MovieGrossLabel = QtWidgets.QLabel(self.tab)
        self.MovieGrossLabel.setGeometry(QtCore.QRect(50, 680, 170, 31))
        self.MovieGrossLabel.setAutoFillBackground(False)
        self.MovieGrossLabel.setObjectName("MovieGrossLabel")

        self.MovieGrossLineEdit = QtWidgets.QLineEdit(self.tab)
        self.MovieGrossLineEdit.setGeometry(QtCore.QRect(210, 680, 300, 51))
        self.MovieGrossLineEdit.setText("")
        self.MovieGrossLineEdit.setObjectName("MovieGrossLineEdit")
        self.MovieGrossLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.GenreAboutlabel = QtWidgets.QLabel(self.tab)
        self.GenreAboutlabel.setGeometry(QtCore.QRect(50, 750, 350, 31))
        self.GenreAboutlabel.setAutoFillBackground(False)
        self.GenreAboutlabel.setObjectName("GenreAboutlabel")

        self.GenreComboBox = QtWidgets.QComboBox(self.tab)
        self.GenreComboBox.setGeometry(QtCore.QRect(210, 750, 251, 51))
        self.GenreComboBox.setEditable(True)
        self.GenreComboBox.setObjectName("MovieRatingComboBox")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.addItem("")
        self.GenreComboBox.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.AddMovieButton = QtWidgets.QPushButton(self.tab)
        self.AddMovieButton.setGeometry(QtCore.QRect(210, 820, 200, 31))
        self.AddMovieButton.setObjectName("AddMovieButton")
        self.AddMovieButton.clicked.connect(self.InsertMovie)
        self.AddMovieButton.setStyleSheet(u"background-color: rgb(57, 255, 226);")
       


        self.MovieIDlabelActor = QtWidgets.QLabel(self.tab)
        self.MovieIDlabelActor.setGeometry(QtCore.QRect(850, 40, 350, 31))
        self.MovieIDlabelActor.setAutoFillBackground(False)
        self.MovieIDlabelActor.setObjectName("MovieIDLabelActor")
    

        self.MovieIDlineEditActor = QtWidgets.QLineEdit(self.tab)
        self.MovieIDlineEditActor.setGeometry(QtCore.QRect(1200, 30, 251, 51))
        self.MovieIDlineEditActor.setInputMask("")
        self.MovieIDlineEditActor.setText("")
        self.MovieIDlineEditActor.setObjectName("MovieIDlineEdit")
        self.MovieIDlineEditActor.setStyleSheet("background-color: rgb(255, 255, 255);") 

        self.ActorIDlabel = QtWidgets.QLabel(self.tab)
        self.ActorIDlabel.setGeometry(QtCore.QRect(1090, 110, 350, 31))
        self.ActorIDlabel.setAutoFillBackground(False)
        self.ActorIDlabel.setObjectName("ActorIDLabel")

        self.ActorIDlineEdit = QtWidgets.QLineEdit(self.tab)
        self.ActorIDlineEdit.setGeometry(QtCore.QRect(1200, 100, 251, 51))
        self.ActorIDlineEdit.setInputMask("")
        self.ActorIDlineEdit.setText("")
        self.ActorIDlineEdit.setObjectName("ActorIDlineEdit")
        self.ActorIDlineEdit.setStyleSheet("background-color: rgb(255, 255, 255);") 

        self.ActorNamelabel = QtWidgets.QLabel(self.tab)
        self.ActorNamelabel.setGeometry(QtCore.QRect(1070, 180, 350, 31))
        self.ActorNamelabel.setAutoFillBackground(False)
        self.ActorNamelabel.setObjectName("ActorNamelabel")

        self.ActorNamelineEdit = QtWidgets.QLineEdit(self.tab)
        self.ActorNamelineEdit.setGeometry(QtCore.QRect(1200, 180, 251, 51))
        self.ActorNamelineEdit.setInputMask("")
        self.ActorNamelineEdit.setText("")
        self.ActorNamelineEdit.setObjectName("ActorNamelineEdit")
        self.ActorNamelineEdit.setStyleSheet("background-color: rgb(255, 255, 255);") 

        self.ActorAboutlabel = QtWidgets.QLabel(self.tab)
        self.ActorAboutlabel.setGeometry(QtCore.QRect(1130, 250, 350, 31))
        self.ActorAboutlabel.setAutoFillBackground(False)
        self.ActorAboutlabel.setObjectName("ActorAboutlabel")

        self.ActorAboutlineEdit = QtWidgets.QTextEdit(self.tab)
        self.ActorAboutlineEdit.setGeometry(QtCore.QRect(1200, 250, 251, 51))
        self.ActorAboutlineEdit.setText("")
        self.ActorAboutlineEdit.setObjectName("ActorAboutlineEdit")
        self.ActorAboutlineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.CharPlayedlabel = QtWidgets.QLabel(self.tab)
        self.CharPlayedlabel.setGeometry(QtCore.QRect(1023, 320, 350, 31))
        self.CharPlayedlabel.setAutoFillBackground(False)
        self.CharPlayedlabel.setObjectName("CharPlayedlabel")

        self.CharPlayedlineEdit = QtWidgets.QTextEdit(self.tab)
        self.CharPlayedlineEdit.setGeometry(QtCore.QRect(1200, 320, 251, 51))
        self.CharPlayedlineEdit.setText("")
        self.CharPlayedlineEdit.setObjectName("CharPlayedlineEdit")
        self.CharPlayedlineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.AddActorButton = QtWidgets.QPushButton(self.tab)
        self.AddActorButton.setGeometry(QtCore.QRect(1200, 390, 200, 31))
        self.AddActorButton.setObjectName("AddActorButton")
        self.AddActorButton.clicked.connect(self.InsertActor)
        self.AddActorButton.setStyleSheet(u"background-color: rgb(57, 255, 226);")

        self.MovieIDlabelDirector = QtWidgets.QLabel(self.tab)
        self.MovieIDlabelDirector.setGeometry(QtCore.QRect(830, 460, 355, 31))
        self.MovieIDlabelDirector.setAutoFillBackground(False)
        self.MovieIDlabelDirector.setObjectName("MovieIDlabelDirector")
        
        self.MovieIDlineEditDirector = QtWidgets.QLineEdit(self.tab)
        self.MovieIDlineEditDirector.setGeometry(QtCore.QRect(1200, 460, 251, 51))
        self.MovieIDlineEditDirector.setInputMask("")
        self.MovieIDlineEditDirector.setText("")
        self.MovieIDlineEditDirector.setObjectName("MovieIDlineEditDirector") 
        self.MovieIDlineEditDirector.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.DirectorIDlabel = QtWidgets.QLabel(self.tab)
        self.DirectorIDlabel.setGeometry(QtCore.QRect(1070, 530, 350, 31))
        self.DirectorIDlabel.setAutoFillBackground(False)
        self.DirectorIDlabel.setObjectName("DirectorIDlabel")

        self.DirectorIDlineEdit = QtWidgets.QLineEdit(self.tab)
        self.DirectorIDlineEdit.setGeometry(QtCore.QRect(1200, 530, 251, 51))
        self.DirectorIDlineEdit.setInputMask("")
        self.DirectorIDlineEdit.setText("")
        self.DirectorIDlineEdit.setObjectName("DirectorIDlineEdit") 
        self.DirectorIDlineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.DirectorNamelabel = QtWidgets.QLabel(self.tab)
        self.DirectorNamelabel.setGeometry(QtCore.QRect(1050, 600, 350, 31))
        self.DirectorNamelabel.setAutoFillBackground(False)
        self.DirectorNamelabel.setObjectName("DirectorNamelabel")

        self.DirectorNamelineEdit = QtWidgets.QLineEdit(self.tab)
        self.DirectorNamelineEdit.setGeometry(QtCore.QRect(1200, 600, 251, 51))
        self.DirectorNamelineEdit.setInputMask("")
        self.DirectorNamelineEdit.setText("")
        self.DirectorNamelineEdit.setObjectName("DirectorNamelineEdit") 
        self.DirectorNamelineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.AddDirectorButoon = QtWidgets.QPushButton(self.tab)
        self.AddDirectorButoon.setGeometry(QtCore.QRect(1200, 670, 200, 31))
        self.AddDirectorButoon.setObjectName("AddDirectorButoon")
        self.AddDirectorButoon.clicked.connect(self.InsertDirector)
        self.AddDirectorButoon.setStyleSheet(u"background-color: rgb(57, 255, 226);")
        
        self.GenreMovieIDlabel = QtWidgets.QLabel(self.tab)
        self.GenreMovieIDlabel.setGeometry(QtCore.QRect(1020, 740, 350, 31))
        self.GenreMovieIDlabel.setAutoFillBackground(False)
        self.GenreMovieIDlabel.setObjectName("GenreMovieIDlabel")


        self.GenreMovieIDlineEdit = QtWidgets.QLineEdit(self.tab)
        self.GenreMovieIDlineEdit.setGeometry(QtCore.QRect(1200, 740, 350, 51))
        self.GenreMovieIDlineEdit.setInputMask("")
        self.GenreMovieIDlineEdit.setText("")
        self.GenreMovieIDlineEdit.setObjectName("DirectorNamelineEdit") 
        self.GenreMovieIDlineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")


        self.GenreAboutlabel2 = QtWidgets.QLabel(self.tab)
        self.GenreAboutlabel2.setGeometry(QtCore.QRect(1050, 820, 350, 31))
        self.GenreAboutlabel2.setAutoFillBackground(False)
        self.GenreAboutlabel2.setObjectName("GenreAboutlabel2")

        self.GenreComboBox2 = QtWidgets.QComboBox(self.tab)
        self.GenreComboBox2.setGeometry(QtCore.QRect(1200, 820, 251, 51))
        self.GenreComboBox2.setEditable(True)
        self.GenreComboBox2.setObjectName("MovieRatingComboBox2")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.addItem("")
        self.GenreComboBox2.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.AddGenreButoon=QtWidgets.QPushButton(self.tab)
        self.AddGenreButoon.setGeometry(QtCore.QRect(1200, 890, 200, 31))
        self.AddGenreButoon.setObjectName("AddDirectorButoon")
        self.AddGenreButoon.clicked.connect(self.InsertGenre)
        self.AddGenreButoon.setStyleSheet(u"background-color: rgb(57, 255, 226);")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.filteredit =QtWidgets.QLineEdit(self.tab_2)
        self.filteredit.setGeometry(QtCore.QRect(20, 25, 1830, 41))
        self.filteredit.textChanged.connect(self.filter)
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filteredit.setFont(font)          
        self.filteredit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border :2px solid ;\n"
        "border-radius:2px;\n"
        "border-color:black;\n")
       

        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 1830, 830))
        self.tableWidget.setStyleSheet("font: 13pt \"MS Shell Dlg 2\";")
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.DisplayMovieButoon = QtWidgets.QPushButton(self.tab_2)
        self.DisplayMovieButoon.setGeometry(QtCore.QRect(1650, 890, 200, 31))
        self.DisplayMovieButoon.setObjectName("DisplayMovieButoon")
        self.DisplayMovieButoon.clicked.connect(self.Tablefill)
        self.DisplayMovieButoon.setStyleSheet(u"background-color: rgb(57, 255, 226);")


        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.filteredit2 =QtWidgets.QLineEdit(self.tab_3)
        self.filteredit2.setGeometry(QtCore.QRect(20, 25, 1830, 41))
        self.filteredit2.textChanged.connect(self.filter2)
    
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filteredit2.setFont(font)          
        self.filteredit2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border :2px solid ;\n"
        "border-radius:2px;\n"
        "border-color:black;\n")
       

        self.tableWidget2 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget2.setGeometry(QtCore.QRect(20, 60, 1830, 830))
        self.tableWidget2.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.tableWidget2.setTabKeyNavigation(False)
        self.tableWidget2.setProperty("showDropIndicator", False)
        self.tableWidget2.setObjectName("tableWidget2")
        self.tableWidget2.setColumnCount(0)
        self.tableWidget2.setRowCount(0)
        self.tableWidget2.setStyleSheet("background-color: rgb(255, 255, 255);")
   


        self.DisplayActorButoon2 = QtWidgets.QPushButton(self.tab_3)
        self.DisplayActorButoon2.setGeometry(QtCore.QRect(1650, 890, 200, 31))
        self.DisplayActorButoon2.setObjectName("DisplayActorButoon")
        self.DisplayActorButoon2.clicked.connect(self.Tablefill2)
        self.DisplayActorButoon2.setStyleSheet(u"background-color: rgb(57, 255, 226);")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.filteredit3 =QtWidgets.QLineEdit(self.tab_4)
        self.filteredit3.setGeometry(QtCore.QRect(315, 25, 1200, 41))
        self.filteredit3.textChanged.connect(self.filter3)

    
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filteredit3.setFont(font)          
        self.filteredit3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border :2px solid ;\n"
        "border-radius:2px;\n"
        "border-color:black;\n")

        self.tableWidget3 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget3.setGeometry(QtCore.QRect(315, 60, 1200, 830))
        self.tableWidget3.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.tableWidget3.setTabKeyNavigation(False)
        self.tableWidget3.setProperty("showDropIndicator", False)
        self.tableWidget3.setObjectName("tableWidget3")
        self.tableWidget3.setColumnCount(0)
        self.tableWidget3.setRowCount(0)
        self.tableWidget3.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.DisplayDirectorButoon2 = QtWidgets.QPushButton(self.tab_4)
        self.DisplayDirectorButoon2.setGeometry(QtCore.QRect(1650, 890, 200, 31))
        self.DisplayDirectorButoon2.setObjectName("DisplayActorButoon2")
        self.DisplayDirectorButoon2.clicked.connect(self.Tablefill3)
        self.DisplayDirectorButoon2.setStyleSheet(u"background-color: rgb(57, 255, 226);")

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_5, "")

        self.filteredit4 =QtWidgets.QLineEdit(self.tab_5)
        self.filteredit4.setGeometry(QtCore.QRect(315, 25, 1200, 41))
        self.filteredit4.textChanged.connect(self.filter4)

    
        
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filteredit4.setFont(font)          
        self.filteredit4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border :2px solid ;\n"
        "border-radius:2px;\n"
        "border-color:black;\n")

        self.tableWidget4 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget4.setGeometry(QtCore.QRect(315, 60, 1200, 830))
        self.tableWidget4.setStyleSheet("font: 15pt \"MS Shell Dlg 2\";")
        self.tableWidget4.setTabKeyNavigation(False)
        self.tableWidget4.setProperty("showDropIndicator", False)
        self.tableWidget4.setObjectName("tableWidget4")
        self.tableWidget4.setColumnCount(0)
        self.tableWidget4.setRowCount(0)
        self.tableWidget4.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.DisplayGenreButoon2 = QtWidgets.QPushButton(self.tab_5)
        self.DisplayGenreButoon2.setGeometry(QtCore.QRect(1650, 890, 200, 31))
        self.DisplayGenreButoon2.setObjectName("DisplayGenreButoon2")
        self.DisplayGenreButoon2.clicked.connect(self.Tablefill4)
        self.DisplayGenreButoon2.setStyleSheet(u"background-color: rgb(57, 255, 226);")


        
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "ADD A MOVIE"))
        
        self.MovieIDlabel.setText(_translate("MainWindow", "Movie ID:"))
        self.MovieIDlineEdit.setPlaceholderText(_translate("MainWindow", "Add The Movie ID"))
       
        self.MovieTitlelabel.setText(_translate("MainWindow", "Movie Title:"))
        self.MovieTitlelineEdit.setPlaceholderText(_translate("MainWindow", "Movie Title"))
        
        self.MovieDescriptionLabel.setText(_translate("MainWindow", "Movie Description"))
        self.MovieDescriptionlineEdit.setPlaceholderText(_translate("MainWindow", "Movie Description"))
        
        self.MovieYearLabel.setText(_translate("MainWindow", "Year Released:"))
        self.MovieYearLineEdit.setPlaceholderText(_translate("MainWindow", "Year Released"))
        
        self.MovieRatingLabel.setText(_translate("MainWindow", "Movie Rating:"))
        self.MovieRatingComboBox.setItemText(0, _translate("MainWindow", "G"))
        self.MovieRatingComboBox.setItemText(1, _translate("MainWindow", "PG"))
        self.MovieRatingComboBox.setItemText(2, _translate("MainWindow", "PG-13"))
        self.MovieRatingComboBox.setItemText(3, _translate("MainWindow", "R"))
        self.MovieRatingComboBox.setItemText(4, _translate("MainWindow", "NC-17"))
        self.MovieRatingComboBox.setItemText(5, _translate("MainWindow", "Not Rated"))
        
        self.MovieimdbRatingLabel.setText(_translate("MainWindow", "IMDB Rating:"))
        self.MovieimdbRatingLineEdit.setPlaceholderText(_translate("MainWindow", "IMDB Rating"))

        self.MovieRunTimeLabel.setText(_translate("MainWindow", "Runtime:"))
        self.MovieRunTimeLineEdit.setPlaceholderText(_translate("MainWindow", "Runtime"))

        self.MovieGrossLabel.setText(_translate("MainWindow", "Gross:"))
        self.MovieGrossLineEdit.setPlaceholderText(_translate("MainWindow", "Gross"))

        self.GenreAboutlabel.setText(_translate("MainWindow", "Genre:"))
        self.GenreComboBox.setItemText(0, _translate("MainWindow", "Action"))
        self.GenreComboBox.setItemText(1, _translate("MainWindow", "Adventure"))
        self.GenreComboBox.setItemText(2, _translate("MainWindow", "Animation"))
        self.GenreComboBox.setItemText(3, _translate("MainWindow", "Biography"))
        self.GenreComboBox.setItemText(4, _translate("MainWindow", "Comedy"))
        self.GenreComboBox.setItemText(5, _translate("MainWindow", "Crime"))
        self.GenreComboBox.setItemText(6, _translate("MainWindow", "Documentary"))
        self.GenreComboBox.setItemText(7, _translate("MainWindow", "Drama"))
        self.GenreComboBox.setItemText(8, _translate("MainWindow", "Family"))
        self.GenreComboBox.setItemText(9, _translate("MainWindow", "Fantasy"))
        self.GenreComboBox.setItemText(10, _translate("MainWindow", "Film Noir"))
        self.GenreComboBox.setItemText(11, _translate("MainWindow", "History"))
        self.GenreComboBox.setItemText(12,_translate("MainWindow", "Horror"))
        self.GenreComboBox.setItemText(13, _translate("MainWindow", "Music"))
        self.GenreComboBox.setItemText(14, _translate("MainWindow", "Musical"))
        self.GenreComboBox.setItemText(15, _translate("MainWindow", "Mystery"))
        self.GenreComboBox.setItemText(16,_translate("MainWindow", "Romance"))
        self.GenreComboBox.setItemText(17, _translate("MainWindow", "Sci-Fi"))
        self.GenreComboBox.setItemText(18, _translate("MainWindow", "Short Film"))
        self.GenreComboBox.setItemText(19,_translate("MainWindow", "Sport"))
        self.GenreComboBox.setItemText(20, _translate("MainWindow", "Superhero"))
        self.GenreComboBox.setItemText(21, _translate("MainWindow", "Thriller"))
        self.GenreComboBox.setItemText(22, _translate("MainWindow", "War"))
        self.GenreComboBox.setItemText(23,_translate("MainWindow", "Western"))

        self.AddMovieButton.setText(_translate("MainWindow", "Add a Movie"))

        self.MovieIDlabelActor.setText(_translate("MainWindow", "Movie ID in which the Actor Starred:"))
        self.MovieIDlineEditActor.setPlaceholderText(_translate("MainWindow", "Movie ID"))

        self.ActorIDlabel.setText(_translate("MainWindow", "Actor'S ID:"))
        self.ActorIDlineEdit.setPlaceholderText(_translate("MainWindow", "Actor's ID"))

        self.ActorNamelabel.setText(_translate("MainWindow", "Actor's Name:"))
        self.ActorNamelineEdit.setPlaceholderText(_translate("MainWindow", "Actor's Name"))

        self.ActorAboutlabel.setText(_translate("MainWindow", "About:"))
        self.ActorAboutlineEdit.setPlaceholderText(_translate("MainWindow", "About"))



        self.CharPlayedlabel.setText(_translate("MainWindow", " Character Played:"))
        self.CharPlayedlineEdit.setPlaceholderText(_translate("MainWindow", " Character Played"))
        self.AddActorButton.setText(_translate("MainWindow", "Add an Actor"))

        self.MovieIDlabelDirector.setText(_translate("MainWindow", "Movie ID in which the Director Directed:"))
        self.MovieIDlineEditDirector.setPlaceholderText(_translate("MainWindow", "Movie ID"))

        self.DirectorIDlabel.setText(_translate("MainWindow", "Director's ID:"))
        self.DirectorIDlineEdit.setPlaceholderText(_translate("MainWindow", "Director's ID"))

        self.DirectorNamelabel.setText(_translate("MainWindow", "Director's Name:"))
        self.DirectorNamelineEdit.setPlaceholderText(_translate("MainWindow", "Director's Name"))


        self.AddDirectorButoon.setText(_translate("MainWindow", "Add a Director "))

        self.GenreMovieIDlabel.setText(_translate("MainWindow", "Genre's Movie ID:"))
        self.GenreMovieIDlineEdit.setPlaceholderText(_translate("MainWindow", "Add a Genre to an already Existing ID"))

        self.GenreAboutlabel2.setText(_translate("MainWindow", "Genre:"))
        self.GenreComboBox2.setItemText(0, _translate("MainWindow", "Action"))
        self.GenreComboBox2.setItemText(1, _translate("MainWindow", "Adventure"))
        self.GenreComboBox2.setItemText(2, _translate("MainWindow", "Animation"))
        self.GenreComboBox2.setItemText(3, _translate("MainWindow", "Biography"))
        self.GenreComboBox2.setItemText(4, _translate("MainWindow", "Comedy"))
        self.GenreComboBox2.setItemText(5, _translate("MainWindow", "Crime"))
        self.GenreComboBox2.setItemText(6, _translate("MainWindow", "Documentary"))
        self.GenreComboBox2.setItemText(7, _translate("MainWindow", "Drama"))
        self.GenreComboBox2.setItemText(8, _translate("MainWindow", "Family"))
        self.GenreComboBox2.setItemText(9, _translate("MainWindow", "Fantasy"))
        self.GenreComboBox2.setItemText(10, _translate("MainWindow", "Film Noir"))
        self.GenreComboBox2.setItemText(11, _translate("MainWindow", "History"))
        self.GenreComboBox2.setItemText(12,_translate("MainWindow", "Horror"))
        self.GenreComboBox2.setItemText(13, _translate("MainWindow", "Music"))
        self.GenreComboBox2.setItemText(14, _translate("MainWindow", "Musical"))
        self.GenreComboBox2.setItemText(15, _translate("MainWindow", "Mystery"))
        self.GenreComboBox2.setItemText(16,_translate("MainWindow", "Romance"))
        self.GenreComboBox2.setItemText(17, _translate("MainWindow", "Sci-Fi"))
        self.GenreComboBox2.setItemText(18, _translate("MainWindow", "Short Film"))
        self.GenreComboBox2.setItemText(19,_translate("MainWindow", "Sport"))
        self.GenreComboBox2.setItemText(20, _translate("MainWindow", "Superhero"))
        self.GenreComboBox2.setItemText(21, _translate("MainWindow", "Thriller"))
        self.GenreComboBox2.setItemText(22, _translate("MainWindow", "War"))
        self.GenreComboBox2.setItemText(23,_translate("MainWindow", "Western"))

        self.AddGenreButoon.setText(_translate("MainWindow", "Add a Genre "))


  




        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "View Movies Details"))
        self.filteredit.setPlaceholderText(_translate("MainWindow", "Search by Movie Title"))
        self.DisplayMovieButoon.setText(_translate("MainWindow", "Display "))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "View Actors Details"))
        self.filteredit2.setPlaceholderText(_translate("MainWindow", "Search by Movie Title"))
        self.DisplayActorButoon2.setText(_translate("MainWindow", "Display "))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "View Directors Details"))
        self.filteredit3.setPlaceholderText(_translate("MainWindow", "Search by Movie Title"))
        self.DisplayDirectorButoon2.setText(_translate("MainWindow", "Display "))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "View Movie Genres"))
        self.filteredit4.setPlaceholderText(_translate("MainWindow", "Search by Movie Title"))
        self.DisplayGenreButoon2.setText(_translate("MainWindow", "Display "))




#Function for filling up / Displaying the table widget  for the table Students_info from the database   

    def Tablefill(self):
        self.tableWidget.setColumnCount(0)
        sql = ("SELECT * FROM Movie")
        mycursor.execute(sql)
        all_data = mycursor.fetchall()
        self.tableWidget.setRowCount(len(all_data[1]))
        self.tableWidget.setColumnCount(len(all_data[0]))
        self.tableWidget.setColumnWidth(0,130)
        self.tableWidget.setColumnWidth(1,300)
        self.tableWidget.setColumnWidth(2,680)
        self.tableWidget.setColumnWidth(3,80)
        self.tableWidget.setColumnWidth(4,150)
        self.tableWidget.setColumnWidth(5,150)
        self.tableWidget.setColumnWidth(6,150)
        self.tableWidget.setColumnWidth(7,150)
       
        self.tableWidget.setHorizontalHeaderLabels(['Movie ID', 'Title', 'Description', 'Year', 'IMDB Rating', 'Runtime', 'Movie Rating', 'Gross'])
        for row in range(1):
            for column in range(0):
                item = QTableWidgetItem(all_data[row][column])
                self.tableWidget.setItem(row, column, item)

        for Row,allval in enumerate(all_data):
            for Column,value in enumerate(allval):
                self.tableWidget.setItem(Row,Column, QTableWidgetItem(str(value)))
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            
            for row in range(self.tableWidget.rowCount()):
                self.tableWidget.setRowHeight(row, 100)

#Function for the search field of the table students_info
    def filter(self, filter_text):
        for i in range(self.tableWidget.rowCount()):
            for j in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(i, j)
                if item is not None:
                    match = filter_text.lower() not in item.text().lower()
                    self.tableWidget.setRowHidden(i, match)
                    if not match:
                        break

    def Tablefill2(self):
        self.tableWidget2.setColumnCount(0)
        sql = ("SELECT Movie.title, Actor.name, Acts.CharacterPlayed, Actor.ActorID FROM Movie, Actor, Acts WHERE Movie.MovieID = Acts.MovieID AND Acts.ActorID = Actor.ActorID   ")
        mycursor.execute(sql)
        all_data = mycursor.fetchall()
        self.tableWidget2.setRowCount(len(all_data[1]))
        self.tableWidget2.setColumnCount(len(all_data[0]))
        self.tableWidget2.setColumnWidth(0,600)
        self.tableWidget2.setColumnWidth(1,600)
        self.tableWidget2.setColumnWidth(2,530)
        self.tableWidget2.setColumnWidth(3,150)

 
        self.tableWidget2.setHorizontalHeaderLabels(['Movie Title', "Actor's Name", 'Character Played', "Actor's ID"])
        for row in range(1):
            for column in range(0):
                item = QTableWidgetItem(all_data[row][column])
                self.tableWidget2.setItem(row, column, item)

        for Row,allval in enumerate(all_data):
            for Column,value in enumerate(allval):
                self.tableWidget2.setItem(Row,Column, QTableWidgetItem(str(value)))
            row_position = self.tableWidget2.rowCount()
            self.tableWidget2.insertRow(row_position)
            
            for row in range(self.tableWidget2.rowCount()):
                self.tableWidget2.setRowHeight(row, 100)

#Function for the search field of the table students_info
    def filter2(self, filter_text):
        for i in range(self.tableWidget2.rowCount()):
            for j in range(self.tableWidget2.columnCount()):
                item = self.tableWidget2.item(i, j)
                if item is not None:
                    match = filter_text.lower() not in item.text().lower()
                    self.tableWidget2.setRowHidden(i, match)
                    if not match:
                        break

    def Tablefill3(self):
        self.tableWidget3.setColumnCount(0)
        sql = ("SELECT Directs.MovieID, Movie.title, Directors.Name, Directors.DirectorID  FROM Directs, Movie, Directors WHERE Movie.MovieID = Directs.MovieID AND Directs.DirectorID = Directors.DirectorID   ")
        mycursor.execute(sql)
        all_data = mycursor.fetchall()
        self.tableWidget3.setRowCount(len(all_data[1]))
        self.tableWidget3.setColumnCount(len(all_data[0]))
        self.tableWidget3.setColumnWidth(0,200)
        self.tableWidget3.setColumnWidth(1,550)
        self.tableWidget3.setColumnWidth(2,200)
        self.tableWidget3.setColumnWidth(3,200)
  
 
        self.tableWidget3.setHorizontalHeaderLabels(['Movie ID', 'Movie Title', "Director's Name", "Director's ID"])
        for row in range(1):
            for column in range(0):
                item = QTableWidgetItem(all_data[row][column])
                self.tableWidget3.setItem(row, column, item)

        for Row,allval in enumerate(all_data):
            for Column,value in enumerate(allval):
                self.tableWidget3.setItem(Row,Column, QTableWidgetItem(str(value)))
            row_position = self.tableWidget3.rowCount()
            self.tableWidget3.insertRow(row_position)
            
            for row in range(self.tableWidget3.rowCount()):
                self.tableWidget3.setRowHeight(row, 100)

#Function for the search field of the table students_info
    def filter3(self, filter_text):
        for i in range(self.tableWidget3.rowCount()):
            for j in range(self.tableWidget3.columnCount()):
                item = self.tableWidget3.item(i, j)
                if item is not None:
                    match = filter_text.lower() not in item.text().lower()
                    self.tableWidget3.setRowHidden(i, match)
                    if not match:
                        break

    def Tablefill4(self):
        self.tableWidget4.setColumnCount(0)
        sql = ("SELECT Movie.title, Genre.name FROM Movie JOIN Genre ON Movie.MovieID = Genre.MovieiD")
        mycursor.execute(sql)
        all_data = mycursor.fetchall()
        self.tableWidget4.setRowCount(len(all_data[1]))
        self.tableWidget4.setColumnCount(len(all_data[0]))
        self.tableWidget4.setColumnWidth(0,900)
        self.tableWidget4.setColumnWidth(1,300)

       
        self.tableWidget4.setHorizontalHeaderLabels(['Movie Title', 'Genre'])
        for row in range(1):
            for column in range(0):
                item = QTableWidgetItem(all_data[row][column])
                self.tableWidget4.setItem(row, column, item)

        for Row,allval in enumerate(all_data):
            for Column,value in enumerate(allval):
                self.tableWidget4.setItem(Row,Column, QTableWidgetItem(str(value)))
            row_position = self.tableWidget4.rowCount()
            self.tableWidget4.insertRow(row_position)
            
            for row in range(self.tableWidget.rowCount()):
                self.tableWidget4.setRowHeight(row, 100)

    def filter4(self, filter_text):
        for i in range(self.tableWidget4.rowCount()):
            for j in range(self.tableWidget4.columnCount()):
                item = self.tableWidget4.item(i, j)
                if item is not None:
                    match = filter_text.lower() not in item.text().lower()
                    self.tableWidget4.setRowHidden(i, match)
                    if not match:
                        break

    def InsertMovie(self):
       
        MovieID = self.MovieIDlineEdit.text()
        Title = self.MovieTitlelineEdit.text()
        Description = self.MovieDescriptionlineEdit.toPlainText() 
        Year =  self.MovieYearLineEdit.text() 
        imdbRating =self.MovieimdbRatingLineEdit.text()  
        runtime =self.MovieRunTimeLineEdit.text() 
        MovieRating=self.MovieRatingComboBox.currentText()
        gross= self.MovieGrossLineEdit.text() 
        genre = self.GenreComboBox.currentText()


        sql = ("INSERT INTO Movie (MovieID, title, description, year, imdb_rating, runtime, Movie_rating, gross)"
 					"VALUES (%s,%s,%s,%s,%s,%s,%s,%s)")

        value = [MovieID, Title, Description,Year, imdbRating, runtime, MovieRating, gross]
        mycursor.execute(sql, value)
        con.commit()

        sql = ("INSERT INTO Genre (name, MovieID)"
 					"VALUES (%s,%s)")

        value = [genre, MovieID]
        mycursor.execute(sql, value)
        con.commit()



        self.Tablefill()
        self.Tablefill4()
        msg=QMessageBox()
        msg.setWindowTitle("--- Add a Movie ---")
        msg.setText("                        ")
        msg.setInformativeText("Succesfully Added a Movie")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        font=QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        msg.setFont(font)
        msg.exec()

    def InsertActor(self):
       
        MovieID1 = self.MovieIDlineEditActor.text()
        ActorID1 = self.ActorIDlineEdit.text()
        CharacterPlayed1 = self.CharPlayedlineEdit.toPlainText()
        name1 =self.ActorNamelineEdit.text()
        about1=self.ActorAboutlineEdit.toPlainText()
        


        sql = ("INSERT INTO Actor (ActorID, name, about)"
 					"VALUES (%s,%s,%s)")
        


        value = [ActorID1, name1, about1]
        mycursor.execute(sql, value)
        con.commit()

        sql = ("INSERT INTO Acts (MovieID, ActorID, CharacterPlayed)"
 					"VALUES (%s,%s,%s)")
        


        value = [MovieID1, ActorID1, CharacterPlayed1]
        mycursor.execute(sql, value)
        con.commit()


        self.Tablefill2()
        msg=QMessageBox()
        msg.setWindowTitle("--- Add a Actor ---")
        msg.setText("                        ")
        msg.setInformativeText("Succesfully Added an Actor")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        font=QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        msg.setFont(font)
        msg.exec()

    def InsertDirector(self):
       
        MovieID = self.MovieIDlineEditDirector.text()
        DirectorID = self.DirectorIDlineEdit.text()
        Name =self.DirectorNamelineEdit.text()
    
        


        sql = ("INSERT INTO Directors (DirectorID, Name)"
 					"VALUES (%s,%s)")

        value = [DirectorID, Name]
        mycursor.execute(sql, value)
        con.commit()
        
        sql=("INSERT INTO Directs (MovieID, DirectorID)"
 					"VALUES (%s,%s)")
        value = [MovieID, DirectorID]
        mycursor.execute(sql, value)
        con.commit()

        self.Tablefill3()
        msg=QMessageBox()
        msg.setWindowTitle("--- Add a Director ---")
        msg.setText("                        ")
        msg.setInformativeText("Succesfully Added a Director")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        font=QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        msg.setFont(font)
        msg.exec()

    def InsertGenre(self):
           
        name2 = self.GenreComboBox2.currentText()
        MovieID2 = self.GenreMovieIDlineEdit.text()
        


        sql = ("INSERT INTO Genre ( name, MovieID)"
 					"VALUES (%s,%s)")
        


        value = [name2, MovieID2]
        mycursor.execute(sql, value)
        con.commit()
        self.Tablefill4()
        msg=QMessageBox()
        msg.setWindowTitle("--- Add a Genre ---")
        msg.setText("                        ")
        msg.setInformativeText("Succesfully Added a Genre")
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