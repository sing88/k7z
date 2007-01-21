"""
K7Z: Basic Archiver
Designed by Chris Giles

File:		Settings.py
Purpose:	Settings handler
"""


### Imports

# K7Z 1
import	Import

# Python
try :
	import	os, platform, sys
except :
	Import.slException( "Python" )

# PyQt4
try :
	from	PyQt4	import QtCore
except :
	Import.slException( "PyQt4" )

# K7Z 2
import	Main


### Variables

# Application
sAppName		= "K7Z"
sAppVer			= "0.6"

# Author
sAuthorName			= "Chris Giles"
sAuthorEmailUser	= "Chris.G.27"
sAuthorEmailDomain	= "@Gmail.com"

# Operating system
sOS			= platform.system()

# Path separator
sPathSep	= QtCore.QDir.separator()

# Home
sHomeKDE	= os.getenv( 'KDEDIR' )
sHomeUser	= os.getenv( 'HOME' )

# Linux
if sOS == "Linux" :

	if not sHomeKDE :
		sHomeKDE	= '/usr/'

	if not sHomeUser :
		sHomeUser	= '/home/' + os.getenv( 'USER' ) + '/'

	sHomeK7Z	= QtCore.QString( sHomeUser + "/.kde/share/apps/K7Z/" )

	# Installation
	if QtCore.QFile.exists( sHomeKDE + "/share/apps/K7Z/Desktop/Context/Backup/" ) :
		sInstK7Z	= QtCore.QString( sHomeKDE + "/share/apps/K7Z/" )
	else :
		sInstK7Z	= sHomeK7Z

	# Commands
	sCmd7z		= QtCore.QString( "7z" )
	sCmdTar		= QtCore.QString( "tar" )

	# Path separator
	#sPathSep	= QtCore.QString( "/" )

# Windows
elif sOS == "Windows" :

	if not sHomeKDE :
		sHomeKDE	= ''

	if not sHomeUser :
		sHomeUser	= ''

	sReg		= QtCore.QSettings( "HKEY_LOCAL_MACHINE\\Software\\Archiving\\K7Z" , QtCore.QSettings.NativeFormat )
	sHomeK7Z	= sReg.value( "Path" ).toString()

	# Installation
	sInstK7Z	= sHomeK7Z

	# Commands
	sReg		= QtCore.QSettings( "HKEY_LOCAL_MACHINE\\Software\\7-Zip" , QtCore.QSettings.NativeFormat )
	sCmd7z		= sReg.value( "Path" ).toString() + "/7z.exe"

	# Path separator
	#sPathSep	= QtCore.QString( "\\" )

# Others
else :

	print ""
	print "Unfortunately, your OS is not supported by " + sAppName + " " + sAppVer + ".  Please email the author, specifying your system details."
	print ""

	sys.exit()

# Flags
bVerbose		= False
bInvisible		= False
bAutoExit		= False

# Input
iNumInputArgs	= len(sys.argv)

# Profiles
iProOther		= 1
iProDefault		= 2
iProStorage		= 3

# Operations
iOpCreate		= 1
iOpExtract		= 2
iOpTest			= 3

# String-lists
slFiles			= QtCore.QStringList()
slTHelpCmdArgs	= QtCore.QStringList()


### Slots

# Settings launch
def slSettingsL() :

	# Linux
	if sOS == "Linux" :

		# Check Top Level
		if QtCore.QFile.exists( sHomeUser + "/.kde/share/apps/konqueror/servicemenus/K7Z.marker.top" ) :
			Main.uiSettings.cbKTopLevel.setCheckState( QtCore.Qt.Checked )
		else :
			Main.uiSettings.cbKTopLevel.setCheckState( QtCore.Qt.Unchecked )

		# Enable
		Main.uiSettings.gbKonq.setEnabled( True )

	# Modal
	Main.dSettings.exec_()


# Settings accepted
def slSettingsA() :

	# Linux
	if sOS == "Linux" :

		sBackupPath = sInstK7Z + "/Desktop/Context/Backup/"
		sDestPath = "/.kde/share/apps/konqueror/servicemenus/"

		# Remove current entries
		QtCore.QFile.remove( sHomeUser + sDestPath + "K7Zc.desktop" )
		QtCore.QFile.remove( sHomeUser + sDestPath + "K7Ze.desktop" )
		QtCore.QFile.remove( sHomeUser + sDestPath + "K7Z.marker.top" )
		QtCore.QFile.remove( sHomeUser + sDestPath + "K7Z.marker.act" )

		# Create servicemenus directory
		dDestPath = QtCore.QDir( sHomeUser + sDestPath )
		if not dDestPath.exists() :
			dDestPath.mkpath( sHomeUser + sDestPath )

		# Top Level?
		if Main.uiSettings.cbKTopLevel.isChecked() :
			sFileExt = "top"
		else :
			sFileExt = "act"

		QtCore.QFile.copy( sBackupPath + "K7Zc.desktop." + sFileExt , sHomeUser + sDestPath + "K7Zc.desktop" )
		QtCore.QFile.copy( sBackupPath + "K7Ze.desktop." + sFileExt , sHomeUser + sDestPath + "K7Ze.desktop" )
		QtCore.QFile.copy( sBackupPath + "K7Z.marker" , sHomeUser + sDestPath + "K7Z.marker." + sFileExt )
