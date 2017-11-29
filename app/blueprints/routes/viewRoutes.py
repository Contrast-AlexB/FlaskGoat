import pickle
import subprocess

import requests
import yaml
from flask import Blueprint, render_template, request, current_app

#TODO - Figure out a proper way to find the top dir templates folder.
router = Blueprint('view_routes', __name__, template_folder='../../../templates/')
from app.lib import padding_oracle as PaddingOracle
from app.lib.models.User import *

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


@router.route('/padding-oracle', methods=['GET'])
def paddingOracle():
    attack = request.args['attack']
    if(attack and str(attack).lower() == 'true'):
        result = PaddingOracle.test_padding_oracle()
    else:
        result = ''
    return render_template("padding_oracle.html", result=result)


@router.route('/path-traversal', methods=['POST'])
def pathTraversal():
    attack = request.form['user_input']
    try:
        f = open(attack, 'r')
        result = f.read()
    except Exception as e:
        result = e.message
        pass
    return render_template('path_traversal.html', result=result)


@router.route('/ssrf', methods=['POST'])
def ssrf():
    user_input = request.form['user_input']
    try:
        url = requests.get(user_input)
        result = url.text
    except Exception as e:
        result = e
    return render_template('ssrf.html', result=result)



@router.route('/sqli', methods=['POST'])
def sqli():
    user_input = request.form['user_input']
    result = ''
    query = 'user.id = \'' + user_input + '\''

    try:
        result = User.query.filter(query).all()
    except Exception as e:
        result = e
        pass
    return render_template('sqli.html', user_input=user_input, result=result)