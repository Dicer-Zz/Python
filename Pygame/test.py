#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Dicer
# @Date:   2019-02-17 15:33:26

s = input()
try:
	number = float(s)
except:
	number = 0
answer = number * number
print("{} * {} = {}".format(number, number, answer))