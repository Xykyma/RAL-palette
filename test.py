from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QTabWidget, QScrollArea, QLabel
import sys
import json


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry (200, 200, 800, 600)
        self.setWindowTitle("RAL Pallete") 

        main_lauout = QGridLayout()
        self.setLayout(main_lauout)

        # Создаем виджет вкладок
        RAL_tab = QTabWidget(self)

        # Вкладка с Classic
        classic_tab = QWidget(self)

        # Добавляем панель с CLassic
        RAL_tab.addTab(classic_tab, "Classic")

        # Добавляем вертикальную прокрутку
        scroll = QScrollArea(classic_tab)
        scroll_widget = QWidget()
        scroll.setWidget(scroll_widget)
        
        classic_scroll_layout = QGridLayout()
        scroll_widget.setLayout(classic_scroll_layout)

        # Заполняем вкалдку цветами Classic
        with open("Ral_classic.json", "r", encoding="utf-8-sig") as ral_file: 
            ral_data = ral_file.read()

            ral_classic = json.loads(ral_data)

            # Количество столбцов в сетке
            NUM_COLUMNS = 6

            # Прохожу по словарю с RAL и создаю label
            for index, ral in enumerate(ral_classic):
                label = QLabel()
                label.setObjectName(ral["RAL"].replace(" ", ""))
                row = index // NUM_COLUMNS
                col = index % NUM_COLUMNS
                label.setText(f"{ral['RAL']}\n{ral['English']}")
                label.setStyleSheet(f"background-color: {ral['HEX']}")
                label.setFixedSize(120, 120)
                #label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                classic_scroll_layout.addWidget(label, row, col)


        main_lauout.addWidget(RAL_tab, 0, 0, 2, 1)




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())