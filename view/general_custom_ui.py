# importar las funciones de pyside6
from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QGraphicsDropShadowEffect
# clase para mover minimizar cerrar las ventanas del programa.
class GeneralCustomUi():
    def __init__(self,ui ):
        
        self.ui = ui
        self.remove_default_title_bar()
        self.ui.top_frame.mouseMoveEvent = self.move_window
        self.set_title_bar_buttons_actions()
        self.set_window_shadow()
    # funcion para maximizaar la ventana
    def maximize_window(self): 
        self.ui.showMaximized()
        self.ui.maximize_button.setVisible(False)
    # funcion para minimizar la ventana
    def restore_window(self):
        self.ui.showNormal()
        self.ui.maximize_button.setVisible(True)
    # Evento de mover la ventaba al hacer ckick en la barra de la ventana
    def set_title_bar_buttons_actions(self):
        self.ui.close_button.clicked.connect(self.ui.close)
        self.ui.minimize_button.clicked.connect(self.ui.showMinimized)
        self.ui.maximize_button.clicked.connect(self.maximize_window)
        self.ui.restore_button.clicked.connect(self.restore_window)
    # funcion para poner sombra en la ventana
    def set_window_shadow(self):
        shadow = QGraphicsDropShadowEffect(self.ui)
        shadow.setBlurRadius(25)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor("#000000")
        self.ui.background_frame.setGraphicsEffect(shadow)
    # funcion para remover la parte superior de la ventana
    def remove_default_title_bar(self):
        self.ui.setAttribute(Qt.WA_TranslucentBackground, True)
        self.ui.setWindowFlag(Qt.FramelessWindowHint)
    # funcion que proporciona el evento click al mouse
    def mouse_press_event(self, event):
        self.drag_pos = event.globalPos()
    # funcion para mover la ventana
    def move_window(self, event):
        if event.buttons() == Qt.LeftButton:
            self.ui.move(self.ui.pos() + event.globalPos() - self.drag_pos) 
            self.drag_pos = event.globalPos()
    
    