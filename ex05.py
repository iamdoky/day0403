import numpy as np

# 연습) 0으로 채워진 5*5 배열을 만들고 대각선을 1로 채우자
# a = np.zeros([5,5],dtype=int)
# a[[0,1,2,3,4],[0,1,2,3,4]] = 1
# print(a)
# a = np.eye(5,5,dtype=int)
# print(a)

# 현재 numpy배열을 순서대로 => sort
# a = [7,6,1,5,3]
# arr = np.array(a)
# arr.sort()
# print(arr)

# 정렬 시 데이터의 요소의 순서를 반환하는 함수  => argsort
# a = [7,6,1,5,3]
# arr = np.array(a)
# idx = np.argsort(arr)
# print(idx)
# print(arr[idx])

# 판매량이 높은 순으로 과일명을 출력
# item = ['사과','딸기','바나나','수박','복숭아','오렌지']
# qty = [200,300,1000,50,30,1000]
#
# i = np.array(item,dtype=str)
# q = np.array(qty,dtype=int)
# # idx = np.argsort(qty)[::-1]
# # id = np.argmax(q)
# # print(idx)
# # print(i[idx])
# # print(i[id])
#
#
# n = np.argwhere(q == np.max(q)) # 중복값찾는거 argwhere
#     # 2차원 배열을 1차원 바열로 reshape에서 size를 써서
# r = i[n]
# r = r.reshape(r.size)
# print(r)
# # print(i[n])
# # print(i[n].flatten())   # 2차원 배열으 1차원 배열로 flatten() 함수사용




