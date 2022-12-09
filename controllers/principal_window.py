# importamos funciones de pyside6
from curses import window
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
# importamos la clase mainwindowform_repuesto del scrip main_window_repuesto de la carpeta controllers 
from controllers.main_window_repuesto import MainwindowForm_repuesto
# importamos las clases MainwindowForm_proveedor, MainwindowForm_personal, MainwindowForm_repuesto de los scripts
# main_window_proveedor, main_window_personal, main_window_repuesto
from main_window_proveedor import MainwindowForm_proveedor
from main_window_personal import MainwindowForm_personal
from main_window_repuesto import MainwindowForm_repuesto
from main_window import MainwindowForm
# importar las clases InicioWidget, generalCustomUi de los scripts ui_ventana1 y general_custom_ui
from view.ui_ventana1 import InicioWidget
from view.general_custom_ui import GeneralCustomUi
# creamos la clase principal para que sea el formulario principal al ejecutar el programa
class PrincipalwindowForm(QWidget, InicioWidget ):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        # permite crear la conexion de los botones con las funciones
        self.maquina_button.clicked.connect(self.open_main_window)
        self.proveedor_button.clicked.connect(self.open_main_window_proveedor)
        self.personal_button.clicked.connect(self.open_main_window_personal)
        self.repuesto_button.clicked.connect(self.open_main_window_repuestos)
    # funcion para que el mouse interactue con las ventanas 
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    # funcion para abrir el formulario de maquina
    def open_main_window(self):
        window = MainwindowForm()
        window.show()
    # funcion para abrir el formulario de proveedor
    def open_main_window_proveedor(self):
        window = MainwindowForm_proveedor()
        window.show()
    # funcion para abrir el formulario de personal
    def open_main_window_personal(self):
        window = MainwindowForm_personal()
        window.show()
    # funcion para abrir el formulario de repuestos
    def open_main_window_repuestos(self):
        window = MainwindowForm_repuesto()
        window.show()

