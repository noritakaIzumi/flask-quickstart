UPLOAD_ALLOWED_EXTENSIONS = {"txt", "ogg"}


def file_is_allowed_to_upload(filename: str) -> bool:
    if "." not in filename:
        return False
    extension = filename.rsplit(".", 1)[1].lower()
    return extension in UPLOAD_ALLOWED_EXTENSIONS
