#!/usr/bin/env python

# encoding: utf-8

'''

@author: Zhao Chi

@contact: Vectors@aliyun.com

@software: PyCharm

@file: predit_mysql.py

@time: 2018/4/10 9:45

@desc:

'''


from __future__ import print_function
import os
import tensorflow as tf
import tensorflow.contrib.keras as kr
from cnn_model import TCNNConfig, TextCNN
from data.cnews_loader import read_category, read_vocab
from connect_mysql import *
from wangyinews_crawler import *
from socket import *
import threading
import time
try:
    bool(type(unicode))
except NameError:
    unicode = str


# 配置训练好的模型信息
base_dir = 'data/cnews'
vocab_dir = os.path.join(base_dir, 'cnews.vocab.txt')

save_dir = 'checkpoints/textcnn'
save_path = os.path.join(save_dir, 'best_validation')  # 最佳验证结果保存路径

# 配置服务器信息
address='127.0.0.1'     #监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
port=12345             #监听自己的哪个端口
buffsize=8192          #接收从客户端发来的数据的缓存区大小
s = socket(AF_INET, SOCK_STREAM)
s.bind((address,port))
s.listen(5)     # 最大连接数

def tcplink(sock,addr):
    '''
    创建tcp链接
    :param sock:
    :param addr:
    :return:
    '''
    print('Accept new connection from %s:%s...' % addr)
    #sock.send(b'Welcome!')
    while True:
        recvdata = sock.recv(buffsize)
        classified = cnn_model.predict(recvdata.decode('utf-8'))

        time.sleep(1)
        if recvdata.decode('utf-8')=='exit' or not recvdata:
            break
        sock.send(classified.encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


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
    while True:
        sock, addr = s.accept()
        print('connect from:', addr)
        t = threading.Thread(target=tcplink, args=(sock, addr))  # t为新创建的线程
        t.start()

