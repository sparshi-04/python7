# -*- coding: utf-8 -*-
"""Q17.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qUeB-Se_n90UnmLePCzrRFKQqD7L0kx-
"""

list = [1,4,6,-5,-3,7,-10,-2]
def repl_negative(list,ind = 0):
  if ind == len(list):
    return list
  if list[ind] < 0:
     list[ind] = 0
  return repl_negative(list, ind + 1)

print('org_list:',list)
repl_negative(list)
print('updated one:',list)