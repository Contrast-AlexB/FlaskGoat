
## Flask Python-Screener-App



###Setup

(Preferably this is done in a virtualenv - see [FAQ](#faq) for instructions)

1. `git clone -b Flask-0.12.x git@bitbucket.org:contrastsecurity/python-screener-apps.git`

2. `cd python-screener-app`

3. `python setup.py install`

4. `python run.py`

After this, you should be able to access the app at: [127.0.0.1:5000](http://127.0.0.1:5000)


###Improving

When adding new features, make sure to update the following:

- `app/blueprints/routes/navRoutes.py` for anything nav-bar endpoint related

- `app/blueprints/routes/viewRoutes.py` for anything view endpoint related

- `app/templates/` is used for any html templates

- `app/static/` is used to serve static files such as CSS or JS



## FAQ
- - - -
#####1 Setting up a virtualenv

- Follow these steps to setup a virtualenv

        1. pip install virtualenv
    
        2. virtualenv envir
    
        3. source envir/bin/activate
        4. Virtualenv is now active
        
    
        - To deactivate virtualenv, type deactivate