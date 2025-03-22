import os
import sys

# Get the absolute path of the project
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SRC_DIR = os.path.join(BASE_DIR, "src")

# Add src to sys.path so Python can find cfehome
sys.path.insert(0, SRC_DIR)

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cfehome.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

print(f"Current Working Directory: {os.getcwd()}")
print(f"Python Path: {sys.path}")


def init():
    os.chdir(BASE_DIR)  # Change to project root
    import django

    django.setup()
