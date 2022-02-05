# standard
import json
# internal
from . import conf


class API(object):
    """Settings API"""
    def __init__(self):
        self.settings = dict()
        self._initialize()

    def _initialize(self):
        try:
            with open(conf.SETTINGS_FILE, 'rt') as f:
                self.settings = json.loads(f.read())

        except Exception as e:
            print(str(e))
            self.settings = conf.DEFAULT_SETTINGS

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value

    def save(self):
        with open(conf.SETTINGS_FILE, 'wt') as f:
            f.write(json.dumps(self.settings, indent=4))


# single instance
_api = API()

# interface
g = _api.get
s = _api.set
save = _api.save
