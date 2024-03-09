import json
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Загружаем форму
        uic.loadUi('form.ui', self)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())

with open("Ral_classic.json", "r", encoding="utf-8-sig") as ral_file: 
    ral_data = ral_file.read()

ral_classic = json.loads(ral_data)

for ral in ral_classic:
    print(f"RAL number - {ral['RAL']}")
    print(f"HEX number - {ral['HEX']}")
    print(f"RAL name - {ral['English']}")