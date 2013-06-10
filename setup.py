"""
Flask-HTTPAuth
--------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-HTTPAuth',
    version='0.6',
    url='http://github.com/miguelgrinberg/flask-httpauth/',
    license='BSD',
    author='Miguel Grinberg',
    author_email='miguelgrinberg50@gmail.com',
    description='Support for Basic and Digest HTTP authentication for Flask routes',
    long_description=__doc__,
    py_modules=['flask_httpauth'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
