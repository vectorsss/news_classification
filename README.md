
---
### 运行环境
服务器：Ubuntu 16.04
数据库：Mysql 5.6
python：Anaconda 5.1
Tensorflow-CPU：1.7
额外的包：参考requirements.txt,有则忽略,无则安装。
```
certifi==2018.1.18
chardet==3.0.4
Django==2.0.4
docopt==0.6.2
idna==2.6
mysql-connector==2.1.6
pipreqs==0.4.9
pytz==2018.4
requests==2.18.4
SQLAlchemy==1.2.6
urllib3==1.22
yarg==0.1.9

```

---

1. 首先安装mysql到数据库，执行text_classification.sql创建数据库。更改数据库配置./text_classification/connect_mysql.py
2. 服务器安装Anaconda(清华大学镜像站自行下载安装),安装TensorFlow-CPU版
3. 将本项目部署至/home/www目录下
4. 安装其他依赖包
 >pip install -r requirements.txt
5. 服务器部署Django环境(apache2.4)
参考：https://code.ziqiangxuetang.com/django/django-deploy.html
6. 关于本项目部署中的Django配置请看以下操作
**安装 apache2 和 mod_wsgi**
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3
**新建网站配置文件**
>vim /etc/apache2/sites-available/text_classification.conf 
输入以下内容
```
<VirtualHost classify.i-ll.cc:80>
    ServerName classify.i-ll.cc
    ServerAlias classify.i-ll.cc
    ServerAdmin dandanv5@hotmail.com
    Alias /static /home/www/text_classification/static
      
    <Directory /home/www/text_classification>
        Require all granted
    </Directory>
  
  
    WSGIScriptAlias / /home/www/text_classification/myweb/wsgi.py
  
    <Directory /home/www/text_classification/myweb>
    <Files wsgi.py>
        Require all granted
    </Files>
    </Directory>
</VirtualHost>

```
**激活新网站**
>sudo a2ensite sitename.conf
7. 启动项目
>cd /home/www/text_classification/text_classification && sh startproject.sh
项目运行日志在./log下

最后本项目使用的THUCNews中文新闻数据集,可以去官网下载。我对数据集进行了整合处理,下载地址见./text_classification/data/cnews/README.md
关于本项目中模型和爬虫部分,详见./text_classification/README.md