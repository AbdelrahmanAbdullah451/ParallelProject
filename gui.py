import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget,QMainWindow,\
    QPushButton, QVBoxLayout,QLineEdit,QLabel,QMessageBox,QLineEdit,QLabel



a = QApplication(sys.argv)

def th():
   label1.setText('first')


def sec():
    label1.setText('second')


def parallel():
    label1.setText('third')


root=QWidget()
root.setWindowTitle('parallel')
b1= QPushButton('get parallel',root) #adding button
b1.move(100,50)
b1.clicked.connect(parallel)

b2= QPushButton('get thread',root) #adding button
b2.move(250,50)
b2.clicked.connect(th)

b3= QPushButton('get sec',root) #adding button
b3.move(400,50)
b3.clicked.connect(sec)


label1= QLabel('',root)
label1.setGeometry(100,100,800,800)




root.show()
sys.exit(a.exec_())