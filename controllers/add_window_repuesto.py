from curses.ascii import CAN
from http.client import PRECONDITION_FAILED
from PySide6.QtWidgets import QWidget, QFileDialog, QLabel, QLineEdit
from PySide6.QtCore import Qt
from view.components import MaquinaImg
from view.ui_AddEditWindow_repuesto import AddEditWindow
from view.general_custom_ui import GeneralCustomUi
from os import getcwd
from PySide6.QtGui import QIcon, QPixmap
from database import maquina
from database import connection

import shutil


class AddWindowForm_repuesto(QWidget, AddEditWindow ):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.parent = parent
    

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)

        self.toolButton.clicked.connect(self.select_img)
        self.add_edit_button.setText("Agregar")
        self.add_edit_button.clicked.connect(self.add_maquina)
        


    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def add_maquina(self):

        NOMBRE_REPUESTO= self.lineEdit_3.text()
        CODIGO_REPUESTO = self.lineEdit_4.text()
        TIPO_REPUESTO = self.lineEdit_5.text()
        PRECIO = self.lineEdit_9.text() 
        CANTIDAD = self.lineEdit_6.text()
        LEAD_TIME = self.lineEdit_8.text()
        img_path = self.img_path_to
        
       

        data = (NOMBRE_REPUESTO,CODIGO_REPUESTO,TIPO_REPUESTO,PRECIO,CANTIDAD,LEAD_TIME,img_path)
        print("personal", data[3])        
        
        a=1
        #if maquina.insert(data):
        if a==1:
            maquina.insert_repuestos(data)
            self.save_img()
            print("repuesto Added")
            self.clear_inputs()
            
            self.parent.set_table_data()
            
    def select_img(self):
        self.img_path_from = QFileDialog.getOpenFileName()[0]
        img_name = self.img_path_from.split("/")[-1]
        self.img_path_to = f"recipe_images\{img_name}"
        self.lineEdit_7.setText(img_name)

    def save_img(self):
        shutil.copy(self.img_path_from, "recipe_images")

    def clear_inputs(self):
        self.lineEdit_7.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()
