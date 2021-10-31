import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_ROOT = os.path.join(APP_ROOT, 'resources', 'data')
USERS_DATA = os.path.join(DATA_ROOT, 'UsersData.json')
USER_TASKS_FILENAME = 'TODOData.json'


def user_tasks_filename(user_id):
    filename = user_id + USER_TASKS_FILENAME
    return os.path.join(DATA_ROOT, filename)
