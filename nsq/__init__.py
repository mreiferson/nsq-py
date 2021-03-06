import logging

# Logging, obviously
logger = logging.getLogger('nsq')
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.FATAL)

# Our underlying json implmentation
try:
    import simplejson as json
except ImportError:  # pragma: no cover
    import json
