# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 23:26:27 2020

@author: Trent Smith
"""

##used to overwrite a file
f = open("demofile3.xml", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.xml", "r")
print(f.read())