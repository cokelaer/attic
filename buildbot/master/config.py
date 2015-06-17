# -*- python -*-
#
#  This file is part of the CNO software
#
#  Copyright (c) 2011-2012 - EBI
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  Distributed under the GPLv2 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-2.0.html
#
#  CNO website: http://www.ebi.ac.uk/saezrodriguez/software.html
#
##############################################################################
# $Id: config.py 3210 2013-01-31 12:36:06Z cokelaer $
"""
This module holds configuration. This is the user interface so that access and
master are untouched.
"""

# General configuration
title = "CNO"
titleURL = "http://www.ebi.ac.uk/saezrodriguez/software/cno"
buildbotURL = "http://localhost:8010/"  # does not seem to be really used...

python_version = "python2.7"   # just for the link to be correct
cnopath = "/nfs/research2/saezrodriguez/cno" # where to copy the tar ball of the R packages

# ------------------------------------------------- The builders
# Configuration of the builders
# key is used internally, value is written in the waterfall header.
builders = {
    'cnor': "continuous_integration (CNOR)",
    'cnomatlab': 'continuous_integration (CNO matlab)',
    'cnolab': 'cnolab continuous integration',
    'cellnopt':'cellnopt (python)',
    'third_parties':'Third parties librairies'
    }

# ----------------------------------------- information related to each builder
# cnor
CellNOptR_packages = {
    'order': ['CellNOptR', 'CNORfuzzy', 'CNORode', 'CNORdt'],
    'CellNOptR':    {'dir':'CellNOptR'}, 
    'CNORfuzzy':    {'dir':'CNOR_fuzzy'}, 
    'CNORode':      {'dir':'CNOR_ode/CNORode'}, 
    'CNORdt':       {'dir': 'CNOR_dt/CNORdt'}
    }

# cnolab
cnolab_packages =  ['greedy', 'pipeline']

# cellnopt
cellnopt_packages =  ['admin', 'data', 'wrapper', 'misc']

third_parties_packages = {"svn":["https://subversion.assembla.com/svn/pyeasydev/"], 
    'packages':["eaydev"]}

# In order to remove a builder, just set it to None
# builders['cnomatlab'] = None

# the order of the builders to appear in the waterfall. Must have the same
# number of element as in builder.keys()
keys = ['cnor', 'cnolab', 'cellnopt', 'third_parties', 'cnomatlab'] 

## NOTHING to CHANGE BELOW

# keys must match builders.keys:
assert sorted(builders.keys()) == sorted(keys)
builderNames = [] 
for key in keys:
    if builders[key]:
        builderNames.append(builders[key])

