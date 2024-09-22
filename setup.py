import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    long_description = f.read()

setup(
    name='lsgi',
    version='0.1.0',
    packages=['lsgi'],
    install_requires=['Werkzeug>=3.0.0'],
    license='MIT License',
    description='Simple AWS Lambda WSGI adapter with a focus on AWS SAM support',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rokclimb15/lsgi',
    author='Brian Morton',
)
