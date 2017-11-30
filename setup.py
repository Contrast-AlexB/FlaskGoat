from setuptools import setup, find_packages

setup(
    name='Flask-Screener-App',
    version='0.5',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    'Jinja2==2.10',
    'requests==2.18.4',
    'lxml==4.1.1',
    'Flask==0.12.2',
    'pycrypto==2.6.1',
    'flask_sqlalchemy==2.3.2',
    'PyYAML==3.12'
    ]
)