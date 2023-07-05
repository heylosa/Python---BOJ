import numpy as np
import math
import pandas as pd
from pandas import Series, DataFrame
from PIL import Image
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
from matplotlib.ticker import MaxNLocator
import glob
import os
import matplotlib.image as mpimg
import openpyxl
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


#############[1]

#raw input으로 변경 / TEXT BOX UI 구성
## 입력값
raw_file = r'D:\#.Secure Work Folder\data\EBSD(Aztec)\HN806 P1 Specimen 2 Site 2 Map Data 5-E1 + E2 + E3.csv'

df = pd.read_csv(raw_file)           # ,encoding='cp949') #re는 encoding안함
print(df.shape)
df = df.drop(df.index[0]).apply(pd.to_numeric).reset_index().drop(['Index','index'],axis=1) #.drop(
df.head(3)

#############[2]
# 빈data drop/ XY 중심 찾기
df1 = df.dropna(axis=0).apply(pd.to_numeric).reset_index().copy()
print('실제 데이터수: ',len(df1), '/drop전 :', len(df))
df1= df1.drop(['index'], axis=1)
X_max, X_min, Y_max, Y_min = max(df1['X']), min(df1['X']),  max(df1['Y']), min(df1['Y'])
print('x 최대,최소: ',X_max,',', X_min,'  ','y최대최소 :', Y_max,',', Y_min)
X_center = round((df1.X.max()-df1.X.min())/2+df1.X.min(),2)
Y_center = round((df1.Y.max()-df1.Y.min())/2+df1.Y.min(),2)
print('x,y중심: ', X_center, Y_center)
df1.tail(3)


#############[3]
# X_center, Y_center = 4.5, 6
print('X,Y중심: ', X_center, Y_center)

plt.figure(figsize=(X_max/2, Y_max/2))
plt.scatter(df1.X, df1.Y)
plt.scatter(X_center, Y_center, c='r')
plt.xlim([df1.X.min(),df1.X.max()])
plt.ylim([df1.Y.max(),df1.Y.min()])
plt.xlabel('X')
plt.ylabel('Y')
# plt.savefig('./LELE/210610_df_1-1.png')
plt.show()
df1.tail(3) # Euler angle로부터 c축 각도 계산



############[4]
#위치벡터 x,y list로
pvX=df1['X'].apply(lambda x: X_center-x).tolist() ############ 위치 x에 마이너스
pvY=df1['Y'].apply(lambda x: x-Y_center).tolist()

pvlist = []                 #위치벡터 (1,3) array 형태로 모아 list
for i in range(len(df1)):
    x=round(pvX[i],3)
    y=round(pvY[i],3)
    vecP = []
    vecP.append(x)
    vecP.append(y)
    vecP.append(0)
    vecP=np.array(vecP)
    vecP=vecP.reshape(1,3)
    vecP/=np.linalg.norm(vecP) #normalize
    pvlist.append(vecP)

pv_x = []
pv_y = []
for i in range(len(df1)):
    a1 = round(pvlist[i][0][0],3)
    pv_x.append(a1)
    b1 = round(pvlist[i][0][1],3)
    pv_y.append(b1)
df1['pvX']=pv_x
df1['pvY']=pv_y

#오일러각 3개 각각 리스트로
Euler1 = df1.loc[:,'Euler 1'].tolist()
Euler2 = df1.loc[:,'Euler 2'].tolist()
Euler3 = df1.loc[:,'Euler 3'].tolist()
cvlist = [] #결정벡터 (1,3) array 형태로
def cos(x):
    return math.cos(x*math.pi/180)
def sin(x):
    return math.sin(x*math.pi/180)
for i in range(len(Euler1)):
    c1=cos(Euler1[i])
    c2=cos(Euler2[i])
    c3=cos(Euler3[i])
    s1=sin(Euler1[i])
    s2=sin(Euler2[i])
    s3=sin(Euler3[i])
    zxz = np.array([[c1*c3-c2*s1*s3, -c1*s3-c2*c3*s1, s1*s2],
                    [c3*s1+c1*c2*s3, c1*c2*c3-s1*s3, -c1*s2],
                    [s2*s3, c2*c3, c2]])
    I= np.array([[0],
                 [0],
                 [1]])
    vecC=np.dot(zxz,I)
    vecC/=np.linalg.norm(vecC) #normalize
    cvlist.append(vecC)

cv_x =[]
cv_y = []
for i in range(len(df1)):
    x1 = round(cvlist[i][0][0],3)
    cv_x.append(x1)
    y1 = round(cvlist[i][1][0],3)
    cv_y.append(y1)
df1['cvX']=cv_x
df1['cvY']=cv_y

#내적 list #위치벡터:pvlist(1,3)array #결정벡터:cvlist(3,1)array
dplist = []
for i in range(len(cvlist)):
    dp = np.dot(pvlist[i], cvlist[i])
    dp = round(dp[0][0],3)
    if abs(dp)>1:
        dp = round(dp)
    else:
        dp = dp
    dplist.append(dp)

cos2 = []                       #cos제곱 list
for i in range(len(dplist)):
    co2 = round(dplist[i]**2, 5)
    cos2.append(co2)
df1['cos_sq']=cos2

anglist = []
for i in dplist:
    ang = round(math.acos(i)*180/math.pi,2)
    if ang > 90:
        ang = 180-ang
    else:
        ang = ang
    anglist.append(ang)
