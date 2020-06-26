# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:33:57 2020

@author: Bastien
"""
import sqlite3
import card
import deck
"""
data = sqlite3.connect('Database/cards.cdb')
cursor = data.cursor()
"""


def deck_import(path):
    try:
        f = open(path)
        f.close()
    except FileNotFoundError:
        print('File does not exist please try again')
        return None
    file =  open(path, "r")
    data = {}
    database = sqlite3.connect('Database/cards.cdb')
    cur = database.cursor()
    for lines in file:
        if lines[0] != '#' and lines[0] != '!':
            line = lines.strip()
            #searches the id in the card database
            t = (line,)
            cur.execute('SELECT name FROM texts WHERE id=?', t)
            line = (cur.fetchone())[0]
            if line in data:
                data[line] += 1
            else:
                data.update({line : 1})
    file.close()
    cur.close()
    database.close()
    return data

def wishlist_printer(data):
    print("\n")
    for info in data.items():
        print(str(info[1]) + " " + str(info[0]))

def wishlist_exporter(data, filename="output.txt"):
    file = open(filename, "w")
    
    for info in data.items():
        file.write(str(info[1]) + " " + str(info[0]) + "\n")
    
    file.close()