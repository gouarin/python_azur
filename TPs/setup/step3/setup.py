from distutils.core import setup

setup(name = 'calc',
      version = '1.0',
      author = 'loic Gouarin',
      description = 'module de calculatrice',
      packages = ['calculatrice'],
      package_data = {'calculatrice': ['data/*']},
      scripts = ['script/calc.py'],
      )
