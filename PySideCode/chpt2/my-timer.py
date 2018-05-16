import sys
#from PySide.QtCore import QDateTime, QTimer, SIGNAL
from PySide.QtCore import *
#from PySide.QtGui import QApplication, QWidget, QLCDNumber, QDesktopWidget
from PySide.QtGui import *

class MyTimer(QWidget):
    """ Our Main Window Class for Timer """
    def __init__(self):
        """ Constructor Function """
        super(MyTimer, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle('My Digital Clock')
        timer = QTimer(self)

        # change background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        p.setColor(self.foregroundRole(), Qt.white)
        self.setPalette(p)

        # on timeout of the timer, call updtTime function
        self.connect(timer, SIGNAL("timeout()"), self.updtTime)

        self.myTimeDisplay = QLCDNumber(self)
        # sets style for QLCDNumber
        self.myTimeDisplay.setSegmentStyle(QLCDNumber.Filled)
        self.myTimeDisplay.setDigitCount(8) # set number of digits
                                            # on display. default=5
        self.myTimeDisplay.resize(500, 150)
        self.updtTime() # To display the current time before call
                        # by timer event. Otherise it will start 
                        # with 0
        self.center()
        timer.start(1000) # times out every 1000ms (1 sec)
        self.show()

    def center(self):
        """ Function to center the application """
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def updtTime(self):
        """ Function to update current time """
        currentTime = QDateTime.currentDateTime().toString('hh:mm:ss')
        self.myTimeDisplay.display(currentTime)

if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        myWindow = MyTimer()

        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error: ", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])