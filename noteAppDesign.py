# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Batuhan Olgaç\Desktop\NoteApp\noteApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.headBarFrame = QtWidgets.QFrame(self.centralwidget)
        self.headBarFrame.setMinimumSize(QtCore.QSize(0, 40))
        self.headBarFrame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.headBarFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.headBarFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headBarFrame.setObjectName("headBarFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headBarFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.IconLbl = QtWidgets.QLabel(self.headBarFrame)
        self.IconLbl.setMinimumSize(QtCore.QSize(50, 0))
        self.IconLbl.setMaximumSize(QtCore.QSize(50, 16777215))
        self.IconLbl.setText("")
        self.IconLbl.setObjectName("IconLbl")
        self.horizontalLayout_2.addWidget(self.IconLbl)
        self.NameLbl = QtWidgets.QLabel(self.headBarFrame)
        self.NameLbl.setStyleSheet("color:white;\n"
"font: 75 11pt \"Century Gothic\";\n"
"")
        self.NameLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.NameLbl.setObjectName("NameLbl")
        self.horizontalLayout_2.addWidget(self.NameLbl)
        spacerItem = QtWidgets.QSpacerItem(218, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.MinimizeBtn = QtWidgets.QPushButton(self.headBarFrame)
        self.MinimizeBtn.setMinimumSize(QtCore.QSize(15, 15))
        self.MinimizeBtn.setMaximumSize(QtCore.QSize(15, 15))
        self.MinimizeBtn.setStyleSheet("#MinimizeBtn{    \n"
"    background-color: rgb(35, 143, 219);\n"
"    border-radius:1px;\n"
"}\n"
"#MinimizeBtn:hover{\n"
"    background-color: rgb(31, 124, 191);\n"
"}\n"
"#MinimizeBtn:pressed{\n"
"    background-color: rgb(41, 166, 255);\n"
"}")
        self.MinimizeBtn.setText("")
        self.MinimizeBtn.setObjectName("MinimizeBtn")
        self.horizontalLayout_2.addWidget(self.MinimizeBtn)
        self.FullScreenBtn = QtWidgets.QPushButton(self.headBarFrame)
        self.FullScreenBtn.setMinimumSize(QtCore.QSize(15, 15))
        self.FullScreenBtn.setMaximumSize(QtCore.QSize(15, 15))
        self.FullScreenBtn.setStyleSheet("#FullScreenBtn{    \n"
"    background-color: rgb(123, 214, 32);\n"
"border-radius:1px;\n"
"}\n"
"#FullScreenBtn:hover{\n"
"    background-color: rgb(107, 186, 28);\n"
"}\n"
"#FullScreenBtn:pressed{\n"
"    \n"
"    background-color: rgb(147, 255, 38);\n"
"}")
        self.FullScreenBtn.setText("")
        self.FullScreenBtn.setObjectName("FullScreenBtn")
        self.horizontalLayout_2.addWidget(self.FullScreenBtn)
        self.ExitBtn = QtWidgets.QPushButton(self.headBarFrame)
        self.ExitBtn.setMinimumSize(QtCore.QSize(15, 15))
        self.ExitBtn.setMaximumSize(QtCore.QSize(15, 15))
        self.ExitBtn.setStyleSheet("#ExitBtn{    \n"
"background-color: rgb(212, 43, 15);\n"
"border-radius:1px;\n"
"}\n"
"#ExitBtn:hover{\n"
"    background-color: rgb(181, 24, 2);\n"
"}\n"
"#ExitBtn:pressed{\n"
"    \n"
"    background-color: rgb(255, 24, 2);\n"
"}")
        self.ExitBtn.setText("")
        self.ExitBtn.setObjectName("ExitBtn")
        self.horizontalLayout_2.addWidget(self.ExitBtn)
        spacerItem1 = QtWidgets.QSpacerItem(4, 19, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addWidget(self.headBarFrame, 0, 0, 1, 2)
        self.menuFrame = QtWidgets.QFrame(self.centralwidget)
        self.menuFrame.setMinimumSize(QtCore.QSize(100, 0))
        self.menuFrame.setMaximumSize(QtCore.QSize(100, 16777215))
        self.menuFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menuFrame.setObjectName("menuFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.menuFrame)
        self.verticalLayout.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.IconLbl_2 = QtWidgets.QLabel(self.menuFrame)
        self.IconLbl_2.setMinimumSize(QtCore.QSize(50, 80))
        self.IconLbl_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.IconLbl_2.setText("")
        self.IconLbl_2.setObjectName("IconLbl_2")
        self.verticalLayout.addWidget(self.IconLbl_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.homeBtn = QtWidgets.QPushButton(self.menuFrame)
        self.homeBtn.setMinimumSize(QtCore.QSize(50, 50))
        self.homeBtn.setObjectName("homeBtn")
        self.verticalLayout.addWidget(self.homeBtn)
        self.noteAddBtn = QtWidgets.QPushButton(self.menuFrame)
        self.noteAddBtn.setMinimumSize(QtCore.QSize(50, 50))
        self.noteAddBtn.setObjectName("noteAddBtn")
        self.verticalLayout.addWidget(self.noteAddBtn)
        self.noteDeleteBtn = QtWidgets.QPushButton(self.menuFrame)
        self.noteDeleteBtn.setMinimumSize(QtCore.QSize(50, 50))
        self.noteDeleteBtn.setObjectName("noteDeleteBtn")
        self.verticalLayout.addWidget(self.noteDeleteBtn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.settingBtn = QtWidgets.QPushButton(self.menuFrame)
        self.settingBtn.setMinimumSize(QtCore.QSize(50, 50))
        self.settingBtn.setObjectName("settingBtn")
        self.verticalLayout.addWidget(self.settingBtn)
        self.gridLayout.addWidget(self.menuFrame, 1, 0, 1, 1)
        self.pageFrame = QtWidgets.QFrame(self.centralwidget)
        self.pageFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pageFrame.setObjectName("pageFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pageFrame)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 6)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.pageFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.HomePage = QtWidgets.QWidget()
        self.HomePage.setObjectName("HomePage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.HomePage)
        self.verticalLayout_3.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.treeWidget = QtWidgets.QTreeWidget(self.HomePage)
        self.treeWidget.setLineWidth(3)
        self.treeWidget.setAutoScrollMargin(30)
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setIndentation(10)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setSortIndicatorShown(False)
        self.verticalLayout_3.addWidget(self.treeWidget)
        self.stackedWidget.addWidget(self.HomePage)
        self.NoteAddPage = QtWidgets.QWidget()
        self.NoteAddPage.setObjectName("NoteAddPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.NoteAddPage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.NoteAddPage)
        self.groupBox.setMinimumSize(QtCore.QSize(440, 45))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.noteNameTbx = QtWidgets.QLineEdit(self.groupBox)
        self.noteNameTbx.setMinimumSize(QtCore.QSize(100, 35))
        self.noteNameTbx.setMaximumSize(QtCore.QSize(100, 16777215))
        self.noteNameTbx.setReadOnly(True)
        self.noteNameTbx.setObjectName("noteNameTbx")
        self.horizontalLayout.addWidget(self.noteNameTbx)
        self.lengthCharacterLbl = QtWidgets.QLabel(self.groupBox)
        self.lengthCharacterLbl.setMinimumSize(QtCore.QSize(110, 0))
        self.lengthCharacterLbl.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lengthCharacterLbl.setObjectName("lengthCharacterLbl")
        self.horizontalLayout.addWidget(self.lengthCharacterLbl)
        self.timeLbl = QtWidgets.QLabel(self.groupBox)
        self.timeLbl.setMinimumSize(QtCore.QSize(140, 0))
        self.timeLbl.setMaximumSize(QtCore.QSize(140, 16777215))
        self.timeLbl.setObjectName("timeLbl")
        self.horizontalLayout.addWidget(self.timeLbl)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.notTextPte = QtWidgets.QPlainTextEdit(self.NoteAddPage)
        self.notTextPte.setStyleSheet("")
        self.notTextPte.setObjectName("notTextPte")
        self.verticalLayout_5.addWidget(self.notTextPte)
        self.addBtn = QtWidgets.QPushButton(self.NoteAddPage)
        self.addBtn.setObjectName("addBtn")
        self.verticalLayout_5.addWidget(self.addBtn)
        self.updateBtn = QtWidgets.QPushButton(self.NoteAddPage)
        self.updateBtn.setObjectName("updateBtn")
        self.verticalLayout_5.addWidget(self.updateBtn)
        self.stackedWidget.addWidget(self.NoteAddPage)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.groupBox_2 = QtWidgets.QGroupBox(self.pageFrame)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.GithubLbl = QtWidgets.QLabel(self.groupBox_2)
        self.GithubLbl.setGeometry(QtCore.QRect(310, 70, 64, 20))
        self.GithubLbl.setStyleSheet("font: italic 9pt \"Century Gothic\";\n"
"color: rgb(245, 245, 245);")
        self.GithubLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.GithubLbl.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.GithubLbl.setObjectName("GithubLbl")
        self.InstagramBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.InstagramBtn.setGeometry(QtCore.QRect(90, 0, 64, 64))
        self.InstagramBtn.setText("")
        self.InstagramBtn.setObjectName("InstagramBtn")
        self.instaLbl = QtWidgets.QLabel(self.groupBox_2)
        self.instaLbl.setGeometry(QtCore.QRect(87, 70, 70, 20))
        self.instaLbl.setStyleSheet("font: italic 9pt \"Century Gothic\";\n"
"color: rgb(245, 245, 245);")
        self.instaLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.instaLbl.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.instaLbl.setObjectName("instaLbl")
        self.GithubBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.GithubBtn.setGeometry(QtCore.QRect(310, 0, 64, 64))
        self.GithubBtn.setText("")
        self.GithubBtn.setObjectName("GithubBtn")
        self.FaceLbl = QtWidgets.QLabel(self.groupBox_2)
        self.FaceLbl.setGeometry(QtCore.QRect(167, 70, 131, 20))
        self.FaceLbl.setStyleSheet("font: italic 9pt \"Century Gothic\";\n"
"color: rgb(245, 245, 245);")
        self.FaceLbl.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.FaceLbl.setObjectName("FaceLbl")
        self.FacebookBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.FacebookBtn.setGeometry(QtCore.QRect(200, 0, 64, 64))
        self.FacebookBtn.setText("")
        self.FacebookBtn.setObjectName("FacebookBtn")
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.copyright = QtWidgets.QLabel(self.pageFrame)
        self.copyright.setStyleSheet("#copyright{\n"
"    font: 75 italic 10pt \"Century Gothic\";\n"
"color: #F53422;\n"
"}")
        self.copyright.setAlignment(QtCore.Qt.AlignCenter)
        self.copyright.setObjectName("copyright")
        self.verticalLayout_2.addWidget(self.copyright)
        self.gridLayout.addWidget(self.pageFrame, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.homeBtn.setIcon(QtGui.QIcon("style/Home.png"))
        self.noteAddBtn.setIcon(QtGui.QIcon("style/add.png"))
        self.noteDeleteBtn.setIcon(QtGui.QIcon("style/delete.png"))
        self.settingBtn.setIcon(QtGui.QIcon("style/setting.png"))
        MainWindow.setWindowIcon(QtGui.QIcon("style/marelogo.ico"))
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Note App | Maresal PRM"))
        self.NameLbl.setText(_translate("MainWindow", "Note App | Maresal PRM"))
        self.homeBtn.setText(_translate("MainWindow", "Anasayfa"))
        self.noteAddBtn.setText(_translate("MainWindow", "Ekle"))
        self.noteDeleteBtn.setText(_translate("MainWindow", "Sil"))
        self.settingBtn.setText(_translate("MainWindow", "Ayarlar"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Not İsmi"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Karakter Sayısı"))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Son Tarih"))
        self.label.setText(_translate("MainWindow", "Not Adı : "))
        self.lengthCharacterLbl.setText(_translate("MainWindow", "Karakter sayısı : "))
        self.timeLbl.setText(_translate("MainWindow", "Zamanı : "))
        self.addBtn.setText(_translate("MainWindow", "Ekle"))
        self.updateBtn.setText(_translate("MainWindow", "Güncelle"))
        self.GithubLbl.setText(_translate("MainWindow", "IMaresaLI"))
        self.instaLbl.setText(_translate("MainWindow", "@maresalp"))
        self.FaceLbl.setText(_translate("MainWindow", "maresalprogramming"))
        self.copyright.setText(_translate("MainWindow", "Copyright ©  Maresal Programming"))
