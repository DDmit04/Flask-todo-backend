import hashlib
import uuid

from repo import UserRepo


def create_user(user_data):
    user = UserRepo.find_by_email_or_username(user_data['email'], user_data['username'])
    if user is None:
        user_data['id'] = str(uuid.uuid4())
        user_data['password'] = hashlib.md5(user_data['password'].encode('utf-8')).hexdigest()
        return UserRepo.save_new_user(user_data)
    else:
        return None


def auth_user(auth_data):
    auth_data['password'] = hashlib.md5(auth_data['password'].encode('utf-8')).hexdigest()
    user = UserRepo.find_by_email_or_username(auth_data['usernameOrEmail'], auth_data['usernameOrEmail'])
    if user is None or user['password'] != auth_data['password']:
        return None
    return user
