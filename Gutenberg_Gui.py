#!/usr/bin/python3.6
import sys
from PyQt5.QtWidgets import QApplication, QComboBox, QWidget, QMainWindow, QLabel, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from search import search

class Gutenberg(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Gutenberg'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 300       
        
        self.UI()

    def UI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #Create Query Box
        self.textbox = QLineEdit(self)
        self.textbox.move(200, 150)
        self.textbox.resize(200, 20)

        #Create extensions dropdown button
        extensions = QComboBox(self)
        extensions.addItem('')
        extensions.addItem('pdf')
        extensions.addItem('ppt')
        extensions.addItem('script')
        extensions.addItem('zip')
        extensions.addItem('docx')
        extensions.addItem('jpg')
        extensions.addItem('html')
        extensions.addItem('gdoc')

        #Default Filetype is none
        self.file_type = ''
        
        #When the file extension is chosen
        extensions.activated[str].connect(self.file_extension)


        #create search button
        self.button = QPushButton('Search', self)
        self.button.move(250, 170)

        #connect button to search function
        self.button.clicked.connect(self.query)
               
        self.show()


    def query(self):
        self.urls = open('urls.txt', 'w+')
        for i in search(self.textbox.text(), self.file_type):
            self.urls.write(i+'\n')

    def file_extension(self, ftype):
        self.file_type = ftype        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gutenberg = Gutenberg()
    sys.exit(app.exec_())


