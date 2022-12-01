# -*- coding: utf-8 -*-
"""
Problem 1 - Advent of code 2022

Created on Thu Dec  1 16:09:12 2022

@author: marinalseoane
"""
import numpy as np

i = 0
elves = [0]

with open('input.txt', 'r') as input:
    for line in input:
        if line != '\n':
            num = float(line)
            elves[i] += num
        if line == '\n':
            i += 1
            elves.append(0)

print("max", max(elves))
