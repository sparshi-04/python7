# -*- coding: utf-8 -*-
"""Q15.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mj2bzTPaKPLXpR1PfGV931EiS0PblLL4
"""

def rev_list(list):
    if len(list) <= 1:
        return list
    else:
        return rev_list(list[1:]) + [list[0]]

no = [1, 2, 3, 4, 5]
rev_no = rev_list(no)
print("Original list:", no)
print("Reversed list:", rev_no)