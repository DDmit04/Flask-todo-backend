from flask import request, Blueprint, Response, session
from marshmallow import ValidationError
from controller.request import UserRequest
from service import UserService, TaskService

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/', methods=['GET'])
def get_user():
    if 'user' not in session and 'anonUser' not in session:
        session['anonUser'] = {
            'id': None,
            'tasks': []
        }
        return session['anonUser']
    elif 'user' in session:
        return session['user']
    elif 'anonUser' in session:
        return session['anonUser']
    else:
        return Response(status=401)


@user_blueprint.route('/', methods=['POST'])
def register_user():
    request_params = request.json
    user_register = UserRequest.UserRegister()
    try:
        register_request = user_register.load(request_params)
        user = UserService.create_user(register_request)
        if user is None:
            return Response("User with this username or email already exists!", status=409)
        user = user_register.dump(user)
        return user
    except ValidationError as err:
        return Response(str(err), status=400)


@user_blueprint.route('/out', methods=['GET'])
def sign_out_user():
    if 'user' in session:
        session.pop('user', None)
        return Response(status=200)
    else:
        return Response(status=401)


@user_blueprint.route('/in', methods=['POST'])
def auth_user():
    request_params = request.json
    user_auth = UserRequest.UserAuth()
    try:
        user_auth = user_auth.load(request_params)
        user = UserService.auth_user(user_auth)
        if user is None:
            return Response("Wrong username/email or password!", status=403)
        if 'anonUser' in session:
            TaskService.save_many_user_tasks(user['id'], session['anonUser']['tasks'])
            session.pop('anonUser', None)
        user = UserRequest.UserRegister().dump(user)
        session['user'] = user
        return user
    except ValidationError as err:
        return Response(str(err), status=400)
