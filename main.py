#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 21:00:31 2021

@author: ideal
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_page():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug = True)