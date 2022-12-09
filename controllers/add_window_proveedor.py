from PySide6.QtWidgets import QWidget, QFileDialog, QLabel, QLineEdit
from PySide6.QtCore import Qt
from view.ui_AddEditWindow_proveedor import AddEditWindow
from view.general_custom_ui import GeneralCustomUi

from os import getcwd
from PySide6.QtGui import QIcon, QPixmap
from database import maquina
from database import connection

import shutil


class AddWindowForm_proveedor(QWidget, AddEditWindow):

    def __init__(self,parent=None):
        
        super().__init__(parent)
        self.parent = parent
        
      

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)

       
        self.add_edit_button.setText("Agregar")
        self.add_edit_button.clicked.connect(self.add_maquina)
        

    

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def add_maquina(self):

        EMPRESA= self.lineEdit.text()
        PERSONA_DE_CONTACTO = self.lineEdit_3.text()
        DIRECCION = self.lineEdit_4.text()
        CORREO_ELECTRONICO = self.lineEdit_5.text()
        TELEFONO= self.lineEdit_6.text()
        PAGINA_WEB= self.lineEdit_7.text()
        TIPO_PROVEEDOR= self.lineEdit_8.text()

        data = (EMPRESA,PERSONA_DE_CONTACTO, DIRECCION,CORREO_ELECTRONICO,TELEFONO,PAGINA_WEB,TIPO_PROVEEDOR)
        #print("rrrr", data[3])        

        a=1
        #if maquina.insert(data):
        if a==1:
            maquina.insert_proveedor(data)
            print("proveedor Added")
            
            self.clear_inputs()
            self.parent.set_table_data()
            


    def clear_inputs(self):
        self.lineEdit_8.clear()
        self.lineEdit_7.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit.clear()
