from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QRadioButton, \
    QPushButton, QLabel, QSpinBox, QButtonGroup, QGroupBox, QApplication
from PyQt5.QtCore import Qt

window = QWidget()

btn_menu = QPushButton("Меню")
btn_rest = QPushButton("Відпочити")
btn_next = QPushButton("Відповісти")

rb_ans1 = QRadioButton("1")
rb_ans2 = QRadioButton("2")
rb_ans3 = QRadioButton("3")
rb_ans4 = QRadioButton("4")
rbGroup = QButtonGroup()
rbGroup.addButton(rb_ans1)
rbGroup.addButton(rb_ans2)
rbGroup.addButton(rb_ans3)
rbGroup.addButton(rb_ans4)

lb_question = QLabel("Запитання")
lb_rest = QLabel("хвилин")
lb_rightAns = QLabel("відповідь")
lb_result = QLabel("Вірно!")

sp_rest = QSpinBox()
gbAns = QGroupBox("Варіанти відповідей")

rb_v1 = QVBoxLayout()
rb_v2 = QVBoxLayout()
rb_h = QHBoxLayout()

rb_v1.addWidget(rb_ans1)
rb_v1.addWidget(rb_ans2)
rb_v2.addWidget(rb_ans3)
rb_v2.addWidget(rb_ans4)

rb_h.addLayout(rb_v1)
rb_h.addLayout(rb_v2)
gbAns.setLayout(rb_h)

gb_result = QGroupBox()
v1 = QVBoxLayout()
v1.addWidget(lb_result)
v1.addWidget(lb_rightAns)
gb_result.setLayout(v1)

h1_main = QHBoxLayout()
h2_main = QHBoxLayout()
h3_main = QHBoxLayout()
h4_main = QHBoxLayout()
h1_main.addWidget(btn_menu)
h1_main.addStretch(1)
h1_main.addWidget(btn_rest)
h1_main.addWidget(sp_rest)
h1_main.addWidget(lb_rest)

h2_main.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

h3_main.addWidget(gbAns)
h3_main.addWidget(gb_result)
gb_result.hide()
h4_main.addStretch(1)
h4_main.addWidget(btn_next)
h4_main.addStretch(1)

v1_main = QVBoxLayout()
v1_main.addLayout(h1_main, stretch= 1)
v1_main.addLayout(h2_main, stretch= 2)
v1_main.addLayout(h3_main, stretch= 8)
v1_main.addLayout(h4_main)
v1_main.setSpacing(5)

window.setLayout(v1_main)
window.resize(550,450)