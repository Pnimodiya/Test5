# -*- coding: utf-8 -*-

 ###This is my first python program
"""
Created on Mon Mar 30 15:31:51 2020

@author: pjaipuri
"""


even_nums=(2,4,6,7)
========================
def raise_power(v1,v2):
    v3=v1**v2
    v4=v2**v1
    return (v3,v4)

x=raise_power(2,3)

=======================

def fibo(n):
    a,b=0,1
    while a<n:
        print (a)
        a,b=b,a+b
        
fibo(80)

=======================

def fibo2(n):
    a,b=0,1
    list1=[]
    while a<n:
        list1.append(a)
        a,b=b,a+b
    return list1

fibo2(80)

=========================

