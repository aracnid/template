import os
import json
import logging
import logging.config
import pkg_resources

# setup logging
logging_filename = 'logging_config.json'
logging_fullpath = os.path.join(os.getcwd(), 'template', logging_filename)
if not os.path.exists(logging_fullpath):
	logging_fullpath = os.path.join(os.getcwd(), logging_filename)

with open(logging_fullpath, 'rt') as f:
	config = json.load(f)
logging.config.dictConfig(config)
logger = logging.getLogger()

def main():
	return 'Hello, World!'

if __name__ == '__main__':
	logger.info(main())
	version = pkg_resources.required('Template')[0].version