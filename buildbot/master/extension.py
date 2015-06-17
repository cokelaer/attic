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
# $Id: extension.py 3224 2013-02-04 15:52:34Z cokelaer $

""" This is the CNO buiildbot.

See documentation in ../doc
"""
import os
import access
import config
#from buildbot.changes.svnpoller import SVNPoller
#from os.path import join as pj


import buildbot.steps.source, buildbot.process.buildstep
from buildbot.status.web.auth import IAuth, AuthBase
from zope.interface import Interface, implements
import hashlib

#from buildbot.status.web.authz import Authz

class SVN(buildbot.steps.source.SVN):
    name = 'simple_head_svn'

    def __init__(self, *args, **kwargs):
        """
        @type  svnurl: string
        @param svnurl: the URL which points to the Subversion server,
                       combining the access method (HTTP, ssh, local file),
                       the repository host/port, the repository path, the
                       sub-tree within the repository, and the branch to
                       check out. Using C{svnurl} does not enable builds of
                       alternate branches: use C{baseURL} to enable this.
                       Use exactly one of C{svnurl} and C{baseURL}.

        @param username: username to pass to svn's --username
        @param password: username to pass to svn's --password
        """
        self.description = [kwargs.pop("description", "svn co")]
        buildbot.steps.source.SVN.__init__(self, *args, **kwargs)

    def startVC(self, branch, revision, patch):
        self.args['svnurl'] = self.svnurl
        self.args['revision'] = 'HEAD'
        self.args['patch'] = patch

        if self.username is not None or self.password is not None:
            if self.username is not None: self.args['username'] = self.username
            if self.password is not None: self.args['password'] = self.password

        if self.extra_args is not None:
            self.args['extra_args'] = self.extra_args

        revstuff = []
        self.description.extend(revstuff)
        self.descriptionDone.extend(revstuff)

        cmd = buildbot.process.buildstep.LoggedRemoteCommand("svn",self.args)
        self.startCommand(cmd)




class Factories(object):
    def __init__(self, valid_names):
        self._factories = {} 
        self.valid_names = valid_names

    def __getitem__ (self, name) :
        return self._factories[name]

    def __setitem__ (self, name, factory) :
        assert name in self.valid_names, "%s not found in %s " % (name, self.valid_names)
        self._factories[name] = factory



class HashAuth(AuthBase):

    implements(IAuth)

    def __init__(self, userkeys):
        self.__userKeys = dict(userkeys)

    def authenticate(self, user, passwd):
        realone = self.__userKeys.get(user)
        if not realone:
            self.err = "%s is not a valid user"%(user,)
            return False
        hasher = hashlib.md5()
        hasher.update(passwd)
        hashed = hasher.hexdigest()
        return realone == hashed



from buildbot.process.factory import BuildFactory
from buildbot.steps.shell import ShellCommand, Compile
 

class PythonFactory(BuildFactory):
    def __init__(self, access, env):
        BuildFactory.__init__(self)
        self.svn = None
        self.name = None
        self.access = access
        self.env = env

    def addStep_svn(self, workdir, mode="update"):
        self.addStep(
            SVN(
                svnurl=self.svn, 
                mode=mode,
                username=self.access.svnUser, 
                password=self.access.svnPassword,
                workdir=workdir,
                description="Updating %s SVN"%self.name))

    def addStep_install(self, workdir=None):
        self.addStep(ShellCommand(workdir=workdir,
            command="python setup.py install sdist",
            description="Installing %s package"%self.name,  
            env=self.env ))

    def addStep_nosetests(self, workdir=None):
        self.addStep(ShellCommand(workdir=workdir, 
            command="python setup.py nosetests ",
            description="Running the test suite of %s"%self.name,
            env=self.env))
