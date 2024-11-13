# MALLIPOHJA QT-SOVELUSTEN RAKENTAMISEEN PySide6-KIRJASTON AVULLA
# ===============================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ==================================

# Järjestelmäkomentojen kirjasto
import sys

# Pyside-kirjastot
from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QApplication # Käyttöliittymän elementit (kaikki), korvaa listalla
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

# LUOKKAMÄÄRITYKSET
# -----------------

# Pääikkunan luokka, joka perii QMainWindow-luokan
class MainWindow(QMainWindow):

    # Konstruktori
    def __init__(self):
        super().__init__(self)

        # Luodaan käyttöliittymän lataaja
        windowLoader = QUiLoader()

        # Annetaan sille käyttöliittymätiedosto

        window = windowLoader.load('mainWindow.ui', None)
        self.setWindowTitle('Hippopotamus')

if __name__ == "__main__":
    application = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(application.exec())