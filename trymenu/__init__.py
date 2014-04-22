#!/usr/bin/env python
from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'random'

__all__ = ["controllers","models"]

