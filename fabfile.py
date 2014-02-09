from fabric.api import *

def create_dev_db():
    local('psql -c "drop database remember"')
    local('psql -c "create database remember"')
    local('python manage.py syncdb')
    local('python manage.py loaddata core/fixtures/sample_data.json')
