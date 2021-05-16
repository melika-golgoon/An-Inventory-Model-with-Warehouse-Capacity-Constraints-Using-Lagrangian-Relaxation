"""
@author: Melika_Golgoon
"""

import numpy as np
# import sympy
from scipy.optimize import fsolve

def func(alpha_star):
    b = 0
    for i in range(j):
        a = f[i]*np.sqrt(2*D[i]*A[i]/(h[i]+2*alpha_star*f[i]))
        b = b + a
    return b-F

# def Lagrangian(f,D,h,A,F,j):
#     alpha_star = sympy.Symbol("alpha_star")
#     b = 0
#     for i in range(j):
#         a = f[i]*sympy.sqrt(2*D[i]*A[i]/(h[i]+2*alpha_star*f[i]))
#         b = b + a
#     alpha = sympy.nonlinsolve(b-F)
#     Q_star = np.zeros([j])
#     for i in range(j):
#         Q_star[i] = np.sqrt(2*D[i]*A[i]/(h[i]+2*alpha[0]*f[i]))
#     return alpha,Q_star

print("Welcome")
print("Please specify your total storage limit : ")
F = float(input())
print("Please specify how many types of products do you have ?")
j = int(input())

f = np.zeros([j])
D = np.zeros([j])
C = np.zeros([j])
h = np.zeros([j])
A = np.zeros([j])

for counter in range(j):
    print("for product ", str(counter+1), " , please specify volume of each product")
    f[counter] = float(input())
    print("for product ", str(counter+1), " ,how many products of this kind are demanded? ")
    D[counter] = int(input())
    print("for product ", str(counter+1), " , what is the price of this product ?")
    C[counter] = float(input())
    print("for product ", str(counter+1), " , what is the cost of maintaining this product?")
    h[counter] = float((input()))
    print("for product ", str(counter+1), " , what is the cost of ordering this product?")
    A[counter] = float(input())

Q_w = np.sqrt(2*D*A/h)
flag = sum(f*Q_w) <= F

if flag == True:
    Q_star = Q_w
else:
    alpha_star = fsolve(func,0)
    # print(func(alpha_star))
    Q_star = np.zeros([j])
    for i in range(j):
        Q_star[i] = np.sqrt(2*D[i]*A[i]/(h[i]+2*alpha_star[0]*f[i]))

print(np.floor(Q_star))


# this method takes a long time to solve the equation
# if flag == True:
#     Q_star = Q_w
# else:
#     [alpha_star , Q_star] = Lagrangian(f,D,h,A,F,j)
# print(Q_star)
