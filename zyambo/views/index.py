""" index view"""
from zyambo.views import app_views
from flask import jsonify, render_template

@app_views.route("/", methods=['GET'], strict_slashes=False)
def index() -> str:
    """ Index route
    """
    return render_template('index.html')

@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status() -> str:
    """ Index route
    """
    return jsonify({'Status': 'OK'}), 200
