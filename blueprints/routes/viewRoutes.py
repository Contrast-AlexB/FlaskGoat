import pickle
from flask import Blueprint, render_template, abort, request, url_for, current_app
from jinja2 import TemplateNotFound
import yaml
import subprocess
router = Blueprint('view_routes', __name__, template_folder='templates')



@router.route('/cmdi', methods=['POST'])
def cmd_injection():
    user_input = request.form['user_input']
    try:
        result = []
        p = subprocess.Popen(user_input, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in iter(p.stdout.readline, b''):
            result.append(line)
    except Exception as e:
        print(e.message)
        result = e

    return render_template('cmdi.html', result=result)


@router.route('/deserialization', methods=['POST'])
def deserialization():
    user_input = request.form['user_input']
    result = ''
    try:
        with current_app.open_resource('static/pickle.pickle') as pik:
            result = pickle.load(pik)
    except Exception as e:
        result = str(e)
    return render_template('deserialization.html', user_input=user_input, result=result)


@router.route('/deserialization_yaml', methods=['POST'])
def deserialzation_yaml():
    user_input = request.form['user_input']
    if user_input:
        result = yaml.load(user_input)
    else:
        result = ''
    return render_template('deserialization_yaml.html', user_input=user_input, result=result)