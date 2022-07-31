#!/usr/bin/env python3
""" Blueprint
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/zyambo/")

from zyambo.views.about import *
from zyambo.views.api import *
from zyambo.views.contact import *
from zyambo.views.index import *
from zyambo.views.project import *
