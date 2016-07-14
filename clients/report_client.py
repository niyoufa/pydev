#coding=utf-8

"""
    author : niyoufa
    date : 2016-05-27

"""

import xlsxwriter
import datetime
import pdb

import ods.settings as settings
import ods.utils as utils

class Xlsx_Reporter(object):
    """
        xlsx报表生成器
        author : niyoufa
        date : 2016-06-16
        refer : xlsxwriter
        example1 : 将数据写入xlsx指定位置
            xlsx_reporter = Xlsx_Reporter(filename="example")
            columns = [u'姓名','age','sex','address']
            data_set = [["niyoufa", "25"], ["liuxiaoyan", "25",'woman'],["liuxiaoyan", "25"]]
            worksheet = xlsx_reporter.get_worksheet()
            xlsx_reporter.init_style(columns=columns,data_set=data_set,worksheet=worksheet)
            xlsx_reporter.init_formula(columns=columns, data_set=data_set, worksheet=worksheet)
            xlsx_reporter.report(columns=columns,data_set=data_set,worksheet=worksheet)
            xlsx_reporter.close()

    """
    @classmethod
    def get_x_index_list(cls):
        x_index_list = []
        for i in range(97,123):
            for j in range(97,123):
                    x_index_list.append( ( chr(i)+chr(j) ).upper() )
        return x_index_list

    @classmethod
    def get_next_x_index(cls,x_index):
        if len(x_index) == 1 :
            return chr(ord(x_index) + 1)

    def __get_workbook_name(self,*args,**options):
        filename =  options.get("filename","")
        if filename == "" :
            filename = settings.REPORT_PATH + str(datetime.datetime.now()).replace("-","_").\
        replace(" ","_").replace(":","_").replace(".","_") + ".xlsx"
        else :
            curr_time = datetime.datetime.now()
            filename = settings.REPORT_PATH + filename + "(%s-%s-%s)"%(curr_time.year,curr_time.month,curr_time.day) + ".xlsx"
        return filename


    def __create_workbook(self,filename,*args,**options):
        return xlsxwriter.Workbook(filename)

    def __create_worksheets(self,workbook,worksheet_names):
        worksheet_dict = {}
        if type(worksheet_names) != type([]):
            raise Exception("param error :work sheet names should be a list")
        elif len(worksheet_names) == 0:
            worksheet_names.append("Sheet1")
        else:
            pass
        for name in worksheet_names :
            worksheet = workbook.add_worksheet(name)
            worksheet_dict[name]= worksheet

        return worksheet_dict

    def __init__(self,*args,**options):
        self.filename = self.__get_workbook_name(*args,**options)
        self.worksheet_names = options.get("worksheet_names",[])
        self.workbook = self.__create_workbook(self.filename)
        self.workbook.worksheet_names = self.worksheet_names
        self.worksheet_dict = self.__create_worksheets(self.workbook,self.workbook.worksheet_names)

    def get_worksheet(self, worksheet_name=None):
        if worksheet_name == None :
            return self.worksheet_dict.values()[0]
        worksheet = self.worksheet_dict.get(worksheet_name, None)
        return worksheet

    def get_worksheets(self,worksheet_names):
        return [self.get_worksheet(name) for name in worksheet_names]

    def get_all_worksheet(self):
        worksheet_names = self.worksheet_names
        worksheets = self.get_worksheets(worksheet_names)
        return worksheets

    def close(self):
        self.workbook.close()

    def __get_columns_range(self,columns,*args,**options):
        if type(columns) != type([]):
            raise Exception("params error : columns must be a list")
        start_index = options.get("start_index","A")
        length = len(columns)
        if length :
            col_range = start_index + ":" + chr(ord("A")+length-1)
        else :
            col_range = start_index + ":" + chr(ord("A"))
        return col_range

    def __get_rows_range(self,data_set,*args,**options):
        if len(data_set):
            if type(data_set[0]) != type([]):
                raise Exception("params error : data_set must be like this [[],[]]")
        if len(data_set):
            rows_range = (len(data_set),max([len(row) for row in data_set ]))
        else :
            rows_range = (0,0)
        return rows_range

    def __get_data_set_range(self, columns, data_set, *args, **options):
        columns_range = self.__get_columns_range(columns)
        rows_range = self.__get_rows_range(data_set)
        if len(columns_range) == 0 :
            date_set_range = ""
        else :
            x_index_list = columns_range.split(":")
            date_set_range = x_index_list[0]+str(1) + ":" + x_index_list[1]+str(rows_range[0]+1)
        return date_set_range

    def init_style(self, *args, **options):

        # init style const
        self.bold = self.workbook.add_format({'bold': 1})

        worksheet = options.get("worksheet", None)
        columns = options.get("columns", [])
        data_set = options.get("data_set", [])

        if len(data_set):
            if type(data_set[0]) != type([]):
                raise Exception("params error : data_set must be like this [[],[]]")

        if len(data_set) and len(columns) < max([len(row) for row in data_set ]):
            raise Exception("params error : the length of columns must equal the length of data_set ")

        if not worksheet:
            raise Exception("params error :please set worksheet")
        else:
            columns_range = self.__get_columns_range(columns)
            worksheet.set_column(columns_range, 20)
            worksheet.set_row(0, 20, self.bold)

    def init_formula(self,*args,**options):
        worksheet = options.get("worksheet", None)
        columns = options.get("columns", [])
        data_set = options.get("data_set", [])

        if not worksheet:
            raise Exception("params error :please set worksheet")
        else:
            data_set_range = self.__get_data_set_range(columns,data_set)
            if data_set_range == "":
                return
            worksheet.autofilter(data_set_range)

    # 生成xlsx报表
    def report(self,*args,**options):
        """
        :param args:
        :param options: worksheet, columns 表头 [], data_set 数据数组 [[],[]]
        :return: None
        """
        worksheet = options.get("worksheet", None)
        columns = options.get("columns", [])
        data_set = options.get("data_set", [])

        if len(data_set):
            if type(data_set[0]) != type([]):
                raise Exception("params error : data_set must be like this [[],[]]")

        if worksheet == None or type(columns) != type([]) or type(data_set) != type([]):
            raise Exception("worksheet can not be None Type")
        else:
            worksheet.write_row('A1', columns)
            row = 1
            for row_data in (data_set):
                worksheet.write_row(row, 0, row_data)
                row += 1
        self.close()

    def export_xlsx(self,*args,**options):
        self.init_style(*args,**options)
        self.init_formula(*args,**options)
        self.report(*args,**options)

        self.close()

if __name__ == "__main__":
    pass