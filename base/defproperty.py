#!/usr/bin/env python
class Student(object):
    def get_score(self):
        return self._score

    def set_score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        else:
            self._score = value
