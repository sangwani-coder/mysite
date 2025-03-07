""" about view"""
from zyambo.views import app_views
from flask import jsonify, render_template
from datetime import datetime

@app_views.route('/zyambo/martial-arts/', methods=['GET'], strict_slashes=False)
def martial_arts() -> str:
    """ 
    My Martial Arts journey
    """
    return render_template('zma.html', title='Zyambo Martial Arts')
