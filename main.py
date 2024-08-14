from PyQt5.QtWidgets import QApplication
from time import sleep
from random import choice, shuffle


app = QApplication([])

from main_window import *
from menu_window import *
class Question():
    def __init__(self, question, answer, wrong_ans1, wrong_ans2, wrong_ans3):
        self.question = question 
        self.answer = answer 
        self.wrong_answer1 = wrong_ans1 
        self.wrong_answer2 = wrong_ans2 
        self.wrong_answer3 = wrong_ans3 
        self.actual = True 
        self.count_asked = 0 
        self.count_right = 0 
    def got_right(self):
        self.count_asked += 1
        self.count_right += 1
    def got_wrong(self):
            self.count_asked += 1
q1 = Question("Яблуко", "apple", "pinapple", "apply", "application")
q2 = Question("Дім", "house", "horse", "hobbi", "hang")
q3 = Question("Новий", "new", "know", "never", "need")
q4 = Question("Школа", "school", "sky", "sun", "snow")
radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
questions = [q1, q2, q3, q4]

def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question_m.setText(cur_q.question)
    lb_rightAns.setText(cur_q.answer)
    shuffle(radio_buttons)

    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)

new_question()
def check():
    rbGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text()==lb_rightAns.text():
                cur_q.got_right()
                lb_result.setText("Вірно!")
                answer.setChecked(False)
                break
        else:
            lb_result.setText("Не вірно!")
            cur_q.got_wrong()
    rbGroup.setExclusive(True)
def click_ok():
    if btn_next.text()=="Відповісти":
        check()
        gbAns.hide()
        gb_result.show()
        btn_next.setText("Наступне питання")
    else:
        new_question()
        gb_result.hide()
        gbAns.show()
        btn_next.setText("Відповісти") 
btn_next.clicked.connect(click_ok)

     

def back_menu():
    menu_w.hide()
    window.show()

btn_back.clicked.connect(back_menu)
def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show()

btn_rest.clicked.connect(rest)
def menu_generation():
    if cur_q.count_asked==0:
        c=0
    else:
        c= (cur_q.count_right/cur_q.count_asked)*100
    text = f'Разів відповіли: {cur_q.count_asked}\n' \
           f'Вірних відповідей: {cur_q.count_right}\n' \
           f'Успішність: {round(c,2)}%'
    lb_statistic.setText(text)
    menu_w.show()
    window.hide()

btn_menu.clicked.connect(menu_generation)
def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()

btn_claer.clicked.connect(clear)
def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(),
                     le_wrong_ans1.text(), le_wrong_ans2.text(),
                     le_wrong_ans3.text())

    questions.append(new_q)
    clear()

btn_add_ques.clicked.connect(add_question)

menu_w.show()
app.exec_()