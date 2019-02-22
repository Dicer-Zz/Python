# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Author: Dicer
# @Date:   2019-01-25 16:41:32

from django.shortcuts import render

def hello(request):
	context = {}
	context['hello'] = 'Hello World!'
	return render(request, 'hello.html', context)
