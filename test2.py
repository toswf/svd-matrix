import cv2
import dlib
import numpy
import math

array1 = numpy.array([[1,1],[2,2]])
#print(array1)
r = math.pi * (30 / 360)
angle = numpy.matrix([[math.cos(r), math.sin(r)],[-math.sin(r), math.cos(r)]])
matrix1 = numpy.matrix(angle)
print(matrix1)
matrix2 = numpy.matrix([[2,0],[0,2]])
print(matrix2)
#求平均值
c1 = numpy.mean(matrix1, axis=0)
c2 = numpy.mean(matrix2, axis=0)
#print(c1)
#print(c2)
s1 = numpy.std(matrix1)
s2 = numpy.std(matrix2) #求标准差,计算离散程度;
print(s1)
print(s2)
U, S, Vt = numpy.linalg.svd(matrix1.T * matrix2)
print(U)
print(Vt)
R = (U * Vt).T #计算出旋转矩阵
print(R)

#print(math.cos(R))



