from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication()
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(255, 255, 255))
    app.setPalette(palette)
    show_ui = MainWindow()
    show_ui.setMinimumSize(800, 530)
    show_ui.show()
    app.exec()
