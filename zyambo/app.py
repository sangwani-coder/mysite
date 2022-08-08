#!/usr/bin/env python3
""" Entr point"""
from flask import Flask, abort, jsonify, render_template
from zyambo.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
app.config["CACHE_TYPE"] = "null"


@app.errorhandler(404)
def PageNotFound(error: str) -> str:
    """ Page not found error"""
    return render_template('error.html', error=error), 404

@app.errorhandler(405)
def methodNotAllowed(error: str) -> str:
    """ unauthorized error"""
    return render_template('error.html', error=error), 405

if __name__ == "__main__":
     app.jinja_env.auto_reload = True
     app.config['TEMPLATES_AUTO_RELOAD'] = True
     app.run(debug=True, host='0.0.0.0')
