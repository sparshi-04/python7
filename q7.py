# -*- coding: utf-8 -*-
"""Q7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AatdG--648MlQSZeZGF3zrbxqYAoqiAp
"""

def ispalindrome(string):
  return string==string[::-1]

str = input('enter str:')
if (ispalindrome(str)):
  print('yes')
else:
  print('no')