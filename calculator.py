#!/bin/env python
from time import sleep
class Calculator():
    delay = 0.7
    
    def __init__(self):
        sleep(Calculator.delay)
        self.result = 0
        
    def set(self, value):
        sleep(Calculator.delay)
        self.result = int(value)    
        
    def add(self, value):
        sleep(Calculator.delay)
        self.result += int(value)        
        
    def sub(self, value):
        sleep(Calculator.delay)
        self.result -= int(value)    
        
    def mul(self, value):
        sleep(Calculator.delay)
        self.result *= int(value)    