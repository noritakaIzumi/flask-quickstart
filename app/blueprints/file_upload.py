import os.path

from app.services.file_upload import file_is_allowed_to_upload
from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for
from werkzeug import Response
from werkzeug.utils import secure_filename

bp = Blueprint(__name__.replace(f"{__package__}.", ""), __name__)


@bp.route("/upload", methods=["GET", "POST"])
def upload_file() -> Response | str:
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part")
            return redirect(url_for(f".{upload_file.__name__}"))

        file = request.files["file"]
        if file.filename is None or file.filename == "":
            flash("No selected file")
            return redirect(url_for(f".{upload_file.__name__}"))

        if not file_is_allowed_to_upload(file.filename):
            flash(f'"{file.filename}" is not allowed to upload')
            return redirect(url_for(f".{upload_file.__name__}"))

        filename = secure_filename(file.filename)
        if filename != file.filename:
            current_app.logger.warning('filename is sanitized to: "%s"', filename)

        file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
        return redirect(url_for(f".{upload_completed.__name__}"))

    return render_template("file_upload.html")


@bp.get("/upload/completed")
def upload_completed() -> str:
    return render_template("upload_completed.html")
