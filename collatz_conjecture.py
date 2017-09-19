# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:03:24 2017

@author: jorei
"""
#Collatz Conjecture - Start with a number n > 1. 
#Find the number of steps it takes to reach one using the following process: 
#If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. 

import matplotlib.pyplot as plt
import numpy as np

def collatzconjecture(number):
    iterations = 0
    while number != 1:
        if number % 2 == 0:
            number = number / 2
            iterations += 1
        else:
            number = 3 * number + 1
            iterations += 1
    return int(iterations)
            
def main():
    maxno = 1000000
    x = np.arange(2,maxno)
    y = np.arange(0,maxno-2)
    for number in x:
        y[number-2] = collatzconjecture(number)
        
    dots = plt.plot(x,y)
    plt.setp(dots, marker='.', linewidth='0.0', markersize='1.5')
    plt.xscale('log')
    plt.grid(True, which="both", ls="-", color='0.65')
    plt.ylabel('Number of iterations')
    plt.xlabel('Starting number')
    plt.savefig('CollatzIterations.png', bbox_inches='tight')
    plt.show()
    
    
if __name__ == '__main__':
    main()