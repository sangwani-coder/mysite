""" contact view"""
from zyambo.views import app_views
from flask import jsonify, render_template

@app_views.route('/contact', methods=['GET', 'POST'], strict_slashes=False)
def contact() -> str:
    """ contact route
    """
    return render_template('contact.html')