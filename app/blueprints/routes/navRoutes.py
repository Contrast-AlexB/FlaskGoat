from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound

router = Blueprint('nav_routes', __name__, template_folder='../../../templates/')


#
#
# Start Navbar Routes
#
#


@router.route('/', defaults={'page' : 'index'})
def home(page):
    try:
        return render_template('base.html')
    except TemplateNotFound:
        abort(404)

@router.route('/cmdi', defaults={'page' : 'CmdInject'}, methods=['GET'])
def cmdi(page):
    try:
        return render_template('cmdi.html')
    except TemplateNotFound:
        abort(404)

@router.route('/deserialization', defaults={'page' : 'Pdeserial'})
def deserial(page):
    try:
        return render_template('deserialization.html')
    except TemplateNotFound:
        abort(404)

@router.route('/deserialization_yaml', defaults={'page' : 'Ydeserial'})
def deserial_yaml(page):
    try:
        return render_template('deserialization_yaml.html')
    except TemplateNotFound:
        abort(404)

@router.route('/padding-oracle', defaults={'page' : 'padding'})
def padding(page):
    try:
        return render_template('padding_oracle.html')
    except TemplateNotFound:
        abort(404)

@router.route('/path-traversal', defaults={'page' : 'path'})
def path(page):
    try:
        return render_template('path_traversal.html')
    except TemplateNotFound:
        abort(404)

@router.route('/ssrf', defaults={'page': 'ssrf'})
def ssrf(page):
    try:
        return render_template('ssrf.html')
    except TemplateNotFound:
        abort(404)

@router.route('/sqli', defaults={'page' : 'sqli'})
def sqli(page):
    try:
        return render_template('sqli.html')
    except TemplateNotFound:
        abort(404)

@router.route('/xxe-lxml', defaults={'page' : 'xxe-lxml'})
def xxe_lxml(page):
    try:
        return render_template('xxe_lxml.html')
    except TemplateNotFound:
        abort(404)

@router.route('/xxe-pulldom', defaults={'page' : 'xxe-pull'})
def xxe_pull(page):
    try:
        return render_template('xxe_pulldom.html')
    except TemplateNotFound:
        abort(404)

@router.route('/xxe-sax', defaults={'page' : 'xxe-sax'})
def xxe_sax(page):
    try:
        return render_template('xxe_sax.html')
    except TemplateNotFound:
        abort(404)

@router.route('/xss', defaults={'page' : 'xss'})
def xxs(page):
    try:
        return render_template('xss.html')
    except TemplateNotFound:
        abort(404)


#
#
# End Navbar Routes
#
#



