#__author__:Omen
#date:2018/4/12
from web.connect_mysql import *
import datetime
def change(time):
    year = time[0:4]
    mounth = time[4:6]
    day = time[6:8]
    hour = time[8:]
    return(year+'.'+mounth+'.' +day+ ' '+' '+hour+' : 00')
def select():
    time = datetime.datetime.now().strftime("%Y%m%d%H")  # 获取当前时间。
    query1 = select_from_mysql(view_news_classify)  # 查询视图，时间符合当前时间。

    info_list = []  # 空的list 用于存储数据。

    for i in query1.filter(view_news_classify.insert_time==time):
        insert_time = change(i.insert_time)
        dict = {'id': i.news_id,  # 新建字典用于存储一条数据。
                'title': i.news_title,
                'time': insert_time,
                'classify': i.classify,
                'url': i.news_url,
                }

        info_list.append(dict)


    return info_list  # 返回list。
