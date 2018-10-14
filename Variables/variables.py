# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:50:49 2018

@author: Can
"""
import math
# dir() Metod,function || help() || type() type of variables,etc.

a1 = 10
a2 = 20.5
a3 = "test"
a4 = bool(False)

type(a1)
type(a2)
type(a3)
type(a4)

# len(a1)
#default func ------------------------


def first_func(d1,d2):
    res = d1*d2
    return res
first_func(5,15)


def circle(r):
    pisayi = math.pi
    res = 2*r*pisayi
    return res
circle(5)

#flexible func ---------------------


def hesapla(boy,kilo,*args, **kwargs):
    print(args)
    output = (boy+kilo)*args[0]
    return output


"""
    Quiz
    
    int variable age
    string variable name
    a function
    function must include print(type(), len(), float())
    *args --> surname
    default parameter --> shoe number    
"""  

age = 15
name = "John"
surname = "O'Brien"

def func_quiz(age,name,*args,shoe_numb=35):
    print("Child's name: ",name,", age: ",age,", shoe number: ",shoe_numb)
    print(type(name))
    print(float(age))
    
    output = args[0] * age
    
    return output

# lambda func -------------------------------------
    
def calc(x):
    return x*x
res = calc(3)


res2 = lambda x: x*x
print(res2(3))


wholedifferent = lambda a: a*a*a
print(wholedifferent(3))



























