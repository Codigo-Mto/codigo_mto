# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maquina_detail_window.ui'
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
    QPlainTextEdit, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Detail_widget(object):
    def setupUi(self, Detail_widget):
        if not Detail_widget.objectName():
            Detail_widget.setObjectName(u"Detail_widget")
        Detail_widget.resize(770, 527)
        self.verticalLayout = QVBoxLayout(Detail_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(Detail_widget)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setFrameShape(QFrame.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Raised)
        self.shadow_layout = QVBoxLayout(self.central_widget_frame)
        self.shadow_layout.setSpacing(0)
        self.shadow_layout.setObjectName(u"shadow_layout")
        self.shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.background_frame = QFrame(self.central_widget_frame)
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


        self.verticalLayout_2.addWidget(self.top_frame)

        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.content_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 150))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.maquina_pic_label = QLabel(self.frame)
        self.maquina_pic_label.setObjectName(u"maquina_pic_label")
        self.maquina_pic_label.setMaximumSize(QSize(170, 170))

        self.horizontalLayout.addWidget(self.maquina_pic_label)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.maquine_title_label = QLabel(self.frame_3)
        self.maquine_title_label.setObjectName(u"maquine_title_label")
        self.maquine_title_label.setGeometry(QRect(60, 10, 191, 16))
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.maquine_title_label.setFont(font1)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 50, 151, 16))
        self.maquina_cat_label = QLabel(self.frame_3)
        self.maquina_cat_label.setObjectName(u"maquina_cat_label")
        self.maquina_cat_label.setGeometry(QRect(240, 50, 241, 16))
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 90, 151, 16))
        self.maquina_fecha_label = QLabel(self.frame_3)
        self.maquina_fecha_label.setObjectName(u"maquina_fecha_label")
        self.maquina_fecha_label.setGeometry(QRect(240, 90, 241, 16))

        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.content_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(230, 18, 221, 211))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_3)

        self.sub_text_edit = QPlainTextEdit(self.layoutWidget)
        self.sub_text_edit.setObjectName(u"sub_text_edit")

        self.verticalLayout_4.addWidget(self.sub_text_edit)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.shadow_layout.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(Detail_widget)

        QMetaObject.connectSlotsByName(Detail_widget)
    # setupUi

    def retranslateUi(self, Detail_widget):
        Detail_widget.setWindowTitle(QCoreApplication.translate("Detail_widget", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("Detail_widget", u"SISTEMA MANTENIMIENTO", None))
        self.minimize_button.setText(QCoreApplication.translate("Detail_widget", u"...", None))
        self.restore_button.setText(QCoreApplication.translate("Detail_widget", u"...", None))
        self.maximize_button.setText(QCoreApplication.translate("Detail_widget", u"...", None))
        self.close_button.setText(QCoreApplication.translate("Detail_widget", u"...", None))
        self.maquina_pic_label.setText("")
        self.maquine_title_label.setText(QCoreApplication.translate("Detail_widget", u"NOMBRE MAQUINA", None))
        self.label.setText(QCoreApplication.translate("Detail_widget", u"Manual de la maquina:", None))
        self.maquina_cat_label.setText(QCoreApplication.translate("Detail_widget", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Detail_widget", u"Fecha Mantenimiento:", None))
        self.maquina_fecha_label.setText(QCoreApplication.translate("Detail_widget", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Detail_widget", u"SUBSISTEMAS", None))
    # retranslateUi

