import numpy as np

# numpy 배열의 연산
# broadcasting              어떤 값 하나가 배열의 요소만큼 연산을 수행
# 1 + [1,2,3,4,5]
# Vector Operation          두개의 배열의 인덱스가 같은 요소끼리 연산을 수행
# [1,2,3] + [4,5,6]         열의 크기가 같아야 한다.
# 브로드캐스팅에 비교연산자를 사용하면 boolean array를 얻어요   ex) b = a > 5
# indexArray                배열의 요소중에 원하느 인덱스의 요소만 추출 ex) print(a[[0,2,5]]) print(a[r])

name = ['슬기','청하','원진아','이솜','김경민']
score = [100,90,95,50,10]
name = np.array(name)
score = np.array(score)
print(name[score>=60])

# name = ['원진아','슬기','이솜','청하','박주호','김경민','김태리']
# score = [100,100,96,88,91,18,100]
# n = np.array(name)
# s = np.array(score)
# m = max(score)
# sc = np.argmax(score)
# w = np.argwhere(score == np.max(score))
# # w = w.reshape(1,3)[0]
# print(w)
# print(n[w])


# a = np.array([1,3,0,7,9,5,6])
# # booleanArray 실험 0,2,5 요소만 출력
# r = [True,False,True,False,False,True,False]
# print(a[r])     # a중에 r이 True인 녀석을 출력해준다

# print(a[2])             # 0번쨰 요소
# print(a[[0,2,5]])       # a가 3차원 배열인줄알고 0번쨰 행의 2번쨰 열 5번째 열

# a = np.array([1,3,0,7,9,5,6])
# b = a > 5
# print(b)

# 두 배열을 더하여 보자
# a = np.array([1,2,3,4,5,6])
# b = np.array([[10,20,30],[40,50,60]]).reshape([1,6])
# a.reshape([2,-1])
# print(b + a)
# a = np.array([1,2,3,4,5,6])
# b = np.array([[10,20,30],[40,50,60]]).reshape([1,6])
# print(b + a)

# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[10,20,30],[40,50,60]])
# print(a+b)

# a = np.array([1,2,3])
# b = np.array([4,5,6])
# c = a + b                     # vector operation
# print(c)

# a = np.array([1,2,3,4,5])
# b = a + 1                   # 배열의 요소에 각각 1씩 더하여 준다.
# print(b)