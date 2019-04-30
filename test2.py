import cv2
import dlib
import numpy
import math

#���������cv2����ʧ�ܵ����⣬���Գ�����anaconda����ִ��conda update hdf5��������һ��opencv�İ汾��
#array1 = numpy.array([[1,1],[2,2]])
#print(array1)
r = math.pi * (30 / 360)
angle = numpy.matrix([[math.cos(r), -math.sin(r)],[math.sin(r), math.cos(r)]])
matrix1 = numpy.matrix(angle)
print(matrix1)
matrix2 = numpy.matrix([[2,0],[0,2]])
print(matrix2)
#��ƽ��ֵ
c1 = numpy.mean(matrix1, axis=0)
c2 = numpy.mean(matrix2, axis=0)
print(c1)
print(c2)
 #���׼��,������ɢ�̶�;
s1 = numpy.std(matrix1)
s2 = numpy.std(matrix2)
print(s1)
print(s2)
U, S, Vt = numpy.linalg.svd(matrix1.T * matrix2)
print(U)
print(Vt)
R = (U * Vt).T #�������ת����
print(R)
print("--------")
print((s2 / s1) * R) #���ź����ת����
print(c2.T)
print(c1.T)
print(c2.T - (s2 / s1) * R * c1.T) #�����ƶ�
#hstack : ������ת�����λ�ƾ�����
ret = numpy.vstack([numpy.hstack(((s2 / s1) * R,c2.T - (s2 / s1) * R * c1.T)),numpy.matrix([0., 0., 1.])])
print("------------")
print(ret)




