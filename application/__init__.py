"""
The flask application package.
"""
import logging

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from application.config import config_dict
from os import environ

app = Flask(__name__)

app.config.from_object(config_dict[environ.get('CONFIG_MODE', 'DEFAULT')])

# Refresh the log level setting - if we don't do this, the
# DebugToolbarExtension won't catch any messages.
logging.getLogger().setLevel(logging.DEBUG if app.debug else logging.INFO)

toolbar = DebugToolbarExtension(app)

import application.views
