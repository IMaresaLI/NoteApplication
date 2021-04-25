################################################
################################################
################################################
#########*******###*******####**********########
########**#####**#**#####**###**######**########
########**#####**#**#####**###**######**########
########**#####**#**#####**###**********########
########**#####**#**#####**###**################
########**#####**#**#####**###**################
########**######***######**###**################
########**###############**###**################
########**###############**###**################
################################################
########Copyright © Maresal Programming#########
################################################

from PyQt5 import QtWidgets,QtCore,QtGui
import os,sys,datetime,json,time
from noteAppDesign import Ui_MainWindow


class NoteApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(NoteApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(open("style\style.css","r").read())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.noteLoad()
        
        self.ui.ExitBtn.clicked.connect(self.exitApp)
        self.ui.MinimizeBtn.clicked.connect(self.minimize)
        self.ui.FullScreenBtn.clicked.connect(self.fullscreen)

        self.ui.homeBtn.clicked.connect(self.home)
        self.ui.noteAddBtn.clicked.connect(self.addNotePage)
        self.ui.noteDeleteBtn.clicked.connect(self.noteDelete)
        self.ui.label.mouseDoubleClickEvent = self.LabelDoubleClick
        self.ui.notTextPte.textChanged.connect(self.textCount)

        self.ui.addBtn.clicked.connect(self.AddedNote)
        self.ui.treeWidget.itemDoubleClicked.connect(self.updateNotePage)
        self.ui.updateBtn.clicked.connect(self.updateClicked)
        self.ui.settingBtn.clicked.connect(self.settings)

        self.ui.InstagramBtn.clicked.connect(self.instaLink)
        self.ui.FacebookBtn.clicked.connect(self.faceLink)
        self.ui.GithubBtn.clicked.connect(self.githubLink)

    def home(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.clearFunc()
        self.ui.noteAddBtn.setEnabled(True)
        self.ui.noteDeleteBtn.setEnabled(True)

    def addNotePage(self):
        self.ui.treeWidget.setAnimated(True)
        self.ui.addBtn.setHidden(False)
        self.ui.updateBtn.setHidden(True)
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.timeLbl.setText("Zaman :"+str(datetime.datetime.now().date()))

    def LabelDoubleClick(self,event):
        self.ui.noteNameTbx.setReadOnly(False)
        self.ui.noteNameTbx.setStyleSheet("background: #052e6b;")

    def textCount(self):
        text = self.ui.notTextPte.toPlainText()
        self.ui.lengthCharacterLbl.setText("Karakter sayısı : "+ str(len(text)))

    def AddedNote(self):
        dict = {}
        noteName = self.ui.noteNameTbx.text()
        note = self.ui.notTextPte.toPlainText()
        date = datetime.datetime.now().date()
        if note !=  "": 
            if noteName == "":
                noteName,ok =QtWidgets.QInputDialog.getText(self,"Not Adı Ataması","Notunuzun Adı:")
                if noteName and ok:
                    self.addFunc(dict, noteName, note, date)
            else :
                self.addFunc(dict, noteName, note, date)

    def addFunc(self, dict, noteName, note, date):
        if os.path.exists("data.json") == True:
            x = self.fileLoadFunc("r")
            x.update({noteName : {"text":note,"date":str(date)}})
            self.noteDump(x)
            self.clearFunc()
            QtWidgets.QMessageBox.information(self,"Bilgilendirme","Notunuz kaydedildi.")
            self.ui.stackedWidget.setCurrentIndex(0)
        else :
            dict.update({noteName : {"text":note,"date":str(date)}})
            self.noteDump(dict)
            self.clearFunc()
            QtWidgets.QMessageBox.information(self,"Bilgilendirme","Notunuz kaydedildi.")
            self.ui.stackedWidget.setCurrentIndex(0)
        self.noteLoad()

    def updateNotePage(self):
        global name
        item = self.ui.treeWidget.currentItem()
        self.ui.updateBtn.setHidden(False)
        self.ui.addBtn.setHidden(True)
        self.ui.stackedWidget.setCurrentIndex(1)
        file = self.fileLoadFunc("r")
        self.ui.noteNameTbx.setText(item.data(0,0))
        self.ui.lengthCharacterLbl.setText("Karakter sayısı : "+str(len(file[item.data(0,0)]["text"])))
        self.ui.timeLbl.setText("Zaman : "+ file[item.data(0,0)]["date"])
        self.ui.notTextPte.setPlainText(file[item.data(0,0)]["text"])
        name = item.data(0,0)
        self.ui.noteAddBtn.setEnabled(False)
        self.ui.noteDeleteBtn.setEnabled(False)

    def updateClicked(self):
        dict = {}
        items = self.fileLoadFunc("r")
        dict.update(items)
        dict.pop(name)
        dict.update({self.ui.noteNameTbx.text():{"text":self.ui.notTextPte.toPlainText(),"date":str(datetime.datetime.now().date())}})
        self.noteDump(dict)
        QtWidgets.QMessageBox.information(self,"Bilgilendirme","Notunuz kaydedildi.")
        self.ui.stackedWidget.setCurrentIndex(0)
        self.noteLoad()
        self.ui.noteAddBtn.setEnabled(True)
        self.ui.noteDeleteBtn.setEnabled(True)


    def noteDelete(self):
        try :
            item = self.ui.treeWidget.currentItem().data(0,0)
            result = QtWidgets.QMessageBox.question(self,"Silme Onayı","%s adlı notunuzu silmek istiyor musunuz?" %item , QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel)
            if result == QtWidgets.QMessageBox.StandardButton.Ok:
                dict = {}
                items = self.fileLoadFunc("r")
                dict.update(items)
                dict.pop(item)
                self.noteDump(dict)
                self.noteLoad()
                QtWidgets.QMessageBox.information(self,"Silme Bilgilendirme","%s adlı notunuz silindi." %item)
        except :
            pass

    def clearFunc(self):
        self.ui.noteNameTbx.clear()
        self.ui.notTextPte.clear()
        self.ui.timeLbl.clear()
        self.ui.lengthCharacterLbl.clear()
        self.ui.timeLbl.setText("Zaman : ")
        self.ui.lengthCharacterLbl.setText("Karakter sayısı : ")

    def noteDump(self, x):
        with open("data.json","w+") as file:
            json.dump(x,file)

    def noteLoad(self):
        self.ui.noteNameTbx.setReadOnly(True)
        self.ui.noteNameTbx.setStyleSheet("background: transparent;")
        self.ui.treeWidget.clear()
        self.ui.treeWidget.setColumnWidth(0,140)
        self.ui.treeWidget.setColumnWidth(1,135)
        self.ui.treeWidget.setColumnWidth(2,135)

        if os.path.exists("data.json") == True:
            x = self.fileLoadFunc("r")
            for i in x :
                item = QtWidgets.QTreeWidgetItem(self.ui.treeWidget)
                item.setText(0,i)
                item.setText(1,str(len(x[i]["text"])))
                item.setText(2,x[i]["date"])

    def fileLoadFunc(self,mod):
        with open("data.json",mod) as file :
            x = json.load(file)
            return x

    def instaLink(self):
        os.startfile("https://www.instagram.com/maresalp/")
    def faceLink(self):
        os.startfile("https://www.facebook.com/maresalprogramming")
    def githubLink(self):
        os.startfile("https://github.com/IMaresaLI")

    def settings(self):
        QtWidgets.QMessageBox.information(self,"Ayarlar Bildirim","Ayarlar seçeneğine henüz bir fonksiyon eklenmemiştir.")

    def minimize(self):
        self.showMinimized()

    def exitApp(self):
        self.close()

    def mousePressEvent(self, event):
        try :
            if event.buttons() == QtCore.Qt.LeftButton:
                self.dragPos = event.globalPos()
                event.accept()
        except :
            pass

    def mouseMoveEvent(self, event):
        try:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()
        except :
            pass

    def fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else :
            self.showFullScreen()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = NoteApp()
    main.show()
    app.setStyle("Fusion")
    app.exit(app.exec_())
