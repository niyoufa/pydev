# -*- coding: utf-8 -*-
#
# @author: Daemon wang
# Created on 2016-03-02
#

import platform
import os
import time

# can't use __file__ directly here because it's parsed by tornado.options
import tnd_api_server
from tnd_api_server.app import get_root_path
root_dir = os.path.dirname(os.path.abspath(tnd_api_server.__file__))

if platform.node() == "iZ2370ct37bZ":
    debug = False
    host = 'dhuicredit'
    login_url = "https://www.dhuicredit.com/login"
else:
    debug = True
    host = 'localhost:8002'
    login_url = "http://localhost:8002/login"


loglevel = "INFO"  # for celeryd
port = 30000
app_url_prefix = ""
sitename = "dhuicredit api"
domain = "www.dhuicredit.com"
home_url = "http://%s/api" % domain

root_path = get_root_path()
cookie_secret = "ace87395-8272-4749-b2f2-dcabd3901a1c"
xsrf_cookies = False

###分页相关设置
#一页显示的条数
page_size = 15
#最多显示的页数
page_show = 10

file_download_store_url = get_root_path()+"/static/download/"
file_upload_store_url = get_root_path()+"/static/download/"

ssl_options={
           "certfile": os.path.join(get_root_path(), "ssl/apache.crt"),
           "keyfile": os.path.join(get_root_path(), "ssl/apache.key"),
       }

mongo = {
            "host":"localhost",
            "port":27017,
            "database":"dhuicredit",
            "user":"dhuicredit",
            "password":"DhuiCreditAdmin",
        }

redis = {
    "host":"localhost",
    "port":6379,
    "db":0
}

smtp = {"host": "smtp.exmail.qq.com",
        "user": "admin@dhuicredit.com",
        "password": "You123456",
        "duration": 30,
        "tls": True
        }

sex = {0: "未知",
              1: "男",
              2: "女"
              }

on_sale_flag = {0: "未上架",
              1: "已上架"
              }

TEST_USER = ["57330c6c006f877f57fcc4e7","572c37bb006f870cf2f75978","5720201c006f873b606394fb","571dbf0c006f874b52b126aa"]

auth_status = {
    "committed":["committed","已提交"],
    "checking":["cheching","审核中"],
    "pass":["pass","审核通过"],
    "nopass":["nopass","审核未通过"],
}
edit_status = {
    "noedit":["noedit","不可修改"],
    "edit":["edit","可修改"],
}
auth_type = {
    "person":["person","个人"],
    "company":["company","企业"],
}

server_addr = "http://localhost:10000"
