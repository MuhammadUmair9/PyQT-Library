import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QComboBox,  QCheckBox, QRadioButton, QComboBox, QVBoxLayout, QMessageBox)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Large Form Example")
window.setGeometry(100, 100, 400, 500)

name_label = QLabel("Full Name:") 
name_input = QLineEdit()

email_label = QLabel("Email:") 
email_input = QLineEdit()

phone_label = QLabel("Phone:")
phone_input = QLineEdit()

gender_label = QLabel("Gender:")

radio1 = QRadioButton("Male")
radio2 = QRadioButton("Female")
radio3 = QRadioButton("other")
gender_male = radio1
gender_female = radio2
gender_other = radio3 

country_label = QLabel("Country:")
country_combo = QComboBox()
country_combo.addItems(["Select", "USA", "UK", "Canada", "Pakistan", "India"])

subcribe_checkbox = QCheckBox("subscribe to newsletter")
conditon_checkbox = QCheckBox("I agree to the Terms and Conditions")

about_label = QLabel("About Yourself:") 
about_input = QTextEdit()

button = QPushButton("Submit")


button.clicked.connect(lambda: QMessageBox.information(
    window,
    "Form Result",
    f"Name: {name_label.text()}\n"
    f"Email: {email_label.text()}\n"
    f"Phone: {phone_label.text()}\n"
    f"Gender: {'Male' if radio1.isChecked() else 'Female' if radio2.isChecked() else 'other' if radio3.isChecked() else 'Not selected'}\n"
    f"Country: {country_label.text()}\n"
    f"Subcribed: {'Yes' if subcribe_checkbox.isChecked() else 'No'}"
    f"Agree to term: {'Yes' if subcribe_checkbox.isChecked() else 'No'}"
    f"About: {about_input.text()}\n"
))

layout = QVBoxLayout()
layout.addWidget(name_label)
layout.addWidget(email_label)
layout.addWidget(phone_label)
layout.addWidget(gender_label)
layout.addWidget(radio1)
layout.addWidget(radio2)
layout.addWidget(radio3)
layout.addWidget(button)

layout.addWidget(country_label)

layout.addWidget(subcribe_checkbox)
layout.addWidget(conditon_checkbox)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())
