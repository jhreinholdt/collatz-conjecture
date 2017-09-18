# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 16:03:24 2017

@author: jorei
"""
#Collatz Conjecture - Start with a number n > 1. 
#Find the number of steps it takes to reach one using the following process: 
#If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. 
def collatzconjecture(number):
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
    return int(number)
            
def main():
    for number in range(2, 1000):
        print(collatzconjecture(number))
    
if __name__ == '__main__':
    main()