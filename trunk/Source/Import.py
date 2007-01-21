"""
K7Z: Basic Archiver
Designed by Chris Giles

File:		Import.py
Purpose:	Importation handler
"""


### Imports

# Python
try :
	import	sys
except :
	#slException( "Python" )

	print ""
	print "The required 'Python' modules could not be found.  See 'Doc/INSTALL.txt' for more info."
	print ""

	sys.exit()

# K7Z
#import	Settings


### Slots

def slException( sAppName ) :

	print ""
	print "The required '" + sAppName + "' modules could not be found.  See 'Doc/INSTALL.txt' for more info."
	print ""

	# K7Z
	if sAppName == "K7Z" :
	#if sAppName == Settings.sAppName :
		print "You must run \"cd ../Build/ ; make ; cd ../Source/\" first."
		print ""

	sys.exit()
