from curses import window
import enum
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout,QFrame
from PySide6.QtCore import Qt

from add_window_proveedor import AddWindowForm_proveedor
from view.ui_main_window_proveedor import MainWidget
from view.general_custom_ui import GeneralCustomUi
from maquina_details_window import DetailWindowForm
from database import maquina
from view import components
#from maquina import select_all

class MainwindowForm_proveedor(QWidget, MainWidget):

    def __init__(self):
        super().__init__()
        

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        #self.populate_table()
        self.config_table()
        self.set_table_data()
        
        
        
        self.new_recipe_button.clicked.connect(self.open_add_window_proveedor)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def open_add_window_proveedor(self):
        window = AddWindowForm_proveedor()
        window.show()

    def open_main_window_proveedor(self):
        window = MainwindowForm_proveedor()
        window.show()

    def config_table(self):
        column_labels = ("ID", "EMPRESA","PERSONA DE CONTACTO","DIRECCION","TELEFONO","PAGINA WEB","")
        self.tableWidget.setColumnCount(len(column_labels))
        self.tableWidget.setHorizontalHeaderLabels(column_labels)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 200)
        self.tableWidget.setColumnWidth(5, 100)
        self.tableWidget.setColumnWidth(6, 100)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.setColumnHidden(0, True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        

    def populate_table(self,data):
        
        data = maquina.select_all_proveedro()
        self.tableWidget.setRowCount(len(data))
        
        for(index_row, rows) in enumerate(data):
            for (index_cell, cell) in enumerate(rows):
                self.tableWidget.setItem(
                        index_row, index_cell, QTableWidgetItem(str(cell))
                    )
                
    
                self.tableWidget.setCellWidget(
                    index_row, 5, self.build_action_buttons()
            )

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
     
        return buttons_frame


    def set_table_data(self):
        data = maquina.select_all_proveedro()
        self.populate_table(data)

    def search(self):
        param = self.serch_line_edit.text()
        print("el parametro esadas",param)
        if param != "":
            data = maquina.select_by_parameter_proveedor(param)
            print("los datos son",data)
            self.populate_table(data)


    def get_maquina_id_from_table(self, table, button):
        row_index = table.indexAt(button.parent().pos()).row()
        cell_id_index = table.model().index(row_index,0)
        maquina_id = table.model().data(cell_id_index)
        return maquina_id