#!env/bin/python
# *-* coding: utf-8 *-*
__author__= 'Ampelio Cherubini'
__version__= '0.1'

from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return 'hello world!!'

if __name__=='__main__':
    app.run(debug=True)
