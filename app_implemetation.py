import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QRadioButton, QVBoxLayout, QMessageBox)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Simple Form")
window.setGeometry(100, 100, 300, 200)

label = QLabel("Enter your name:") 
input_field = QLineEdit()

checkbox = QCheckBox("subscribe to newsletter")

radio1 = QRadioButton("Male")
radio2 = QRadioButton("Female")

button = QPushButton("Submit")

button.clicked.connect(lambda: QMessageBox.information(
    window,
    "Form Result",
    f"Name: {input_field.text()}\n"
    f"Gender: {'Male' if radio1.isChecked() else 'Female' if radio2.isChecked() else 'Not selected'}\n"
    f"Subcribed: {'Yes' if checkbox.isChecked() else 'No'}"
))

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(input_field)
layout.addWidget(checkbox)
layout.addWidget(radio1)
layout.addWidget(radio2)
layout.addWidget(button)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
