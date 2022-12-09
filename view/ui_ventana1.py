# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana1.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)
import rc_resources_from_qt

class InicioWidget(object):
    def setupUi(self, InicioWidget):
        if not InicioWidget.objectName():
            InicioWidget.setObjectName(u"InicioWidget")
        InicioWidget.resize(770, 527)
        InicioWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(InicioWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(InicioWidget)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setAutoFillBackground(False)
        self.central_widget_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
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
        self.action_frame.setStyleSheet(u"background-image: url(:/images/fondo2.jpg);")
        self.action_frame.setFrameShape(QFrame.StyledPanel)
        self.action_frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.action_frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(240, 80, 241, 271))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.maquina_button = QPushButton(self.layoutWidget)
        self.maquina_button.setObjectName(u"maquina_button")
        self.maquina_button.setMinimumSize(QSize(150, 40))
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.maquina_button.setFont(font1)
        self.maquina_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 85, 127);\n"
"	color: white\n"
"}\n"
"QPushButton::hover {background-color: rgb(0, 170, 255)};")
        icon4 = QIcon()
        icon4.addFile(u"./../icons/engrane.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.maquina_button.setIcon(icon4)
        self.maquina_button.setIconSize(QSize(20, 20))

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.maquina_button)

        self.proveedor_button = QPushButton(self.layoutWidget)
        self.proveedor_button.setObjectName(u"proveedor_button")
        self.proveedor_button.setMinimumSize(QSize(150, 40))
        self.proveedor_button.setFont(font1)
        self.proveedor_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 85, 127);\n"
"	color: white\n"
"}\n"
"QPushButton::hover {background-color: rgb(0, 170, 255)};")
        self.proveedor_button.setIcon(icon4)
        self.proveedor_button.setIconSize(QSize(20, 20))

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.proveedor_button)

        self.repuesto_button = QPushButton(self.layoutWidget)
        self.repuesto_button.setObjectName(u"repuesto_button")
        self.repuesto_button.setMinimumSize(QSize(150, 40))
        self.repuesto_button.setFont(font1)
        self.repuesto_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 85, 127);\n"
"	color: white\n"
"}\n"
"QPushButton::hover {background-color: rgb(0, 170, 255)};")
        self.repuesto_button.setIcon(icon4)
        self.repuesto_button.setIconSize(QSize(20, 20))

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.repuesto_button)

        self.orde_trabajo_button = QPushButton(self.layoutWidget)
        self.orde_trabajo_button.setObjectName(u"orde_trabajo_button")
        self.orde_trabajo_button.setMinimumSize(QSize(150, 40))
        self.orde_trabajo_button.setFont(font1)
        self.orde_trabajo_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 85, 127);\n"
"	color: white\n"
"}\n"
"QPushButton::hover {background-color: rgb(0, 170, 255)};")
        self.orde_trabajo_button.setIcon(icon4)
        self.orde_trabajo_button.setIconSize(QSize(20, 20))

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.orde_trabajo_button)

        self.personal_button = QPushButton(self.layoutWidget)
        self.personal_button.setObjectName(u"personal_button")
        self.personal_button.setMinimumSize(QSize(150, 40))
        self.personal_button.setFont(font1)
        self.personal_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 85, 127);\n"
"	color: white\n"
"}\n"
"QPushButton::hover {background-color: rgb(0, 170, 255)};")
        self.personal_button.setIcon(icon4)
        self.personal_button.setIconSize(QSize(20, 20))

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.personal_button)


        self.verticalLayout_4.addWidget(self.action_frame)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(InicioWidget)

        QMetaObject.connectSlotsByName(InicioWidget)
    # setupUi

    def retranslateUi(self, InicioWidget):
        InicioWidget.setWindowTitle(QCoreApplication.translate("InicioWidget", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("InicioWidget", u"SISTEMA MANTENIMIENTO", None))
        self.minimize_button.setText(QCoreApplication.translate("InicioWidget", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("InicioWidget", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("InicioWidget", u"...", None))
        self.close_button.setText(QCoreApplication.translate("InicioWidget", u"...", None))
        self.maquina_button.setText(QCoreApplication.translate("InicioWidget", u"MAQUINA", None))
        self.proveedor_button.setText(QCoreApplication.translate("InicioWidget", u"PROVEEDOR", None))
        self.repuesto_button.setText(QCoreApplication.translate("InicioWidget", u"REPUESTO", None))
        self.orde_trabajo_button.setText(QCoreApplication.translate("InicioWidget", u"ORDEN DE TRABAJO", None))
        self.personal_button.setText(QCoreApplication.translate("InicioWidget", u"PERSONAL", None))
    # retranslateUi

