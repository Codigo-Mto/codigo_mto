from http.client import ImproperConnectionState
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt

from view.ui_AddEditWindow_personal import AddEditWindow
from view.general_custom_ui import GeneralCustomUi

from database import maquina
import os
import shutil


class EditWindowForm_personal(QWidget, AddEditWindow):
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
        self.toolButton.clicked.connect(self.select_img)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def update_maquina(self):


        NOMBRE= self.lineEdit_3.text()
        TELEFONO = self.lineEdit_4.text()
        DIRECCION = self.lineEdit_6.text()
        CARGO = self.lineEdit_8.text() 
        ESPECIALIDAD = self.lineEdit_9.text()
        FECHA_DE_NACIMIENTO= self.lineEdit_5.text()
        img_path = f"recipe_images\{self.lineEdit_7.text()}"       

        data = (NOMBRE,TELEFONO,DIRECCION,CARGO,ESPECIALIDAD,FECHA_DE_NACIMIENTO,img_path)
        print("normal data", data)        
        
        a=1
        #if maquina.insert(data):
        if a==1:
            maquina.update_personal(self.maquina_id,data)
            self.replace_img()
            print("personal edited")
            self.clear_inputs()
            #self.parent.set_table_data()
            self.parent.set_table_data()
            self.close()
               

    def fill_inputs(self):
        data= maquina.select_by_id_personal(self.maquina_id)
        print("fill imputs",data)

        self.lineEdit_3.setText(data[1])
        self.lineEdit_4.setText(data[2])
        self.lineEdit_8.setText(data[4])
        self.lineEdit_9.setText(data[5])
        self.lineEdit_5.setText(data[6])
        self.lineEdit_6.setText(data[3])
        
        img_name = data[7].split("\\")[-1]

        self.old_image = img_name
        self.new_img = img_name

        self.lineEdit_7.setText(img_name)
        
    def select_img(self):
        self.img_path_from = QFileDialog.getOpenFileName()[0]

        if self.img_path_from:
            self.new_img = self.img_path_from.split("/")[-1]
            self.lineEdit_7.setText(self.new_img)


    def replace_img(self):
        if self.old_image != self.new_img:
            os.remove("recipe_images\\" + self.old_image)
            shutil.copy(self.img_path_from,"recipe_images")

    def clear_inputs(self):
        self.lineEdit_7.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()


    
