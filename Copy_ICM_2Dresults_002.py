# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:44:56 2018

@author: simon.desmet
"""

import os
import shutil


# ask user for location to save ICM 2D results
#savepath  = raw_input("path for new files to be saved in:")
savepath  = "B:\\South_Cave\\50sop_out"
# ask user for location of existing results files
#existingfldr  = raw_input("path for existing results folders:")
existingfldr  = "B:\\South_Cave\\50sop"
# create list of results folders

ProjectName = 'SouthCave'

ICMresfldrs = os.walk(existingfldr) # uses  os.walk function to create tuple describing folder tree down from target folder


ICMfldrlst =[x[0] for x in ICMresfldrs] # lists out 1st tier folders from os.walk output and puts them in a list
del ICMfldrlst[0]
# we now have a list with each results file folder in it to work on.





# for each item in results folder list - for loop start
for i in ICMfldrlst:


    # open the folder, read all files in to temporary list
    shapefile = os.listdir(i+'\\') # creates list called shapefile and reads in files in the dolder
    print shapefile
    
    # get name for results
    pathsplit = i.split("\\") # takes path saved in i and splits it up to get result name
    filename = pathsplit[-1].split(" ") # takes the last item in the list created by pathsplit and splits it again to get the return period, scenario etc
    print filename
    rawreturn = str(filename[3]) # get return period and format it appropriately
    trimreturn = int(rawreturn[0:-2]) # take off 'yr' and convert to interger
    returnYR = str(format(trimreturn,'04d'))#turn into a 4 digit 0000 string
    Epochful =  str(filename[4])
    Epoch = Epochful[2:4]
    sop = int(filename[7])
    sopdigits = str(format(sop,'03d'))
    scenarioname = str(filename[8])
    scenario = str(scenarioname[-1]+sopdigits)
    version = str(filename[1])
    print returnYR
    print Epoch
    print scenario
    print version

    # for each file in temporary list copy each file with new name

    for a in shapefile:
        extensionsplit = a.split(".")
        ext = str(extensionsplit[-1])
        source = str(i+'\\'+a)
        shutil.copy2(source,savepath+'\\'+returnYR+Epoch+scenario+'_'+ProjectName+'_'+version+'.'+ext)