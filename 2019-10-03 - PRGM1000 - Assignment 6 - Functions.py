# -*- coding: utf-8 -*-
#Donald Szeto
#PRGM1000 - Scripting Fundamentals
#Assignment 6 - Functions
#2019-10-05
#Version 1

import shutil

#Print the instructions and an example.
print("INSTRUCTIONS\n\nThis script requires two inputs to archive a directory:\
      \n\n1. The filepath of the directory to be archived.\n2. The desired\
      filename of the resulting archive.\n\nFor example, an input directory \
filepath of \"C:\\Users\\Administrator\\Desktop\\TESTFOLDER\" and a \
desired filename of Zipped_Folder will create an archive named \
\"Zipped_Folder.zip\" located in the same filepath as the input \
directory (i.e. \"C:\\Users\\Administrator\\Desktop\\\").")

#Define input directory & file name modification module.
def Process_Inputs(Input_FileDirectory, Input_DesiredFileName):
    
    #Determine the output directory by removing string ends until the last '\' character.
    StringCountdown = len(Input_FileDirectory) - 1

    while Input_FileDirectory[StringCountdown] != "\\":
        StringCountdown -= 1

    FileDirectory = Input_FileDirectory[0:(StringCountdown + 1)]
    
    #Append the input directory to the desired archive name.
    Output_FileDirectory = FileDirectory + Input_DesiredFileName
    
    return Output_FileDirectory


#Define archiving module
def make_archive(Input_FileDirectory, Output_FileDirectory):

    #Execute the archiving operation.
    shutil.make_archive(Output_FileDirectory, 'zip', Input_FileDirectory)


#Get directory and filename inputs.
Input_FileDirectory = input("Enter the directory you want to archive: ")
Input_DesiredFileName = input("Enter the name of the archive you'd like to create: ")

#Generate the output file directory with the desired file name.
Output_FileDirectory = Process_Inputs(Input_FileDirectory, Input_DesiredFileName)

#Execute the archiving module with the needed inputs.
make_archive(Input_FileDirectory, Output_FileDirectory)