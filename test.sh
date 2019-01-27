pip freeze
nosetests --with-coverage --cover-package moban_haml --cover-package tests tests  docs/source moban_haml && flake8 . --exclude=.moban.d,docs --builtins=unicode,xrange,long
