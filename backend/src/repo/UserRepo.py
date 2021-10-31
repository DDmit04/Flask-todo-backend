import json
import os
import uuid

import Config


def find_by_email_or_username(email, username):
    users = read_all_users()
    for user in users:
        if user['email'] == email or user['username'] == username:
            return user
    return None


def save_new_user(new_user):
    users_data = read_all_users()
    users_data.append(new_user)
    write_all_users(users_data)
    return new_user


def read_all_users():
    path = Config.USERS_DATA
    if os.path.exists(path):
        with open(path) as users_data_file:
            return json.load(users_data_file)
    else:
        with open(path, 'w') as users_data_file:
            json.dump([], users_data_file)
    return []


def write_all_users(users):
    path = Config.USERS_DATA
    if os.path.exists(path):
        with open(path, 'w') as users_data_file:
            json.dump(users, users_data_file)
            return True
    else:
        with open(path, 'w') as users_data_file:
            json.dump([], users_data_file)
    return False
