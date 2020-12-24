"""
Para que el programa pueda ejercer cambios, es necesario ejecutarlo con permisos de administrador.

Requisitos:
1. Cada seccion de repositiorio a activar tiene q estar encerrado por una identificacion.
2. La identificacion de apertura tiene que tener la forma #repo_ seguido del nombre deseado.
3. La identificacion de cerrar la seccion tiene que ser igual que la de apertura con un "/", #/repo_

Ejemplos de una seccion:

#repo_casa
.
.
.
#/repo_casa

#repo_Hola
.
.
.
#/repo_Hola

"""

from PyQt5 import QtCore, QtGui, QtWidgets
import re

class Ui_Dialog(object):
        
    def __init__(self):
        super().__init__()
        self.direction = "/etc/apt/sources.list"
        self.list_repo, self.data_repo= self.read_file(self.direction)
        self.set_repo(self.list_repo[1])
        
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Repo")
        Dialog.resize(266, 122)
        #--------------tags-----------------
        self.tags = QtWidgets.QComboBox(Dialog)
        self.tags.setEnabled(True)
        self.tags.setGeometry(QtCore.QRect(10, 50, 251, 23))
        font = QtGui.QFont()
        font.setFamily("Droid Sans Fallback")
        font.setPointSize(10)
        
        self.tags.setFont(font)
        self.tags.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tags.setEditable(False)
        self.tags.setModelColumn(0)
        self.tags.setObjectName("tags")
        self.tags.addItems(self.list_repo.values())
        self.tags.activated.connect(lambda: self.set_repo(self.list_repo[self.tags.currentIndex()+1]))

        #--------------Title-----------------------
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(10, 30, 251, 16))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        
        #---------Button--------------------
        self.set_Button = QtWidgets.QPushButton(Dialog)
        self.set_Button.setGeometry(QtCore.QRect(169, 90, 91, 23))
        font = QtGui.QFont()
        font.setFamily("FreeMono")
        font.setPointSize(10)
        font.setItalic(True)
        self.set_Button.setFont(font)
        self.set_Button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.set_Button.setDefault(True)
        self.set_Button.setFlat(False)
        self.set_Button.setObjectName("set_Button")
        self.set_Button.clicked.connect(lambda: self.write_file(self.direction))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "Select a tag to active it:"))
        self.set_Button.setText(_translate("Dialog", "Select"))

#------------functions--------------------------

    def read_file(self, dir):
        """
        Leer el fichero a trabajar y lista los identificadores de los repositorios
        """
        data_repo = []
        list_repo = {}
        cont = 1
        with open(dir, 'r') as file:
            for line in file:
                line = re.sub('\n', '', line)
                if "#repo_" in line:
                    list_repo.setdefault(cont, line[1:])
                    cont = cont + 1
                data_repo.append(line)
            file.close()
        return list_repo, data_repo
    
    
    def set_repo(self,tag):
        """
        Selecionar determinada por sion de repositiorio atendiendo al identificador introducido.
        """
        set_repo = False
        #tag = self.list_repo[self.tags.currentIndex()+1]
        print(tag)
        for i, direcc in zip(range(len(self.data_repo)), self.data_repo):
            if ("#"+tag.lower()) == direcc.lower():
                set_repo = True
            if ("#/"+tag.lower()) == direcc.lower():
                set_repo = False

            if "deb http" in direcc:
                is_sharp = "#" in direcc
                if set_repo == True and is_sharp == True:
                    self.data_repo[i] = direcc[1:]
                elif set_repo == False and is_sharp == False:
                    self.data_repo[i] = "#" + direcc
            
       # return data_repositorie


    def write_file(self, dir):
        """
        Escribir el fichero con los cambios sleccionados.
        """
        with open(dir, 'w+') as file:
            for line in self.data_repo:
                line = line + "\n"
                file.write(line)
            file.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationDisplayName("Repo")
    Dialog = QtWidgets.QDialog()
    Dialog.setWindowTitle("Repo")
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

