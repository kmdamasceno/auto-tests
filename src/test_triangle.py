# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 18:15:08 2023

@author: Klaus Damasceno
"""

import pytest

def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return 'Not a triangle'
    elif a == b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    else:
        return 'Scalene'

def test_nottriangle():
        assert triangle_type(1,1,3) == 'Not a triangle'
    
def test_equilateral():
        assert triangle_type(1,1,1) == 'Equilateral'
    
def test_isoceles():
        assert triangle_type(2,2,1) == 'Isosceles'

def test_scalene():
        assert triangle_type(5,4,3) == 'Scalene'