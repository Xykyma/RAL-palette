import json
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        
        super().__init__()

        # Загружаем форму
        uic.loadUi('form.ui', self)

        self.fill_classic_pallete()

        self.setFixedSize(self.sizeHint().width(), 600)

        print(f"Size Policy: {self.sizePolicy()}")
        print(f"Size Hint: {self.sizeHint()}")
        print(f"Actual Size: {self.size()}")


    # Заполняем вкалдку цветами Classic
    def fill_classic_pallete(self):
        with open("Ral_classic.json", "r", encoding="utf-8-sig") as ral_file: 
            ral_data = ral_file.read()

            ral_classic = json.loads(ral_data)

            # Количество столбцов в сетке
            NUM_COLUMNS = 6

            # Прохожу по словарю с RAL и создаю label
            for index, ral in enumerate(ral_classic):
                label = QLabel(self.classic_scroll_widget)
                label.setObjectName(ral["RAL"].replace(" ", ""))
                row = index // NUM_COLUMNS
                col = index % NUM_COLUMNS
                label.setText(f"{ral['RAL']}\n{ral['English']}")
                label.setStyleSheet(f"background-color: {ral['HEX']}")
                label.setFixedSize(120, 120)
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.classic_grid.addWidget(label, row, col)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())