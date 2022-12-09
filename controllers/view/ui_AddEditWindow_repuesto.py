# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddEditWindow_repuesto.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class AddEditWindow(object):
    def setupUi(self, AddEditWindow):
        if not AddEditWindow.objectName():
            AddEditWindow.setObjectName(u"AddEditWindow")
        AddEditWindow.resize(770, 527)
        self.verticalLayout = QVBoxLayout(AddEditWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_frame = QFrame(AddEditWindow)
        self.central_frame.setObjectName(u"central_frame")
        self.central_frame.setFrameShape(QFrame.StyledPanel)
        self.central_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.central_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: rgb(255, 220, 215)")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.top_frame = QFrame(self.background_frame)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(0, 40))
        self.top_frame.setMaximumSize(QSize(16777215, 40))
        self.top_frame.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.title_label = QLabel(self.top_frame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMinimumSize(QSize(120, 30))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(14)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"color: white\n"
"")

        self.horizontalLayout_3.addWidget(self.title_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.buttons_holder_frame = QFrame(self.top_frame)
        self.buttons_holder_frame.setObjectName(u"buttons_holder_frame")
        self.buttons_holder_frame.setMinimumSize(QSize(110, 30))
        self.buttons_holder_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_holder_frame.setFrameShadow(QFrame.Raised)
        self.minimize_button = QToolButton(self.buttons_holder_frame)
        self.minimize_button.setObjectName(u"minimize_button")
        self.minimize_button.setGeometry(QRect(10, 0, 21, 22))
        icon = QIcon()
        icon.addFile(u"../../icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(25, 25))
        self.restore_button = QToolButton(self.buttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(50, 0, 21, 22))
        icon1 = QIcon()
        icon1.addFile(u"../../icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon1)
        self.restore_button.setIconSize(QSize(25, 25))
        self.maximize_button = QToolButton(self.buttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(50, 0, 21, 22))
        icon2 = QIcon()
        icon2.addFile(u"../../icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setIconSize(QSize(25, 25))
        self.close_button = QToolButton(self.buttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(90, 0, 21, 22))
        icon3 = QIcon()
        icon3.addFile(u"../../icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)


        self.verticalLayout_2.addWidget(self.top_frame)

        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.content_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 50, 131, 16))
        self.lineEdit_3 = QLineEdit(self.content_frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(80, 80, 200, 30))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid red;")
        self.label_4 = QLabel(self.content_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 130, 151, 16))
        self.lineEdit_4 = QLineEdit(self.content_frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(80, 160, 200, 30))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid red;")
        self.label_5 = QLabel(self.content_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 210, 71, 16))
        self.lineEdit_5 = QLineEdit(self.content_frame)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(80, 240, 200, 30))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid red;")
        self.label_6 = QLabel(self.content_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(420, 50, 131, 16))
        self.lineEdit_6 = QLineEdit(self.content_frame)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(420, 80, 200, 30))
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid red;")
        self.label_7 = QLabel(self.content_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(420, 130, 161, 16))
        self.lineEdit_7 = QLineEdit(self.content_frame)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(420, 160, 151, 30))
        self.lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid red;")
        self.toolButton = QToolButton(self.content_frame)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(580, 160, 31, 31))
        icon4 = QIcon()
        icon4.addFile(u"../../icons/open-file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon4)
        self.add_edit_button = QPushButton(self.content_frame)
        self.add_edit_button.setObjectName(u"add_edit_button")
        self.add_edit_button.setGeometry(QRect(320, 370, 85, 30))
        self.add_edit_button.setStyleSheet(u"QPushButton{background-color: rgb(170, 0, 0);\n"
"color: white;}\n"
"QPushButton::hover{background-color:#ffc13b}")
        icon5 = QIcon()
        icon5.addFile(u"../../icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_edit_button.setIcon(icon5)
        self.lineEdit_8 = QLineEdit(self.content_frame)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(420, 240, 200, 30))
        self.lineEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid red;")
        self.label_8 = QLabel(self.content_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(420, 210, 71, 16))
        self.lineEdit_9 = QLineEdit(self.content_frame)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(80, 320, 200, 30))
        self.lineEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid red;")
        self.label_9 = QLabel(self.content_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(80, 290, 71, 16))

        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_frame)


        self.retranslateUi(AddEditWindow)

        QMetaObject.connectSlotsByName(AddEditWindow)
    # setupUi

    def retranslateUi(self, AddEditWindow):
        AddEditWindow.setWindowTitle(QCoreApplication.translate("AddEditWindow", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("AddEditWindow", u"DATOS DE REPUESTO", None))
        self.minimize_button.setText(QCoreApplication.translate("AddEditWindow", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("AddEditWindow", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("AddEditWindow", u"...", None))
        self.close_button.setText(QCoreApplication.translate("AddEditWindow", u"...", None))
        self.label_3.setText(QCoreApplication.translate("AddEditWindow", u"NOMBRE REPUESTO", None))
        self.label_4.setText(QCoreApplication.translate("AddEditWindow", u"CODIGO DE REPUESTO", None))
        self.label_5.setText(QCoreApplication.translate("AddEditWindow", u"TIPO REPUESTO", None))
        self.label_6.setText(QCoreApplication.translate("AddEditWindow", u"CANTIDAD", None))
        self.label_7.setText(QCoreApplication.translate("AddEditWindow", u"SELECCIONE UNA IMAGEN", None))
        self.toolButton.setText(QCoreApplication.translate("AddEditWindow", u"...", None))
        self.add_edit_button.setText(QCoreApplication.translate("AddEditWindow", u"text", None))
        self.label_8.setText(QCoreApplication.translate("AddEditWindow", u"LEAD TIME", None))
        self.label_9.setText(QCoreApplication.translate("AddEditWindow", u"PRECIO", None))
    # retranslateUi

