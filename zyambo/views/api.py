""" api view"""
from zyambo.views import app_views
from flask import jsonify, render_template

@app_views.route('/api/v1/', methods=['GET', 'POST'], strict_slashes=False)
def api_route() -> str:
    """ api route
    """
    return render_template('api.html')
