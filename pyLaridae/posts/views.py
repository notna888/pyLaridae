# -*- coding: utf-8 -*-
"""Post Section."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from pyLaridae.utils import flash_errors

blueprint = Blueprint("posts", __name__, static_folder="../static")


@blueprint.route("/posts", methods=["GET"])
def post_index():
    current_app.logger.info("post index loaded!")
    return render_template('posts/post_list.html')

@blueprint.route("/posts/new", methods=["GET"])
def new_post():
    current_app.logger.info("New Post Page loaded!")
    return render_template('posts/edit_interface.html')
