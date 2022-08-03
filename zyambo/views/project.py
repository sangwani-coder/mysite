""" project view"""
from zyambo.views import app_views
from flask import jsonify, render_template

@app_views.route("/zyambo/projects/", methods=['GET', 'POST'], strict_slashes=False)
def projects() -> str:
    """ projects route
    """
    return render_template('projects.html')


