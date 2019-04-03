import  numpy as np

# 2차원 배열에서의 slicing
# fancy indexing의 형식 배열명 [행,열]
#                      배열명 [[index array], [index array]]
#                      배열명 [[index array], [index array]]

a = [
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18],
    [19,20,21,22,23,24]]
b = np.array(a)

# 배열중에 9,12,14,17,20,22,23이 있는 요소를 fancy indexing을 사용하여 추출하시오.

# rows = [1,1,2,2,3,3,3]
# cols = [2,5,1,4,1,3,4]

# print(b[rows,cols])

# 모든 행에 대항 1열부터, 4열 까지의 데이터를 출력
# print(b[:,1:5])
# 모든 행에 대하여 1 , 3 , 5열의 데이터를 출력
# print(b[:,[0,2,4]])
# 짝수 행만 모두 출력해 봅니다.
# print(b[1::2])
# print(b[1::2,:])
# 짝수 행에 대하여 1열 부터 4열 까지의 데이터를 출력
# print(b[1::,[0,1,2,3]])
# print(b[1::,0:4])

# 모든 행에 대항 1열부터, 4열 까지의 데이터를 출력
# print(b[:,0:4])
# print()
# 모든 행에 대하여 1 , 3 , 5열의 데이터를 출력
# print(b[:,:1])
# print(b[:,2:3])
# print(b[:,4:5])
# print()
# 짝수 행만 모두 출력해 봅니다.
# print(b[1::2])
# print()
# 짝수 행에 대하여 1열 부터 4열 까지의 데이터를 출력
# print(b[1::2,:4])

# print(b[1:3,])
# print(b[[1,2],])
# c = np.array([1,2,3,4,5,6,7,8,9,10])
# print(b[1,2])       # fancy indexing은 numpy 배열에서 가능
# print(b[3,3])

# 값 하나를 추출 할 때는 가능하지만 범위에서 slicing 할떄는 불가
# fancy indexing을 사용해야 한다.

# print(a[1:3][0:3])
# print(a[1][2])
# print(a[:])
# print(b[:])
# print(c[:])
# print(a[:4])
# print(b[:4])
# print(c[:4])
# print(c[1:4])
# print(a[1:4])
# print(b[1:4])
# print(c[1])
# print(a[1])
# print(b[1])
# print(a[1][2])
# print(b[1][2])
# print(c[8])

# a = [0,1,2,3,4,5,6,7,8,9]       # 파이썬 배열
# print(a[0])
# print(a[1])
# print(a[0:3])
# print(a[-1])
# print(a[-2])
# print(a[:])
# print(a[3:])
# print(a[:5])
# print(a[0,3,4]) 인덱스 어레이가 되지 않음
# print(a[[False,False,False,False,False,False,False,False,False,False]])
# print(a[0:10:2])
# print(a[::2])
# print(a[::-1])

# 시작하는 인덱스는 포함되지만 마지막 인덱스는 포함되지 않는다.

# b = np.array(a)                 # 넘파이 배열
# print(b[0])
# print(b[1])
# print(b[0:3])
# print(b[-1])
# print(b[-2])
# print(b[:])
# print(b[3:])
# print(b[:5])
# print(b[[0,3,4]])
# print(b[[False,True,False,False,False,False,False,False,False,True]])
# print(b[0:10:2])
# print(b[::2])
# print(b[::-1])