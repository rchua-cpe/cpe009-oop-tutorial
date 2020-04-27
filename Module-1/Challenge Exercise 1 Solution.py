#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 00:57:09 2020

@author: royce
"""

#Enter the product price: 2000
#Enter the 1st offer (Discount): 0.3
#Enter the 2nd offer (less): 500
#
#The final price in 1st offer is: 1400
#The final price in 2nd offer is: 1500

# Ask for the product's price
original_price = float(input("Enter the product price: "))
# Ask for the 1st discount offer (in percent)
discount = float(input("Enter the 1st offer (Discount): "))
# Ask for the 2nd offer less 
less = float(input("Enter the 2nd offer (less): "))

# compute for the discounted price
discount = original_price - (original_price * discount)
# compute for the less price
less = original_price - less

# display the results 
print(f"The final price in 1st offer is: {discount:.2f}")
print(f"The final price in 2nd offer is: {less:.2f}")