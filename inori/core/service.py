# -*- coding: utf-8 -*-

class Service(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
