# Some Angstrom images are missing the py_compile module; get it if not
# present:
# Fix credit:https://github.com/alexanderhiam/PyBBIO/blob/master/setup.py
import random, os
python_lib_path = random.__file__.split('random')[0]
if not os.path.exists(python_lib_path + 'py_compile.py'):
  print "py_compile module missing; installing to %spy_compile.py" %\
                                                          python_lib_path
  import urllib2
  url = "http://hg.python.org/cpython/raw-file/4ebe1ede981e/Lib/py_compile.py"
  py_compile = urllib2.urlopen(url)
  with open(python_lib_path+'py_compile.py', 'w') as f:
    f.write(py_compile.read())
  print "testing py_compile..."
  try:
    import py_compile
    print "py_compile installed successfully"
  except Exception, e:
    print "*py_compile install failed, could not import"
    print "*Exception raised:"
    raise e


import distribute_setup
distribute_setup.use_setuptools()
from setuptools import setup, Extension, find_packages

classifiers = ['Development Status :: 3 - Alpha',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.6',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: Home Automation',
               'Topic :: System :: Hardware']

setup(name             = 'WB_IO',
      version          = '1.0.0',
      author           = 'Evgeny Boger',
      author_email     = 'boger@contactless.ru',
      description      = 'A module to control WB IO channels',
      long_description = open('README.rst').read() + open('CHANGELOG.rst').read(),
      license          = 'MIT',
      keywords         = 'WirenBoard Linux IO GPIO PWM ADC',
      url              = 'https://github.com/contactless/wb-io-python',
      classifiers      = classifiers,
      packages         = find_packages(),
      py_modules       = ['gpio_sysfs'],
      ext_modules      = [Extension('WB_IO.GPIO', ['source/py_gpio.c', 'source/event_gpio.c', 'source/constants.c', 'source/common.c']),
                          Extension('WB_IO.SPI', ['source/spimodule.c', 'source/constants.c', 'source/common.c']),
                         ]
	 )
