# Se importa todas librerias de PySide6
import sys 
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QLineEdit
# Se importa la clase PrincipalwindowForm del script principal_window de la carpeta controllers
from controllers.principal_window import PrincipalwindowForm

#ejecuta todo el programa, se llama a la ventana de inicio, llamada PrincipalwindowForm
if __name__ == '__main__':
    app= QApplication()
    window= PrincipalwindowForm()
    window.show()
    sys.exit(app.exec()) 