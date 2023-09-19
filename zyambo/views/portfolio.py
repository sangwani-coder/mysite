# portfolio view

from zyambo.views import app_views
from flask import jsonify, render_template

@app_views.route("/zyambo/portfolio/", methods=['GET'], strict_slashes=False)
def portfolio() -> str:
    """
    route to list previous industries and projects
    """
    return render_template('portfolio.html')