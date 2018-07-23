import numpy as np

world_data = np.genfromtxt('../data/world_alcohol.txt',delimiter=',', dtype=str)
print(type(world_data))
print(world_data)
#print(help(np.genfromtxt))

vector1 = np.array([1,2,3,4,5,6])
print(vector1[vector1>3])
print(vector1.shape)

vector2 = np.array(["1","2","3"])
print(vector2,vector2.dtype)
vector2 = vector2.astype(float)
print(vector2,vector2.dtype)

matrix1 = np.array([[1,2,3],
                    [10,20,30],
                    [100,200,300]])
print(np.sum(matrix1[:,1]),matrix1.sum(axis=1),matrix1.sum(axis=0)[1])

print(np.zeros((3,4),dtype=np.int32))
print(np.random.random(6).reshape(2,3))
print(np.linspace(0,2*np.pi,100))
print(np.exp(1))
print(np.sqrt(4))
ra = np.floor(10*np.random.random(12).reshape(3,4))
rb = np.floor(10*np.random.random(12).reshape(3,4))
print(ra)
print(ra.ravel().reshape(2,-1))
print(np.hstack((ra,rb)))
print(np.vstack((ra,rb)))

sa = np.arange(12).reshape(3,-1)
sb = sa
print(id(sa),id(sb))
sc = sa.view()#指向的对象地址是不一样的，但是两个对象共享内容，对任意一个进行操作，共享内容就会改变，另一个对象存储的值也就改变了
print(sa,'\n',sc,id(sc))
sc[0,1]=22222
print(sa,'\n',sc,id(sc))

sd=sa.copy()#地址和内容都不一样
print(sd)
maxv = sd.argmax(axis=1)
print(maxv)
print(sd[range(maxv.shape[0]),maxv])
print(sd,'\n',np.sort(sd,axis=1),np.argsort(sd,axis=1))
print(sd<6,sd[sd<6])
print(sd[np.argwhere(sd<6)[:,0],np.argwhere(sd<6)[:,1],])
print(np.argsort(sd,axis=1),sd[:,np.argsort(sd,axis=1)][:,1])