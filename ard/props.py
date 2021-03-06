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

"""
Contains dictionaries of atomic properties, such as atomic numbers and masses.
"""

###############################################################################

# Atomic numbers
atomnum = {1: 'H', 6: 'C', 7: 'N', 8: 'O', 9: 'F', 14: 'Si', 15: 'P', 16: 'S', 17: 'Cl', 35: 'Br'}
atomnum_inv = dict((v, k) for k, v in atomnum.iteritems())

# Atomic weights in g/mol (from http://www.ciaaw.org/atomic-weights.htm#m)
atomweights = {1: 1.007975, 6: 12.0106, 7: 14.006855, 8: 15.9994, 9: 18.9984031636, 14: 28.085, 15: 30.9737619985,
               16: 32.0675, 17: 35.4515, 35: 79.904}

# Valence electrons of neutral atoms
valenceelec = {1: 1, 6: 4, 7: 5, 8: 6, 9: 7, 14: 4, 15: 5, 16: 6, 17: 7, 35: 7}

# Maximum valences of atoms
maxvalences = {1: 1, 6: 4, 7: 3, 8: 2, 9: 1, 14: 4, 15: 5, 16: 6, 17: 7, 35: 7}
