import sys
from PySide.QtGui import *

class MainWindow(QWidget):
    """ Our Main Window Class """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("Vertical Layout")
        self.setGeometry(600, 450, 800, 600)
        self.SetLayout()
        self.show()


    #=====================================================
    #   GRID LAYOUT
    #=====================================================
    def SetLayout(self):
        """ Function to add buttons and set the layout """
        gridLayout = QGridLayout(self)
        gButton1 = QPushButton('Button 1', self)
        gButton2 = QPushButton('Button 2', self)
        gButton3 = QPushButton('Button 3', self)
        gButton4 = QPushButton('Button 4', self)
        gButton5 = QPushButton('Button 5', self)
        gButton6 = QPushButton('Button 6', self)
        gButton7 = QPushButton('Button 7', self)
        gButton8 = QPushButton('Button 8', self)

        gridLayout.addWidget(gButton1, 0, 0)
        gridLayout.addWidget(gButton2, 0, 1)
        gridLayout.addWidget(gButton3, 1, 0, 1, 2)
        gridLayout.addWidget(gButton4, 2, 0)
        gridLayout.addWidget(gButton5, 2, 1)
        gridLayout.addWidget(gButton6, 3, 1, 1)
        gridLayout.addWidget(gButton7, 4, 1)
        gridLayout.addWidget(gButton8, 5, 2, 1, 3)

        self.setLayout(gridLayout)


if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error: ", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
