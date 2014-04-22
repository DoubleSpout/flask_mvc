# -*- coding: utf-8 -*-


class Hello(object):
    name=""
    def __init__(self,name="world"):
        self.name = name

    def MyName(self):
        text = self.name 
        return "hello " + text

