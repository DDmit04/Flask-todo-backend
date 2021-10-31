import json
import os
import Config


def read_all_user_tasks(user_id):
    data_path = Config.user_tasks_filename(user_id)
    if os.path.exists(data_path):
        with open(data_path) as tasks_data_file:
            return json.load(tasks_data_file)
    else:
        with open(data_path, 'w') as tasks_data_file:
            json.dump([], tasks_data_file)
            return []
    return []


def write_all_users_tasks(user_id, tasks):
    data_path = Config.user_tasks_filename(user_id)
    if os.path.exists(data_path):
        with open(data_path, 'w') as tasks_data_file:
            json.dump(tasks, tasks_data_file, default=str)
            return True
    return False
