from Classes import Project as p, Task as t, Subtask as st
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import sys, json, os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Project Manager")
        self.setGeometry(700, 300, 500, 500) # x,y,width px,height px
        self.setWindowIcon(QIcon("app_icon.png"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 30)) # fontname, size
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color: #3F3F3F;"
                            "background-color: #6fdcf7")
        
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

def EditProject():
    pass

def DeleteProject():
    pass

def EditTask():
    pass

def DeleteTask():
    pass

def EditSubtask():
    pass

def DeleteSubtask():
    pass

def EditTag():
    pass

def DeleteTag():
    pass


if __name__ == "__main__":
    main()