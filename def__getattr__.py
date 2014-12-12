#!/usr/bin/env python
class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='firstn':
            return 'yunzhi'
        else:
            return 'funny'
