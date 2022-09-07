# -*- coding: utf-8 -*-
"""MM PS - 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xFpv__eVXu_Ld-UqomouFFIIdA1ygvtx
"""

import random
from matplotlib import pyplot as plt
import math
import scipy.stats as stats
from statistics import mean

"""#Question - 1"""

# Part 1
a0 = 0
r = 0
aN = []
for i in range(0,20):
  aN.append(pow(r,i)*a0)
print("a0 = 0 and r = 0 then aN = ", aN)

X = list(range(0,20))
plt.plot(X,aN)
plt.show()

# Part 2
a0 = 50
r = 0.5
aN = []
for i in range(0,20):
  aN.append(pow(r,i)*a0)
print("a0 = ", a0, "and r = ", r, "then aN = ", aN)

X = list(range(0,20))
plt.plot(X,aN)
plt.show()

# Part 3
a0 = 50
r = -0.5
aN = []
for i in range(0,20):
  aN.append(pow(r,i)*a0)
print("a0 = ", a0, "and r = ", r, "then aN = ", aN)

X = list(range(0,20))
plt.plot(X,aN)
plt.show()

# Part 4
a0 = 50
r = 2
aN = []
for i in range(0,20):
  aN.append(pow(r,i)*a0)
print("a0 = ", a0, "and r = ", r, "then aN = ", aN)

X = list(range(0,20))
plt.plot(X,aN)
plt.show()

"""#Question 2"""

def fun(n, a0):
  a=[a0]
  for i in range(n):
    a.append(0.5*a[-1] + a0)
  return a

a0_1 = 0.1
a0_2 = 0.2
a0_3 = 0.3

a1 = fun(20,a0_1)
a2 = fun(20,a0_2)
a3 = fun(20,a0_3)
plt.plot(a1)
plt.plot(a2)
plt.plot(a3)

"""#Question 3"""

def forward_difference_table(arr):
  forward_difference_tab=[]

  while len(arr)>1:
    temp=[]
    
    for i in range(1,len(arr)):
      temp.append(arr[i]-arr[i-1])
    forward_difference_tab.append(temp)
    arr = temp

  return forward_difference_tab

def ncr(n, r):
  val = 1
  for i in range(r):
    val *= (n - i)
  if r == 1:
    return val
  a = val / math.factorial(r)
  return a

def forward_interpolation(y_0, n, fdt, u):
  val = y_0
  for i in range(n):
    val += ncr(u, i+1) * fdt[i][0]
  return val

n = list(range(1,17))
aN = [3,6,11,21,32,47,65,87,112,110,171,204,241,282,325,376]

forward_diff_table = forward_difference_table(aN)
print(forward_diff_table)
plt.plot(forward_diff_table[0])

error = []

for i in range(len(aN)):
  u = (n[i]-n[0])/(n[1]-n[0])
  y_cap = forward_interpolation(aN[0], len(forward_diff_table), forward_diff_table, u)
  error.append(y_cap - aN[i])

print(error)
plt.plot(n,error)

"""#Question 4"""

force=[10, 20, 30, 40, 50, 60, 70, 80, 90]
stretch=[19, 57, 94, 134, 173, 216, 256, 297, 343,]

forward_diff_table = forward_difference_table(stretch)
print(forward_diff_table)
plt.plot(forward_diff_table[0])

error = []
y_cap = []

for i in range(len(stretch)):
  u = (force[i]-force[0])/(force[1]-force[0])
  y_cap.append(forward_interpolation(stretch[0], len(forward_diff_table), forward_diff_table, u))
  error.append(y_cap[-1] - stretch[i])

print(error)
plt.plot(force,error)
plt.show()

plt.plot(force,y_cap)
plt.show()

y_cap = []
force_x = [15,17,85]
for i in range(len(force_x)):
  u = (force_x[i]-force[0])/(force[1]-force[0])
  y_cap.append(forward_interpolation(stretch[0], len(forward_diff_table), forward_diff_table, u))


print(y_cap)
t_statistic, p_value = stats.ttest_ind(stretch, y_cap)
print(t_statistic , p_value)