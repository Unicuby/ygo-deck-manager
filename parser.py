# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:43:02 2020

@author: Bastien
"""

def export(path):
    
    file =  open(path, "r")
    L = []
    for lines in file:
        L.append(lines)
    
    file.close()
    return L