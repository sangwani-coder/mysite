""" about view"""
from zyambo.views import app_views
from flask import jsonify, render_template
from datetime import datetime

@app_views.route('/zyambo/business/', methods=['GET'], strict_slashes=False)
def business() -> str:
    """ 
    My entrepreneurial journey
    """
    return render_template('zep.html', title='Zyambo Business')
