""" project view"""
# if __name__=="__main__":
from zyambo.views import app_views
from flask import render_template
# from zyambo.app import Project

@app_views.route("/zyambo/projects/", methods=['GET', 'POST'], strict_slashes=False)
def projects() -> str:
    """ projects route
    """
    # models = Project.query.all()  # Fetch data
    # print(models)
    return render_template('projects.html')
