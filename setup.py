#!/usr/bin/env python
import twilio_net_neutrality
from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

def install():

    setup(
        name='twilio_net_neutrality',
        version=twilio_net_neutrality.__version__,
        description='twilio_net_neutrality website project',
        long_description=readme,
        author=twilio_net_neutrality.__author__,
        license='MIT',
        platforms=['POSIX'],
        classifiers=[
            'Development Status :: 1 - Planning',
            'License :: OSI Approved :: MIT License',
            'Environment :: Console',
            'Operating System :: POSIX',
            'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
            'Framework :: Flask',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',],
        packages=find_packages(exclude=('tests', )),
        install_requires=[
            'Flask==0.12',
            'Flask-Migrate==2.0.0',
            'Flask-Script==2.0.5',
            'Flask-SQLAlchemy==2.1',
            'mysqlclient==1.3.9',
        ],
    )

if __name__ == "__main__":
    install()
