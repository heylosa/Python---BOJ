import os
import sys
import math
import glob
import openpyxl
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import seaborn as sns
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import matplotlib.ticker as ticker
from matplotlib.ticker import MaxNLocator
from matplotlib.backends.backend_qt5agg import FigureCanvasQT as fc
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as Navigation
from matplotlib.figure import Figure
from PIL import Image
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QMainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QMessageBox, QSizePolicy

# Pyqt에서 출력해야하는 그래프 1. matplotlib - image, figure, pyplot, imshow, ticker
# PIL import image

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

        self.result_label = QLabel("")

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
        test = df.shape
        self.result_label.setText(test)



app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec_())