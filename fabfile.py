import os
from fabric.api import *

def create_dev_db():
    local('psql -c "drop database remember"')
    local('psql -c "create database remember"')
    local('python manage.py syncdb')
    local('python manage.py loaddata core/fixtures/sample_data.json')

def create_venv():
    if (
        os.access('venv', os.F_OK) and
        prompt('venv exists, delete?',
            default='y', validate='y|n|Y|N'
        ) in ('y', 'Y')
    ):
        local('rm -rf venv')
    local('virtualenv venv')
    local('. venv/bin/activate && pip install -r requirements.txt')
    
