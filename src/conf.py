# standard
import os


# application information
APP_NAME = 'innerfire'
APP_VERSION = '1.0'
APP_AUTHOR = 'Amin Eidgahian'

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

# log
LOG_NAME = APP_NAME
LOG_DIR = os.path.join(BASE_DIR, 'log')
LOG_FILE = os.path.join(LOG_DIR, 'innerfire.log')
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
