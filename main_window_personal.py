from curses import window
import enum
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout,QFrame
from PySide6.QtCore import Qt
# Se importa las clases AddWindowForm, AddWindowForm_personal y EditWindowForm_personal de 
# la carpeta controllers
from controllers.add_window import AddWindowForm
from controllers.add_window_personal import AddWindowForm_personal
from controllers.edit_window_personal import EditWindowForm_personal
# Se importa las clases MainWidget, GeneralCustomUi de la carpeta view
from view.ui_main_window_personal import MainWidget
from view.general_custom_ui import GeneralCustomUi
# Se importa la clase DetailWindowForm de la carpeta controllers
from controllers.maquina_details_window import DetailWindowForm
# Se importa el script de la carpeta database
from database import maquina
# Se importa el script de la carpeta view
from view import components
# Se importa la funcion select_all_personal del script maquina
from maquina import select_all_personal

# Se crea la clase MainwindowForm_personal el cual contiene el formulario principal para llenar datos del personal
class MainwindowForm_personal(QWidget, MainWidget ):

    def __init__(self):
        super().__init__()
        

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.config_table()
        self.set_table_data()
        
        
        # Se conecta el Click del botton para que ejecute una funcion
        self.new_recipe_button.clicked.connect(self.open_add_window)
        self.serch_line_edit.returnPressed.connect(self.search)
        self.serch_line_edit.textChanged.connect(self.restore_table_data)
        self.pushButton.clicked.connect(self.set_table_data)

    # Funcion para que el Click del mouse funcione 
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
    # llama a la clase AddWindowForm_personal
    def open_add_window(self):
        window = AddWindowForm_personal()
        window.show()
    # llama ala clase open_main_window    
    def open_main_window(self):
        window = MainwindowForm_personal()
        window.show()
    # Se configura la tabla para visualizar los datos que contiene la base de datos
    def config_table(self):
        column_labels = ("ID", "IMG","NOMBRE","TELEFONO","DIRECCION","CARGO","ESPECIALIDAD","FECHA DE NACIMIENTO","")
        self.tableWidget.setColumnCount(len(column_labels))
        self.tableWidget.setHorizontalHeaderLabels(column_labels)
        # configura el tamano de las box de la tabla de visualizacion de los datos
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(4, 120)
        self.tableWidget.setColumnWidth(5, 120)
        self.tableWidget.setColumnWidth(7, 200)
        self.tableWidget.verticalHeader().setDefaultSectionSize(150)
        self.tableWidget.setColumnHidden(0, True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        
    # se organiza la tabla de viasualizacion
    def populate_table(self,data):
        
        #data = maquina.select_all_personal()
        self.tableWidget.setRowCount(len(data))
        
        for(index_row, rows) in enumerate(data):
            for (index_cell, cell) in enumerate(rows):
                if index_cell == 1:
                    self.tableWidget.setCellWidget(
                        index_row, index_cell, components.MaquinaImg(cell)

                    )
                else:
                    self.tableWidget.setItem(
                        index_row, index_cell, QTableWidgetItem(str(cell))
                    )
            self.tableWidget.setCellWidget(
                index_row, 8, self.build_action_buttons()
            )
    # se crea botones de editar y borrar
    def build_action_buttons(self):
        #view_button = components.Button("view", "#17A288")
        edit_button = components.Button("edit", "#007BFF")
        delete_button = components.Button("delete", "#DC3545")

        buttons_layout = QHBoxLayout()
        #buttons_layout.addWidget(view_button)
        buttons_layout.addWidget(edit_button)
        buttons_layout.addWidget(delete_button)

        buttons_frame = QFrame()
        buttons_frame.setLayout(buttons_layout)

        #view_button.clicked.connect(self.view_maquina)
        delete_button.clicked.connect(self.delete_recipe)
        edit_button.clicked.connect(self.edit_maquina)

        return buttons_frame
    # funcion de borrado de una fila de datos de la tabla y la base de datos
    def delete_recipe(self):
        button = self.sender()
        table = self.tableWidget

        if button:
            maquina_id = self.get_maquina_id_from_table(table, button)
            data = maquina.select_by_id_personal(maquina_id)
            if maquina.delete_personal(maquina_id):
                
                self.set_table_data()

    # funcion que selecciona los datos de la base de datos y lo establece en la tabla populate
    def set_table_data(self):
        data = maquina.select_all_personal()
        self.populate_table(data)
    # funcion que restaura los datos de la tabla despues de buscar un dato en especifico 
    def restore_table_data(self):
        param = self.serch_line_edit.text()
        if param == "":
            self.set_table_data()
    # funcion de busqueda en la base de datos
    def search(self):
        param = self.serch_line_edit.text()
        print("el parametro esadas",param)
        if param != "":
            data = maquina.select_by_parameter_personal(param)
            print("los datos son",data)
            self.populate_table(data)
    # funcion que abre el formulario de detalles 
    def open_detail_window(self, maquina_id):
        window = DetailWindowForm(self, maquina_id)
        window.show()
    # funcion que abre el formulario de editar datos
    def open_edit_window(self,maquina_id):
        window = EditWindowForm_personal(self, maquina_id)
        window.show()
    # funcion que abre el formulario de visualizacion de datos
    def view_maquina(self):
        button = self.sender()
        table = self.tableWidget

        if button:
            maquina_id = self.get_maquina_id_from_table(table, button)
            self.open_detail_window(maquina_id)
    # funcion que proporciona el boton la capacidad de ejecutar el formulario de editar datos
    def edit_maquina(self):
        button = self.sender()
        table = self.tableWidget

        if button:
            maquina_id = self.get_maquina_id_from_table(table, button)
            self.open_edit_window(maquina_id)
    # funcion para optener el ID de la tabla 
    def get_maquina_id_from_table(self, table, button):
        row_index = table.indexAt(button.parent().pos()).row()
        cell_id_index = table.model().index(row_index,0)
        maquina_id = table.model().data(cell_id_index)
        return maquina_id