# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 22:32:18 2021

@author: ROG
"""

# Import Part
import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from sympy import expand

def exp(si):
    for a in preorder_traversal(si):
        if isinstance(a, Float):
            # si = si.subs(a, np.format_float_positional(a, precision=4, unique=False, fractional=False, trim='k'))
            si = si.subs(a, round(a,4))
    return si
# Problem 1 question 1
#Need to extract 12 sampling points from the data curve

# Plan: the date change dx = 1 and it is collected from January 1 to Janurary12 2021
# Assume that Jan 1st is 0 and Jan 2nd is 1 such like this

# Lets collect the data for x and y, date is stored in day
# Daily new case is stored in n_case
day = []
for i in range(12):
    day.append(i)
n_case = [4831.14, 5222.14, 5251.71, 5390.57, 5378.43, 5435.43, 5625.43, 6130.71, 5764.14, 6081.71, 6137.14, 6191.0]
# print(len(day))
# print(len(n_case))

# Plot the data from Jan 1 to Jan 12
# plt.plot(day,n_case, label = "Daily new case")

# Problem 1 Question 2, Use cubic spline to perform a interpolitan function
# Requsite
# 1) Neeed to show the cubic spline function
# 2) Plot original sample and cubic spline function in the same chart
# Need to display two importnt variable dx and H_i
h = 1
H = []
# Recall that H_i = (y_i+1 - y_i)/h = y_(i+1) - y_i
# remind that all numbers round to 4 significant digits
for i in range(1,12):
    H.append( round(n_case[i] - n_case[i-1],4) )
    
# Sp_mtx is for storing matrix for solving Az = B, for which A - Sp_mtx
Sp_mtx = np.zeros((10,10), dtype = float)
# firstly set up [0:10][1:11]
# Secondly set up [1:11][0:10]
# Thirdly all the entries on diagonal should be 2(dx_i + dx_i+1) = 4
for i in range(9):
    Sp_mtx[i][i+1] = 1.0
    Sp_mtx[i+1][i] = 1.0
    Sp_mtx[i][i] = 4
    if i == 8:
        Sp_mtx[i+1][i+1] = 4
    
# b's entries are 6*
b = np.zeros((10,1), dtype = float)
for i in range(10):
    b.itemset((i,0), 6.0 * (H[i+1] - H[i]) )
z = np.linalg.solve(Sp_mtx,b)
# By continuity of the equation system, z_0 = z_11 = 0.
z = np.vstack([z, [0.]])
z = np.vstack([[0.], z])

x = symbols('x')
s0 = (z.item(1,0)/6.0) * (x - day[0])**3 - (z.item(0,0)/6.0)*(x-day[1])**3 + (n_case[1] - (z.item(1,0)/6.0))*(x-day[0]) - (n_case[0] - (z.item(0,0)/6.0))*(x-day[1])
s1 = (z.item(2,0)/6.0) * (x - day[1])**3 - (z.item(1,0)/6.0)*(x-day[2])**3 + (n_case[2] - (z.item(2,0)/6.0))*(x-day[1]) - (n_case[1] - (z.item(1,0)/6.0))*(x-day[2])
s2 = (z.item(3,0)/6.0) * (x - day[2])**3 - (z.item(2,0)/6.0)*(x-day[3])**3 + (n_case[3] - (z.item(3,0)/6.0))*(x-day[2]) - (n_case[2] - (z.item(2,0)/6.0))*(x-day[3])
s3 = (z.item(4,0)/6.0) * (x - day[3])**3 - (z.item(3,0)/6.0)*(x-day[4])**3 + (n_case[4] - (z.item(4,0)/6.0))*(x-day[3]) - (n_case[3] - (z.item(3,0)/6.0))*(x-day[4])
s4 = (z.item(5,0)/6.0) * (x - day[4])**3 - (z.item(4,0)/6.0)*(x-day[5])**3 + (n_case[5] - (z.item(5,0)/6.0))*(x-day[4]) - (n_case[4] - (z.item(4,0)/6.0))*(x-day[5])
s5 = (z.item(6,0)/6.0) * (x - day[5])**3 - (z.item(5,0)/6.0)*(x-day[6])**3 + (n_case[6] - (z.item(6,0)/6.0))*(x-day[5]) - (n_case[5] - (z.item(5,0)/6.0))*(x-day[6])
s6 = (z.item(7,0)/6.0) * (x - day[6])**3 - (z.item(6,0)/6.0)*(x-day[7])**3 + (n_case[7] - (z.item(7,0)/6.0))*(x-day[6]) - (n_case[6] - (z.item(6,0)/6.0))*(x-day[7])
s7 = (z.item(8,0)/6.0) * (x - day[7])**3 - (z.item(7,0)/6.0)*(x-day[8])**3 + (n_case[8] - (z.item(8,0)/6.0))*(x-day[7]) - (n_case[7] - (z.item(7,0)/6.0))*(x-day[8])
s8 = (z.item(9,0)/6.0) * (x - day[8])**3 - (z.item(8,0)/6.0)*(x-day[9])**3 + (n_case[9] - (z.item(9,0)/6.0))*(x-day[8]) - (n_case[8] - (z.item(8,0)/6.0))*(x-day[9])
s9 = (z.item(10,0)/6.0) * (x - day[9])**3 - (z.item(9,0)/6.0)*(x-day[10])**3 + (n_case[10] - (z.item(10,0)/6.0))*(x-day[9]) - (n_case[9] - (z.item(9,0)/6.0))*(x-day[10])
s10 = (z.item(11,0)/6.0) * (x - day[10])**3 - (z.item(10,0)/6.0)*(x-day[11])**3 + (n_case[11] - (z.item(11,0)/6.0))*(x-day[10]) - (n_case[10] - (z.item(10,0)/6.0))*(x-day[11])
print("The cubic spline functions are:")
s1 = expand(s1)
s2 = expand(s2)
s3 = expand(s3)
s4 = expand(s4)
s5 = expand(s5)
s6 = expand(s6)
s7 = expand(s7)
s8 = expand(s8)
s9 = expand(s9)
s10 = expand(s10)
s0 = exp(s0)
s1 = exp(s1)
s2 = exp(s2)
s3 = exp(s3)
s4 = exp(s4)
s5 = exp(s5)
s6 = exp(s6)
s7 = exp(s7)
s8 = exp(s8)
s9 = exp(s9)
s10 = exp(s10)
print("s0 =")
print(s0)
print("s1 =")
print(s1)
print("s2 =")
print(s2)
print("s3 =")
print(s3)
print("s4 =")
print(s4)
print("s5 =")
print(s5)
print("s6 =")
print(s6)
print("s7 =")
print(s7)
print("s8 =")
print(s8)
print("s9 =")
print(s9)
print("s10 =")
print(s10)


# Problem 1 Question 2 Plot part
# 1)Original sample plot
# 2)Cubic Spline plot

def f1(x):
    if x>=0 and x<=1:
        return -107.9923*x**3 + 498.9923*x + 4831.14
    if x>1 and x<=2:
        return 178.5317*x**3 - 859.572*x**2 + 1358.5643*x + 4544.616
    if x>2 and x<=3:
        return -135.4143*x**3 + 1024.1038*x**2 - 2408.7873*x + 7056.1837
    if x>3 and x<=4:
        return 102.8356*x**3 - 1120.145*x**2 + 4023.9592*x + 623.4372
    if x>4 and x<=5:
        return -55.788*x**3 + 783.3372*x**2 - 3589.9697*x + 10775.3425
    if x>5 and x<=6:
        return 184.1763*x**3 - 2816.1259*x**2 + 14407.3458*x - 19220.1834
    if x>6 and x<=7:
        return -498.6371*x**3 + 9474.5136*x**2 - 59336.4913*x + 128267.4909
    if x>7 and x<=8:
        return 623.242*x**3 - 14084.9458*x**2 + 105579.7246*x - 256537.013
    if x>8 and x<=9:
        return -438.3408*x**3 + 11393.0408*x**2 - 98244.1678*x + 286993.3669
    if x>9 and x<=10:
        return 183.8413*x**3 - 5405.8752*x**2 + 52946.0759*x - 166577.3642
    if x>10 and x<=11:
        return -36.4543*x**3 + 1202.9904*x**2 - 13142.5796*x + 53718.154
    
temp1 = np.arange(0.,11.01,0.01)
plot_x = []
plot_y = []
for i in temp1:
    plot_x.append(i)
for i in plot_x:
    plot_y.append(f1(i))
plt.plot(day,n_case,label = "Sample") 
plt.legend()
plt.plot(plot_x,plot_y,label="Cubic Spline")
plt.legend()
plt.savefig('Covid Jan Interpolation')



# Problem 1 Question 3
# Recall the formula of Trapzoid Rule
# h/2 * [f_0+f_n + 2 * (f_1 + f_2 + ... + f_n-1)]
# Remind that h = 1
total = 0.
for i in range(1,11):
    total += n_case[i]
int_val = 0.5 * (n_case[0] + n_case[11] + 2. * total)
print(int_val)
total += n_case[0] + n_case[11]
print(total)













