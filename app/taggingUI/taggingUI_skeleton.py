# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taggingUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_taggingTool(object):
    def setupUi(self, MainWindow_taggingTool):
        MainWindow_taggingTool.setObjectName("MainWindow_taggingTool")
        MainWindow_taggingTool.resize(651, 595)
        self.centralwidget = QtWidgets.QWidget(MainWindow_taggingTool)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_general = QtWidgets.QGridLayout()
        self.gridLayout_general.setObjectName("gridLayout_general")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1gram = QtWidgets.QWidget()
        self.tab_1gram.setObjectName("tab_1gram")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_1gram)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_1gram_general = QtWidgets.QGridLayout()
        self.gridLayout_1gram_general.setObjectName("gridLayout_1gram_general")
        self.horizontalSlider_1gram_FindingThreshold = QtWidgets.QSlider(self.tab_1gram)
        self.horizontalSlider_1gram_FindingThreshold.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_1gram_FindingThreshold.setObjectName("horizontalSlider_1gram_FindingThreshold")
        self.gridLayout_1gram_general.addWidget(self.horizontalSlider_1gram_FindingThreshold, 2, 1, 1, 1)
        self.verticalLayout_1gram_SimilarityPattern = QtWidgets.QVBoxLayout()
        self.verticalLayout_1gram_SimilarityPattern.setObjectName("verticalLayout_1gram_SimilarityPattern")
        self.gridLayout_1gram_general.addLayout(self.verticalLayout_1gram_SimilarityPattern, 1, 1, 1, 1)
        self.label_1gram_PatternFindingDescription = QtWidgets.QLabel(self.tab_1gram)
        self.label_1gram_PatternFindingDescription.setObjectName("label_1gram_PatternFindingDescription")
        self.gridLayout_1gram_general.addWidget(self.label_1gram_PatternFindingDescription, 0, 1, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_1gram_PropertyEditorDescription = QtWidgets.QLabel(self.tab_1gram)
        self.label_1gram_PropertyEditorDescription.setObjectName("label_1gram_PropertyEditorDescription")
        self.gridLayout_1gram_general.addWidget(self.label_1gram_PropertyEditorDescription, 0, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_1gram_TableTagDescription = QtWidgets.QLabel(self.tab_1gram)
        self.label_1gram_TableTagDescription.setObjectName("label_1gram_TableTagDescription")
        self.gridLayout_1gram_general.addWidget(self.label_1gram_TableTagDescription, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_1gram_PropertiesEditor = QtWidgets.QVBoxLayout()
        self.verticalLayout_1gram_PropertiesEditor.setObjectName("verticalLayout_1gram_PropertiesEditor")
        self.label_1gram_AliasDescription = QtWidgets.QLabel(self.tab_1gram)
        self.label_1gram_AliasDescription.setObjectName("label_1gram_AliasDescription")
        self.verticalLayout_1gram_PropertiesEditor.addWidget(self.label_1gram_AliasDescription)
        self.lineEdit_1gram_AliasEditor = QtWidgets.QLineEdit(self.tab_1gram)
        self.lineEdit_1gram_AliasEditor.setObjectName("lineEdit_1gram_AliasEditor")
        self.verticalLayout_1gram_PropertiesEditor.addWidget(self.lineEdit_1gram_AliasEditor)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_1gram_PropertiesEditor.addItem(spacerItem)
        self.radioButton_1gram_ItemEditor = QtWidgets.QRadioButton(self.tab_1gram)
        self.radioButton_1gram_ItemEditor.setObjectName("radioButton_1gram_ItemEditor")
        self.buttonGroup_1Gram_Classification = QtWidgets.QButtonGroup(MainWindow_taggingTool)
        self.buttonGroup_1Gram_Classification.setObjectName("buttonGroup_1Gram_Classification")
        self.buttonGroup_1Gram_Classification.addButton(self.radioButton_1gram_ItemEditor)
        self.verticalLayout_1gram_PropertiesEditor.addWidget(self.radioButton_1gram_ItemEditor)
        self.radioButton_1gram_ProblemEditor = QtWidgets.QRadioButton(self.tab_1gram)
        self.radioButton_1gram_ProblemEditor.setObjectName("radioButton_1gram_ProblemEditor")
        self.buttonGroup_1Gram_Classification.addButton(self.radioButton_1gram_ProblemEditor)
        self.verticalLayout_1gram_PropertiesEditor.addWidget(self.radioButton_1gram_ProblemEditor)
        self.radioButton_1gram_SolutionEditor = QtWidgets.QRadioButton(self.tab_1gram)
        self.radioButton_1gram_SolutionEditor.setObjectName("radioButton_1gram_SolutionEditor")
        self.buttonGroup_1Gram_Classification.addButton(self.radioButton_1gram_SolutionEditor)
        self.verticalLayout_1gram_PropertiesEditor.addWidget(self.radioButton_1gram_SolutionEditor)
        self.radioButton_1gram_UnknownEditor = QtWidgets.QRadioButton(self.tab_1gram)
        self.radioButton_1gram_UnknownEditor.setObjectName("radioButton_1gram_UnknownEditor")
        self.buttonGroup_1Gram_Classification.addButton(self.radioButton_1gram_UnknownEditor)
        self.verticalLayout_1gram_PropertiesEditor.addWidget(self.radioButton_1gram_UnknownEditor)
        self.radioButton_1gram_StopWordEditor = QtWidgets.QRadioButton(self.tab_1gram)
        self.radioButton_1gram_StopWordEditor.setObjectName("radioButton_1gram_StopWordEditor")
        self.buttonGroup_1Gram_Classification.addButton(self.radioButton_1gram_StopWordEditor)
        self.verticalLayout_1gram_PropertiesEditor.addWidget(self.radioButton_1gram_StopWordEditor)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_1gram_PropertiesEditor.addItem(spacerItem1)
        self.radioButton_1gram_NotClassifiedEditor = QtWidgets.QRadioButton(self.tab_1gram)
        self.radioButton_1gram_NotClassifiedEditor.setObjectName("radioButton_1gram_NotClassifiedEditor")
        self.buttonGroup_1Gram_Classification.addButton(self.radioButton_1gram_NotClassifiedEditor)
        self.verticalLayout_1gram_PropertiesEditor.addWidget(self.radioButton_1gram_NotClassifiedEditor)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_1gram_PropertiesEditor.addItem(spacerItem2)
        self.label_1gram_NoteDescription = QtWidgets.QLabel(self.tab_1gram)
        self.label_1gram_NoteDescription.setObjectName("label_1gram_NoteDescription")
        self.verticalLayout_1gram_PropertiesEditor.addWidget(self.label_1gram_NoteDescription)
        self.textEdit_1gram_NoteEditor = QtWidgets.QTextEdit(self.tab_1gram)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_1gram_NoteEditor.sizePolicy().hasHeightForWidth())
        self.textEdit_1gram_NoteEditor.setSizePolicy(sizePolicy)
        self.textEdit_1gram_NoteEditor.setMaximumSize(QtCore.QSize(16777215, 50))
        self.textEdit_1gram_NoteEditor.setTabChangesFocus(False)
        self.textEdit_1gram_NoteEditor.setLineWrapColumnOrWidth(4)
        self.textEdit_1gram_NoteEditor.setObjectName("textEdit_1gram_NoteEditor")
        self.verticalLayout_1gram_PropertiesEditor.addWidget(self.textEdit_1gram_NoteEditor)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_1gram_PropertiesEditor.addItem(spacerItem3)
        self.gridLayout_1gram_general.addLayout(self.verticalLayout_1gram_PropertiesEditor, 1, 2, 1, 1)
        self.tableWidget_1gram_TagContainer = QtWidgets.QTableWidget(self.tab_1gram)
        self.tableWidget_1gram_TagContainer.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget_1gram_TagContainer.setTabKeyNavigation(False)
        self.tableWidget_1gram_TagContainer.setDragDropOverwriteMode(False)
        self.tableWidget_1gram_TagContainer.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_1gram_TagContainer.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_1gram_TagContainer.setObjectName("tableWidget_1gram_TagContainer")
        self.tableWidget_1gram_TagContainer.setColumnCount(0)
        self.tableWidget_1gram_TagContainer.setRowCount(0)
        self.gridLayout_1gram_general.addWidget(self.tableWidget_1gram_TagContainer, 1, 0, 1, 1)
        self.gridLayout_1gram_ActionButton = QtWidgets.QGridLayout()
        self.gridLayout_1gram_ActionButton.setObjectName("gridLayout_1gram_ActionButton")
        self.pushButton_1gram_UpdateTokenProperty = QtWidgets.QPushButton(self.tab_1gram)
        self.pushButton_1gram_UpdateTokenProperty.setObjectName("pushButton_1gram_UpdateTokenProperty")
        self.gridLayout_1gram_ActionButton.addWidget(self.pushButton_1gram_UpdateTokenProperty, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_1gram_SaveTableView = QtWidgets.QPushButton(self.tab_1gram)
        self.pushButton_1gram_SaveTableView.setObjectName("pushButton_1gram_SaveTableView")
        self.gridLayout_1gram_ActionButton.addWidget(self.pushButton_1gram_SaveTableView, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_1gram_general.addLayout(self.gridLayout_1gram_ActionButton, 2, 2, 1, 1)
        self.progressBar_1gram_TagComplete = QtWidgets.QProgressBar(self.tab_1gram)
        self.progressBar_1gram_TagComplete.setProperty("value", 24)
        self.progressBar_1gram_TagComplete.setObjectName("progressBar_1gram_TagComplete")
        self.gridLayout_1gram_general.addWidget(self.progressBar_1gram_TagComplete, 2, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_1gram_general, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_1gram, "")
        self.tab_Ngram = QtWidgets.QWidget()
        self.tab_Ngram.setObjectName("tab_Ngram")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_Ngram)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_Ngram_general = QtWidgets.QGridLayout()
        self.gridLayout_Ngram_general.setObjectName("gridLayout_Ngram_general")
        self.label_Ngram_TableTagDescription = QtWidgets.QLabel(self.tab_Ngram)
        self.label_Ngram_TableTagDescription.setObjectName("label_Ngram_TableTagDescription")
        self.gridLayout_Ngram_general.addWidget(self.label_Ngram_TableTagDescription, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.tableWidget_Ngram_TagContainer = QtWidgets.QTableWidget(self.tab_Ngram)
        self.tableWidget_Ngram_TagContainer.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget_Ngram_TagContainer.setTabKeyNavigation(False)
        self.tableWidget_Ngram_TagContainer.setDragDropOverwriteMode(False)
        self.tableWidget_Ngram_TagContainer.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_Ngram_TagContainer.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_Ngram_TagContainer.setObjectName("tableWidget_Ngram_TagContainer")
        self.tableWidget_Ngram_TagContainer.setColumnCount(0)
        self.tableWidget_Ngram_TagContainer.setRowCount(0)
        self.tableWidget_Ngram_TagContainer.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_Ngram_TagContainer.verticalHeader().setStretchLastSection(False)
        self.gridLayout_Ngram_general.addWidget(self.tableWidget_Ngram_TagContainer, 1, 0, 1, 1)
        self.label_Ngram_PropertyEditorDescription = QtWidgets.QLabel(self.tab_Ngram)
        self.label_Ngram_PropertyEditorDescription.setObjectName("label_Ngram_PropertyEditorDescription")
        self.gridLayout_Ngram_general.addWidget(self.label_Ngram_PropertyEditorDescription, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_Ngram_CompositionDisplay = QtWidgets.QVBoxLayout()
        self.verticalLayout_Ngram_CompositionDisplay.setObjectName("verticalLayout_Ngram_CompositionDisplay")
        self.gridLayout_Ngram_general.addLayout(self.verticalLayout_Ngram_CompositionDisplay, 1, 1, 1, 1)
        self.label_Ngram_CompositionDescription = QtWidgets.QLabel(self.tab_Ngram)
        self.label_Ngram_CompositionDescription.setObjectName("label_Ngram_CompositionDescription")
        self.gridLayout_Ngram_general.addWidget(self.label_Ngram_CompositionDescription, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.verticalLayout_Ngram_PropertiesEditor = QtWidgets.QVBoxLayout()
        self.verticalLayout_Ngram_PropertiesEditor.setObjectName("verticalLayout_Ngram_PropertiesEditor")
        self.label_Ngram_AliasDescription = QtWidgets.QLabel(self.tab_Ngram)
        self.label_Ngram_AliasDescription.setObjectName("label_Ngram_AliasDescription")
        self.verticalLayout_Ngram_PropertiesEditor.addWidget(self.label_Ngram_AliasDescription)
        self.lineEdit_Ngram_AliasEditor = QtWidgets.QLineEdit(self.tab_Ngram)
        self.lineEdit_Ngram_AliasEditor.setObjectName("lineEdit_Ngram_AliasEditor")
        self.verticalLayout_Ngram_PropertiesEditor.addWidget(self.lineEdit_Ngram_AliasEditor)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_Ngram_PropertiesEditor.addItem(spacerItem4)
        self.radioButton_Ngram_ItemEditor = QtWidgets.QRadioButton(self.tab_Ngram)
        self.radioButton_Ngram_ItemEditor.setObjectName("radioButton_Ngram_ItemEditor")
        self.buttonGroup_NGram_Classification = QtWidgets.QButtonGroup(MainWindow_taggingTool)
        self.buttonGroup_NGram_Classification.setObjectName("buttonGroup_NGram_Classification")
        self.buttonGroup_NGram_Classification.addButton(self.radioButton_Ngram_ItemEditor)
        self.verticalLayout_Ngram_PropertiesEditor.addWidget(self.radioButton_Ngram_ItemEditor)
        self.radioButton_Ngram_ProblemItemEditor = QtWidgets.QRadioButton(self.tab_Ngram)
        self.radioButton_Ngram_ProblemItemEditor.setObjectName("radioButton_Ngram_ProblemItemEditor")
        self.buttonGroup_NGram_Classification.addButton(self.radioButton_Ngram_ProblemItemEditor)
        self.verticalLayout_Ngram_PropertiesEditor.addWidget(self.radioButton_Ngram_ProblemItemEditor)
        self.radioButton_Ngram_SolutionItemEditor = QtWidgets.QRadioButton(self.tab_Ngram)
        self.radioButton_Ngram_SolutionItemEditor.setObjectName("radioButton_Ngram_SolutionItemEditor")
        self.buttonGroup_NGram_Classification.addButton(self.radioButton_Ngram_SolutionItemEditor)
        self.verticalLayout_Ngram_PropertiesEditor.addWidget(self.radioButton_Ngram_SolutionItemEditor)
        self.radioButton_Ngram_UnknownEditor = QtWidgets.QRadioButton(self.tab_Ngram)
        self.radioButton_Ngram_UnknownEditor.setObjectName("radioButton_Ngram_UnknownEditor")
        self.buttonGroup_NGram_Classification.addButton(self.radioButton_Ngram_UnknownEditor)
        self.verticalLayout_Ngram_PropertiesEditor.addWidget(self.radioButton_Ngram_UnknownEditor)
        self.radioButton_Ngram_StopWordEditor = QtWidgets.QRadioButton(self.tab_Ngram)
        self.radioButton_Ngram_StopWordEditor.setObjectName("radioButton_Ngram_StopWordEditor")
        self.buttonGroup_NGram_Classification.addButton(self.radioButton_Ngram_StopWordEditor)
        self.verticalLayout_Ngram_PropertiesEditor.addWidget(self.radioButton_Ngram_StopWordEditor)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_Ngram_PropertiesEditor.addItem(spacerItem5)
        self.radioButton_Ngram_NotClassifiedEditor = QtWidgets.QRadioButton(self.tab_Ngram)
        self.radioButton_Ngram_NotClassifiedEditor.setObjectName("radioButton_Ngram_NotClassifiedEditor")
        self.buttonGroup_NGram_Classification.addButton(self.radioButton_Ngram_NotClassifiedEditor)
        self.verticalLayout_Ngram_PropertiesEditor.addWidget(self.radioButton_Ngram_NotClassifiedEditor)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_Ngram_PropertiesEditor.addItem(spacerItem6)
        self.label_Ngram_NoteDescription = QtWidgets.QLabel(self.tab_Ngram)
        self.label_Ngram_NoteDescription.setObjectName("label_Ngram_NoteDescription")
        self.verticalLayout_Ngram_PropertiesEditor.addWidget(self.label_Ngram_NoteDescription)
        self.textEdit_Ngram_NoteEditor = QtWidgets.QTextEdit(self.tab_Ngram)
        self.textEdit_Ngram_NoteEditor.setMaximumSize(QtCore.QSize(16777215, 50))
        self.textEdit_Ngram_NoteEditor.setObjectName("textEdit_Ngram_NoteEditor")
        self.verticalLayout_Ngram_PropertiesEditor.addWidget(self.textEdit_Ngram_NoteEditor)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_Ngram_PropertiesEditor.addItem(spacerItem7)
        self.gridLayout_Ngram_general.addLayout(self.verticalLayout_Ngram_PropertiesEditor, 1, 2, 1, 1)
        self.progressBar_Ngram_TagComplete = QtWidgets.QProgressBar(self.tab_Ngram)
        self.progressBar_Ngram_TagComplete.setProperty("value", 24)
        self.progressBar_Ngram_TagComplete.setObjectName("progressBar_Ngram_TagComplete")
        self.gridLayout_Ngram_general.addWidget(self.progressBar_Ngram_TagComplete, 2, 0, 1, 1, QtCore.Qt.AlignBottom)
        self.gridLayout_Ngram_ActionButton = QtWidgets.QGridLayout()
        self.gridLayout_Ngram_ActionButton.setObjectName("gridLayout_Ngram_ActionButton")
        self.pushButton_Ngram_UpdateTokenProperty = QtWidgets.QPushButton(self.tab_Ngram)
        self.pushButton_Ngram_UpdateTokenProperty.setObjectName("pushButton_Ngram_UpdateTokenProperty")
        self.gridLayout_Ngram_ActionButton.addWidget(self.pushButton_Ngram_UpdateTokenProperty, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_Ngram_SaveTableView = QtWidgets.QPushButton(self.tab_Ngram)
        self.pushButton_Ngram_SaveTableView.setObjectName("pushButton_Ngram_SaveTableView")
        self.gridLayout_Ngram_ActionButton.addWidget(self.pushButton_Ngram_SaveTableView, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_Ngram_general.addLayout(self.gridLayout_Ngram_ActionButton, 2, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_Ngram_general, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_Ngram, "")
        self.gridLayout_general.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_general, 0, 0, 1, 1)
        MainWindow_taggingTool.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_taggingTool)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 22))
        self.menubar.setObjectName("menubar")
        MainWindow_taggingTool.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_taggingTool)
        self.statusbar.setObjectName("statusbar")
        MainWindow_taggingTool.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_taggingTool)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_taggingTool)

    def retranslateUi(self, MainWindow_taggingTool):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_taggingTool.setWindowTitle(_translate("MainWindow_taggingTool", "MainWindow"))
        self.label_1gram_PatternFindingDescription.setText(_translate("MainWindow_taggingTool", "Similar Pattern"))
        self.label_1gram_PropertyEditorDescription.setText(_translate("MainWindow_taggingTool", "Property Editor"))
        self.label_1gram_TableTagDescription.setText(_translate("MainWindow_taggingTool", "Tag Annotation"))
        self.label_1gram_AliasDescription.setText(_translate("MainWindow_taggingTool", "Preferred Alias"))
        self.radioButton_1gram_ItemEditor.setText(_translate("MainWindow_taggingTool", "Item"))
        self.radioButton_1gram_ProblemEditor.setText(_translate("MainWindow_taggingTool", "Problem"))
        self.radioButton_1gram_SolutionEditor.setText(_translate("MainWindow_taggingTool", "Solution"))
        self.radioButton_1gram_UnknownEditor.setText(_translate("MainWindow_taggingTool", "Ambiguous (Unknown)"))
        self.radioButton_1gram_StopWordEditor.setText(_translate("MainWindow_taggingTool", "Stop-word"))
        self.radioButton_1gram_NotClassifiedEditor.setText(_translate("MainWindow_taggingTool", "not yet classified"))
        self.label_1gram_NoteDescription.setText(_translate("MainWindow_taggingTool", "Notes"))
        self.pushButton_1gram_UpdateTokenProperty.setText(_translate("MainWindow_taggingTool", "Update"))
        self.pushButton_1gram_SaveTableView.setText(_translate("MainWindow_taggingTool", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1gram), _translate("MainWindow_taggingTool", "1 Gram Token"))
        self.label_Ngram_TableTagDescription.setText(_translate("MainWindow_taggingTool", "Tag Annotation"))
        self.label_Ngram_PropertyEditorDescription.setText(_translate("MainWindow_taggingTool", "Property Editor"))
        self.label_Ngram_CompositionDescription.setText(_translate("MainWindow_taggingTool", "Composition"))
        self.label_Ngram_AliasDescription.setText(_translate("MainWindow_taggingTool", "Preferred Alias"))
        self.radioButton_Ngram_ItemEditor.setText(_translate("MainWindow_taggingTool", "Item"))
        self.radioButton_Ngram_ProblemItemEditor.setText(_translate("MainWindow_taggingTool", "Problem Item"))
        self.radioButton_Ngram_SolutionItemEditor.setText(_translate("MainWindow_taggingTool", "Solution Item"))
        self.radioButton_Ngram_UnknownEditor.setText(_translate("MainWindow_taggingTool", "Ambiguous (Unknown)"))
        self.radioButton_Ngram_StopWordEditor.setText(_translate("MainWindow_taggingTool", "Stop-word"))
        self.radioButton_Ngram_NotClassifiedEditor.setText(_translate("MainWindow_taggingTool", "not yet classified"))
        self.label_Ngram_NoteDescription.setText(_translate("MainWindow_taggingTool", "Notes"))
        self.pushButton_Ngram_UpdateTokenProperty.setText(_translate("MainWindow_taggingTool", "Update"))
        self.pushButton_Ngram_SaveTableView.setText(_translate("MainWindow_taggingTool", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Ngram), _translate("MainWindow_taggingTool", "N Gram Token"))

