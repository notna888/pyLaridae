# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from pyLaridae.file_management.forms import AddFileForm
from pyLaridae.utils import flash_errors
from pyLaridae.classes import FileObj

blueprint = Blueprint("file_management", __name__, static_folder="../static")


@blueprint.route("/media_management/upload", methods=["POST"])
def upload():
    form = AddFileForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            flash("File Uploaded Successfully.", "success")
            return render_template('file_management/upload/upload_success.html')
        else:
            flash_errors(form)

@blueprint.route("/media_management", methods=["GET", "POST"])
def media():
    """Media page."""
    current_app.logger.info("Media Page Loaded!")
    form = AddFileForm(request.form)

    all_found_files = [
        FileObj('Folder 1', True),
        FileObj('File 1'),
        FileObj('Folder 2', True),
        FileObj('File 2'),
        FileObj('File 3'),
        FileObj('File 4'),
        FileObj('File 5'),
    ]

    context = {
        'form': form,
        'all_files': all_found_files
    }

    return render_template("file_management/media.html", **context)
