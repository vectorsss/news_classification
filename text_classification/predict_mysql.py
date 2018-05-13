#!/usr/bin/env python

# encoding: utf-8

'''

@author: Zhao Chi

@contact: Vectors@aliyun.com

@software: PyCharm

@file: predict_mysql.py

@time: 2018/4/10 9:45

@desc:

'''


from __future__ import print_function

import os
import tensorflow as tf
import tensorflow.contrib.keras as kr
from cnn_model import TCNNConfig, TextCNN
from data.cnews_loader import read_category, read_vocab
import time as time1
from connect_mysql import *
from wangyinews_crawler import *
try:
    bool(type(unicode))
except NameError:
    unicode = str

base_dir = 'data/cnews'
vocab_dir = os.path.join(base_dir, 'cnews.vocab.txt')

save_dir = 'checkpoints/textcnn'
save_path = os.path.join(save_dir, 'best_validation')  # 最佳验证结果保存路径


class CnnModel:
    def __init__(self):
        self.config = TCNNConfig()
        self.categories, self.cat_to_id = read_category()
        self.words, self.word_to_id = read_vocab(vocab_dir)
        self.config.vocab_size = len(self.words)
        self.model = TextCNN(self.config)

        self.session = tf.Session()
        self.session.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        saver.restore(sess=self.session, save_path=save_path)  # 读取保存的模型

    def predict(self, message):
        # 支持不论在python2还是python3下训练的模型都可以在2或者3的环境下运行
        content = unicode(message)
        data = [self.word_to_id[x] for x in content if x in self.word_to_id]

        feed_dict = {
            self.model.input_x: kr.preprocessing.sequence.pad_sequences([data], self.config.seq_length),
            self.model.keep_prob: 1.0
        }

        y_pred_cls = self.session.run(self.model.y_pred_cls, feed_dict=feed_dict)
        return self.categories[y_pred_cls[0]]


if __name__ == '__main__':
    cnn_model = CnnModel()
    # 程序整点执行
    time1.sleep((int(time1.time() / 3600) + 1) * 3600 - time1.time())
    while True:

        # 获取程序执行时间
        start_time = time1.time()
        time = wangyinews_crawler()  # 爬虫爬取时间
        # 获取当前时间格式为2018041018
        query1 = select_from_mysql(wangyi_news)  # 从wangyi_news中读取对象
        # time和爬虫插入的时间同步 暂未定义
        for i in query1.order_by(wangyi_news.news_id.asc()).filter(wangyi_news.insert_time==time):
            insert_wangyinews_classify_into_mysql(wangyi_news_classify, i.news_id,  classify_dict[cnn_model.predict(i.news_article)])
        query2 = select_from_mysql(view_news_classify) # 从视图中读取对象
        # 打印分析的内容 部署完成之后注释
        # for i in query2.filter(view_news_classify.insert_time==time):
        #     print(i.news_title, '\t', i.classify, '\t', i.insert_time, '\t', i.news_url)
        print(time, "Finished!")
        # 获取程序结束时间
        end_time = time1.time()
        # 每小时爬取一次
        time1.sleep(3600-(end_time-start_time))
