# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visionchess.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem, QAction, QLineEdit, QMessageBox,QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1077, 806)
        Form.setStyleSheet("")
        self.textbox = QtWidgets.QLineEdit(Form)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        self.button = QPushButton('Show text', Form)
        self.button.move(20,80)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(100, 60, 591, 591))
        self.tableWidget.setRowCount(8)
        self.rownums=8
        self.tableWidget.setColumnCount(8)
        self.colnums=8
        self.tableWidget.setObjectName("tableWidget")
        self.lblCoords = QtWidgets.QLabel(Form)
        self.lblCoords.setGeometry(QtCore.QRect(100, 640, 741, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.lblCoords.setFont(font)
        self.lblCoords.setObjectName("lblCoords")
        self.lblCelda = QtWidgets.QLabel(Form)
        self.lblCelda.setGeometry(QtCore.QRect(780, 490, 231, 101))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.lblCelda.setFont(font)
        self.lblCelda.setStyleSheet("color: rgb(0, 170, 255);")
        self.lblCelda.setObjectName("lblCelda")
        self.btnStart = QtWidgets.QPushButton(Form)
        self.btnStart.setGeometry(QtCore.QRect(720, 600, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnStart.setFont(font)
        self.btnStart.setObjectName("btnStart")
        self.lblTime = QtWidgets.QLabel(Form)
        self.lblTime.setGeometry(QtCore.QRect(750, 0, 251, 141))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lblTime.setFont(font)
        self.lblTime.setObjectName("lblTime")
        self.lblCorrectas = QtWidgets.QLabel(Form)
        self.lblCorrectas.setGeometry(QtCore.QRect(710, 140, 91, 371))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblCorrectas.setFont(font)
        self.lblCorrectas.setStyleSheet("color: rgb(85, 0, 255);")
        self.lblCorrectas.setObjectName("lblCorrectas")
        self.lblErradas = QtWidgets.QLabel(Form)
        self.lblErradas.setGeometry(QtCore.QRect(960, 150, 91, 361))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblErradas.setFont(font)
        self.lblErradas.setStyleSheet("color: rgb(255, 0, 127);")
        self.lblErradas.setObjectName("lblErradas")
        self.checkCoordsYes = QtWidgets.QCheckBox(Form)
        self.checkCoordsYes.setGeometry(QtCore.QRect(790, 660, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkCoordsYes.setFont(font)
        self.checkCoordsYes.setAutoExclusive(True)
        self.checkCoordsYes.setObjectName("checkCoordsYes")
        self.checkCoordsNot = QtWidgets.QCheckBox(Form)
        self.checkCoordsNot.setGeometry(QtCore.QRect(790, 700, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.checkCoordsNot.setFont(font)
        self.checkCoordsNot.setAutoExclusive(True)
        self.checkCoordsNot.setObjectName("checkCoordsNot")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self.string="rnbkqbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBKQBNR"
        #RnbkqbnR/PPPppppp/8/8/8/8/PPPPPPPP/RNBKQBNR
        colcount=0
        rowcount=0
        for i in self.string:
            if(i=='/')and(colcount==8):
                colcount=0
                rowcount+=1
            elif(colcount<8)and(i=='/'):
                print("Error sin suficiente espacios en fila: "+str(rowcount))
                return
            elif(rowcount>self.rownums):
                print("Error en collumna: "+str(colcount))
                return
            elif(colcount>self.rownums):
                print("Error en fila: "+str(rowcount))
                return
            elif(ord (i)>=97)and(ord (i)<=122):
                colcount+=1
            elif(ord(i)>=65 and(ord(i)<=132)):
                colcount+=1
            elif(ord(i)>48 and ord(i)<58):
                colcount+=int(i)
            

        self.blancas=True
        self.timestart=0
        self.timetotal=3600
        self.prevrow=0
        self.prevcol=0
        self.selected=False
        self.correctas=0
        self.malas=0
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Semillero de Ajedrez UCN - VisionChess  - Fundación Universitaria Católica del Norte - Desarrollado por Alexander Narváez - anarvaez@ucn.edu.co"))
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(True)
        for i in range(self.colnums):
            self.tableWidget.setColumnWidth(i, 71)
        self.tableWidget.cellClicked.connect(self.eventFilter)
        self.lblCoords.setText(_translate("Form", "H  G  F  E  D  C  B  A"))
        self.lblCelda.setText(_translate("Form", "¿Listo?"))
        self.btnStart.setText(_translate("Form", "Comenzar"))
        self.btnStart.clicked.connect(self.clicked)
        self.lblTime.setText(_translate("Form", "Tiempo: "+str(self.timetotal)))
        self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
        self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
        self.checkCoordsYes.setText(_translate("Form", "Mostrar Coordenadas"))
        self.checkCoordsNot.setText(_translate("Form", "Ocultar Coordenadas"))
        self.start=False
        self.checkCoordsYes.clicked.connect(self.checkt)
        self.checkCoordsNot.clicked.connect(self.checkN)
        self.button.clicked.connect(self.on_click)
        self.textbox.setVisible(False)
        self.button.setVisible(False)

    def checkt(self):
        self.tableWidget.verticalHeader().setVisible(True)
        self.lblCoords.setVisible(True)
        pass
    def checkN(self):
        self.tableWidget.verticalHeader().setVisible(False)
        self.lblCoords.setVisible(False)
        pass
    def on_click(self):
        if(self.start==True):
            self.string= self.textbox.text()
            colcount=0
            rowcount=0
            error=False
            errormsg=""
            for i in str(self.string):
                if(i=='/')and(colcount==8):
                    colcount=0
                    rowcount+=1
                elif(colcount<8)and(i=='/'):
                    errormsg=("Error sin suficiente espacios en fila: "+str(rowcount))
                    error=True
                    break
                elif(rowcount>self.rownums):
                    errormsg=("Error en collumna(Mas espacios de los necesarios en la columna)): "+str(colcount))
                    error=True
                    break
                elif(colcount>self.rownums):
                    errormsg=("Error en fila(Mas filas de lo que permite el tablero)): "+str(rowcount))
                    error=True
                    break
                elif(ord (i)>=97)and(ord (i)<=122):
                    colcount+=1
                elif(ord(i)>=65 and(ord(i)<=132)):
                    colcount+=1
                elif(ord(i)>48 and ord(i)<58):
                    colcount+=int(i)
            if(error==True):
                QMessageBox.question(Form, 'Message - pythonspot.com', "Creatoin Failed: "+errormsg)
            else:
                columnacount=0
                rowcount=0
                for i in range(int(len(self.string))):
                    if(self.string[i]=='/'):
                        columnacount=0
                        rowcount+=1
                    elif(self.string[i]=='r'):
                        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u2656'))
                        columnacount+=1
                    elif(self.string[i]=='k'):
                        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u2654'))
                        columnacount+=1
                    elif(self.string[i]=='q'):
                        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u2655'))
                        columnacount+=1
                    elif(self.string[i]=='n'):
                        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u2658'))
                        columnacount+=1
                    elif(self.string[i]=='b'):
                        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u2657'))
                        columnacount+=1
                    elif(self.string[i]=='p'):
                        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u2659'))
                        columnacount+=1
                    elif(self.string[i]=='R'):
                        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u265C'))
                        columnacount+=1
                    elif(self.string[i]=='K'):
                        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u265A'))
                        columnacount+=1
                    elif(self.string[i]=='Q'):
                        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u265B'))
                        columnacount+=1
                    elif(self.string[i]=='N'):
                        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u265E'))
                        columnacount+=1
                    elif(self.string[i]=='B'):
                        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u265D'))
                        columnacount+=1
                    elif(self.string[i]=='P'):
                        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u265F'))
                        columnacount+=1
                    elif(ord(self.string[i])>48 and ord(self.string[i])<58):
                        for j in range(0,int(self.string[i])):
                            self.tableWidget.setItem(rowcount,columnacount+j,None)
                        columnacount+=int(self.string[i])
            self.textbox.setText("")
    def eventFilter(self):
        if(self.start==True):
            _translate = QtCore.QCoreApplication.translate
            row = self.tableWidget.currentRow()
            column = self.tableWidget.currentColumn()
            if(self.selected==False):
                if(self.tableWidget.item(row,column)==None):
                    return
                if(self.blancas==True):
                    if((u'\u2656')==self.tableWidget.item(row,column).text()): #<---Tower
                        self.prevrow=row
                        self.prevcol=column
                        self.selected=True
                        print("tower")
                    elif((u'\u2658')==self.tableWidget.item(row,column).text()): #<---Horse
                        self.prevrow=row
                        self.prevcol=column
                        self.selected=True
                        print("cabalo")
                    elif((u'\u2657')==self.tableWidget.item(row,column).text()): #<---alfil
                        self.prevrow=row
                        self.prevcol=column
                        self.selected=True
                        print("alfil")
                    elif((u'\u2659')==self.tableWidget.item(row,column).text()): #<---Peon
                        self.prevrow=row
                        self.prevcol=column
                        self.selected=True
                        print("Peon")
                    elif((u'\u2654')==self.tableWidget.item(row,column).text()): #<---Rey
                        self.prevrow=row
                        self.prevcol=column
                        self.selected=True
                        print("Rey")
                    elif((u'\u2655')==self.tableWidget.item(row,column).text()): #<---Reina
                        self.prevrow=row
                        self.prevcol=column
                        self.selected=True
                        print("Reina")
                    #self.blancas=False
                    self.timetotal=self.timetotal-(time.time()-self.timestart)
                    self.timestart=time.time()
                    self.lblTime.setText(_translate("Form", "Tiempo: "+str(int(self.timetotal))))
                else:
                    if((u'\u265C')==self.tableWidget.item(row,column).text()): #<---Tower
                        self.prevrow=row
                        self.prevcol=column
                        self.selected=True
                        print("tower")
                    elif((u'\u265E')==self.tableWidget.item(row,column).text()): #<---Horse
                        self.prevrow=row
                        self.prevcol=column
                        self.selected=True
                        print("Horse")
                    elif((u'\u265A')==self.tableWidget.item(row,column).text()): #<---Rey
                        self.prevrow=row
                        self.prevcol=column
                        self.selected=True
                        print("Rey")
                    elif((u'\u265B')==self.tableWidget.item(row,column).text()): #<---Reina
                        self.prevrow=row
                        self.prevcol=column
                        self.selected=True
                        print("Reina")
                    elif((u'\u265D')==self.tableWidget.item(row,column).text()): #<---alfil
                        self.prevrow=row
                        self.prevcol=column
                        self.selected=True
                        print("alfil")
                    elif((u'\u265F')==self.tableWidget.item(row,column).text()): #<---Peon
                        self.prevrow=row
                        self.prevcol=column
                        self.selected=True
                        print("Peon")

            else:
                row = self.tableWidget.currentRow()
                column = self.tableWidget.currentColumn()
                prevrow=self.prevrow
                prevcol=self.prevcol
                if(self.blancas==True):
                    if((u'\u2656')==self.tableWidget.item(prevrow,prevcol).text()): #<---Tower
                        if(prevrow==row and prevcol==column):
                            self.tableWidget.setCurrentItem(None)
                            self.selected=False
                            return
                        elif(prevrow>row and prevcol==column):
                            while(prevrow>row):
                                prevrow-=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2656'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=False                        
                            return
                        elif(prevrow==row and prevcol>column):
                            print("left")
                            while(prevcol>column):
                                prevcol-=1
                                if(prevcol==column)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2656'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=False
                            return
                        elif(prevrow<row and prevcol==column):
                            print("down")
                            while(prevrow<row):
                                prevrow+=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2656'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=False                        
                            return
                        elif(prevrow==row and prevcol<column):
                            print("right")
                            while(prevcol<column):
                                prevcol+=1
                                if(prevcol==column)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2656'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=False
                            return
                        print("tower")
                    elif((u'\u2658')==self.tableWidget.item(prevrow,prevcol).text()): #<---Horse
                        if(prevrow==row and prevcol==column):
                            self.tableWidget.setCurrentItem(None)
                            self.selected=False
                            return
                        for i in -1,1:
                            for j in 2,-2:
                                if(self.tableWidget.item(row,column)!=None)and((prevrow+i==row and prevcol+j==column)):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                    self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2658'))
                                    self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                    self.selected=False
                                    self.tableWidget.setCurrentItem(None)
                                    self.correctas+=1
                                    self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                    self.blancas=False
                                elif((prevrow+i==row and prevcol+j==column)):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                    self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2658'))
                                    self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                    self.selected=False
                                    self.tableWidget.setCurrentItem(None)
                                    self.correctas+=1
                                    self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                    self.blancas=False
                        for j in -1,1:
                            for i in 2,-2:
                                if(self.tableWidget.item(row,column)!=None)and((prevrow+i==row and prevcol+j==column)):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                    self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2658'))
                                    self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                    self.selected=False
                                    self.tableWidget.setCurrentItem(None)
                                    self.correctas+=1
                                    self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                    self.blancas=False
                                elif((prevrow+i==row and prevcol+j==column)):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                    self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2658'))
                                    self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                    self.selected=False
                                    self.tableWidget.setCurrentItem(None)
                                    self.correctas+=1
                                    self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                    self.blancas=False
                        print("cabalo")
                    elif((u'\u2657')==self.tableWidget.item(prevrow,prevcol).text()): #<---alfil
                        print("alfil")
                        if(prevrow==row and prevcol==column):
                            self.tableWidget.setCurrentItem(None)
                            self.selected=False
                            return
                        elif(prevrow<row and prevcol<column)and(abs(row-prevrow)==abs(column-prevcol)):
                            print("alfilder")
                            while(prevrow<row):
                                prevrow+=1
                                prevcol+=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2657'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=False                        
                            return
                        elif(prevrow<row and prevcol>column)and(abs(row-prevrow)==abs(column-prevcol)):
                            print("alfilizq")
                            while(prevrow<row):
                                prevrow+=1
                                prevcol-=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2657'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=False                        
                            return
                        elif(prevrow>row and prevcol>column)and(abs(row-prevrow)==abs(column-prevcol)):
                            print("alfilaizq")
                            while(prevrow<row):
                                prevrow-=1
                                prevcol-=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2657'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=False                        
                            return
                        elif(prevrow>row and prevcol<column)and(abs(row-prevrow)==abs(column-prevcol)):
                            print("alfilader")
                            while(prevrow<row):
                                prevrow-=1
                                prevcol+=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2657'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=False                        
                            return
                    elif((u'\u2659')==self.tableWidget.item(prevrow,prevcol).text()): #<---Peon
                        if(prevrow==row and prevcol==column):
                            self.tableWidget.setCurrentItem(None)
                            self.selected=False
                            return
                        if(prevrow<row and prevcol==column):
                            if(prevrow==1):
                                if((self.tableWidget.item(prevrow+1,prevcol)==None) and (prevrow+1==row)):
                                    self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2659'))
                                    self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                    self.selected=False
                                    self.tableWidget.setCurrentItem(None)
                                    self.correctas+=1
                                    self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                    self.blancas=False
                                elif(self.tableWidget.item(prevrow+1,prevcol)!=None)and (prevrow+1==row):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Correctas: "+str(self.malas)))
                                    return
                                elif((self.tableWidget.item(prevrow+1,prevcol)==None)and (self.tableWidget.item(prevrow+2,prevcol)==None)and(prevrow+2==row)):
                                    self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2659'))
                                    self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                    self.selected=False
                                    self.tableWidget.setCurrentItem(None)
                                    self.correctas+=1
                                    self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                    self.blancas=False
                            else:
                                if((self.tableWidget.item(prevrow+1,prevcol)==None) and (prevrow+1==row)):
                                    self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2659'))
                                    self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                    self.selected=False
                                    self.tableWidget.setCurrentItem(None)
                                    self.correctas+=1
                                    self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                    self.blancas=False
                        if(prevrow<row and prevcol>column):
                            if((self.tableWidget.item(prevrow+1,prevcol-1)!=None)):
                                self.tableWidget.setItem(prevrow+1,prevcol-1,None)
                                self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2659'))
                                self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                self.selected=False
                                self.tableWidget.setCurrentItem(None)
                                self.correctas+=1
                                self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                self.blancas=False
                            pass
                        if(prevrow<row and prevcol<column):
                            if(self.tableWidget.item(prevrow+1,prevcol+1)!=None):
                                self.tableWidget.setItem(prevrow+1,prevcol+1,None)
                                self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2659'))
                                self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                self.selected=False
                                self.tableWidget.setCurrentItem(None)
                                self.correctas+=1
                                self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                self.blancas=False
                            pass
                        print("Peond")
                    elif((u'\u2654')==self.tableWidget.item(prevrow,prevcol).text()): #<---Rey
                        for i in 1,-1,0:
                            for j in 1,-1:
                                if(prevrow+i==row and prevcol+j==column):
                                    self.tableWidget.setItem(row,column,None)
                                    self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2654'))
                                    self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                    self.selected=False
                                    self.tableWidget.setCurrentItem(None)
                                    self.correctas+=1
                                    self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                    self.blancas=False
                        for i in 1,-1:
                            if(prevrow+i==row and prevcol==column):
                                self.tableWidget.setItem(row,column,None)
                                self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2654'))
                                self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                self.selected=False
                                self.tableWidget.setCurrentItem(None)
                                self.correctas+=1
                                self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                self.blancas=False
                        print("Rey")
                    elif((u'\u2655')==self.tableWidget.item(prevrow,prevcol).text()): #<---Reina
                        print("Reina")
                        if(prevrow==row and prevcol==column):
                            self.tableWidget.setCurrentItem(None)
                            self.selected=False
                            return
                        elif(prevrow>row and prevcol==column):
                            while(prevrow>row):
                                prevrow-=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2655'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=False                        
                            return
                        elif(prevrow==row and prevcol>column):
                            print("left")
                            while(prevcol>column):
                                prevcol-=1
                                if(prevcol==column)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2655'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=False
                            return
                        elif(prevrow<row and prevcol==column):
                            print("down")
                            while(prevrow<row):
                                prevrow+=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2655'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=False                        
                            return
                        elif(prevrow==row and prevcol<column):
                            print("right")
                            while(prevcol<column):
                                prevcol+=1
                                if(prevcol==column)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2655'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=False
                            return
                        elif(prevrow<row and prevcol<column)and(abs(row-prevrow)==abs(column-prevcol)):
                            print("alfilder")
                            while(prevrow<row):
                                prevrow+=1
                                prevcol+=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2655'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=False                        
                            return
                        elif(prevrow<row and prevcol>column)and(abs(row-prevrow)==abs(column-prevcol)):
                            print("alfilizq")
                            while(prevrow<row):
                                prevrow+=1
                                prevcol-=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2655'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=False                        
                            return
                        elif(prevrow>row and prevcol>column)and(abs(row-prevrow)==abs(column-prevcol)):
                            print("alfilaizq")
                            while(prevrow<row):
                                prevrow-=1
                                prevcol-=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2655'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=False                        
                            return
                        elif(prevrow>row and prevcol<column)and(abs(row-prevrow)==abs(column-prevcol)):
                            print("alfilader")
                            while(prevrow<row):
                                prevrow-=1
                                prevcol+=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u2655'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=False                        
                            return
                else:
                    if((u'\u265C')==self.tableWidget.item(prevrow,prevcol).text()): #<---Tower
                        if(prevrow==row and prevcol==column):
                            self.tableWidget.setCurrentItem(None)
                            self.selected=False
                            return
                        elif(prevrow>row and prevcol==column):
                            while(prevrow>row):
                                prevrow-=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265C'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=True                        
                            return
                        elif(prevrow==row and prevcol>column):
                            print("left")
                            while(prevcol>column):
                                prevcol-=1
                                if(prevcol==column)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265C'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=True
                            return
                        elif(prevrow<row and prevcol==column):
                            print("down")
                            while(prevrow<row):
                                prevrow+=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265C'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=True                        
                            return
                        elif(prevrow==row and prevcol<column):
                            print("right")
                            while(prevcol<column):
                                prevcol+=1
                                if(prevcol==column)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265C'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=True
                            return
                        print("tower")
                    elif((u'\u265E')==self.tableWidget.item(prevrow,prevcol).text()): #<---Horse
                        if(prevrow==row and prevcol==column):
                            self.tableWidget.setCurrentItem(None)
                            self.selected=False
                            return
                        for i in -1,1:
                            for j in 2,-2:
                                if(self.tableWidget.item(row,column)!=None)and((prevrow+i==row and prevcol+j==column)):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                    self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265E'))
                                    self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                    self.selected=False
                                    self.tableWidget.setCurrentItem(None)
                                    self.correctas+=1
                                    self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                    self.blancas=True
                                elif((prevrow+i==row and prevcol+j==column)):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                    self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265E'))
                                    self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                    self.selected=False
                                    self.tableWidget.setCurrentItem(None)
                                    self.correctas+=1
                                    self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                    self.blancas=True
                        for j in -1,1:
                            for i in 2,-2:
                                if(self.tableWidget.item(row,column)!=None)and((prevrow+i==row and prevcol+j==column)):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                    self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265E'))
                                    self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                    self.selected=False
                                    self.tableWidget.setCurrentItem(None)
                                    self.correctas+=1
                                    self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                    self.blancas=True
                                elif((prevrow+i==row and prevcol+j==column)):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                    self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265E'))
                                    self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                    self.selected=False
                                    self.tableWidget.setCurrentItem(None)
                                    self.correctas+=1
                                    self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                    self.blancas=True
                        print("cabalo")
                    elif((u'\u265D')==self.tableWidget.item(prevrow,prevcol).text()): #<---alfil
                        print("alfil")
                        if(prevrow==row and prevcol==column):
                            self.tableWidget.setCurrentItem(None)
                            self.blancas=True
                            return
                        elif(prevrow<row and prevcol<column)and(abs(row-prevrow)==abs(column-prevcol)):
                            print("alfilder")
                            while(prevrow<row):
                                prevrow+=1
                                prevcol+=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265D'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=True                        
                            return
                        elif(prevrow<row and prevcol>column)and(abs(row-prevrow)==abs(column-prevcol)):
                            print("alfilizq")
                            while(prevrow<row):
                                prevrow+=1
                                prevcol-=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265D'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=True                        
                            return
                        elif(prevrow>row and prevcol>column)and(abs(row-prevrow)==abs(column-prevcol)):
                            print("alfilaizq")
                            while(prevrow<row):
                                prevrow-=1
                                prevcol-=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265D'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=True                        
                            return
                        elif(prevrow>row and prevcol<column)and(abs(row-prevrow)==abs(column-prevcol)):
                            print("alfilader")
                            while(prevrow<row):
                                prevrow-=1
                                prevcol+=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265D'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=True                        
                            return
                    elif((u'\u265F')==self.tableWidget.item(prevrow,prevcol).text()): #<---Peon
                        if(prevrow==row and prevcol==column):
                            self.tableWidget.setCurrentItem(None)
                            self.selected=False
                            return
                        if(prevrow>row and prevcol==column):
                            if(prevrow==6):
                                if((self.tableWidget.item(prevrow-1,prevcol)==None) and (prevrow-1==row)):
                                    self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265F'))
                                    self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                    self.selected=False
                                    self.tableWidget.setCurrentItem(None)
                                    self.correctas+=1
                                    self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                    self.blancas=True
                                elif(self.tableWidget.item(prevrow-1,prevcol)!=None)and (prevrow-1==row):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Correctas: "+str(self.malas)))
                                    return
                                elif((self.tableWidget.item(prevrow-1,prevcol)==None)and (self.tableWidget.item(prevrow-2,prevcol)==None)and(prevrow-2==row)):
                                    self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265F'))
                                    self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                    self.selected=False
                                    self.tableWidget.setCurrentItem(None)
                                    self.correctas+=1
                                    self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                    self.blancas=True
                            else:
                                if((self.tableWidget.item(prevrow-1,prevcol)==None) and (prevrow-1==row)):
                                    self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265F'))
                                    self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                    self.selected=False
                                    self.tableWidget.setCurrentItem(None)
                                    self.correctas+=1
                                    self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                    self.blancas=True
                        if(prevrow>row and prevcol<column):
                            if((self.tableWidget.item(prevrow-1,prevcol+1)!=None)):
                                self.tableWidget.setItem(prevrow-1,prevcol+1,None)
                                self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265F'))
                                self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                self.selected=False
                                self.tableWidget.setCurrentItem(None)
                                self.correctas+=1
                                self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                self.blancas=True
                            pass
                        if(prevrow>row and prevcol>column):
                            if(self.tableWidget.item(prevrow-1,prevcol-1)!=None):
                                self.tableWidget.setItem(prevrow-1,prevcol-1,None)
                                self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265F'))
                                self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                self.selected=False
                                self.tableWidget.setCurrentItem(None)
                                self.correctas+=1
                                self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                self.blancas=True
                            pass
                        print("Peond")
                    elif((u'\u265A')==self.tableWidget.item(prevrow,prevcol).text()): #<---Rey
                        for i in 1,-1,0:
                            for j in 1,-1:
                                if(prevrow+i==row and prevcol+j==column):
                                    self.tableWidget.setItem(row,column,None)
                                    self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265A'))
                                    self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                    self.selected=False
                                    self.tableWidget.setCurrentItem(None)
                                    self.correctas+=1
                                    self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                    self.blancas=True
                        for i in 1,-1:
                            if(prevrow+i==row and prevcol==column):
                                self.tableWidget.setItem(row,column,None)
                                self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265A'))
                                self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                                self.selected=False
                                self.tableWidget.setCurrentItem(None)
                                self.correctas+=1
                                self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                                self.blancas=True
                        print("Rey")
                    elif((u'\u265B')==self.tableWidget.item(prevrow,prevcol).text()): #<---Reina
                        print("Reina")
                        if(prevrow==row and prevcol==column):
                            self.tableWidget.setCurrentItem(None)
                            self.selected=False
                            return
                        elif(prevrow>row and prevcol==column):
                            while(prevrow>row):
                                prevrow-=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265B'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=True                        
                            return
                        elif(prevrow==row and prevcol>column):
                            print("left")
                            while(prevcol>column):
                                prevcol-=1
                                if(prevcol==column)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265B'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=True
                            return
                        elif(prevrow<row and prevcol==column):
                            print("down")
                            while(prevrow<row):
                                prevrow+=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265B'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=True                        
                            return
                        elif(prevrow==row and prevcol<column):
                            print("right")
                            while(prevcol<column):
                                prevcol+=1
                                if(prevcol==column)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265B'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=True
                            return
                        elif(prevrow<row and prevcol<column)and(abs(row-prevrow)==abs(column-prevcol)):
                            print("alfilder")
                            while(prevrow<row):
                                prevrow+=1
                                prevcol+=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265B'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=True                        
                            return
                        elif(prevrow<row and prevcol>column)and(abs(row-prevrow)==abs(column-prevcol)):
                            print("alfilizq")
                            while(prevrow<row):
                                prevrow+=1
                                prevcol-=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265B'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=True                        
                            return
                        elif(prevrow>row and prevcol>column)and(abs(row-prevrow)==abs(column-prevcol)):
                            print("alfilaizq")
                            while(prevrow<row):
                                prevrow-=1
                                prevcol-=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265B'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=True                        
                            return
                        elif(prevrow>row and prevcol<column)and(abs(row-prevrow)==abs(column-prevcol)):
                            print("alfilader")
                            while(prevrow<row):
                                prevrow-=1
                                prevcol+=1
                                if(prevrow==row)and(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.tableWidget.setItem(prevrow,prevcol,None)
                                elif(self.tableWidget.item(prevrow,prevcol)!=None):
                                    self.malas+=1
                                    self.lblErradas.setText(_translate("Form", "Erradas: "+str(self.malas)))
                                    print("no")
                                    return
                            self.tableWidget.setItem(row,column,QTableWidgetItem(u'\u265B'))
                            self.tableWidget.setItem(self.prevrow,self.prevcol,None)
                            self.selected=False
                            self.tableWidget.setCurrentItem(None)
                            self.correctas+=1
                            self.lblCorrectas.setText(_translate("Form", "Correctas: "+str(self.correctas)))
                            self.blancas=True                        
                            return
    def clicked(self):
        self.timetotal=3600
        #columnacount=0
        #rowcount=0
        #for i in range(int(len(self.string))):
        #    if(self.string[i]=='/'):
        #        columnacount=0
        #        rowcount+=1
        #    elif(self.string[i]=='r'):
        #        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u2656'))
        #        columnacount+=1
        #    elif(self.string[i]=='k'):
        #        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u2654'))
        #        columnacount+=1
        #    elif(self.string[i]=='q'):
        #        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u2655'))
        #        columnacount+=1
        #    elif(self.string[i]=='n'):
        #        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u2658'))
        #        columnacount+=1
        #    elif(self.string[i]=='b'):
        #        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u2657'))
        #        columnacount+=1
        #    elif(self.string[i]=='p'):
        #        columnacount+=1
        #        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u2659'))
        #    elif(self.string[i]=='R'):
        #        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u265C'))
        #        columnacount+=1
        #    elif(self.string[i]=='K'):
        #        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u265A'))
        #        columnacount+=1
        #    elif(self.string[i]=='Q'):
        #        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u265B'))
        #        columnacount+=1
        #    elif(self.string[i]=='N'):
        #        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u265E'))
        #        columnacount+=1
        #    elif(self.string[i]=='B'):
        #        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u265D'))
        #        columnacount+=1
        #    elif(self.string[i]=='P'):
        #        columnacount+=1
        #        self.tableWidget.setItem(rowcount,columnacount,QTableWidgetItem(u'\u265F'))
        #    elif(ord(self.string[i])>48 and ord(self.string[i])<58):
        #        for j in range(int(self.string[i])):
        #            self.tableWidget.setItem(rowcount,columnacount+j,None)
        #        columnacount+=int(self.string[i])
        #for i in range(self.rownums):
        #    for j in range(self.colnums):
        #     self.tableWidget.setItem(j, i, None)
        #self.tableWidget.setItem(0, 4, QTableWidgetItem(u'\u2654'))
        #self.tableWidget.setItem(0, 3, QTableWidgetItem(u'\u2655'))
        #self.tableWidget.setItem(0, 5, QTableWidgetItem(u'\u2657'))
        #self.tableWidget.setItem(0, 2, QTableWidgetItem(u'\u2657'))
        #self.tableWidget.setItem(0, 1, QTableWidgetItem(u'\u2658'))
        #self.tableWidget.setItem(0, 6, QTableWidgetItem(u'\u2658'))
        #self.tableWidget.setItem(0, 0, QTableWidgetItem(u'\u2656'))
        #self.tableWidget.setItem(0, 7, QTableWidgetItem(u'\u2656'))
        #self.tableWidget.setItem(7, 4, QTableWidgetItem(u'\u265A'))
        #self.tableWidget.setItem(7, 3, QTableWidgetItem(u'\u265B'))
        #self.tableWidget.setItem(7, 5, QTableWidgetItem(u'\u265D'))
        #self.tableWidget.setItem(7, 2, QTableWidgetItem(u'\u265D'))
        #self.tableWidget.setItem(7, 1, QTableWidgetItem(u'\u265E'))
        #self.tableWidget.setItem(7, 6, QTableWidgetItem(u'\u265E'))
        #self.tableWidget.setItem(7, 0, QTableWidgetItem(u'\u265C'))
        #self.tableWidget.setItem(7, 7, QTableWidgetItem(u'\u265C'))
        #for i in range(self.rownums):
        #    self.tableWidget.setItem(6, i, QTableWidgetItem(u'\u265F'))
        #for i in range(self.rownums):
        #    self.tableWidget.setItem(1, i, QTableWidgetItem(u'\u2659'))
        self.button.setVisible(True)
        self.textbox.setVisible(True)
        self.start=True
        self.timestart=time.time()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())