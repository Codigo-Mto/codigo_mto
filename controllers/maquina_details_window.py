# importamos las funciones de pyside6
from unicodedata import category
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
# importamos las clases generalcustomUi y detail_widget de los scripts general_custom_ui y ui_maquina_detail_window 
from view.general_custom_ui import GeneralCustomUi
from view.ui_maquina_detail_window import Detail_widget
# importamos el script maquina de la carpeta database
from database import maquina

# la clase Detailwindowform contiene algunos datos extra de la maquina
class DetailWindowForm(QWidget, Detail_widget):
    def __init__(self, parent=None, maquina_id=None):
        super().__init__(parent)

        self.maquina_id = maquina_id
        print("en maquinas",maquina_id)
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)
        self.fill_widgets()
    # funcion para dar evento al click de mouse
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
    # funcion para llenar los espacios vacios con datos segun el ID
    def fill_widgets(self):
        data = maquina.select_by_id(self.maquina_id)
        title= data[1]
        url = data[5]
        img_path= data [4]
        print("este si",data)
        # Establecer los datos en los labels de detalles
        self.maquine_title_label.setText(title)
        self.set_manual_url(url)
        self.set_maquina_image(img_path)
        
    # funcion para que el url te mande a la pagina web
    def set_manual_url(self,url):
        url = f"<a href={url}>{url}</a>"
        self.maquina_cat_label.setOpenExternalLinks(True)
        self.maquina_cat_label.setText(url)
    # funcion para establecer la imagen
    def set_maquina_image (self, img_path):
        pix_map = QPixmap(img_path)
        self.maquina_pic_label.setPixmap(pix_map)
        self.maquina_pic_label.setScaledContents(True)