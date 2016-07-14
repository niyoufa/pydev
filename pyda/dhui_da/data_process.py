#coding=utf-8

"""
author : niyoufa
date   : 2016-07-12
desc   : 该文档
"""

import pandas as pd
import sys,pdb
sys.path.append("../..")
import pyda.pdio as pp

def statistic_pay_type(*args,**options):
    df = pp.import_from_csv("sale.order.csv")
    data = df[["id","order_customer_id","pay_time","pay_type"]]
    res = data["pay_type"].value_counts()
    print res
    df = pd.DataFrame(res,columns=[u"数量"])
    pp.export_to_excel(df,"pay_type.xlsx","Sheet1")
    pp.export_to_png(df,"pay_type.png")

if __name__ == "__main__":
    statistic_pay_type()