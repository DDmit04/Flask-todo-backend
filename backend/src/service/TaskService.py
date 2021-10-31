import datetime
import uuid

from flask import session

from repo import TaskRepo


def get_user_tasks(user_id):
    if user_id is None:
        return session['anonUser']['tasks']
    else:
        return TaskRepo.read_all_user_tasks(user_id)


def create_task(task_data):
    task_data['id'] = str(uuid.uuid4())
    task_data['creationDate'] = datetime.datetime.now()
    return task_data


def create_many_tasks(tasks_data):
    result = []
    for task_data in tasks_data:
        result.append(create_task(task_data))
    return result


def turn_task(user_id, task_id):
    tasks = []
    if user_id is None:
        tasks = session['anonUser']['tasks']
    else:
        tasks = TaskRepo.read_all_user_tasks(user_id)
    turned = False
    for task in tasks:
        if task['id'] == task_id:
            turned = True
            task['completed'] = not task['completed']
    if turned and user_id is None:
        session['anonUser']['tasks'] = tasks
    elif turned:
        TaskRepo.write_all_users_tasks(user_id, tasks)


def delete_task(user_id, task_id):
    tasks = []
    if user_id is None:
        tasks = session['anonUser']['tasks']
    else:
        tasks = TaskRepo.read_all_user_tasks(user_id)
    tasks = list(filter(lambda tsk: tsk['id'] != task_id, tasks))
    if user_id is None:
        session['anonUser']['tasks'] = tasks
    else:
        TaskRepo.write_all_users_tasks(user_id, tasks)


def save_user_task(user_id, task):
    if user_id is None:
        session['anonUser']['tasks'].append(task)
    else:
        tasks = TaskRepo.read_all_user_tasks(user_id)
        tasks.append(task)
        TaskRepo.write_all_users_tasks(user_id, tasks)
        return task


def save_many_user_tasks(user_id, new_tasks):
    new_tasks = create_many_tasks(new_tasks)
    old_tasks = TaskRepo.read_all_user_tasks(user_id)
    for task in new_tasks:
        old_tasks.append(task)
    TaskRepo.write_all_users_tasks(user_id, old_tasks)
    return old_tasks
