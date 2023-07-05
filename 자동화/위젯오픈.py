import sys
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout, QTableWidget, QTableWidgetItem, QGridLayout, QDialog, QTextEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #Label Name
        self.label_where = QLabel("저장경로")
        self.line_edit_where = QLineEdit()
        self.label_step_size = QLabel("step_size (unit: um)")
        self.line_edit_step_size = QLineEdit()
        self.label_intv_value = QLabel("intv_value")
        self.line_edit_intv_value = QLineEdit()
        self.label_cr_value = QLabel("cr_value")
        self.line_edit_cr_value = QLineEdit()
        self.button = QPushButton("실행")

        self.button.clicked.connect(self.showresult) #showresult 으로 연결

        #Layout Widget 설정란
        layout = QVBoxLayout()
        layout.addWidget(self.label_where)
        layout.addWidget(self.line_edit_where)
        layout.addWidget(self.label_step_size)
        layout.addWidget(self.line_edit_step_size)
        layout.addWidget(self.label_intv_value)
        layout.addWidget(self.line_edit_intv_value)
        layout.addWidget(self.label_cr_value)
        layout.addWidget(self.line_edit_cr_value)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.show()
        self.setFixedSize(250, 250)         # 창 크기를 조절할 수 없도록 합니다.
        self.setWindowTitle("EBSD-구조배향성")

    def showresult(self):
        where = self.line_edit_where.text()
        step_size = self.line_edit_step_size.text()
        intv_value = self.line_edit_intv_value.text()
        cr_value = self.line_edit_cr_value.text()

        raw_file = where
        df = pd.read_csv(raw_file)  # ,encoding='cp949') #re는 encoding안함

        # 새로운 창을 생성하고 결과를 표시
        result_dialog = ResultDialog(df)
        result_dialog.exec_()

class ResultDialog(QDialog):
    def __init__(self, df):
        super().__init__()

        self.df = df
        self.initUI()

    def initUI(self):
        self.setWindowTitle("결과 확인")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # 그래프를 표시하기 위한 FigureCanvas 위젯 생성
        self.canvas = plt.figure().canvas
        layout.addWidget(self.canvas)

        # 테이블을 표시하기 위한 QTableWidget 생성
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)

        # 텍스트를 표시하기 위한 QTextEdit 생성
        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        # 그래프 생성
        plt.figure()
        self.df.plot(kind='bar', x='x_axis_column', y='y_axis_column', legend=False)
        plt.xlabel('x축 레이블')
        plt.ylabel('y축 레이블')
        self.canvas.draw()

        # 테이블 생성
        self.table_widget.setRowCount(self.df.shape[0])
        self.table_widget.setColumnCount(self.df.shape[1])
        for row in range(self.df.shape[0]):
            for col in range(self.df.shape[1]):
                item = QTableWidgetItem(str(self.df.iat[row, col]))
                self.table_widget.setItem(row, col, item)

        # 텍스트 표시
        text_result = f"입력된 값: \n저장경로: {self.df.where}\nstep_size: {self.df.step_size}\nintv_value: {self.df.intv_value}\ncr_value: {self.df.cr_value}"
        self.text_edit.setPlainText(text_result)

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
