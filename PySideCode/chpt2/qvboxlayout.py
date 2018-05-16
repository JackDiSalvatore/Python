import sys
from PySide.QtGui import *

class MainWindow(QWidget):
    """ Our Main Window Class """
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("Vertical Layout")
        self.setGeometry(300, 250, 400, 300)
        self.SetLayout()
        self.show()

    def SetLayout(self):
        """ Function to add buttons and set the layout """
        verticalLayout = QVBoxLayout(self)

        vButton1 = QPushButton('Button 1', self)
        vButton2 = QPushButton('Button 2', self)
        vButton3 = QPushButton('Button 3', self)
        vButton4 = QPushButton('Button 4', self)
        vButton5 = QPushButton('Button 5', self)
        vButton6 = QPushButton('Button 6', self)

        verticalLayout.addWidget(vButton1)
        verticalLayout.addWidget(vButton2)
        verticalLayout.addWidget(vButton3)

        verticalLayout.addStretch()

        verticalLayout.addWidget(vButton4)
        verticalLayout.addWidget(vButton5)
        verticalLayout.addWidget(vButton6)

        self.setLayout(verticalLayout)


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
