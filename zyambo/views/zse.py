""" about view"""
from zyambo.views import app_views
from flask import jsonify, render_template
from datetime import datetime

@app_views.route('/zyambo/software-engineer/', methods=['GET'], strict_slashes=False)
def software_engineer() -> str:
    """ 
    My SE journey
    """
    return render_template('zse.html', title='Zyambo Software Engineer')
