__author__ = 'Tyler'
from PyQt4 import QtGui,QtCore
import sys
class SMSProj(QtGui.QMainWindow):

    def __init__(self):
        super(SMSProj, self).__init__()

        self.initUI()

    def initUI(self):

        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()
        exitAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()

def main():

    app = QtGui.QApplication(sys.argv)
    ex = SMSProj()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()