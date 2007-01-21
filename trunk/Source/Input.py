"""
K7Z: Basic Archiver
Designed by Chris Giles

File:		Input.py
Purpose:	Input arguments handler
"""


### Imports

# K7Z 1
import	Import

# Python
try :
	import	sys
except :
	Import.slException( "Python" )

# PyQt4
try :
	from	PyQt4	import QtCore
except :
	Import.slException( "PyQt4" )

# K7Z 2
import	Main, Profile, Settings, Thread


### Slots

# Print K7Z info
def slPK7ZInfo() :
	print ""
	print Settings.sAppName + " " + Settings.sAppVer + ": Basic Archiver"
	print "Designed by " + Settings.sAuthorName
	print ""

# Print Usage
def slPUsage() :

	print "Usage: " + Settings.sAppName + " [commands] [files]"
	print ""
	print "commands"
	print ""
	print "	c: create"
	print "	e: extract"
	print "	t: test"
	print ""
	print "	d: default"
	print "	s: storage"
	print "	b: beneath"
	print ""
	print "	i: invisible"
	print "	v: verbose"
	print "	h: help"
	print ""


# Input arguments
def slArgTest() :

	# Supplied arguments
	if Settings.iNumInputArgs >= 2 :

		# Help
		if "h" in sys.argv[1] :

			# K7Z
			slPK7ZInfo()

			# Usage
			slPUsage()

			# Exit
			sys.exit()

		# Profile
		if "s" in sys.argv[1] :
			Profile.slProLStorage()
		else :
			Profile.slProLDefault()

		# Verbose
		if "v" in sys.argv[1] :

			Settings.bVerbose = True

			slPK7ZInfo()

			print "OS = " + Settings.sOS
			print "$KDEDIR = " + Settings.sHomeKDE
			print "$HOME = " + Settings.sHomeUser
			print ""

		# Supplied arguments
		if Settings.iNumInputArgs >= 3 :

			# List of files to archive
			for iEntry in range(2,Settings.iNumInputArgs) :
				Settings.slFiles.append( sys.argv[iEntry] )

			# Create Archive
			if "c" in sys.argv[1] :

				# Arrange the interface
				Main.uiMain.leSDir.setText( "External File(s)" )
				Main.uiMain.leSDir.setEnabled( False )
				Main.uiMain.pbSDir.setEnabled( False )
				Main.uiMain.twOperations.setCurrentIndex( 0 )
				Main.uiMain.twOperations.setTabEnabled( 1 , False )
				Main.uiMain.pbCreate.setDefault( True )

				# Default and storage
				if "d" in sys.argv[1] or "s" in sys.argv[1] :
					Settings.bAutoExit = True
					Thread.slCreate()

			# Extract Archive
			elif "e" in sys.argv[1] :

				# Arrange the interface
				Main.uiMain.leArchive.setText( "External File" )
				Main.uiMain.leArchive.setEnabled( False )
				Main.uiMain.pbSArc.setEnabled( False )
				Main.uiMain.twOperations.setCurrentIndex( 1 )
				Main.uiMain.twOperations.setTabEnabled( 0 , False )
				Main.uiMain.pbExtract.setDefault( True )

				# Beneath
				if "b" in sys.argv[1] :

					# Arrange the interface
					Main.uiMain.gbEDestination.setChecked( True )
					Main.uiMain.cbBeneath.setCheckState( QtCore.Qt.Checked )

				# Profile
				if "d" in sys.argv[1] :
					Settings.bAutoExit = True
					Thread.slExtract()

			# Extract Archive
			elif "t" in sys.argv[1] :

				# Arrange the interface
				Main.uiMain.leArchive.setText( "External File" )
				Main.uiMain.leArchive.setEnabled( False )
				Main.uiMain.pbSArc.setEnabled( False )
				Main.uiMain.twOperations.setCurrentIndex( 1 )
				Main.uiMain.twOperations.setTabEnabled( 0 , False )
				Main.uiMain.pbExtract.setDefault( True )
				Main.uiMain.cbETest.setChecked( True )

				# Default
				if "d" in sys.argv[1] :
					Settings.bAutoExit = True
					Thread.slExtract()

			# Invisible
			if "i" in sys.argv[1] :
				Settings.bInvisible = True

	else :

		# Load 'Default' profile
		Profile.slProLDefault()
