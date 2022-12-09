from http.client import ImproperConnectionState
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt

from view.ui_AddEditWindow_proveedor import AddEditWindow
from view.general_custom_ui import GeneralCustomUi

from database import maquina
import os
import shutil


class EditWindowForm_proveedor(QWidget, AddEditWindow):
    def __init__(self, parent=None, maquina_id=None):
        self.maquina_id = maquina_id
        self.parent = parent

        super().__init__(parent)
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        #self.ui.fill_category_cb()
        self.fill_inputs()
        self.add_edit_button.setText("Editar")
        self.add_edit_button.clicked.connect(self.update_maquina)
        

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def update_maquina(self):


        EMPRESA = self.lineEdit.text()
        PERSONA_DE_CONTACTO = self.lineEdit_3.text()
        DIRECCION = self.lineEdit_4.text()
        CORREO_ELECTRONICO = self.lineEdit_5.text() 
        TELEFONO = self.lineEdit_6.text()
        PAGINA_WEB = self.lineEdit_7.text()
        TIPO_PROVEEDOR =self.lineEdit_8.text() 
             

        data = (EMPRESA,PERSONA_DE_CONTACTO,DIRECCION,CORREO_ELECTRONICO,TELEFONO,PAGINA_WEB,TIPO_PROVEEDOR)
        print("normal data", data)        
        
        a=1
        #if maquina.insert(data):
        if a==1:
            maquina.update_proveedor(self.maquina_id,data)
            print("personal edited")
            self.clear_inputs()
            self.parent.set_table_data()
            self.close()
               

    def fill_inputs(self):
        data= maquina.select_by_id_proveedor(self.maquina_id)
        print("fill imputs",data)

        self.lineEdit.setText(data[1])
        self.lineEdit_3.setText(data[2])
        self.lineEdit_4.setText(data[3])
        self.lineEdit_5.setText(data[4])

        self.lineEdit_6.setText(data[5])
        self.lineEdit_7.setText(data[6])
        self.lineEdit_8.setText(data[7])
        

    def clear_inputs(self):
        self.lineEdit_7.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_8.clear()
    


    