df1['angle']=anglist
df1.tail(3)
# 1-cos2=sin2 클수록 c축-radial 직각, Lipath-radial평행
df1['sin_sq']= 1-df1['cos_sq']
print('sin제곱 평균: ',round(df1['sin_sq'].mean(),4))
df1.tail(3)


#[5]
# 계산된 표를 excel로 저장하기

## 입력값
raw_file = r'D:\#.Secure Work Folder\data\EBSD(Aztec)\HN806 P1 Specimen 2 Site 2 Map Data 5-E1 + E2 + E3.csv'
df1.to_excel(raw_file[:-4]+'-processed.xlsx') #파일저장.png

#[6]
##
step = 0.075 #입력값
##

#[7]
print("크기:", X_max, Y_max, "중심:", X_center, Y_center)
print(15/X_max*Y_max)
st = 1/step  #       1/step size : ticker locator

#[8]
pv = df1.pivot(index='Y',columns='X',values='sin_sq') # 결정벡,위치벡 90도 가장 좋음 cos=0
print("크기:", X_max, Y_max, "중심:", X_center, Y_center)
label_x = [0]+[i for i in range(int(X_max+1))]
label_y = [0]+[i for i in range(int(Y_max+1))]

plt.figure(figsize=((15+3)/2,(15/X_max*Y_max)/2))
plt.axis([0, X_max, 0, Y_max])
ax = sns.heatmap(pv, cmap='RdYlGn')
ax.yaxis.set_major_locator(ticker.MultipleLocator(st)) #1/0.05step
ax.yaxis.set_major_formatter(ticker.FixedFormatter(label_y))
ax.xaxis.set_major_locator(ticker.MultipleLocator(st))
# ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
ax.set_xticklabels(label_x, rotation=0)
plt.title('Li path way color map', fontsize = 25, pad=10)
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=15)
plt.savefig(raw_file[:-4]+'-Li path cmap.png')  #파일저장.png
plt.show()

#[9]
print(len(df1.X))
# intervalfor i in range(len(df1.X)):
##
intv = 1300 #입력값
##
X_100 = []
for i in range(len(df1.X)):
    if i%intv==0:
        X_100.append(df1.X[i])
print(len(X_100))
Y_100 = [df1.Y[i] for i in range(len(df1.Y)) if i%intv==0]
print("남은 데이터 수: ",len(Y_100))
cvx_100 = [cv_x[i] for i in range(len(cv_x)) if i%intv==0]
cvy_100 = [cv_y[i] for i in range(len(cv_y)) if i%intv==0]
cvy_100m = [-cv_y[i] for i in range(len(cv_y)) if i%intv==0]
# cvx_100[:3]
# cvy_100m[:3]

#[10]
plt.figure(figsize=(15/2,15/X_max*Y_max/2))
# image = mpimg.imread('./210823 HC ebsd/AE 1-1 1 edge1.tif')
# plt.imshow(image, extent=[0, X_max, Y_max, 0])
plt.xlim([0,X_max])
plt.ylim([Y_max,0])
plt.scatter(X_center,Y_center,color='b', label = 'center', marker='x')
quiveropts = dict(headlength=0, pivot='middle', headwidth=1) #arrow head, 표현중심, 두께
# plt.quiver(XM, YM, MVX, MVY,label='major.direc.', **quiveropts)
# plt.quiver(X_100, Y_100, cvx_100, cvy_100, color='grey', label='c-axis.direc.', **quiveropts)
plt.quiver(X_100, Y_100, cvy_100m, cvx_100, color='r', label='Li.path.direc.', **quiveropts)
plt.legend()
plt.savefig(raw_file[:-4]+'-arrow map.png',transparent=True) #파일저장.png
plt.show()
# quiver opts : https://www.py4u.net/discuss/232106


#[11]
##
cr = 0.4  #입력값
##
#[12]
pvX[:3], pvY[:3]
dist = [ (pvX[i]**2+pvY[i]**2)**(1/2) for i in range(len(pvX))]
print("최대 반경: ",max(dist))
df1['dist'] = dist

df2 = df1[df1.dist > 5.7*cr]
print("shell 데이터 비율: ", len(df2)/len(df1),'\n')
print("shell배향도: ", df2['sin_sq'].mean())

#[13]
X_center = round((df1.X.max()-df1.X.min())/2+df1.X.min(),2)
Y_center = round((df1.Y.max()-df1.Y.min())/2+df1.Y.min(),2)
pv2 = df2.pivot(index='Y',columns='X',values='sin_sq') # 결정벡,위치벡 90도 가장 좋음 cos=0
print("크기:", X_max, Y_max, "중심:", X_center/2, Y_center/2)
label_x = [0]+[i for i in range(int(X_max+1))]
label_y = [0]+[i for i in range(int(Y_max+1))]

plt.figure(figsize=(((15)+3)/2,(15/X_max*Y_max)/2))
plt.axis([0, X_max, 0, Y_max])
ax = sns.heatmap(pv2, cmap='RdYlGn')
ax.yaxis.set_major_locator(ticker.MultipleLocator(40)) #1/0.05step
ax.yaxis.set_major_formatter(ticker.FixedFormatter(label_y))
ax.xaxis.set_major_locator(ticker.MultipleLocator(40))
ax.set_xticklabels(label_x, rotation=0)
plt.title('Li path way color map', fontsize = 25, pad=10)
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=15)
plt.savefig(raw_file[:-4]+'-shell cmap.png') #파일저장.png
plt.show()