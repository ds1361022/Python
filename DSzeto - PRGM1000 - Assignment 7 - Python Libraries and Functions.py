# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 08:27:32 2019

@author: net1121
"""

import os, sys
import datetime

#Define time & date function.
def now():
    
    #Get the date & time and format accordingly.
    PresentTime = datetime.datetime.now(tz=None)
    ISOFormat = PresentTime.isoformat(sep=':', timespec='seconds')
    Date = ISOFormat[:11]
    Time = ISOFormat[11:]
    FormattedTime = Date + ':' + Time
    #Print date and time.
    print("The date and time is: %s." % (FormattedTime))

    
#Define file count function.
def countfile():
    
    #Get an input directory or use the default (current) working directory.
    InputDirectory = input("Please enter a valid directory or press \"Enter\" to use\
 your current working directory: ")
    
    #Set default directory to current working directory if directory selected.
    if InputDirectory == '': 
        InputDirectory = os.getcwd()
        
    #Generate a list of files and subdirectories.
    DirectoryListing = []
    DirectoryListing = os.listdir(InputDirectory)
    
    #Count number of files in DirectoryListing list
    FileCount = 0
    for Entry in DirectoryListing:
        if os.path.isfile(InputDirectory+'\\'+Entry):
            FileCount += 1
    
    #Print conditional file count result statement.
    if FileCount == 0:
        print("There are no files in \"%s\"." % (FileCount, InputDirectory))  
    elif FileCount == 1:
        print("There is only one file in \"%s\"." % (InputDirectory)) 
    else:
        print("There are %d files in \"%s\"." % (FileCount, InputDirectory))
   
 
#Get and print number of command line parameters.
CLP = len(sys.argv)

print("The number of command line parameters passed to the script is: %d."\
      % (CLP))

now() 
countfile()