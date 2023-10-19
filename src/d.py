import csv

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from pathlib import Path


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.left = 20
        self.top = 20

        self.setStyleSheet("background-color: #31363A;")

        #Init Value
        self.flag = False
        self.data_array = []
        self.total_count = 0
        self.review_count = 0
        self.step1_count = 0
        self.step2_count = 0
        self.step3_count = 0
        self.filename = ""

        self.InitUI()

    def InitUI(self):
        #Setting Font
        titlefont = QFont()
        titlefont.setFamily("Arial")
        titlefont.setPointSize(20)

        buttonfont = QFont()
        buttonfont.setFamily("Arial")
        buttonfont.setPointSize(12)

        main_image = QLabel(self)
        pixmap = QPixmap('main.png')
        main_image.setPixmap(pixmap)
        main_image.move(30,30)

        main_title = QLabel(self)
        main_title.setFont(titlefont)
        main_title.setText("<font color='white'>Company Categorisation Tool</font>")
        main_title.move(140, 40)

        # Set the Header three button

        fileopen_button = QPushButton(self)
        fileopen_button.setText("<font color='white'>File Location</font>")
        fileopen_button.setGeometry(40, 100, 150, 40)
        fileopen_button.setFont(buttonfont)
        fileopen_button.setStyleSheet("border-radius : 50;")
        fileopen_button.setStyleSheet("background-color: #3FE4C0;")
        fileopen_button.setIcon(QIcon('search.png'))

        save_button = QPushButton(self)
        save_button.setText("<font color='white'>Save</font>")
        save_button.setGeometry(230, 100, 150, 40)
        save_button.setFont(buttonfont)
        save_button.setStyleSheet("border-radius : 50;")
        save_button.setStyleSheet("background-color: #3FE4C0;")
        save_button.setIcon(QIcon('search.png'))

        openExist_button = QPushButton(self)
        openExist_button.setText("<font color='white'>Open Existing</font>")
        openExist_button.setGeometry(420, 100, 150, 40)
        openExist_button.setFont(buttonfont)
        openExist_button.setStyleSheet("border-radius : 50;")
        openExist_button.setStyleSheet("background-color: #3FE4C0;")
        openExist_button.setIcon(QIcon('search.png'))

        #Set ProgressBar
        process_label = QLabel(self)
        process_label.setFont(buttonfont)
        process_label.setText("<font color='white'>Working it out...</font>")
        process_label.setGeometry(40, 165, 130, 30)

        prog_bar = QProgressBar(self)
        prog_bar.setGeometry(180, 160, 400, 30)
        prog_bar.setValue(40)

        result_static_label = QLabel(self)
        result_static_label.setFont(buttonfont)
        result_static_label.setText("<font color='white'>Here are the results...</font>")
        result_static_label.setGeometry(40, 200, 130, 30)




if __name__ == '__main__':
    app = QApplication([])
    dialog = MyDialog()
    dialog.resize(1024, 800)
    dialog.exec()
