#coding=utf-8


"""
author : niyoufa
date   : 2016-07-12
desc   : 该文档封装了pandas输入输出操作
"""

import numpy as np
import pandas as pd
import MySQLdb as msqldb
import xlrd
import matplotlib.pyplot as plt

import pdb
import settings

def import_from_csv(filename):
    file_path = settings.IMPORT_PATH + filename
    if file_path.find(".csv"):
        df = pd.read_csv(file_path)
    else :
        raise Exception("file type error,need csv file")
    return df

def import_from_mysql(table_name="demosite_links",db_name="demosite"):
    try:
        mysql_cn= msqldb.connect(host=settings.MYSQL_HOST,
            port=settings.MYSQL_PORT,
            user=settings.MYSQL_USER, passwd=settings.MYSQL_PASS, db=db_name)
    except Exception,e:
        raise Exception("connect mysql db:%s,table:%s error"%(db_name,
            table_name))
    df = pd.read_sql('select * from %s'%table_name, con=mysql_cn)    
    mysql_cn.close()
    return df

def import_from_excel(filename,sheetname):
    file_path = settings.IMPORT_PATH + filename
    if file_path.find(".xls"):
        df = pd.read_excel(file_path,sheetname)
    else :
        raise Exception("file type error,need xls file")
    return df

def export_to_csv(filename,df):
    file_path = settings.EXPORT_PATH + filename
    if not type(df) == type(pd.DataFrame([])):
        raise "df type params error, must be pd.DataFrame object"
    else:
        df.to_csv(file_path,encoding='utf-8',index=False)
    print "export to csv : %s"%file_path

def export_to_excel(df,filename,sheetname):
    file_path = settings.EXPORT_PATH + filename
    if not type(df) == type(pd.DataFrame([])):
        raise "df type params error, must be pd.DataFrame object"
    else:
        if file_path.find(".xlsx"):
            df.to_excel(file_path,sheetname)
        else :
            raise Exception("file type error,need xls file")
    print "export to excel : %s"%file_path

#savefig : eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff.
def export_to_png(df,filename,kind="bar"):
    file_path = settings.EXPORT_PATH + filename
    if file_path.find(".png"):
            plt = df.plot(kind=kind).get_figure()
            plt.savefig(file_path)
    else :
        raise Exception("file type error,need png file")
    print "export to png : %s"%file_path
