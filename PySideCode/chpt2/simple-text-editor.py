import sys, time
from PySide.QtGui import QMainWindow, QApplication, QStatusBar, QLabel, \
QProgressBar, QDesktopWidget, QTextEdit, QAction, QIcon, QKeySequence, \
QMessageBox, QFileDialog, QFontDialog, QFont

#=====================================================================#
# MainWindow : Custom Widget Class
#=====================================================================#
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle("A Simple Text Editor")
        self.setWindowIcon(QIcon('appicon.png'))
        self.setGeometry(100, 100, 800, 600)
        self.center()

        # Text Editor
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.fileName = None

        self.filters = "Text files (*.txt)"
        # Setup and Show
        self.setupComponents()
        self.show()

    def center(self):
        """ Function to center the application """
        qRect = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    #=================================================================#
    # Create Central Widget Component to use QTextEdit
    #=================================================================#
    def setupComponents(self):
        """ Setting the central widget """

        # Progress Bar
        #self.progressBar = QProgressBar()
        #self.progressBar.setMinimum(0)
        #self.progressBar.setMaximum(100)

        # Status Label
        #self.statusLabel = QLabel('Status', self)

        # Status Bar
        self.myStatusBar = QStatusBar()
        #self.myStatusBar.addWidget(self.statusLabel, 1)
        #self.myStatusBar.addWidget(self.progressBar, 5)
        self.setStatusBar(self.myStatusBar)
        self.myStatusBar.showMessage('Ready', 1000)

        self.createActions()
        self.createMenus()
        self.createToolBar()

        # File Menu
        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)

        # Edit Menu
        self.editMenu.addAction(self.cutAction)
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.pasteAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.undoAction)
        self.editMenu.addAction(self.redoAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.selectAllAction)

        # Format Menu
        self.formatMenu.addAction(self.fontAction)

        # Help Menu
        self.helpMenu.addAction(self.aboutAction)
        self.helpMenu.addSeparator()
        self.helpMenu.addAction(self.aboutQtAction)

        # Tool Bar
        self.mainToolBar.addAction(self.newAction)
        self.mainToolBar.addAction(self.openAction)
        self.mainToolBar.addAction(self.saveAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.cutAction)
        self.mainToolBar.addAction(self.copyAction)
        self.mainToolBar.addAction(self.pasteAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.undoAction)
        self.mainToolBar.addAction(self.redoAction)

    # NOT-NEEDED : For progress bar
    def showProgress(self, progress):
        """ Function to show progress """
        self.progressBar.setValue(progress)
        if progress == 100:
            self.statusLabel.setText('Ready')
            return

    #=================================================================#
    # Helper Functions
    #=================================================================#
    def msgApp(self, title, message):
        """ Fuction to show dialog box with message """
        userInfo = QMessageBox.question(self, title, message,
                                QMessageBox.Yes | QMessageBox.No)
        if userInfo == QMessageBox.Yes:
            return "Y"
        if userInfo == QMessageBox.No:
            return "N"
        self.close()

    #=================================================================#
    # Slots: called when the menu actions are triggered
    #=================================================================#
    def newFile(self):
        response = self.msgApp("Confirmation", "Do you want to save the current file?")

        if response == "Y":
            self.saveFile()

        self.textEdit.setText('')
        self.fileName = None

    def openFile(self):
        response = self.msgApp("Confirmation", "Save the current file before open a new one?")

        if response == "Y":
            self.saveFile()

        (self.fileName, self.filterName) = QFileDialog.getOpenFileName(self)
        self.textEdit.setText(open(self.fileName).read())

    def saveFile(self):
        if self.fileName == None or self.fileName == '':
            (self.fileName, self.filterName) = \
                           QFileDialog.getSaveFileName(self, filter=self.filters)

        if (self.fileName != ''):
            file = open(self.fileName, 'w')
            file.write(self.textEdit.toPlainText())
            self.statusBar().showMessage("File saved", 2000)

    def exitFile(self):
        response = self.msgApp("Confirmation", 
                                "This will quit the application, continue?")
        if response == "Y":
            myApp.quit()
        else:
            pass

    def fontChange(self):
        (font, ok) = QFontDialog.getFont(QFont("Helvetica [Cronyx]",
                                               10), self)
        if ok:
            self.textEdit.setCurrentFont(font)

    def aboutHelp(self):
        QMessageBox.about(self, "About Simple Text Editor",
                          "This example demonstrates the use of " + \
                          "a Menu Bar")

    def aboutQt(self):
        QMessageBox.aboutQt(self ,title="Qt Version")

    #=================================================================#
    # Actions: send signals to slots
    #=================================================================#
    def createActions(self):
        """ Function to create actions for menus """
        # Parameters are as follows
        # 1. Icon to be displayed on the left
        # 2. The name, '&' means the the letter following
        #    will the be underlined (press 'Alt' to see)
        # 3. Implies the parent, which is the main window
        # 4. Shortcut key
        # 5. status tip in bottom status bar
        # 6. slot to be called
        self.newAction = QAction(QIcon('new.png'),
                         '&New File',
                         self,
                         shortcut=QKeySequence.New,
                         statusTip="Create a New File",
                         triggered=self.newFile)

        self.openAction = QAction(QIcon('open.png'),
                          '&Open File',
                          self,
                          shortcut=QKeySequence.Open,
                          statusTip="Open an existing file",
                          triggered=self.openFile)

        self.saveAction = QAction(QIcon('save.png'),
                          '&Save File',
                          self,
                          shortcut=QKeySequence.Save,
                          statusTip="Save the current file",
                          triggered=self.saveFile)

        self.cutAction = QAction(QIcon('cut.png'),
                         '&Cut',
                         self,
                         shortcut=QKeySequence.Cut,
                         statusTip="Cut the current selection to clipboard",
                         triggered=self.textEdit.cut)

        self.copyAction = QAction(QIcon('copy.png'),
                          '&Copy',
                          self,
                          shortcut="Ctrl+C",
                          statusTip="Copy",
                          triggered=self.textEdit.copy)

        self.pasteAction = QAction(QIcon('paste.png'),
                           '&Paste',
                           self,
                           shortcut="Ctrl+V",
                           statusTip="Paste",
                           triggered=self.textEdit.paste)

        self.selectAllAction = QAction(QIcon('selectAll.png'),
                               '&Select All',
                               self,
                               statusTip="Select All",
                               triggered=self.textEdit.selectAll)

        self.redoAction = QAction(QIcon('redo.png'),
                          '&Redo',
                          self,
                          shortcut=QKeySequence.Redo,
                          statusTip="Redo previous action",
                          triggered=self.textEdit.redo)

        self.undoAction = QAction(QIcon('undo.png'),
                          '&Undo',
                          self,
                          shortcut=QKeySequence.Undo,
                          statusTip="Undo previous action",
                          triggered=self.textEdit.undo)

        self.fontAction = QAction('F&ont',
                                   self,
                                   statusTip="Modify font properties",
                                   triggered=self.fontChange)

        self.aboutAction = QAction(QIcon('about.png'),
                           '&About',
                           self,
                           statusTip="Displays info about text editor",
                           triggered=self.aboutHelp)

        self.aboutQtAction = QAction('About &Qt',
                                     self,
                                     statusTip="Show the Qt library's About box",
                                     triggered=self.aboutQt)

        self.exitAction = QAction(QIcon('exit.png'),
                          '&Exit',
                          self,
                          shortcut="Ctrl+Q",
                          statusTip="Exit the program",
                          triggered=self.exitFile)

    #=================================================================#
    # Actual menu bar item creation
    #=================================================================#
    def createMenus(self):
        """ Function to create actual menu bar """
        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.formatMenu = self.menuBar().addMenu("&Format")
        self.helpMenu = self.menuBar().addMenu("&Help")

    #=================================================================#
    # Tool Bar
    #=================================================================#
    def createToolBar(self):
        """ Function to create tool bar """
        self.mainToolBar = self.addToolBar('Main Tool Bar')


#=====================================================================#
# Main Application
#=====================================================================#
if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        mainWindow = MainWindow()
        #mainWindow.showProgress(87)
        myApp.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error: ", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window...")
    except Exception:
        print(sys.exc_info()[1])
