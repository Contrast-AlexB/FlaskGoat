import pickle
import subprocess
from xml.sax import SAXParseException

import requests
import yaml

from flask import Blueprint, render_template, request, current_app
# XML Parsing
from xml.dom import pulldom
from lxml import etree
import xml.sax as sax
from xml.sax.handler import ContentHandler,EntityResolver,DTDHandler


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


@router.route('/xxe-lxml', methods=['POST'])
def xxe_lxml():
    attack = request.form['attack']
    test_string = "<!DOCTYPE doc [ " \
                  "<!ENTITY lxml SYSTEM \"file:///etc/passwd\"> " \
                  "]>\n" \
                  "<root>\n" \
                  "<element>&lxml;</element>\n" \
                  "</root>\n"
    if str(attack).lower() == 'true':
        etree.fromstring(test_string)
        result = 'LXML XXE Attack Attempted'
    else:
        result = ''
    return render_template('xxe_lxml.html', result=result)


@router.route('/xxe-pulldom', methods=['POST'])
def xxe_pulldom():
    attack = request.form['attack']
    test_string = "<!DOCTYPE doc [ " \
                  "<!ENTITY pulldom SYSTEM \"file:///tmp/marker\"> " \
                  "<!ENTITY pulldom2 SYSTEM \"http://www.google.com/marker\"> " \
                  "]>\n" \
                  "<root>\n" \
                  "<element>&pulldom;</element>\n" \
                  "<element>&pulldom2;</element>\n" \
                  "</root>\n"
    if str(attack).lower() == 'true':
        pulldom.parseString(test_string)
        result = 'PullDOM XXE Attack Attempted'
    else:
        result = ''
    return render_template('xxe_pulldom.html', result=result)

@router.route('/xxe-sax', methods=['POST'])
def xxe_sax():
    attack = request.form['attack']
    test_string = "<!DOCTYPE doc [ " \
                  "<!ENTITY sax SYSTEM \"file:///etc/passwd\"> " \
                  "<!ENTITY sax2 SYSTEM \"http://www.google.com/marker\"> " \
                  "]>\n" \
                  "<root>\n" \
                  "<element>&sax;</element>\n" \
                  "<element>&sax2;</element>\n" \
                  "</root>\n"
    if str(attack).lower() == 'true':
        try:
            sax.parseString(test_string, ContentHandler())
            result = 'SAX XXE Attack Attempted'
        except SAXParseException as e:
            result = 'SAX XXE Attack Attempted'
    else:
        result = ''

    return render_template('xxe_sax.html', result=result)


@router.route('/xss', methods=['POST'])
def xxs():
    user_input = request.form['user_input']
    return render_template('xss.html', user_input=user_input)




