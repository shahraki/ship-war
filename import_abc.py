import numpy as np
#inputs
inputArray = np.array([[35,53,63],[72,12,22],[43,84,56]])
new_col = np.array([[20,30,40]])
# delete 2nd column
arr = np.delete(inputArray , 1, axis = 0)
print(arr)
#insert new_col to array
arr = np.insert(arr , 1, new_col, axis = 1)
print (arr)
# import pandas
# dataframe = pandas.DataFrame( data, index, columns, dtype)
# class p:
#     def __init__(self) -> None:
#         print("p")
#     def pf(self):
#         print("djdjdjd")
        

# class c(p):
#     def __init__(self) -> None:
#         print("c")
#     def pf(self):
#         s=2
#         print(s)

# s = c()
# s.pf()  
# # c.mro()
# p.pf(s)
        
# def help1(e,**t):
#     print(e)
#     for w,w1 in t.items():
#         print(w,w1)
# help1(4,a=1,b=1)
# help1(4,b=6)
# def fib(n):
#     p, q = 0, 1
#     while(p < n-2):
#         # yield p
#         p, q = q, p + q
#     return p    
# x = fib(10)
# print(x)
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# def myWrapper(n):
#  return lambda a : a * n
# mulFive = myWrapper(5)
# print(mulFive(2)) 

# for i in range(1,10):    # numbers from 1 to 9
#     print(i)

# import torch
# x = torch.rand(5, 3)*9
# print(x)

import abc
from abc import ABC, abstractmethod
 
class parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "parent class"
class child(parent):
      
    @property
    def geeks(self):
        return "child class"

try:
    # r =parent()
    print(parent.geeks)
    print( r.geeks)
except Exception as err:
    print (err)
  
r = child()

print (r.geeks)