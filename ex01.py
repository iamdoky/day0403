import numpy as np

# np.zsros       배열의 요소를 0으로 채운다
# np.ones        배열의 요소를 1로 채운다
# np.full        배열의 요소를 특정값으로 채운다
# np.arange      연속된 데이터를 갖는 numpy 배열을 생성
# np.array       파이썬 배열 => 넘파이 배열
# list           넘파이 배열 => 파이썬 배열
# type           배열의 자료형 확인
# dtype          배열의 요소의 자료형
# ndim           배열의 차수를 확인
# shpae          배열의 모양,행열을 확인
# reshape        numpy 배열의 차원을 변경 / 차원 변경 시 행 열 중에 하나를 생략 하려면 -1을 사용
# 2차원배열을 1차원 배열로 만들떄는 직접 데이터의 수를 파악하기 보다는 shape를 통하여 행열의 길이를
# 행 x 열 만큼의 배열을 생성하도록 한다.
# size => 배열의 요소의 수를 알 수 있어요
# 2차원에서 1차원 배열로 차원을 변경할때 알아서 해죠 -1 옵션을 넣는게 간결하다.

a = np.array([[1,2,3],[4,5,6]])
# b = a.reshape(a.size)
b = a.reshape(-1)
print(a.size)
print(b)
# b = a.reshape( len(a) * len(a[0]))
# row, col = a.shape
# b = a.reshape(row*col)
# print(row, col)
# print(len(a)) #행의 길이
# print(len(a[0])) # 열의길이
# print(b)

# a = np.array([1,2,3,4,5,6])
# b = a.reshape([-1,3])
# print(a)
# print(b)

# a = np.array([1,2,3,4,5,6])
# b = a.reshape([2,3])
# print(a)
# print(b)

# a = np.array([1,2,3,4,5])
# b = np.array([10.5,2.7,3.5])
# c = np.array([[1,2,3],[4,5,6]])
#
# print(a.dtype)
# print(type(b))
# print(a.ndim)
# print(a.shape)
# print(c.ndim)
# print(c.shape)

# a = np.arange(10,-10,-1)
# print(a)
# b = list(a)
# print(b)

# a = [1,2,3,4,5]
# b = np.array(a)
# print(a)
# print(b)

# a = np.arange(10)
# print(a)
# b = np.arange(1,11)
# print(b)
# c = np.arange(1,11,2) # 1부터 11까지 2스텝씩 증가
# print(c)
# d = np.arange(10,-10,-1)
# print(d)

# a = np.zeros([2,3],dtype=int)
# b = np.ones([5,5],dtype=int)
# c = np.full([5,5],100,dtype=int)
# print(a)
# print(b)
# print(c)

# a = np.zeros(10, dtype=int)
# b = np.ones(5, dtype=np.int32)
# c = np.full(7, 5)
# print(a)
# print(b)
# print(c)
