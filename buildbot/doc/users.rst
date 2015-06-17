
User interface
==================

Where is it ?
----------------

For the time being the buildbot is hosted at EBI on my personal laptop so its access is
restricted to those being on the campus.  

Alternatively, you can install this package on your own computer. You will then
be able to acess to the web interface on your localhost (http://localhost:8010). 

For the moment, just go to http://172.22.68.130:8010/waterfall
you should see a window like this:

.. image:: buildbot.png
    :width: 50%

Each column corresponds to a different test suite that we will call **builder**. 
For instance the first column is dedicated to CNOR packages (CellNOptR, CNORode, ...)

How to run a builder ?
-------------------------

If you want to run the test yourself, you will need a login/password; ask
Thomas. Then, go to the **waterfall** page (http://172.22.68.130:8010/waterfall) and select
the builder you want to run from the top grey row. For instance, to run CNOR,
the first column provide a link called continuous_integration (CNOR). Click
there, you should reach this page: http://172.22.68.130:8010/builders/continuous_integration(CNOR).

It looks like:

.. image:: builder.png
   :width: 50%

Here, you need to provide your login and password. Once done, you can click on
"Force build" at the bottom of the page. Come back to the waterfall. You should
see the status of the builder (in the first column) changing (you may need to
refresh the page). 

Color code is intuitive: 

 * green : everything seems fine
 * orange: warning
 * red: failure.

What are the available builders and what they are doing
---------------------------------------------------------

First column: CNOR
~~~~~~~~~~~~~~~~~~~~~~

 #. remove the CNOR package from the previous installation
 #. Install or udpate the dependencies (e.g., Rgraphviz, RBGL, ...)
 #. CNOR

    #. checkout CNOR from SVN
    #. run R CMD install
    #. run R CMD build
    #. run R CMD check

 #. CNOR fuzzy

    #. checkout CNOR from SVN
    #. run R CMD install

 #. CNOR ode

    #. checkout CNOR from SVN
    #. run R CMD install
    #. run R CMD build
    #. run R CMD check

 #. CNOR discreteTime

    #. checkout CNOR from SVN
    #. run R CMD install


Second column: cinapps
~~~~~~~~~~~~~~~~~~~~~~~~~

 #. checkout cinapps
 #. build, install, run tests of cinapps.deploy
 #. build, install, run tests of cinapps.cno
 #. build, install, run tests of cinapps.greedy
 #. create the sphinx documentation
 #. create this documentation and upload

CNO matlab
~~~~~~~~~~~~

 #. Checkout CNO (matlab  version)
 #. run the tests in ./tests

sampleModels
~~~~~~~~~~~~~~~~~


 #. Go in the SVN and checkout Model_with_data/sampleModels/
 #. Run the script create_images.py that goes into each subdirectory, read the
    sif/csv files and create a graph out of the model
 #. create the sphinx documentation

