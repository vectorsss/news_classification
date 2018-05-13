#!/usr/bin/env python

# encoding: utf-8

'''

@author: Zhao Chi

@contact: Vectors@aliyun.com

@software: PyCharm

@file: connect_mysql.py

@time: 2018/4/10 0:13

@desc:

'''
# 导入:
from sqlalchemy import Column, create_engine, ForeignKey
from sqlalchemy.types import String,Integer,VARCHAR,TEXT
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()


# 定义表对象:
class wangyi_news(Base):
    '''
    wangyi_news:存放爬虫爬取的数据
    '''
    # 表的名字:
    __tablename__ = 'wangyi_news'
    # 表的结构:
    news_id = Column(Integer, primary_key=True)
    news_title = Column(VARCHAR(600))
    news_url = Column(VARCHAR(600))
    news_article = Column(TEXT)
    insert_time = Column(VARCHAR(11))


class news_classify(Base):
    '''
    news_classify:存放新闻的种类以及新闻id,固定的,不更新
    '''
    # 表的名字
    __tablename__ = 'news_classify'
    # 表的结构
    classify_id = Column(Integer, primary_key=True)
    classify = Column(VARCHAR(10))


class wangyi_news_classify(Base):
    '''
    wangyi_news_classify:存放经过程序分类后的结果
    '''
    __tablename__ = 'wangyi_news_classify'
    id = Column(Integer, primary_key=True)
    news_id = Column(Integer, ForeignKey(wangyi_news.news_id)) # 外键
    classify_id = Column(Integer, ForeignKey(news_classify.classify_id)) # 外键


# 定义视图
class view_news_classify(Base):
    '''
    view_news_classify:通过以下sql语句
    create view view_news_classify AS
    select wangyi_news_classify.news_id,news_title,news_url,insert_time,classify
    from wangyi_news,news_classify,wangyi_news_classify
    where wangyi_news.news_id = wangyi_news_classify.news_id
    and news_classify.classify_id = wangyi_news_classify.classify_id
    order by insert_time desc
    创建的视图
    '''
    # 视图名字
    __tablename__ = 'view_news_classify'
    # 视图结构
    news_id = Column(Integer, primary_key=True)
    news_title = Column(VARCHAR(600))
    insert_time = Column(VARCHAR(11))
    classify = Column(VARCHAR(10))
    news_url = Column(VARCHAR(600))



# 定义字典 加快读取速度
classify_dict = {

    '体育': 1,
    '财经': 2,
    '房产': 3,
    '家居': 4,
    '教育': 5,
    '科技': 6,
    '时尚': 7,
    '时政': 8,
    '游戏': 9,
    '娱乐': 10,
    '股票': 11,
    '彩票': 12,
    '社会': 13,
    '星座': 14
}

engine = create_engine('mysql+mysqlconnector://root:password@xx.xx.xx.xx/text_classification')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

def insert_wangyinews_into_mysql(table_name, news_title, news_url, news_article, insert_time):
    '''

    :param table_name:表名
    :param news_title:新闻标题
    :param news_url:新闻地址
    :param news_article:新闻文章内容
    :param insert_time:将新闻插入数据库的时间
    :return:
    '''
    # 创建session对象:
    session = DBSession()
    # 创建新new_object对象:
    new_object = table_name(news_title=news_title, news_url=news_url, news_article=news_article,insert_time=insert_time)
    # 添加到session:
    session.add(new_object)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()
def insert_wangyinews_classify_into_mysql(table_name, news_id, classify_id):
    '''
    :param table_name:表名
    :param news_id:新闻id
    :param classify_id:分类id
    :return:
    '''
    # 创建session对象:
    session = DBSession()
    # 创建新new_object对象:
    new_object = table_name(news_id=news_id, classify_id=classify_id)
    # 添加到session:
    session.add(new_object)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()
def select_from_mysql(table_name):
    '''
    从表中查询，返回一个query对象
    :param table_name:
    :return:
    '''
    # 创建session对象:
    session = DBSession()
    query1 = session.query(table_name)
    # article_list = []
    # for i in query1.order_by(table_name.news_id.asc()).all():
    #     article_list.append(i.news_article)
    # session.close()
    return query1





