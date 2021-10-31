from flask import Blueprint, request, session, Response, render_template, jsonify
from flask_mail import Message
from marshmallow import ValidationError

from MailConfig import MailConfig
from controller.request import TaskRequest
from service import TaskService

task_blueprint = Blueprint('task', __name__)


@task_blueprint.route('/', methods=['POST'])
def add_task():
    request_params = request.json
    task_request = TaskRequest.Task()
    try:
        task = task_request.load(request_params)
        task = TaskService.create_task(task)
        user = {'id': None}
        if 'user' in session:
            user = session['user']
        elif 'anonUser' in session:
            user = session['anonUser']
        else:
            return Response(status=401)
        TaskService.save_user_task(user['id'], task)
        return jsonify(task)
    except ValidationError as err:
        return Response(str(err), status=400)


@task_blueprint.route('/', methods=['GET'])
def get_tasks():
    tasks = []
    if 'user' in session:
        user = session['user']
        tasks = TaskService.get_user_tasks(user['id'])
    elif 'anonUser' in session:
        tasks = TaskService.get_user_tasks(None)
    return jsonify(tasks)


@task_blueprint.route('/<string:task_id>', methods=['DELETE'])
def delete_tasks(task_id):
    user = {'id': None}
    if 'user' in session:
        user = session['user']
    elif 'anonUser' in session:
        user = session['anonUser']
    else:
        return Response(status=401)
    TaskService.delete_task(user['id'], task_id)
    return Response(status=204)


@task_blueprint.route('/<string:task_id>', methods=['PATCH'])
def turn_task(task_id):
    user = {'id': None}
    if 'user' in session:
        user = session['user']
    elif 'anonUser' in session:
        user = session['anonUser']
    else:
        return Response(status=401)
    TaskService.turn_task(user['id'], task_id)
    return Response(status=204)


@task_blueprint.route('/mail', methods=['GET'])
def mail_tasks():
    if 'user' in session:
        user = session['user']
        tasks = TaskService.get_user_tasks(user['id'])
        tasksHtml = render_template("TasksMail.html", tasks=tasks)
        msg = Message("Here is your tasks!", sender="danya.dmit1@gmail.com", recipients=[user['email']])
        msg.html = tasksHtml
        MailConfig.get_instance().mail.send(msg)
        return Response(status=204)
    else:
        return Response(status=401)
