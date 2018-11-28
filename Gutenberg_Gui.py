#!/usr/bin/python3.6 
import sys
from PyQt5.QtWidgets import QApplication, QCheckBox, QComboBox, QWidget, QMainWindow, QLabel, QPushButton, QAction, QLineEdit, QMessageBox, QProgressBar
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
        extensions.addItem('') #The default is no specified filetype
        extension_list = open('extensions.txt', 'r')
        for i in extension_list:
            i = i.replace('\n', '')
            if i != '':
                extensions.addItem(i)

        #Make Progress Bar
        self.progress = QProgressBar(self)
        self.progress.setGeometry(255 ,175, 225, 20)
        

        #Default Filetype is none
        self.file_type = ''
        
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
        for i in search(self.textbox.text(), self.file_type, self.enable_blacklist):
            self.urls.write(i+'\n')
        self.urls.close()
        self.progress.setValue(100)
        self.enable_blacklist = False

    def file_extension(self, ftype):
        self.file_type = ftype        

    def use_blacklist(self, state):
        if state == Qt.Checked:
            self.enable_blacklist = True
            print('blacklist activated')
            print(self.enable_blacklist)
        else:
            self.enable_blacklist = False
            print('blacklist deactivated')
            print(self.enable_blacklist)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gutenberg = Gutenberg()
    sys.exit(app.exec_())


