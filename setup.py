#!/usr/bin/env python

from distutils.core import setup

setup(name='icytoscapy',
      version='1.0',
      description='Cytoscape visualization with IPython Notebook',
      author='Naoki Nishida, Keiichiro Ono, Kozo Nishida',
      author_email='knishida@riken.jp',
      url='https://github.com/kozo2/cytoscape-ipy',
      packages=['icytoscapy'],
      package_data={'icytoscapy': ['data/*', 'js/*']}
     )
