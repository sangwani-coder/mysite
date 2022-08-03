""" about view"""
from zyambo.views import app_views
from flask import jsonify, render_template

@app_views.route('/zyambo/about/', methods=['GET', 'POST'], strict_slashes=False)
def about() -> str:
    """ about route
    """
    return render_template('about.html')
