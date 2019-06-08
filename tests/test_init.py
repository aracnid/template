import os

def test_load_dotenv():
	# verify that the environment variable is not already set
	meaning_of_life = os.environ.get('MEANING_OF_LIFE')
	assert not meaning_of_life

	# load the main application
	from template import app	

	# verify that the environment variable is now set
	meaning_of_life = os.environ.get('MEANING_OF_LIFE')
	assert meaning_of_life == '42'