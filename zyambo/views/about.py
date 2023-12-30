""" about view"""
from zyambo.views import app_views
from flask import jsonify, render_template
from datetime import datetime

@app_views.route('/zyambo/about/', methods=['GET'], strict_slashes=False)
def about() -> str:
    """ about route
    """
    from zyambo.storage.db import DB
    today = datetime.today().year
    dates = {
        'eng_year': today - 2019,
        'mus_year': today - 2004,
        'mat_year': today - 2001,
        'coach': today - 2008,
    }
    print(dates['coach'])
    DB = DB()
    about = DB.read_about()
    return render_template('about.html', about=about, dates=dates)
