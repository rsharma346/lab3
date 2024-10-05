#!/usr/bin/env python3
'''Lab 3 Part 1 script - functions'''
# Author ID: [seneca_id]

# Function to add two numbers
def sum_numbers(number1, number2):
    return int(number1) + int(number2)

# Function to subtract two numbers
def subtract_numbers(number1, number2):
    return int(number1) - int(number2)

# Function to multiply two numbers
def multiply_numbers(number1, number2):
    return int(number1) * int(number2)

if __name__ == '__main__':
    print(sum_numbers(10, 5))      # Should return 15
    print(subtract_numbers(10, 5)) # Should return 5
    print(multiply_numbers(10, 5)) # Should return 50

