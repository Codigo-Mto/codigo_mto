# importamos librerias de Pyside6 para poder utilizar la GUI realiazda con Pyside6 editor
from PySide6.QtWidgets import QWidget, QFileDialog, QLabel, QLineEdit
from PySide6.QtCore import Qt
# importamos las clases de los scripts components, ui_AddEditWindow y general_custom de la carpeta view
from view.components import MaquinaImg
from view.ui_AddEditWindow import AddEditWindow
from view.general_custom_ui import GeneralCustomUi
from os import getcwd
from PySide6.QtGui import QIcon, QPixmap
# importamos los scrpts maquina y connection de la carpeta database
from database import maquina
from database import connection

import shutil

# esta clase es para anadir nuevos datos en las tablas de la base de datos
class AddWindowForm(QWidget, AddEditWindow ):

    def __init__(self,parent=None):
        super().__init__(parent)
        self.parent = parent
    

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        # dar la funcion de click a los botones seleccionar iamgen y agregar
        self.toolButton.clicked.connect(self.select_img)
        self.add_edit_button.setText("Agregar")
        self.add_edit_button.clicked.connect(self.add_maquina)
        

    # funcion para mover las ventanas con el mouse
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
    # funcion para añadir muna nueva maquina
    def add_maquina(self):

        NOMBRE_MAQUINA= self.lineEdit_3.text()
        SECCION = self.lineEdit_4.text()
        AREA = self.lineEdit_5.text()
        img_path = self.img_path_to
        url_manual= self.lineEdit_6.text() 
       
        # almacenamos los datos de la base de datos en un vector 
        data = (NOMBRE_MAQUINA,SECCION,AREA,img_path,url_manual)
        print("rrrr", data[3])        
        
        a=1
        #if maquina.insert(data):
        if a==1:
            maquina.insert(data)
            self.save_img()
            print("Maquina Added")
            self.clear_inputs()
            self.parent.set_table_data()

    # funcion para seleccionar la imagen del equipo
    def select_img(self):
        self.img_path_from = QFileDialog.getOpenFileName()[0]
        img_name = self.img_path_from.split("/")[-1]
        self.img_path_to = f"recipe_images\{img_name}"
        self.lineEdit_7.setText(img_name)
    # guardar la imagen en la carpeta recipe images
    def save_img(self):
        shutil.copy(self.img_path_from, "recipe_images")
    # limpiar los campos en en formulario addwindowform.
    def clear_inputs(self):
        self.lineEdit_7.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
