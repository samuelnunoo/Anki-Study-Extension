from PyQt5 import QtCore, QtGui, QtWidgets
import keyboard
import sys
import Cards as create
from PIL import ImageGrab
import cv2
import os
import math
import numpy as np
from PyQt5.QtCore import Qt
import random
import time


class Decks(QtWidgets.QWidget):
    switch_window=QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)


    def setupUi(self, Form):
        print('yeah')
        Form.setObjectName("Form")
        Form.resize(4540, 4290)
        Form.setWindowTitle("")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 4, 1, 1, 1)

        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(self.Selection)

        self.gridLayout.addWidget(self.listWidget, 3, 1, 1, 2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 2, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 2, 3, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form) 
        self.List()   

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("Form", "Create"))
        self.label.setText(_translate("Form", "Change Card Decks"))
        self.pushButton.clicked.connect(self.Create)

    def List(self):
       # model=QtGui.QStandardItemModel(self.listWidget)
        items=create.Search_Decks()

        for item in items:
            x=QtGui.QStandardItem(item[0])
            self.listWidget.addItem(item[0])

    def Selection(self,item):
        
        controller.Deck=create.Select_Deck(item.text())
        controller.check()
        controller.ChosenDeck=item.text()
        print(item.text())
        self.close()
        self.switch_window.emit('o')

    def Create(self):
        self.close()
        name=self.lineEdit.text()
        id=int(random.randrange(1 << 30, 1 << 31))
        create.New_Deck(name,id)
        controller.Deck=create.Select_Deck(name)
        controller.ChosenDeck=name
        self.close()
        self.switch_window.emit('o')
        
    



class Main(QtWidgets.QWidget):

    switch_window=QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.new = False
        self.cwd = os.getcwd()
        self.Front = Qt.Key_R
        self.Back = Qt.Key_T
        self.Current = 'Front'
        self.Package = Qt.Key_U
        self.Side = 'Front'
        self.Choose = Qt.Key_Q
        self.Decks=Qt.Key_1
        self.Choice = False

        self.layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel()
        self.label.setObjectName("label")
        self.label.setStyleSheet('QLabel#label {color: black}')
        self.label.setText(controller.ChosenDeck)
        self.layout.addWidget(self.label)
        
        self.setAutoFillBackground(True)
        self.paint = self.palette()

        

        self.ScreenShot()


    def ColorWindow(self,color):
            
            self.paint.setColor(self.backgroundRole(), color)
            self.setPalette(self.paint)
            
        

    def ScreenShot(self):
        self.repaint()
        self.title = ''
        
        self.label.setText(controller.ChosenDeck)
        self.setLayout(self.layout) 
        self.label.move(0,0)

        screen = QtWidgets.QApplication.primaryScreen()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        size = screen.size()
        self.setGeometry(0, 0, size.width(), size.height())
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setActiveWindow(self)
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))

        # Set window background color
       

        self.show()
        self.activateWindow()

    def paintEvent(self, event):

        qp = QtGui.QPainter(self)

        if self.new is True:

            qp.eraseRect(QtCore.QRect(self.begin, self.end))

        else:
            qp.setPen(QtGui.QPen(QtGui.QColor('black'), 3))
            qp.setBrush(QtGui.QColor(128, 128, 255, 128))
            qp.drawRect(QtCore.QRect(self.begin, self.end))
  
    def keyPressEvent(self, event):
        print(event)
        if event.key() == self.Front:
            print('alright')
            self.Current = 'Front'
            self.update()

        elif event.key() == self.Back:
            print('ok')
            self.Current = 'Back'
            self.update()

        elif event.key() == self.Package:
            self.close()
            create.Cards(controller.Deck, create.TEST_MODEL)
            controller.hook()

        elif event.key() == self.Choose:
            if self.Choice is False:
                self.Choice = True
            else:
                self.Choice = False
        
        elif event.key()==self.Decks:
            self.switch_window.emit("Decks")

    def mousePressEvent(self, event):
        if self.Current == '':
            return 'no'
        else:
            self.new = False
            self.begin = event.pos()
            self.end = self.begin

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.new = True
        self.repaint()
        self.close()

        Directory = os.getcwd() + "/Flashcards"

        File_Number = create.Card_Database()+1
        print(File_Number)

        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))

        Name = str(File_Number) + self.Side

        print(x1,x2,y1,y2)
        if x1==x2 or y1==y2:
            print('start over')
            
            self.ColorWindow(Qt.red)
            self.show()
            time.sleep(1)
            
            self.ColorWindow(Qt.white)
            self.close()
            return self.ScreenShot()

        img.save(Directory + '/' + Name + ".png")
        img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

        if self.Side == 'Front':
            self.Side = 'Back'
            if not self.Choice:
                self.ScreenShot()
            else:
                controller.hook()
        else:
            self.Side = 'Front'
            create.Insert_Card()
            controller.hook()



class Controller:
    def __init__(self):
        self.Deck=create.my_deck
        self.ChosenDeck="Default"
        pass

    def check(self):
        print('checking',self.Deck)
    #Add App Starter
    def hook(self):
        keyboard.wait('ctrl+e',suppress=True)
        print('running')
        self.show_main()

    def show_decks(self):
        print('ok')
        self.decks=Decks()
        self.decks.switch_window.connect(self.show_main)        
        self.decks.show()
        self.decks.activateWindow()
        

    def show_main(self):
        self.main=Main()
        self.main.show()
        self.main.switch_window.connect(self.show_decks)
        self.main.activateWindow()


if __name__ == "__main__":
   #Creating required UI things
    app = QtWidgets.QApplication(sys.argv)
    controller=Controller()
    controller.hook()
    sys.exit(app.exec_())
    
        


