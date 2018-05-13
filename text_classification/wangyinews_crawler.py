#!/usr/bin/env python

# encoding: utf-8

'''

@author: Zhao Chi

@contact: Vectors@aliyun.com

@software: PyCharm

@file: wangyinews_crawler.py

@time: 2018/4/10 11:19

@desc:

'''
from bs4 import BeautifulSoup
import requests
import re
import datetime
from connect_mysql import *


def wangyinews_crawler():
    # 获取当前时间格式为2018041018
    time = datetime.datetime.now().strftime("%Y%m%d%H")
    url = r'http://news.163.com/special/0001386F/rank_news.html'
    # 模拟真实浏览器进行访问
    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/55.0.2883.87 Safari/537.36'}
    response = requests.get(url, headers=headers)
    page_html = response.text

    # 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
    soup = BeautifulSoup(page_html, 'html.parser')

    #获取一小时前点击率最高的前20个新闻标题和链接
    titles = soup.find('div', 'area-half left').find('div', 'tabContents active').find_all('a', limit=20)
    for title in titles:
        # 打印爬取到的title和url
        #print(str(title.string))
        #print(title.get('href'))

        '''
        news_url:新闻链接
        news_html:新闻页网页源代码 
        '''
        news_url = (str(title.get('href')))
        news_response = requests.get(news_url, headers=headers)
        news_html = news_response.text
        # 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
        news_soup = BeautifulSoup(news_html, 'html.parser')
        # 从网页源代码中找到属于post_text类的div，并将所有p标签内容存入列表news_contents
        if news_soup.find('div', 'post_text') is None:  # 如果网页丢失,跳出本次循环
            continue
        news_title = news_soup.find('h1')
        contents = news_soup.find('div', 'post_text').find_all('p')
        news_contents = []
        for content in contents:
            if content.string is not None:
                #去掉特殊字符
                news_contents.append(re.sub('[\r\n\t ]', '', str(content.string)))
        #字符串拼接
        news_contents = ''.join(news_contents)
        # print(news_contents)
        # print(type(news_contents))
        # 将爬取到的数据存入数据库
        insert_wangyinews_into_mysql(wangyi_news, str(news_title.string), news_url, news_contents, time)
    # print('Finished')
    # 返回当前爬取时间
    return time