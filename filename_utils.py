import re
import os

def sanitize_filename(name):
    """Sanitizes a string to make it a valid filename."""
    return re.sub(r'[\\/*?:"<>|]', "", name)


def create_output_directory(output_path):
    """Creates the output directory if it does not exist."""
    if not os.path.exists(output_path):
        os.makedirs(output_path)
