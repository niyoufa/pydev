#coding=utf-8

"""
    author : niyoufa
    date : 2016-05-20

"""

import pymongo, pdb
import ods.settings as settings

class DB_CONST :
    DB_NAME = "db_name"
    COLL_NAME = "coll_name"
    COLL_HOST = "host"
    COLL_PORT = "port"
    USERNAME = "username"
    PASSWORD = "password"
    COLL_TYPE = "coll_type"

class Collections :

    # MongoDB文档配置
    __COLLECTIONS = dict(

        DHUI_Product = dict(
            coll_name="goods",
            db_name="dhui100",
            host=settings.SERVER_MONGODB_HOST,
            port=settings.SERVER_MONGODB_PORT,
            username = settings.SERVER_MONGODB_USER,
            password = settings.SERVER_MONGODB_PASS,
            coll_type=None),

        DHUI_SaleOrder = dict(
            coll_name="order",
            db_name="dhui100",
            host=settings.SERVER_MONGODB_HOST,
            port=settings.SERVER_MONGODB_PORT,
            username=settings.SERVER_MONGODB_USER,
            password=settings.SERVER_MONGODB_PASS,
            coll_type=None),

        DHUI_User = dict(
            coll_name="user",
            db_name="dhui100",
            host=settings.SERVER_MONGODB_HOST,
            port=settings.SERVER_MONGODB_PORT,
            username=settings.SERVER_MONGODB_USER,
            password=settings.SERVER_MONGODB_PASS,
            coll_type=None),

        DHUI_Address = dict(
            coll_name="address",
            db_name="dhui100",
            host=settings.SERVER_MONGODB_HOST,
            port=settings.SERVER_MONGODB_PORT,
            username=settings.SERVER_MONGODB_USER,
            password=settings.SERVER_MONGODB_PASS,
            coll_type=None),

        DHUI_Shipping=dict(
            coll_name="shipping",
            db_name="dhui100",
            host=settings.SERVER_MONGODB_HOST,
            port=settings.SERVER_MONGODB_PORT,
            username=settings.SERVER_MONGODB_USER,
            password=settings.SERVER_MONGODB_PASS,
            coll_type=None),

        DHUI_Partner = dict(
            coll_name="Partner",
            db_name="dhuiodoo",
            host=settings.LOCAL_MONGODB_HOST,
            port=settings.LOCAL_MONGODB_PORT,
            username="",
            password="",
            coll_type=None),

        DHUI_GoodPartner=dict(
            coll_name="GoodPartner",
            db_name="dhuiodoo",
            host=settings.LOCAL_MONGODB_HOST,
            port=settings.LOCAL_MONGODB_PORT,
            username="",
            password="",
            coll_type=None),

        DHUI_PartnerGoodDeliverDetail=dict(
            coll_name="PartnerGoodDeliverDetail",
            db_name="dhuiodoo",
            host=settings.LOCAL_MONGODB_HOST,
            port=settings.LOCAL_MONGODB_PORT,
            username="",
            password="",
            coll_type=None),

        DHUI_PartnerOrderDeliverDetail = dict(
            coll_name="PartnerOrderDeliverDetail",
            db_name="dhuiodoo",
            host=settings.LOCAL_MONGODB_HOST,
            port=settings.LOCAL_MONGODB_PORT,
            username="",
            password="",
            coll_type=None),
        area = dict(
            coll_name="area",
            db_name="dhuiodoo",
            host=settings.LOCAL_MONGODB_HOST,
            port=settings.LOCAL_MONGODB_PORT,
            username="",
            password="",
            coll_type=None),
        province = dict(
            coll_name="province",
            db_name="dhuiodoo",
            host=settings.LOCAL_MONGODB_HOST,
            port=settings.LOCAL_MONGODB_PORT,
            username="",
            password="",
            coll_type=None),
        files = dict(
            coll_name = "files",
            db_name = "niyoufa",
            username="",
            password="",
            host=settings.NEWBIE_MONGODB_HOST,
            port=settings.NEWBIE_MONGODB_PORT,
        ),
        links = dict(
            coll_name = "links",
            db_name = "niyoufa",
            username="",
            password="",
            host=settings.NEWBIE_MONGODB_HOST,
            port=settings.NEWBIE_MONGODB_PORT,
        ),
        repository = dict(
            coll_name = "repository",
            db_name = "niyoufa",
            username="",
            password="",
            host=settings.NEWBIE_MONGODB_HOST,
            port=settings.NEWBIE_MONGODB_PORT,
        ),

    )

    @classmethod
    def get_db_name(cls,table_name) :
        if cls.__COLLECTIONS.has_key(table_name):
            db_name = cls.__COLLECTIONS[table_name][DB_CONST.DB_NAME]
        else :
            db_name = ""
        return db_name

    @classmethod
    def get_coll_name(cls,table_name) :
        if cls.__COLLECTIONS.has_key(table_name):
            coll_name = cls.__COLLECTIONS[table_name][DB_CONST.COLL_NAME]
        else :
            coll_name = ""
        return coll_name

    @classmethod
    def get_coll_host(cls,table_name) :
        if cls.__COLLECTIONS.has_key(table_name):
            coll_host = cls.__COLLECTIONS[table_name][DB_CONST.COLL_HOST]
        else :
            coll_host = ""
        return coll_host
   
    @classmethod
    def get_coll_port(cls,table_name) :
        if cls.__COLLECTIONS.has_key(table_name):
            coll_port = cls.__COLLECTIONS[table_name][DB_CONST.COLL_PORT]
        else :
            coll_port = ""
        return coll_port

    @classmethod
    def get_coll_username(cls,table_name) :
        if cls.__COLLECTIONS.has_key(table_name):
            username = cls.__COLLECTIONS[table_name][DB_CONST.USERNAME]
        else :
            username = ""
        return username

    @classmethod
    def get_coll_password(cls,table_name) :
        if cls.__COLLECTIONS.has_key(table_name):
            password = cls.__COLLECTIONS[table_name][DB_CONST.PASSWORD]
        else :
            password = ""
        return password

