import numpy as np
treated = [1,2,3,4,4]
control = [2,3,4,5,4]
treated = np.array(treated)
control = np.array(control)
lfc = np.log2(treated/control)
# print(lfc)


A= [3,"a",7]
B= [9,"b",18]
for x,y in zip(A,B):
    # print(x+y)
    pass

ll = [[1,2,3],[4,"c",6],[7,8,9]]
a = np.array(ll)
# print(np.array(ll))
# print(a.shape)
# print(a.dtype)
# print(a.nbytes)
# b = a.astype(float)
# print(b.dtype)


c = np.array([2_000_000_000,
 2_000_000_000], dtype=np.int32)
print(c[0] + c[1])