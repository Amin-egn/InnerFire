# standard
import os


# base directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

# settings file
SETTINGS_FILE = os.path.join(BASE_DIR, 'settings.json')

# deafault settings
DEFAULT_SETTINGS = {
    'servername': '.\\',
    'username': 'sa',
    'databasename': ''
}
