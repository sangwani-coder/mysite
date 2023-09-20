# portfolio view

from zyambo.views import app_views
from flask import jsonify, render_template

@app_views.route("/zyambo/estimate-price/", methods=['GET', 'POST'], strict_slashes=False)
def quote() -> str:
    """
    route to estimate price
    """
    return render_template('quote.html')