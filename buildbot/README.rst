This is a continous integration master and slave dedicated to CNO integration. 

It uses buildbot as a framework. The master should be run within a virtualenv
otherwise packages will be installed on your system. Similarly, the R packages
are downloaded and installed in ./slave/continuous_integration. So, R_HOME
must be set accordingly.


How to start the Buildbot 

To start the master:  buildbot start master
To start the slave:   buildslave start slave

If you update the master configuration file, you need to update the master: 

    buildslave stop slave
    buildbot sighup master
    buildslave start slave

Then goto your http://localhost:8010

See also the documentation in ./doc
