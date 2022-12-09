from PySide6.QtWidgets import QLabel, QPushButton,QTableWidget
from PySide6.QtGui import QPixmap, QIcon, QCursor, QIcon
from PySide6.QtCore import Qt

class MaquinaImg(QLabel):
    
    def __init__(self,img_path):
        super().__init__()
        #print(img_path)

        self.img = QPixmap(img_path).scaledToWidth(200)
        self.setPixmap(self.img)

class Button(QPushButton):

    def __init__(self, icon, color):
        super().__init__()
        self.setMinimumSize(30,30)
        self.set_cursor()
        self.setIcon(QIcon(f"assets/icons/{icon}.png"))
        self.setStyleSheet(f"border-radius: 15px; background-color: {color};")
    
    def set_cursor(self):
        pointer = QCursor(Qt.PointingHandCursor)
        self.setCursor(pointer)