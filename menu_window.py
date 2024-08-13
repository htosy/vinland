from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QRadioButton, \
    QPushButton, QLabel, QSpinBox, QButtonGroup, QGroupBox, QLineEdit, QApplication
from PyQt5.QtCore import Qt

menu_w = QWidget()

lb_question = QLabel("Введіть запитання:")
lb_right_ans = QLabel("Введіть вірну відповідь:")
lb_wrong_ans1 = QLabel("Введіть першу хибну відповідь:")
lb_wrong_ans2 = QLabel("Введіть другу хибну відповідь:")
lb_wrong_ans3 = QLabel("Введіть третю хибну відповідь:")
le_question = QLineEdit()
le_right_ans = QLineEdit()
le_wrong_ans1 = QLineEdit()
le_wrong_ans2 = QLineEdit()
le_wrong_ans3 = QLineEdit()

lb_head_stat = QLabel("Статистика")
lb_head_stat.setStyleSheet('font-size: 19px; font-weight: bold;')

lb_statistic = QLabel()
v1_labels = QVBoxLayout()
v1_labels.addWidget(lb_question)
v1_labels.addWidget(lb_right_ans)
v1_labels.addWidget(lb_wrong_ans1)
v1_labels.addWidget(lb_wrong_ans2)
v1_labels.addWidget(lb_wrong_ans3)

v1_lineEdits = QVBoxLayout()
v1_lineEdits.addWidget(le_question)
v1_lineEdits.addWidget(le_right_ans)
v1_lineEdits.addWidget(le_wrong_ans1)
v1_lineEdits.addWidget(le_wrong_ans2)
v1_lineEdits.addWidget(le_wrong_ans3)
h1_question = QHBoxLayout()
h1_question.addLayout(v1_labels)
h1_question.addLayout(v1_lineEdits)

btn_back = QPushButton("Назад")
btn_add_ques = QPushButton("Додати запитання")
btn_claer = QPushButton("Очистити")

h1_buttons = QHBoxLayout()
h1_buttons.addWidget(btn_add_ques)
h1_buttons.addWidget(btn_claer)
v1_res = QVBoxLayout()
v1_res.addLayout(h1_question)
v1_res.addLayout(h1_buttons)
v1_res.addWidget(lb_head_stat)
v1_res.addWidget(lb_statistic)
v1_res.addWidget(btn_back)


menu_w.setLayout(v1_res)
menu_w.resize(400,300)