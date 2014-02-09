import os
from fabric.api import *

def create_dev_db():
    local('dropdb --if-exists remember')
    local('createdb remember')
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
    local('. venv/bin/activate && pip uninstall readline')
    local('. venv/bin/activate && easy_install readline')
