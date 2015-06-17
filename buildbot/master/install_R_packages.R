# -*- python -*-
#
#  Copyright 2011 EBI
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
# $Id: install_R_packages.R 3210 2013-01-31 12:36:06Z cokelaer $

source("http://bioconductor.org/biocLite.R")




installation<-function(package){

 libraryPath = "/slave/continuous_integration__CNOR_/RPackages"
 libraryPath = paste(Sys.getenv("VIRTUAL_ENV"), libraryPath, sep="")

 dir.create(libraryPath)
 print(package)
 #library(package, lib.loc=libraryPath, character.only=TRUE)
 status = tryCatch({
            library(package, lib.loc=libraryPath, character.only=TRUE)},
            error=function(e){

        print(libraryPath)
        #print(c(package, status))
           biocLite(package, lib=libraryPath)
        })
}


installation("RBGL")
installation("graph")
installation("nloptr")
installation("abind")
installation("xtable") # CNORfuzzy documentation

installation("RCurl")
installation("Rgraphviz")
installation("ggplot2")
installation("hash")