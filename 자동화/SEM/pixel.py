import io
import sys
import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# EBSD 구조배향도 - OIM ver 1.1
# LG CHEMICAL
# 특허P, 양극재평가/분석PJT
# Ver 1.1.
# Orientation missing value (sin square) FIX
# pyinstaller --onefile -w --icon=.\1.ico 231105_OIM_pixel_v1.1.py

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global imagew, imageh  # step_size

        # QRect(0, 0, btn_width, btn_height)
        # label1 안에다가 그래프 넣기
        imagew = 850
        imageh = 800

        self.label1 = QLabel(self)
        self.label1.setGeometry(QRect(25, 80, imagew, imageh))
        self.label1.setStyleSheet("color: red;"
                                  "border-style: solid;"
                                  "border-width: 1px;"
                                  "border-color: #1E90FF;"
                                  "border-radius: 3px")

        self.label5_sin_sq = QLabel(self)
        self.label5_sin_sq.setText("구조배향도:")
        self.label5_sin_sq.setGeometry(QRect(300, 45, 150, 20))

        self.label5_sin_sq_c = QLabel(self)
        self.label5_sin_sq_c.setText("0")
        self.label5_sin_sq_c.setGeometry(QRect(400, 45, 150, 20))

        # btn_push/function
        self.btn1_where = QPushButton(self)
        self.btn1_where.setGeometry(QRect(30, 20, 100, 40))
        self.btn1_where.setText("파일열기")

        self.btn2_apply = QPushButton(self)
        self.btn2_apply.setGeometry(QRect(150, 20, 100, 40))
        self.btn2_apply.setText("실행")
        self.btn2_apply.setEnabled(False)

        # Function
        self.btn1_where.clicked.connect(self.fileload)  # btn1.where로 연결 // 파일경로호출필요
        self.btn2_apply.clicked.connect(self.Euler_processing)  # showresult 으로 연결

        self.setFixedSize(900, 900)
        self.setWindowTitle("EBSD(OIM) - 구조배향성 ver.1.1")
        self.show()
        print(
            "EBSD OIM - 구조배향성 ver.1.1\n"
            "특허P, 양극재평가/분석PJT\n"
            "cr = 0.4\n"
            "no tap"
        )

    def fileload(self):  # csv확장자만 설정
        global where
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', 'txt(*.txt)')

        if fname[0]:
            where = fname[0]
            self.btn2_apply.setEnabled(True)
        else:
            return

    def Euler_processing(self):

        raw_file = where

        # df = pd.read_csv(raw_file, header=None, skiprows=17, sep='\s+')


        df = pd.read_csv(raw_file, header=None, sep='\s+',
                                   comment='#',on_bad_lines = 'skip')

        df = df.drop(df.index[0:16]).iloc[:, :10].apply(pd.to_numeric)
        df.columns = ['orient1', 'orient2', 'orient3', 'X', 'Y', 'IQ', 'CI',
                      'Fit', 'grain', 'edge']

        # df.to_excel(raw_file[:-4] + '-processed.xlsx')  ### 확인용저장2

        e1 = len(df.loc[df['edge'] == 1])
        e0 = len(df.loc[df['edge'] == 0])
        em1 = len(df.loc[df['edge'] == -1])

        df = df[df.edge == 0].reset_index().drop(['index'], axis=1)
        df1 = df.dropna(axis=0).apply(pd.to_numeric).reset_index().drop(['index'], axis=1).copy()

        X_max, X_min, Y_max, Y_min = max(df1['X']), min(df1['X']), max(df1['Y']), min(df1['Y'])
        X_mid = round((df1.X.max() - df1.X.min()) / 2 + df1.X.min(), 2)
        Y_mid = round((df1.Y.max() - df1.Y.min()) / 2 + df1.Y.min(), 2)

        pvX = df1['X'].apply(lambda x: x - X_mid).tolist()
        pvY = df1['Y'].apply(lambda x: Y_mid - x).tolist()

        pvlist = []
        for i in range(len(df1)):
            x = round(pvX[i], 3)
            y = round(pvY[i], 3)
            vecP = []
            vecP.append(x)
            vecP.append(y)
            vecP.append(0)
            vecP = np.array(vecP)
            vecP = vecP.reshape(1, 3)
            vecP /= np.linalg.norm(vecP)  # normalize
            pvlist.append(vecP)

        ###### 오일러각 3개 각각 리스트로
        Euler1 = df1.loc[:, 'orient1'].tolist()
        Euler2 = df1.loc[:, 'orient2'].tolist()
        Euler3 = df1.loc[:, 'orient3'].tolist()
        cvlist = []

        def cos(x):
            return math.cos(x)

        def sin(x):
            return math.sin(x)

        for i in range(len(Euler1)):
            c1 = cos(Euler1[i])
            c2 = cos(Euler2[i])
            c3 = cos(Euler3[i])
            s1 = sin(Euler1[i])
            s2 = sin(Euler2[i])
            s3 = sin(Euler3[i])
            zxz = np.array([[c1 * c3 - c2 * s1 * s3, -c1 * s3 - c2 * c3 * s1, s1 * s2],
                            [c3 * s1 + c1 * c2 * s3, c1 * c2 * c3 - s1 * s3, -c1 * s2],
                            [s2 * s3, c2 * c3, c2]])
            I = np.array([[0],
                          [0],
                          [1]])
            vecC = np.dot(zxz, I)
            vecC /= np.linalg.norm(vecC)  # normalize
            cvlist.append(vecC)

        for i in cvlist:
            a = i[0].copy()
            i[0] = -i[1].copy()
            i[1] = a

        dplist = []
        for i in range(len(cvlist)):
            dp = np.dot(pvlist[i], cvlist[i])
            dp = round(dp[0][0], 3)
            if abs(dp) > 1:
                dp = round(dp)
            else:
                dp = dp
            dplist.append(dp)

        cos2 = []

        for i in range(len(dplist)):
            co2 = round(dplist[i] ** 2, 5)
            cos2.append(co2)
        df1['cos_sq'] = cos2

        anglist = []
        for i in dplist:
            ang = round(math.acos(i) * 180 / math.pi, 2)
            if ang > 90:
                ang = 180 - ang
            else:
                ang = ang
            anglist.append(ang)
        df1['angle'] = anglist
        df1['sin_sq'] = 1 - df1['cos_sq']


        # step = round(df1.X[1] - df1.X[0], 3)
        pv = df1.pivot(index='Y', columns='X', values='sin_sq')
        # df1.to_excel(raw_file[:-4] + '_df1_check.xlsx')  ## 231027 데이터 짤린거 체크용

        pv2 = pv.copy()
        for row in range(len(pv) - 1, 0, -1):
            pv2.iloc[row] = pv2.iloc[row - 1].values
            pv2.iloc[row - 1] = np.nan
        # pivot_table2의 NaN 값으로 pivot_table을 업데이트
        pv = pv2.combine_first(pv)


        if X_max >13 or Y_max > 13:
            plt.figure(figsize=(X_max * 0.6, Y_max * 0.5))
        else:
            plt.figure(figsize=(X_max * 0.72, Y_max * 0.6))

        plt.axis([0, X_max, 0, Y_max])
        ax = sns.heatmap(pv, cmap='RdYlGn')
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        plt.title('Li path way color map', fontsize=25, pad=10)
        cbar = ax.collections[0].colorbar
        cbar.ax.tick_params(labelsize=15)
        plt.savefig(raw_file[:-4] + '-Li path cmap.png')

        buf2 = io.BytesIO()
        plt.savefig(buf2, format='png')
        buf2.seek(0)
        img2 = QPixmap.fromImage(QImage.fromData(buf2.getvalue()))

        self.label1.setPixmap(img2)
        self.label5_sin_sq_c.setText(str(round(df1['sin_sq'].mean(), 4)))

        df_check = pd.DataFrame([['X_max', X_max], ['Y_max', Y_max],['sin_sq',str(round(df1['sin_sq'].mean(),4))],
                                 ['Edge=1', e1], ['Edge=0', e0], ['Edge=-1', em1]],
                                columns=['Data_name', 'Value'])
        df_check.to_excel(raw_file[:-4] + '-check.xlsx')  ### 확인용

        # print(X_max, Y_max, e1, e0, em1)
        # print('x 최대,최소: ', X_max, ',', X_min, '  ', 'y최대최소 :', Y_max, ',', Y_min)
        # print(e1, e0, em1)
        # print('실제 데이터수: ', len(df1), '/drop전 :', len(df))
        # print('x,y중심: ', X_mid, Y_mid)
        # print('sin제곱 면적평균: ', round(df1['sin_sq'].mean(), 4))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
