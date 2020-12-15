run:
	python3 main.py

watch:
	watchgod main.main

#
# Setup
#

setup:
	pyenv install -s
	pyenv virtualenv -f discord-me
	@echo "Now run 'pyenv activate discord-me'"
	@echo "and 'pip install -r requirements.txt'"
