import io
import sys
import math
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# EBSD 형상배향도 - OIM ver 1.0
# LG CHEMICAL
# 특허P, 양극재평가/분석PJT
# Ver 1.1.
# All Column Check

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        global imagew, imageh

        # QRect(0, 0, btn_width, btn_height)
        # label1 안에다가 그래프 넣기
        imagew = 850
        imageh = 800

        self.label1 = QLabel(self)
        self.label1.setGeometry(QRect(25, 90, imagew, imageh))
        self.label1.setStyleSheet("color: blue;"
                                  "border-style: solid;"
                                  "border-width: 1px;"
                                  "border-color: #1E90FF;"
                                  "border-radius: 3px")

        self.label3_scale_value = QLabel(self)
        self.label3_scale_value.setText("scale_value:")
        self.label3_scale_value.setGeometry(QRect(270, 30, 150, 20))

        self.label3e_scale_value = QLineEdit(self)
        self.label3e_scale_value.setGeometry(QRect(350, 30, 100, 20))
        self.label3e_scale_value.setEnabled(False)

        self.label5_AR_avg = QLabel(self)
        self.label5_AR_avg.setText("Aspect ratio avg.:")
        self.label5_AR_avg.setGeometry(QRect(560, 20, 150, 20))

        self.label5_AR_avg_c = QLabel(self)
        self.label5_AR_avg_c.setText("0")
        self.label5_AR_avg_c.setGeometry(QRect(680, 20, 150, 20))

        self.label6_cos_sq_area = QLabel(self)
        self.label6_cos_sq_area.setText("형상배향수치:")
        self.label6_cos_sq_area.setGeometry(QRect(560, 60, 150, 20))

        self.label6_cos_sq_area_c = QLabel(self)
        self.label6_cos_sq_area_c.setText("0")
        self.label6_cos_sq_area_c.setGeometry(QRect(680, 60, 150, 20))

        self.label7_diameter_avg = QLabel(self)
        self.label7_diameter_avg.setText("Grain size avg:")
        self.label7_diameter_avg.setGeometry(QRect(560, 40, 150, 20))

        self.label7_diameter_avg_c = QLabel(self)
        self.label7_diameter_avg_c.setText("0")
        self.label7_diameter_avg_c.setGeometry(QRect(680, 40, 150, 20))

        # btn_push/function
        self.btn1_where = QPushButton(self)
        self.btn1_where.setGeometry(QRect(30, 20, 100, 40))
        self.btn1_where.setText("파일열기")

        self.btn2_apply = QPushButton(self)
        self.btn2_apply.setGeometry(QRect(150, 20, 100, 40))
        self.btn2_apply.setText("실행")
        self.btn2_apply.setEnabled(False)

        self.btn4_change_scale = QPushButton(self)
        self.btn4_change_scale.setGeometry(QRect(460, 30, 60, 20))
        self.btn4_change_scale.setText("Change")
        self.btn4_change_scale.setEnabled(False)

        # Function
        self.btn1_where.clicked.connect(self.fileload)
        self.btn2_apply.clicked.connect(self.processing)
        self.btn2_apply.clicked.connect(self.plot2_scale_value)
        self.btn4_change_scale.clicked.connect(self.plot2_scale_value)

        self.setFixedSize(900, 900)
        self.setWindowTitle("EBSD(OIM) - 형상배향도 ver.1.0")
        self.show()
        print(
            "EBSD - 형상배향도 (OIM) ver.1.0\n"
            "특허P, 양극재평가/분석PJT\n"
        )

    def fileload(self):  #csv확장자만 설정
        global where
        fname = QFileDialog.getOpenFileName(self, 'Open file', '', 'txt(*.txt)')

        if fname[0]:
            where = fname[0]
            self.btn2_apply.setEnabled(True)
            self.label3e_scale_value.setEnabled(True)
        else:
            return

    def processing(self):
        global X_max, Y_max, X_mid, Y_mid, df1, raw_file, major_xlist, major_ylist

        raw_file = where

        with open(raw_file, 'r') as f:
            column_list = f.readlines()


        column_list = [line.rstrip(' \n') for line in column_list]
        c_lst = column_list[9:40]

        raw_list = []

        #최적화 필요
        for i in range(len(c_lst)):

            # Grain Number
            if 'Integer identifying grain' in c_lst[i]:
                raw_list.append('grain')

            # Integer Phase
            elif 'An integer identifying the phase' in c_lst[i]:
                raw_list.append('interger_phase')


            # Euler None Radian
            elif '360, 360, 360 for anti-grains' in c_lst[i]:
                raw_list.append('orient1')
                raw_list.append('orient2')
                raw_list.append('orient3')

            # Euler Radian
            elif '2pi, 2pi, 2pi for anti-grains' in c_lst[i]:
                raw_list.append('orient1r')
                raw_list.append('orient2r')
                raw_list.append('orient3r')

            # Orient-Integer
            elif '[u v w] in integers' in c_lst[i]:
                raw_list.append('ori_integer1')
                raw_list.append('ori_integer2')
                raw_list.append('ori_integer3')
                raw_list.append('ori_integer4')
                raw_list.append('ori_integer5')
                raw_list.append('ori_integer6')

            # Orient-Float
            elif '[u v w] in floats' in c_lst[i]:
                raw_list.append('ori_floats1')
                raw_list.append('ori_floats2')
                raw_list.append('ori_floats3')
                raw_list.append('ori_floats4')
                raw_list.append('ori_floats5')
                raw_list.append('ori_floats6')

            # Position of Map point (Mapping data)
            elif 'Position' in c_lst[i]:
                raw_list.append('X')
                raw_list.append('Y')

            # Image Quality
            elif 'Image Quality' in c_lst[i]:
                raw_list.append('IQ')

            # Confidence Index (CI) => 어떤 개념?
            elif 'Confidence Index' in c_lst[i]:
                raw_list.append('con_index')

            elif 'Fit (degrees' in c_lst[i]:  # Columns 25
                raw_list.append('fit_degrees')

            elif 'Video Signal' in c_lst[i]:
                raw_list.append('VS')

            # RGB Point => 배향도 시각화 결정하는 추가 데이터로 활용 가능성 생각
            elif 'Color in Red' in c_lst[i]:
                raw_list.append('R')
                raw_list.append('G')
                raw_list.append('B')

            elif 'Edge grain' in c_lst[i]:
                raw_list.append('edge')

            elif 'Number of measurement points in grain' in c_lst[i]:
                raw_list.append('points')

            # Step size 별 square가 어느정도의 area로 나뉘는지, 영향을 미치는지 ! CHECK !
            elif 'Area of grain in square microns' in c_lst[i]:
                raw_list.append('area')

            elif 'Diameter of grain in microns' in c_lst[i]:
                raw_list.append('diameter')

            elif 'ASTM grain size' in c_lst[i]:
                raw_list.append('ASTM_grain_size')

            elif 'Aspect ratio of ellipse fit to grain' in c_lst[i]:
                raw_list.append('AR_fit')

            elif 'Length of major axis' in c_lst[i]:
                raw_list.append('major_fit')

            elif 'Length of minor axis' in c_lst[i]:
                raw_list.append('mino_fit')

            elif 'Orientation (relative to the horizontal) of major axis' in c_lst[i]:
                raw_list.append('major_angle')

            elif 'Grain ellipticity' in c_lst[i]:
                raw_list.append('ellipcity')

            elif 'Grain circularity' in c_lst[i]:
                raw_list.append('circularity')

            elif 'Maximum Feret diameter' in c_lst[i]:
                raw_list.append('max_Feret')

            elif 'Minimum Feret diameter' in c_lst[i]:
                raw_list.append('min_Feret')

            elif 'Average orientation spread in grain' in c_lst[i]:
                raw_list.append('orient_spread')

            elif 'Average misorientation in grain' in c_lst[i]:
                raw_list.append('misorient')

            elif 'Number of grains neighboring' in c_lst[i]:
                raw_list.append('num_neighbor')

        print(raw_list)

        df = pd.read_csv(raw_file, header=None, sep='\s+',
                         comment='#', on_bad_lines='skip',
                         usecols=[i for i in range(len(raw_list))])

        print(len(raw_list))

        df.columns = raw_list

        df1 = df.dropna(axis=0).drop(['edge', 'points', 'ellipcity', 'circularity'], axis=1).copy()
        # df1.to_excel(raw_file[:-4] + '-processed.xlsx')  ### 저장1
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
            vecP /= np.linalg.norm(vecP)
            pvlist.append(vecP)

        Euler1 = df1.loc[:, 'orient1'].tolist()
        Euler2 = df1.loc[:, 'orient2'].tolist()
        Euler3 = df1.loc[:, 'orient3'].tolist()
        cvlist = []

        def cos(x):
            return math.cos(x * math.pi / 180)

        def sin(x):
            return math.sin(x * math.pi / 180)

        for i in range(len(Euler1)):
            c1 = float(cos(Euler1[i]))
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
            vecC = np.dot(zxz, I) # z축값 내적
            vecC /= np.linalg.norm(vecC)
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

        cvX = []
        cvY = []
        for i in range(len(df1)):
            x1 = round(cvlist[i][0][0], 3)
            cvX.append(x1)
            y1 = round(cvlist[i][1][0], 3)
            cvY.append(y1)

        ang_list = df1.loc[:, 'major_angle'].tolist()
        major_xlist = []
        major_ylist = []
        for i in ang_list:
            mx = math.cos(i * math.pi / 180) * (-1)
            my = math.sin(i * math.pi / 180)
            major_xlist.append(mx)
            major_ylist.append(my)

        mvlist = []
        for i in range(len(major_xlist)):
            c = []
            c.append(major_xlist[i])
            c.append(major_ylist[i])
            c.append(0)
            c = np.array(c)
            c = c.reshape(3, 1)
            c /= np.linalg.norm(c)
            mvlist.append(c)

        coslist = []
        for i in range(len(df1)):
            dp = np.dot(pvlist[i], mvlist[i])
            dp = dp[0]
            coslist.append(dp)

        cos2_maj = []
        for i in range(len(coslist)):
            co = coslist[i][0]
            co2 = round(co ** 2, 3)
            cos2_maj.append(co2)
        df1['cos2'] = cos2_maj

        AR_avg = round(df1.AR_fit.sum() / len(df1.AR_fit), 4)
        sin_sq_avg = round(df1['sin_sq'].mean(), 4)
        sin_sq_area_avg = round(sum(df1.area * df1.sin_sq) / df1.area.sum(), 4)
        cos_sq_avg = round(np.mean(cos2_maj), 4)
        cos_sq_area_avg = round(sum(df1.area * df1.cos2) / df1.area.sum(), 4)
        Diameter_avg = round(df1['diameter'].mean(), 4)
        Diameter_area_avg = round(sum(df1.area * df1.diameter) / df1.area.sum(), 4)


        df_check = pd.DataFrame([['X_max', X_max], ['Y_max', Y_max],
                                 ['AR_avg', AR_avg], ['Diameter_avg', Diameter_avg],
                                 ['Diameter_area_avg', Diameter_area_avg],
                                 ['sin_sq_avg', sin_sq_avg], ['sin_sq_area_avg', sin_sq_area_avg],
                                 ['cos_sq_avg', cos_sq_avg], ['cos_sq_area_avg', cos_sq_area_avg]],
                                columns=['Data_name', 'Value'])
        df_check.to_excel(raw_file[:-4] + '-check.xlsx')  ### 확인용

        # print('Aspect ratio: ', round(df1.AR_fit.sum() / len(df1.AR_fit), 4))
        # print('sin제곱 수평균: ', round(df1['sin_sq'].mean(), 4))
        # print('sin2 면적평균: ', round(sum(df1.area * df1.sin_sq) / df1.area.sum(), 4))  # sin2_area =  #면적평균
        # print('cos제곱 평균: ', round(np.mean(cos2_maj), 4))
        # print('cos2 면적평균: ', round(sum(df1.area * df1.cos2) / df1.area.sum(), 4))  # cos2_area =  #면적평균
        # print(X_max, Y_max)

        self.label5_AR_avg_c.setText(f"{round(df1.AR_fit.sum() / len(df1.AR_fit), 4)}")
        self.label6_cos_sq_area_c.setText(f"{round(sum(df1.area * df1.cos2) / df1.area.sum(), 4)}")
        self.label7_diameter_avg_c.setText(f"{round((df1.diameter.sum()) / len(df1.diameter), 4)}")
        self.btn4_change_scale.setEnabled(True)

    def plot2_scale_value(self):

        sca = int(self.label3e_scale_value.text())

        if X_max >13 or Y_max > 13:
            plt.figure(figsize=(X_max * 0.6, Y_max * 0.5))
        else:
            plt.figure(figsize=(X_max * 0.72, Y_max * 0.6))
        norm = matplotlib.colors.Normalize()
        cm = matplotlib.cm.copper_r  # RdYlGn  #copper
        area = df1.area * round(sca, 0)
        plt.xlim([0, X_max + 0.2])
        plt.ylim([Y_max + 0.2, 0])
        plt.scatter(df1.X, df1.Y, s=area, c=cm(norm(df1.cos2)), alpha=0.5)
        plt.scatter(X_mid, Y_mid, color='black', label='center', marker='+')
        quiveropts = dict(headlength=0, pivot='middle', headwidth=1)  # arrow head, 표현중심, 두께
        plt.quiver(df1.X, df1.Y, major_xlist, major_ylist,
                   label='major.direc.', color=cm(norm(df1.cos2)), scale=50, **quiveropts)
        plt.colorbar(matplotlib.cm.ScalarMappable(cmap=cm, norm=norm))
        plt.legend()
        plt.savefig(raw_file[:-4] + ' - major align.png', transparent=True)

        # 그래프를 이미지로 변환
        buf2 = io.BytesIO()
        plt.savefig(buf2, format='png')
        buf2.seek(0)
        img2 = QPixmap.fromImage(QImage.fromData(buf2.getvalue()))
        self.label1.setPixmap(img2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
