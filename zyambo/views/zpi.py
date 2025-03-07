""" about view"""
from zyambo.views import app_views
from flask import jsonify, render_template
from datetime import datetime

@app_views.route('/zyambo/private-investigator/', methods=['GET'], strict_slashes=False)
def private_investigator() -> str:
    """ 
    My Pi journey
    """
    return render_template('zpi.html', title='Zyambo Private-Investigator')
