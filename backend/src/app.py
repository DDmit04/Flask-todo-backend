import os

from flask import Flask, render_template, session
from flask_cors import CORS
import mimetypes

from MailConfig import MailConfig
from repo import TaskRepo
from controller.TaskController import task_blueprint
from controller.UserController import user_blueprint

current_dir_path = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.abspath(os.path.join(current_dir_path, '..', 'templates'))
static_dir = os.path.abspath(os.path.join(current_dir_path, '..', 'static'))

mimetypes.add_type('application/javascript', '.js')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.config.update(
    SECRET_KEY="BAD_SECRET_KEY",
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='danya.dmit1@gmail.com',
    MAIL_DEFAULT_SENDER='danya.dmit1@gmail.com',
    MAIL_PASSWORD='ivabypuzbqbjwbzg'
)
MailConfig(app)
CORS(app)


@app.route('/')
def main():
    session.permanent = True
    user = None
    tasks = []
    if 'user' not in session and 'anonUser' not in session:
        session['anonUser'] = {
            'id': None,
            'tasks': []
        }
        tasks = []
    elif 'user' in session:
        user = session['user']
        tasks = TaskRepo.read_all_user_tasks(user['id'])
    elif 'anonUser' in session:
        tasks = session['anonUser']['tasks']
    return render_template("TODOMain.html", tasks=tasks, user=user)


@app.route('/features')
def help_mapping():
    session.permanent = True
    user = None
    if 'user' not in session and 'anonUser' not in session:
        session['anonUser'] = {
            'id': None,
            'tasks': []
        }
    elif 'user' in session:
        user = session['user']
    return render_template("features.html", user=user)


app.register_blueprint(task_blueprint, url_prefix='/task')
app.register_blueprint(user_blueprint, url_prefix='/user')

if __name__ == '__main__':
    app.run(port=3000)
