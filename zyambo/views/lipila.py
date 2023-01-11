""" lipila view"""
from zyambo.views import app_views
from flask import render_template

@app_views.route('/zyambo/projects/lipila', methods=['GET'], strict_slashes=False)
def lipila() -> str:
    """ lipila project route
    """
    return render_template('lipila.html')
