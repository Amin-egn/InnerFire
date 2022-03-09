# standard
import logging
# internal
from src import conf


# logger
_logger = logging.Logger(conf.LOG_NAME)
_logger_level = logging.WARNING
_logger.setLevel(_logger_level)

# file handler
fh = logging.FileHandler(conf.LOG_FILE, 'w', 'utf-8')
fh.setLevel(_logger_level)

# format
formatter = logging.Formatter(conf.LOG_FORMAT)

# add format to fild handler
fh.setFormatter(formatter)
# add file handler to logger
_logger.addHandler(fh)

# interface
warning = _logger.warning
error = _logger.error
