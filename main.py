import json
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Загружаем форму
        uic.loadUi('form.ui', self)

        self.fill_classic_pallete()


    # Заполняем вкалдку цветами Classic
    def fill_classic_pallete(self):
        with open("Ral_classic.json", "r", encoding="utf-8-sig") as ral_file: 
            ral_data = ral_file.read()

            ral_classic = json.loads(ral_data)

            classic_grid = QGridLayout(self.Classic_tab)

            # Количество столбцов
            num_columns = 6

            # Прохожу по словарю с RAL и создаю label
            for index, ral in enumerate(ral_classic):
                label = QLabel(parent=self.Classic_tab)
                label.setObjectName(ral["RAL"].replace(" ", ""))
                row = index // num_columns
                col = index % num_columns
                label.setText(f"{ral['RAL']}\n{ral['English']}")
                label.setStyleSheet(f"background-color: {ral['HEX']}")
                classic_grid.addWidget(label, row, col)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())