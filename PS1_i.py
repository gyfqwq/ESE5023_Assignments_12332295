# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:09:01 2023

@author: a
"""

#1
import random
a=random.randint(0,100)
b=random.randint(0,100)
c=random.randint(0,100)
print(a,b,c)
def Print_values(a,b,c):
    if a>b:
        if b>c:
            print(a,b,c)
        else:
            if a>c:
                print(a,c,b)
            else:
                print(c,a,b)
    else:
        if b>c:
            if a>c:
                print(a,c,b)
            else:
                print(c,a,b)
        else:
            print(c,b,a)
Print_values(a,b,c)

#2
import numpy as np
M1 = np.random.randint(0,51,(5,10))
M2 = np.random.randint(0,51,(10,5))
print(M1)
print(M2)
def Matrix_multip():
    result = np.zeros((5,5))
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for k in range(len(M2)):
                result[i][j] += M1[i][k] * M2[k][j]
    return result.astype(int)
Matrix_multip()

#3
def Pascal_triangle(k):
    triangle = []
    for i in range(k):
        row = []
        for j in range(i+1):
            if j==0 or j==i:
                row.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)
    if k == 100 or k ==200:
        print(triangle[k-1])
Pascal_triangle(100)
Pascal_triangle(200)

#4
count = 0
RMB = 1
import random
x = random.randint(1,101)
print(x)
def Least_moves(x):
    global RMB,count
    while RMB < x:
        if 2*RMB <= x:
            RMB = 2*RMB
        else:
            RMB += 1
        count += 1
    print(count)
Least_moves(x)

#5
def Find_expression(target, current='', total=0, idx=0):
    nums = '123456789'
    if idx == len(nums) and total == target:
        print(f'{current} = {target}')
    for i in range(idx + 1, len(nums) + 1):
        num = int(nums[idx:i])
        if idx == 0:
            Find_expression(target, str(num), num, i)
        else:
            Find_expression(target, current + '+' + str(num), total + num, i)
            Find_expression(target, current + '-' + str(num), total - num, i)
import random
n = random.randint(1, 101)
Find_expression(n)

def Find_expression_count(target, current='', total=0, idx=0):
    nums = '123456789'
    count = 0
    if idx == len(nums) and total == target:
        count += 1
    for i in range(idx + 1, len(nums) + 1):
        num = int(nums[idx:i])
        if idx == 0:
            count += Find_expression_count(target, str(num), num, i)
        else:
            count += Find_expression_count(target, current + '+' + str(num), total + num, i)
            count += Find_expression_count(target, current + '-' + str(num), total - num, i)
    return count

Total_solutions = [Find_expression_count(i) for i in range(1, 101)]
import matplotlib.pyplot as plt
plt.plot(range(1, 101), Total_solutions)
plt.xlabel('Target Number')
plt.ylabel('Number of Solutions')
plt.show()
max_solutions_num = max(Total_solutions)
min_solutions_num = min(Total_solutions)
max_numbers_indices = [i for i, x in enumerate(Total_solutions, start=1) if x == max_solutions_num]
min_numbers_indices = [i for i, x in enumerate(Total_solutions, start=1) if x == min_solutions_num]
print("Maximum number of solutions is", max_solutions_num, "for the numbers:", max_numbers_indices)
print("Minimum number of solutions is", min_solutions_num, "for the numbers:", min_numbers_indices)