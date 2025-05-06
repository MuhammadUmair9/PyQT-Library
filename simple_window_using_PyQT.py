import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Hello World')
window.setGeometry(100, 100, 280, 80)

label = QLabel('Hello First App', parent=window)
window.show()

sys.exit(app.exec_())