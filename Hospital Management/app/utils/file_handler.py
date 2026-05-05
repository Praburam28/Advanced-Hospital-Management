ALLOWED_TYPES = [
    "image/jpeg",
    "image/png",
    "application/pdf"
]

MAX_SIZE = 5 * 1024 * 1024

def validate_file(file):

    if file.content_type not in ALLOWED_TYPES:
        return False

    return True