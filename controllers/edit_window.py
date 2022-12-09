# importarmos las librerias de PySide6 
from http.client import ImproperConnectionState
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt
# importamos las clases de los scripts ui addeditwindow y general custom ui de la carpeta view
from view.ui_AddEditWindow import AddEditWindow
from view.general_custom_ui import GeneralCustomUi
# importamos el script maquina de la carpeta database
from database import maquina
import os
import shutil

# esta clase edita los datos que metimos en la base de datos
class EditWindowForm(QWidget, AddEditWindow):
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
    # funsion que da accion al mouse
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
    # funcion para actualizar los datos de la base de datos
    def update_maquina(self):

        # las variables toman el valor de las lineas de edicion y lo guarda en un vector data
        NOMBRE_MAQUINA= self.lineEdit_3.text()
        SECCION = self.lineEdit_4.text()
        AREA = self.lineEdit_5.text()
        img_path = f"recipe_images\{self.lineEdit_7.text()}"
        url_manual= self.lineEdit_6.text()
       

        data = (NOMBRE_MAQUINA,AREA, SECCION,img_path,url_manual)
        print("rrrr", data[3])        
        
        a=1
        #if maquina.insert(data):
        if a==1:
            maquina.update(self.maquina_id,data)
            self.replace_img()
            print("Maquina edited")
            self.clear_inputs()
            #self.parent.set_table_data()
            self.parent.set_table_data()
            self.close()
               
    # funcion que rellena los datos en los espacios del GUi mediante la ID
    def fill_inputs(self):
        data= maquina.select_by_id(self.maquina_id)

        self.lineEdit_3.setText(data[1])
        self.lineEdit_4.setText(data[2])
        self.lineEdit_5.setText(data[3])
        img_name = data[4].split("\\")[-1]

        self.old_image = img_name
        self.new_img = img_name

        self.lineEdit_7.setText(img_name)
        self.lineEdit_6.setText(data[5])
        
    # funcion para insertar imagen desde la computadora
    def select_img(self):
        self.img_path_from = QFileDialog.getOpenFileName()[0]

        if self.img_path_from:
            self.new_img = self.img_path_from.split("/")[-1]
            self.lineEdit_7.setText(self.new_img)

    # remplazar la imagen antigua por otra imagen nueva
    def replace_img(self):
        if self.old_image != self.new_img:
            os.remove("recipe_images\\" + self.old_image)
            shutil.copy(self.img_path_from,"recipe_images")
    # limpiar las entradas de los campos de editar datos
    def clear_inputs(self):
        self.lineEdit_7.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()

    
