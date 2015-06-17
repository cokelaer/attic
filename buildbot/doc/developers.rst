

Developers 
===================
Buildbot provides a framework to build applications on a server. It manages a
master and some slaves for you. The buidlbot provided in the SVN
(continuous_integration directory) is dedicated to CNO integration. 

Installation
----------------

You may or may not have root access. This is not important because we will use
**virtualenv** to create a virtual directory where you can install everything.
All you need is a server (local or global) where you can access to port 8010 and
port 9989.

We suppose that virtualenv is installed globally. Create your virtual
environment that we will call buildbot::

    virtualenv buildbot

This creates a directory called buildbot where you will install your packages.
So, let us activate it::

    cd buildbot
    source bin/activate

You are ready to work in your virtual environment. We can now install new python
packages locally. Let us install buildbot::

    easy_install buildbot
    easy_install buildbot-slave

As you can see, there is no need to be root anymore. 

Now, you need the source of the continuous_integration package. In the same directory, type::

    svn co https://svn.ebi.ac.uk/sysbiomed/trunk/continuous_integration

This directory contains the continuous integration tools dedicated to CNO. There
is a master directory and a slave directory. The master will run jobs in the
slave directory.

You must change 2 files to provide the full path where you installed the tools. 
There is a file in master/buildbot.tac that requires to be
edited (change the pathname line 7 according to your directory). Similarly in
./slave/buildbot.tac



How to start the Buildbot 
-----------------------------

Once you have thr svn, we recommend to copy trunk/continuous_integration to
another directory (let us say buildot for the following discussion). Then, just
go in it::

    cd buildbot


To start the master::

    buildbot start master/


To start the slave::

    buildslave start slave/

.. warning:: need to edit buildbot.tac to set the proper directory. You will
   want to edit access.py in ./master to set the username/pwss of the svnuser.


If you update the master configuration file, you need to update the master::

    buildslave stop slave
    buildbot sighup master
    buildslave start slave

Then goto your http://localhost:8010/waterfall ou should see a window like this:

.. image:: buildbot.png
    :width: 50%



Documentation Updated
~~~~~~~~~~~~~~~~~~~~~~~~

some documentation that are generated during the buildbot are then copied in
/master/public_html. This is the case of sampleModels and cinapps
.

* http://localhost:8010/sampleModels
* http://localhost/cinapps




Installation issues 
-----------------------------

I got an error while installing buildbot because sqlite3 is not available
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If sqlite3 is not installed and you do not have permission to install it
globally, you can install it locally. First download sqlite http://www.sqlite.org/download.html, untar the file and type::

    ./configure --prefix=PathToYoutVirtual
    make
    make install

Then get pysqlite sources. One way to do it is::

    easy_install pysqlite

an error occurs if sqlite3 is not available. From the error message, you can
find the link to the tar ball. Get it using wget. Then, you need to tell
pysqlite where is the sqlite librairy. Edit the setup.cfg and change it::

    [build_ext]
    #define=
    include_dirs=/homes/user/Work/buildbot/include
    library_dirs=/homes/user/Work/buildbot/lib
    libraries=sqlite3
    define=SQLITE_OMIT_LOAD_EXTENSION

anf finally, install it::

    python setup.py install


Running buildbot on the virtual machine
--------------------------------------------

Prerequisites
~~~~~~~~~~~~~~

* Change the python_verswion in config 
* change path in master.cfg
* set passwrod in access.py 

::

    export PYTHONPATH=$VIRTUAL_ENV/lib/python2.7/site-packages/:/usr/lib64/python2.7/site-packages/

::

    easy_install numpy coverage nose


