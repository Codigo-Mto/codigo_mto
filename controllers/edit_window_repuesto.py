# se importa las clases de la libreria de PySide6
from curses.ascii import CAN
from http.client import ImproperConnectionState
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
# se importa las clases ui_AddEditWindow_repuesto y general_custom_ui de la carpeta de view
from view.ui_AddEditWindow_repuesto import AddEditWindow
from view.general_custom_ui import GeneralCustomUi
# se importa el script maquina de la carpeta database
from database import maquina
import os
import shutil

# se define la clase encargada de editar el formulario
class EditWindowForm_repuesto(QWidget, AddEditWindow):
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
    #funcion para dar el evento click al mouse
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
    #funcion para actualizar  los datos en la base de datos
    def update_maquina(self):


        NOMBRE_REPUESTO = self.lineEdit_3.text()
        CODIGO_REPUESTO = self.lineEdit_4.text()
        TIPO_REPUESTO = self.lineEdit_5.text()
        PRECIO = self.lineEdit_9.text() 
        CANTIDAD = self.lineEdit_6.text()
        LEAD_TIME = self.lineEdit_8.text()
        img_path = f"recipe_images\{self.lineEdit_7.text()}"       
        # se almacena los datos de las lineas de edicion en el vector data
        data = (NOMBRE_REPUESTO,CODIGO_REPUESTO,TIPO_REPUESTO,PRECIO,CANTIDAD,LEAD_TIME,img_path)
        print("rrrr", data)        
        
        a=1
        #if maquina.insert(data):
        if a==1:
            maquina.update_repuesto(self.maquina_id,data)
            self.replace_img()
            print("repuesto edited")
            self.clear_inputs()
            #self.parent.set_table_data()
            self.parent.set_table_data()
            self.close()
               
    # mediante el ID se selecciona los datos para mostrar en la tabla
    def fill_inputs(self):
        data= maquina.select_by_id_repuestos(self.maquina_id)
        print(data)

        self.lineEdit_3.setText(str(data[1]))
        self.lineEdit_4.setText(str(data[2]))
        self.lineEdit_8.setText(str(data[6]))
        self.lineEdit_9.setText(str(data[4]))
        self.lineEdit_5.setText(str(data[3]))
        self.lineEdit_6.setText(str(data[5]))
        
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


    
