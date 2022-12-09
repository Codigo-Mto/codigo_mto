# se importa las funciones de PySide6
from curses import window
import enum
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt
# se importa las clases de los scripts de la carpeta controllers 
from controllers.add_window import AddWindowForm
from controllers.add_window_proveedor import AddWindowForm_proveedor
from controllers.maquina_details_window import DetailWindowForm
from controllers.edit_window import EditWindowForm
#from maquina import select_all
# se importa las clases de los scripts de la carpeta view
from view.ui_main_window import MainWidget
from view.general_custom_ui import GeneralCustomUi
from database import maquina
from maquina import select_all
from view import components
import os
# esta clase contiene la tabla que muestra los datos, los botones de editar borrar y detalles.
class MainwindowForm(QWidget, MainWidget ):

    def __init__(self):
        super().__init__()
        

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        #self.populate_table()
        self.config_table()
        self.set_table_data()
        
        # conecta el Click de los botones con una funcion 
        self.new_recipe_button.clicked.connect(self.open_add_window)
        self.serch_line_edit.returnPressed.connect(self.search)
        self.serch_line_edit.textChanged.connect(self.restore_table_data)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
    # funcion que abre el formulario de adicion de datos
    def open_add_window(self):
        window = AddWindowForm(self)
        window.show()

    # funcion que abre el formulario de mainwindowForm
    def open_main_window(self):
        window = MainwindowForm()
        window.show()
    # funcion que configura la tabla donde se viasualiza los datos contenidos en la base de datos
    def config_table(self):
        column_labels = ("ID", "IMG","AREA","SECCION","NOMBRE_MAQUINA","")
        self.tableWidget.setColumnCount(len(column_labels))
        self.tableWidget.setHorizontalHeaderLabels(column_labels)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(4, 120)
        self.tableWidget.setColumnWidth(5, 120)
        self.tableWidget.verticalHeader().setDefaultSectionSize(150)
        self.tableWidget.setColumnHidden(0, True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        
    # se crea la tabla, teniendo en cuenta la cantidad de datos que existen en la base de datos
    def populate_table(self,data):
        
        #data = maquina.select_all()
        self.tableWidget.setRowCount(len(data))
        
        for(index_row, rows) in enumerate(data):
            for (index_cell, cell) in enumerate(rows):
                # si el index es 1 se coloca la imagen
                if index_cell == 1:
                    self.tableWidget.setCellWidget(
                        index_row, index_cell, components.MaquinaImg(cell)

                    )
                else:
                    self.tableWidget.setItem(
                        index_row, index_cell, QTableWidgetItem(str(cell))
                    )
            # se establece las columnas y filas de la tabla
            self.tableWidget.setCellWidget(
                index_row, 5, self.build_action_buttons()
            )
    # se crea los botones de viwe, edit and delete
    def build_action_buttons(self):
        view_button = components.Button("view", "#17A288")
        edit_button = components.Button("edit", "#007BFF")
        delete_button = components.Button("delete", "#DC3545")

        # se añade botones mediante la funcion addWidget
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(view_button)
        buttons_layout.addWidget(edit_button)
        buttons_layout.addWidget(delete_button)

        buttons_frame = QFrame()
        buttons_frame.setLayout(buttons_layout)
        # se proporciona el evento Click a los botones de view, edit y delete
        view_button.clicked.connect(self.view_maquina)
        edit_button.clicked.connect(self.edit_maquina)
        delete_button.clicked.connect(self.delete_recipe)

        return buttons_frame

    # se establce los datos en la tabla populate
    def set_table_data(self):
        data = maquina.select_all()
        self.populate_table(data)
    # se restaura los datos despues de realizar una busqueda
    def restore_table_data(self):
        param = self.serch_line_edit.text()
        if param == "":
            self.set_table_data()
    # funcion de busqueda de una fila de datos en especifico
    def search(self):
        param = self.serch_line_edit.text()
        print("el parametro esadas",param)
        # si el parametro esta en la base de datos extrae  los datos que contiene
        if param != "":
            data = maquina.select_by_parameter(param)
            print("los datos son",data)
            self.populate_table(data)
    # funcion que abre el formulario de detalles 
    def open_detail_window(self, maquina_id):
        window = DetailWindowForm(self, maquina_id)
        window.show()
    # funcion que abre el formulario de editar
    def open_edit_window(self,maquina_id):
        window = EditWindowForm(self, maquina_id)
        window.show()
    # funcion que abre el formulario de view datos
    def view_maquina(self):
        button = self.sender()
        table = self.tableWidget

        if button:
            maquina_id = self.get_maquina_id_from_table(table, button)
            self.open_detail_window(maquina_id)
    # funcion que abre el formulario de editar dependindo el ID 
    def edit_maquina(self):
        button = self.sender()
        table = self.tableWidget

        if button:
            maquina_id = self.get_maquina_id_from_table(table, button)
            self.open_edit_window(maquina_id)
    # funcion que elimina datos de la base de datos
    def delete_recipe(self):
        button = self.sender()
        table = self.tableWidget

        if button:
            maquina_id = self.get_maquina_id_from_table(table, button)
            data = maquina.select_by_id(maquina_id)
            if maquina.delete(maquina_id):
                # eliminar la imagen de la base de datos  y de la carpeta recipe images
                self.remove_img(data[4])
                self.set_table_data()
    # funcion para remover la imagen
    def remove_img(self,img_path):
        os.remove(img_path)
    # funcion para ubicar los botones dentro de la tabla
    def get_maquina_id_from_table(self, table, button):
        row_index = table.indexAt(button.parent().pos()).row()
        cell_id_index = table.model().index(row_index,0)
        maquina_id = table.model().data(cell_id_index)
        return maquina_id
