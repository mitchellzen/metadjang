#!/bin/sh

sleep 10
su -m myuser -c "celery worker -A intelligencer.celeryconf -Q default -n default@%h"
