import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
import numpy as np

# 연습) 0.01에서 2까지의 0.01씩 증가하여 2까지의 값들에 대한
# 지수값, 로그값을 하나의 차트에 출력
# 2두개의 차트를 가로로 나타내 봅니다.
path = "C:/Windows/Fonts/malgun.ttf"
rc('font', family=font_manager.FontProperties(fname=path).get_name())
qty = [10,20,10,30,50]
plt.bar(range(5),qty,0.4)    #plt.bar(분활 칸, 막대그래프에 나타날 그래프, 사이즈)
plt.title('요일별 과일 판매량')
plt.show()

# 차트에 한글이 안써질때
# rc('font', family=font_manager.FontProperties(fname=path).get_name())
# matplotlib의 rc와 font_manager 가 필요하다.
# from matplotlib import rc, font_maneger

# arr = np.arange(0.01,2,0.01)
# ep = np.exp(arr)
# lg = np.log(arr)
# plt.subplot(121)
# plt.plot(ep)
# plt.subplot(122)
# plt.plot(lg)
# plt.show()

# print(np.exp(2))    # 지수함수...?
# print(np.log(2))    # 로그함수...?

# t1 = np.arange(0,5,0.1)
# t2 = np.arange(0,5,0.02)
# plt.subplot(211)    #subplot(2행 1열 1번째)
# plt.plot(t1)
# plt.subplot(212)    #subplot(2행 1열 2번째)
# plt.plot(t2,'b')
# plt.show()
# plt.figure(1)
# plt.plot(t1,'yo')
# plt.figure(2)
# plt.plot(t2,'bo')
# plt.show()



# 연습) x의 범위가 -10에서 10일때 x의 제곱값을 차트로 그려주세요
# x = np.arange(-10,10)
# y = x**2
# plt.plot(x,y)
# plt.plot(x,y,"o")
# plt.show()


# height = np.array([170.5,177.7,185.5,162.1,168.8],dtype=float)
# weight = np.array([77.5,80.5,100.4,66.4,61.1],dtype=float)
# plt.plot(weight,height,'yo')
# plt.xlim(50.150)
# plt.ylim(150.200)
# plt.show()

# qty = np.array([[1000,1100,900,1000,1500],[80,70,100,50,40],[60,70,40,50,80]])
# 수박의 평균 판매량과 월별 판매량의 차이를 차트로
# a = np.abs(qty[1] - np.mean(qty[1]))
# plt.plot(a,'yo')
# plt.plot(qty[1],a,'bo')
# plt.xlim(0,5)
# plt.plot(a)
# plt.show()

# avg = np.average(qty[1])
# a = np.array(range(len(qty[0])))
# plt.plot(avg,'bo')
# plt.plot(avg)
# plt.plot(qty[1],'ro')
# plt.plot(qty[1])
# plt.show()


# 수박에 대한 판매량의 정보를 차트로
# plt.plot(qty[1],'ro')
# plt.plot(qty[1])
# plt.show()
