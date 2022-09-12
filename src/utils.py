from copy import deepcopy
import pytest
import re
import math
import random

the = {}

def coerce(s: str):
    def fun(s1: str):
        if s1 == "true":
            return True
        if s1 == "false":
            return False
        return s1
    string = s
    try:
        string = int(s)
    except ValueError:
        try:
            string = float(s)
        except ValueError:
            string = fun(re.search('^\s*(.-)\s*$', s)).group(1)
        return string
    except Exception as e:
        print("Error 101: coerce_file_crashed")
    
def the_function(help: str):
    the = {}
    try:
        valuesToAppend = re.findall('\n [-][^\s]+[\s]+[-][-]([^\s]+)[^\n]+= ([^\s]+)', help)
        for match in valuesToAppend:
            the[match[0]] = coerce(match[1])
        return the
    except Exception as e:
        print("Error 102: the_function crashed",e)
        
        
def per(t, p):
    
    '''
    Return the pth item from the sorted list 't'
    Arguments:
        p: Denotes index
        t: Denotes sorted list
    '''
    p = math.floor(((p or 0.5) * len(t)) + 0.5)
    return t[math.max(1, math.min(len(t), p))]
    
def o(t):
    '''
    Generates a string from nested list
    Arguments:
        t: Denotes list of values
    '''

    if type(t) != list:
        return str(t)

    def show(k, v):
        if str(k).find('^_') == -1:
            v = o(v)
            return len(t) == 0 and format(':{} {}', k, v) or str(v)

    u = []
    index = 0
    dict_keys = list(t.keys())
    for key in dict_keys:
        u[index] = show(key, t[key])
    if len(t) == 0:
        u.sort()
    return '{' + ' '.join(str(item) for item in u) + '}'

def oo(t):
    '''
    Prints the string from o()
    Arguments:
        t: Denotes list of values
    '''
    print(o(t))
    return t

def copy(t: dict):
    
    # deepcopy

    u = {}
    if type(t) != dict:
        return t
    for k,v in t.items():
        u[k] = copy[v]

    return u