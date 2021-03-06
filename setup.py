#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#
#   ARD - Automatic Reaction Discovery
#
#   Copyright (c) 2016 Prof. William H. Green (whgreen@mit.edu) and Colin
#   Grambow (cgrambow@mit.edu)
#
#   Permission is hereby granted, free of charge, to any person obtaining a
#   copy of this software and associated documentation files (the "Software"),
#   to deal in the Software without restriction, including without limitation
#   the rights to use, copy, modify, merge, publish, distribute, sublicense,
#   and/or sell copies of the Software, and to permit persons to whom the
#   Software is furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#   FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#   DEALINGS IN THE SOFTWARE.
#
###############################################################################

import os

from distutils.core import setup

###############################################################################

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

modules = []
for root, dirs, files in os.walk('ard'):
    for f in files:
        if f.endswith('.py') or f.endswith('.pyx'):
            if 'Test' not in f and '__init__' not in f:
                module = 'ard' + root.partition('ard')[-1].replace('/', '.') + '.' + f.partition('.py')[0]
                modules.append(module)

setup(
    name='ARD',
    version=0.1,
    description='Automatic Reaction Discovery',
    long_description=readme,
    author='William H. Green and Colin Grambow',
    author_email='cgrambow@mit.edu',
    url='https://github.com/cgrambow/AutomaticReactionDiscovery',
    license=license,
    packages=['ard'],
    py_modules=modules
)
