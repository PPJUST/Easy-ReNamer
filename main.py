from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')
    show_ui = MainWindow()
    show_ui.setFixedSize(800, 530)
    show_ui.show()
    app.exec()
