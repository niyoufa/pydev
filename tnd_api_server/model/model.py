# -*- coding: utf-8 -*-

"""
    author : youfaNi
    date : 2016-07-13
"""

import pdb
import dhuicredit.model.mongo as mongo

class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

class BaseModel(object):

    def __init__(self,name):
        self.__name = name

    def coll_name(self):
        return self.__name.split(".")[1]

    def db_name(self):
        return self.__name.split(".")[0]

    def get_coll(self):
        coll_name = self.coll_name()
        coll = mongo.get_coll(coll_name)
        return coll