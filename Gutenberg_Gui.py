#!/usr/bin/python3.6
import sys
from PyQt5.QtWidgets import QApplication, QCheckBox, QComboBox, QWidget, QMainWindow, QLabel, QPushButton, QAction, QLineEdit, QMessageBox, QProgressBar, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt
from search import search

class Gutenberg(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Gutenberg'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 300 

        #Make Logo
        self.setWindowIcon(QIcon('Gutenberg.ico'))
        
        self.UI()
        
    def UI(self):
    
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Make Title
        title = QLabel('Gutenberg', self)
        title.move(260, 0)

        #Make the variables for menu
        makeblist = QAction('blacklist', self)
        makeblist.setStatusTip('Make/Edit blacklist.txt')
        makeblist.triggered.connect(self.makeblacklist)
        
        make_extension = QAction('extensions', self)
        make_extension.setStatusTip('Make/Edit extensions.txt')
        make_extension.triggered.connect(self.makeextension) 
        
        make_pattern = QAction('search patterns', self)
        make_pattern.setStatusTip('Make/Edit search_patterns.txt')
        make_pattern.triggered.connect(self.makepattern)

        
        #Make the Menu
        menubar = self.menuBar()
        filemenu = menubar.addMenu('File')
        filemenu.addAction(makeblist)
        filemenu.addAction(make_extension)
        filemenu.addAction(make_pattern)

        #Create Query Box
        self.textbox = QLineEdit(self)
        self.textbox.move(100, 150)
        self.textbox.resize(150, 20)
        self.textbox.setPlaceholderText('query')

        #Create txt file
        self.txt = QLineEdit(self)
        self.txt.resize(150, 20)
        self.txt.move(330, 150)
        self.txt.setPlaceholderText('txt file name')

        #Create extensions dropdown button
        extensions = QComboBox(self)
        extensions.move(255, 150)
        extensions.resize(70, 20)
        extensions.addItem('file extensions') #The default is no specified filetype
        try:
            extension_list = open('extensions.txt', 'r')
            for i in extension_list:
                i = i.replace('\n', '')
                if i != 'file extensions':
                    extensions.addItem(i)
        except FileNotFoundError:
            extension_list = open('extensions.txt', 'w+')
            extension_list.close()


        #Create search pattern dropdown button
        search_pattern = QComboBox(self)
        search_pattern.setGeometry(25, 150, 70, 20)
        search_pattern.addItem('search patterns')#The default is no specified search pattern
        try:
            search_pattern_list = open('search_pattern.txt', 'r')
            for i in search_pattern_list:
                i = i.replace('\n', '')
                if i != 'search patterns':
                    search_pattern.addItem(i)
        except FileNotFoundError:
            search_pattern_list = open('search_pattern.txt', 'w+')
            search_pattern_list.close()

        search_pattern.activated[str].connect(self.pattern)

        #Make Progress Bar
        self.progress = QProgressBar(self)
        self.progress.setGeometry(255 ,175, 225, 20)
        
        
        #Default Filetype is none
        self.file_type = ''
        
        #Default Search Pattern is none
        self.s_pattern = ''

        #When the file extension is chosen
        extensions.activated[str].connect(self.file_extension)


        #create search button
        self.button = QPushButton('Search', self)
        self.button.move(138, 175) 
        self.button.resize(70, 20)

        #connect button to search function
        self.button.clicked.connect(self.query)

        #create blacklist checkbox
        self.enable_blacklist = False
        self.blacklist = QCheckBox('blacklist', self)
        self.blacklist.stateChanged.connect(self.use_blacklist)
        self.blacklist.move(485, 145)
               
        self.show()


    def query(self):
        text_file = self.txt.text()+'.txt'
        self.urls = open(text_file, 'w+')
        self.progress.setValue(0)
        for i in search(self.textbox.text(), self.file_type, self.enable_blacklist, self.s_pattern):
            self.urls.write(i+'\n')
        self.urls.close()
        self.progress.setValue(100)
        self.enable_blacklist = False
        self.edit = Edit(text_file)
        self.edit.show()

    def file_extension(self, ftype):
        self.file_type = ftype        

    def pattern(self, spattern):
        self.s_pattern = spattern

    def use_blacklist(self, state):
        if state == Qt.Checked:
            self.enable_blacklist = True
        else:
            self.enable_blacklist = False

    def makepattern(self):
        self.edit = Edit('search_pattern.txt')
        self.edit.show()

    def makeextension(self):
        self.edit = Edit('extensions.txt')
        self.edit.show()

    def makeblacklist(self):
        self.edit = Edit('blacklist.txt')
        self.edit.show()

class Edit(QMainWindow):
    def __init__(self, name):
        super().__init__()
        self.title = 'Edit'
        self.left = 620
        self.top = 10
        self.height = 150
        self.width = 300

        self.UI2(name)

    def UI2(self, name):
        #Make dimensions of secondary window
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #Make the editor to display/edit txt files
        self.editBox = QTextEdit()
        self.setCentralWidget(self.editBox)
        
        try:            
            file_to_edit = open(name, 'r')
            self.editBox.setText(file_to_edit.read())
        except FileNotFoundError:
            file_to_edit = open(name, 'w+')
            file_to_edit.close()
            file_to_edit = open(name, 'r')
            self.editBox.setText(file_to_edit.read())

        #Make the save button
        save = QAction(QIcon('save.png'), 'Save', self)
        save.setStatusTip('Save Editted File')
        save.triggered.connect(lambda: self.save_file(name))
        
        #Make Taskbar
        menubar = self.menuBar()
        menubar.addAction(save)

    def save_file(self, name):
        file_to_edit = open(name, 'w+')
        file_to_edit.write(self.editBox.toPlainText())
        file_to_edit.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gutenberg = Gutenberg()
    sys.exit(app.exec_())


