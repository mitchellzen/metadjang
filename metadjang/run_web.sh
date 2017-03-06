#!/bin/sh
curl -sL https://deb.nodesource.com/setup_6.x | bash -
apt-get --assume-yes install nodejs
apt-get --assume-yes install build-essential
apt-get --assume-yes install git
apt-get --assume-yes install mercurial
apt-get --assume-yes install libpq-dev python-dev
apt-get --assume-yes build-dep python-imaging
apt-get --assume-yes install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev
apt-get --assume-yes install libxml2-dev libxslt1-dev lib32z1-dev zlib1g-dev
apt-get --assume-yes install python-lxml
sleep 10
su -m myuser -c "python manage.py migrate"
su -m myuser -c "python manage.py runserver 0.0.0.0:8000"
