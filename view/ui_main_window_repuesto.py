# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_repuesto.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)


class MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(770, 527)
        MainWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(MainWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(MainWidget)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setAutoFillBackground(False)
        self.central_widget_frame.setStyleSheet(u"background-color: rgb(255, 220, 215)\n"
"\n"
"")
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.central_widget_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setAutoFillBackground(False)
        self.background_frame.setStyleSheet(u"")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setStyleSheet(u"")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.top_frame = QFrame(self.content_frame)
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
        icon.addFile(u"./../icons/minimize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(25, 25))
        self.restore_button = QToolButton(self.buttons_holder_frame)
        self.restore_button.setObjectName(u"restore_button")
        self.restore_button.setGeometry(QRect(50, 0, 21, 22))
        icon1 = QIcon()
        icon1.addFile(u"./../icons/restore-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_button.setIcon(icon1)
        self.restore_button.setIconSize(QSize(25, 25))
        self.maximize_button = QToolButton(self.buttons_holder_frame)
        self.maximize_button.setObjectName(u"maximize_button")
        self.maximize_button.setGeometry(QRect(50, 0, 21, 22))
        icon2 = QIcon()
        icon2.addFile(u"./../icons/maximize-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize_button.setIcon(icon2)
        self.maximize_button.setIconSize(QSize(25, 25))
        self.close_button = QToolButton(self.buttons_holder_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(90, 0, 21, 22))
        icon3 = QIcon()
        icon3.addFile(u"./../icons/close-window.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon3)
        self.close_button.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.buttons_holder_frame)


        self.verticalLayout_4.addWidget(self.top_frame)

        self.action_frame = QFrame(self.content_frame)
        self.action_frame.setObjectName(u"action_frame")
        self.action_frame.setMinimumSize(QSize(0, 39))
        self.action_frame.setFrameShape(QFrame.StyledPanel)
        self.action_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.action_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.new_recipe_button = QPushButton(self.action_frame)
        self.new_recipe_button.setObjectName(u"new_recipe_button")
        self.new_recipe_button.setMinimumSize(QSize(150, 30))
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.new_recipe_button.setFont(font1)
        self.new_recipe_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(170, 0, 0);\n"
"	color: white\n"
"}\n"
"QPushButton::hover {background-color: rgb(0, 170, 255)};")
        icon4 = QIcon()
        icon4.addFile(u"./../icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_recipe_button.setIcon(icon4)
        self.new_recipe_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.new_recipe_button)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label = QLabel(self.action_frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(30, 30))
        self.label.setMaximumSize(QSize(30, 16777215))
        self.label.setStyleSheet(u"background-color: white;\n"
"border-radius: 0px;")
        self.label.setPixmap(QPixmap(u"./../icons/search.png"))

        self.horizontalLayout.addWidget(self.label)

        self.serch_line_edit = QLineEdit(self.action_frame)
        self.serch_line_edit.setObjectName(u"serch_line_edit")
        self.serch_line_edit.setMinimumSize(QSize(0, 30))
        self.serch_line_edit.setMaximumSize(QSize(500, 16777215))
        self.serch_line_edit.setStyleSheet(u"background-color: white;\n"
"border-radius: 0px;")

        self.horizontalLayout.addWidget(self.serch_line_edit)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.action_frame)

        self.pushButton = QPushButton(self.content_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(100, 200))
        font3 = QFont()
        font3.setPointSize(12)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_4.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.tableWidget = QTableWidget(self.content_frame)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_4.addWidget(self.tableWidget)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(MainWidget)

        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("MainWidget", u"REPUESTOS DE MANTENIMIENTO", None))
        self.minimize_button.setText(QCoreApplication.translate("MainWidget", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("MainWidget", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("MainWidget", u"...", None))
        self.close_button.setText(QCoreApplication.translate("MainWidget", u"...", None))
        self.new_recipe_button.setText(QCoreApplication.translate("MainWidget", u"Nuevo Repuesto", None))
        self.label.setText("")
        self.serch_line_edit.setText("")
        self.serch_line_edit.setPlaceholderText(QCoreApplication.translate("MainWidget", u"Buscar Repuesto", None))
        self.pushButton.setText(QCoreApplication.translate("MainWidget", u"Actualizar", None))
    # retranslateUi

