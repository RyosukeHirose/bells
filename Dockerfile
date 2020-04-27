FROM python:3.7

# 作業ディレクトリを設定  
WORKDIR /usr/src/app  

ADD requirements.txt /usr/src/app  

# Pipenvをインストール  
RUN apt-get update \
&& pip install --upgrade pip \
&& pip install -r requirements.txt \
&& apt-get install -y python3-dev default-libmysqlclient-dev \
&& pip install mysqlclient \
&& pip install django-bootstrap4 \
# mdeditorの場合
&& pip install django-mdeditor \
&& pip install Markdown
# mediumeditorの場合
pip install django-mediumeditor

# mkdir bells_pro
# django-admin startproject config .
# python manage.py startapp bells
# python manage.py makemigrations
# python manage.py migrate
#  python manage.py createsuperuser

# python manage.py runserver 0:8000