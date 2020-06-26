# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:43:28 2020

@author: Bastien
"""
import random

class deck:
    
    def __init__(self, content = []):
        deck.size = len(content)
        deck.content = content
        
    def shuffle(self):
        if self.size > 1:
            random.shuffle(self.content)
            
class main(deck):#main deck
    
    def __init__(self, content = []):
        deck.__init__(self, content)
    
class extra(deck):#extra-deck
    
    def __init__(self, content = []):
        deck.__init__(self, content)