"""
This module holds authentication and urls used by buildbot master and slaves.
"""
from svn import *

slavePort="9989"

# -- the builder's svn identity --
svnUser = 'cokelaer'
svnPassword = 'XXXXXXX'  # adapt to you needs


# -- authorized users --
auth_users = [("cokelaer", "bf5dcfeb011146e48b6708ff49af5a5f"),] 

