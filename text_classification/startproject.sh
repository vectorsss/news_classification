nohup python -u /home/www/text_classification/text_classification/predict_mysql.py > /home/www/text_classification/log/predict_mysql.log 2>&1 &
nohup python -u /home/www/text_classification/text_classification/server_predict.py > /home/www/text_classification/log/server_predict.log 2>&1 &
nohup python -u /home/www/text_classification/manage.py runserver 0.0.0.0:80 > /home/www/text_classification/log/websit.log 2>&1 &
