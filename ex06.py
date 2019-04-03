import numpy as np

qty = np.array([[1000,1100,900,1000,1500],[80,80,100,50,40],[60,70,40,50,80]])
print(qty)
print('월별 행: ',np.sum(qty,axis=0))
print('과일별 열: ',np.sum(qty,axis=1))
print(np.max(qty))
print(np.max(qty,axis=0))
print(np.max(qty,axis=1))

# qty = np.array([200,300.10,20,30,1000],dtype=int)
# r = np.sum(qty)
# r2 = np.max(qty)
# print(r)
# print(r2)