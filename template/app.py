import os
import json
import logging
import logging.config

# setup logging
logging_filename = 'logging_config.json'
logging_fullpath = os.path.join(os.getcwd(), 'template', logging_filename)
if not os.path.exists(logging_fullpath):
	logging_fullpath = os.path.join(os.getcwd(), logging_filename)

with open(logging_fullpath, 'rt') as f:
	config = json.load(f)
logging.config.dictConfig(config)
logger = logging.getLogger()

if __name__ == '__main__':
	logger.info('Hello, World!')
