import numpy as np

# 연습) 속은 0으로 채워지고 테두리는 1로 채워지는 5*5 배열을

# a = np.zeros([5,5],dtype=int)
# a = np.ones([5,5],dtype=int)
# a[::,[0,4]] = 1
# a[4:1,] = 1
# a[:1,] = 1
# print(a)
#
# n = np.ones([5,5],dtype=int)
# n[1:-1,1:-1] = 0
# print(n)

# a[:,[0,-1]] = 1
# a[[0,-1]]=1
# print(a)

# a[1:-1,1:-1] = 0
# a[1:4,1:4] = 0
# print(a)

# a = np.zeros([8,8],dtype=int)
# col = [2,2,4,4,5,5]
# row = [2,5,3,4,3,4]
# a[col,row] = 1

a = [5,5,5,4,3,2]
# 위에 데이터는 숫자 1을 표현하기 위한 최소한의 정보입니다.
# a 배열의 요소수 만큼의 행 요소중에 가장 큰값 + 1 만큼의 열을 갖는 2차원 배열을 만들고
# 각 행 배열의 해당하는 여에 1을 설정합니다.

# n = np.zeros([len(a),len(a)],dtype=int)
# col = a
# row = [0,1,2,3,4,5]
# n[row,col] = 1
# print(n)

# arr = np.zeros([len(a),np.max(a)+1],dtype=int)
# arr[[0,1,2,3,4,5],a] = 1
# print(arr)

arr = np.zeros([len(a),np.max(a)+1],dtype=int)
arr[range(6),a] = 1
print(arr)

# one hot Encoding
# 기계학습을 하려면 학습시키고자 하는 정보(내용 글자 그림)
# 기계합습이 가능한 상태로 만들어야 하는데 그중 가장많이 사용되는
# 기법이 one hot 기법이다.