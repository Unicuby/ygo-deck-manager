# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 15:04:14 2020

@author: Bastien
"""

import data

def __main__():
    print(50 * '=')
    print("Welcome to the yu-gi-oh! deck manager")
    print(50 * '=')
    
    path = input("please give the path of the deck\n")
    
    while data.deck_import(path) is None:
        path = input("please give the path of the deck\n")
    
    deck = data.deck_import(path)
    data.wishlist_printer(deck)
    input("\n \n Finished exporting, press any key to continue ...")
    save = input("Would you like to save the result into a file? Y/N\n")
    save = save.upper()
    while save != "YES" and save != "Y" and save != "NO" and save != "N":
        save = input("Would you like to save the result into a file? Y/N\n")
    
    if save == "YES" or save == "Y":
        data.wishlist_exporter(data)
        input("saved the wishlist press any key to exit...")

__main__()