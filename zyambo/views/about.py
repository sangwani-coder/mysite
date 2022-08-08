""" about view"""
from zyambo.views import app_views
from flask import jsonify, render_template

@app_views.route('/zyambo/about/', methods=['GET'], strict_slashes=False)
def about() -> str:
    """ about route
    """
    from zyambo.storage.db import DB
    DB = DB()
    about = DB.read_about()
    return render_template('about.html', about=about)
