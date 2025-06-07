from Classes import Project as p, Task as t, Subtask as st
# from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
import sys, json, os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

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