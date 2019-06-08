import os
import json
import logging
import logging.config
from dotenv import load_dotenv
from flask import Flask

# setup dotenv
load_dotenv()

# initialize flask app
app = Flask(__name__)

# setup logging
logging_filename = 'logging_config.json'
logging_fullpath = os.path.join(os.getcwd(), 'template', logging_filename)
if not os.path.exists(logging_fullpath):
	logging_fullpath = os.path.join(os.getcwd(), logging_filename)

with open(logging_fullpath, 'rt') as f:
	config = json.load(f)
logging.config.dictConfig(config)
logger = logging.getLogger()

@app.route('/')
def hello_world():
	return 'Hello, World!'

if __name__ == '__main__':
	# logger.info('The meaning of life: {}'.format(os.environ.get('MEANING_OF_LIFE')))
	app.run()
