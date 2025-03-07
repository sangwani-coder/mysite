""" about view"""
from zyambo.views import app_views
from flask import jsonify, render_template
from datetime import datetime

@app_views.route('/zyambo/music/', methods=['GET'], strict_slashes=False)
def music() -> str:
    """ 
    My Music journey
    """
    return render_template('zms.html', title='Zyambo Music')
