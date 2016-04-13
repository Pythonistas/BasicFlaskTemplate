from application import app
from flask import render_template

import logging


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    logging.debug("Rendering home page")
    return render_template(
        'index.html',
        title='Home Page',
    )