def get_client(table_name) :
    host = Collections.get_coll_host(table_name)
    port = Collections.get_coll_port(table_name)
    client = pymongo.MongoClient(host,port)
    return client

def get_address(client=None):
    if client :
        address = client.address
    else :
        client = get_client()
        address = client.address
    return address

def get_db_names(client=None):
    if client :
        db_names = client.database_names()
    else :
        client = get_client()
        db_names = client.database_names()
    return db_names

def get_database(db_name,**kwargs) :
    client = get_client()
    db = client.get_database(db_name)
    return db

def drop_db(db_name,client=None) :
    if client == None :
        client = get_client()
    client.drop_database(db_name)
    print db_name + " dropped!"

def get_coll_names(db_name) :
    db = get_database(db_name)
    coll_names = db.collection_names(include_system_collections=False)
    return coll_names

coll_dict = {}
def get_coll(table_name) :
    if coll_dict.has_key((table_name)):
        return coll_dict[table_name]
    else : 
        db_name = Collections.get_db_name(table_name)
        coll_name = Collections.get_coll_name(table_name)
        username = Collections.get_coll_username(table_name)
        password = Collections.get_coll_password(table_name)
        if db_name and coll_name :
            if username and password :
                client = get_client(table_name)
                db = client[db_name]
                db.authenticate(username,password)
                coll = client[db_name][coll_name]
            else :
                client = get_client(table_name)
                coll = client[db_name][coll_name]
        else :
            coll = None
            print u"集合不存在!"
            return coll
        coll_dict[table_name] = coll
        return coll

def get_coll_db_name(table_name) :
    db_name = Collections.get_db_name(table_name)
    return db_name

def drop_coll(table_name) :
    db_name = Collections.get_db_name(table_name)
    if db_name == "" :
        print u"集合不存在!"
    else :
        try :
            db = get_database(db_name)
        except Exception ,e :
            print u"查询数据库失败" + str(e)
            return
        db.drop_collection(table_name)
        print table_name + " dropped!"
